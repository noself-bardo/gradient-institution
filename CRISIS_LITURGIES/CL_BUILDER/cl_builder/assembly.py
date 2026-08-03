from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image
from reportlab.lib.colors import Color, black
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas as pdfcanvas

from .io import dump_json


ISSUE_RE = re.compile(r"^ISSUE\s+(\d{2})\s+[—-]\s+(.+?)\s*$")
PAGE_RE = re.compile(r"^PAGE\s+([1-4])\s+[—-]\s+(.+?)\s*$")


@dataclass(frozen=True)
class CopyBlock:
    issue_number: int
    issue: str
    page_number: int
    title: str
    text: str


def parse_manuscript(text: str) -> list[CopyBlock]:
    lines = [line.strip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    issue_number: int | None = None
    issue = ""
    page_number: int | None = None
    page_title = ""
    body: list[str] = []
    blocks: list[CopyBlock] = []

    def flush() -> None:
        nonlocal body
        if issue_number is None or page_number is None:
            body = []
            return
        cleaned = "\n\n".join(part for part in body if part)
        blocks.append(CopyBlock(issue_number, issue, page_number, page_title, cleaned))
        body = []

    for line in lines:
        if line in {"NOTES", "FINALIZATION RECORD"}:
            flush()
            page_number = None
            break
        issue_match = ISSUE_RE.match(line)
        if issue_match:
            flush()
            issue_number = int(issue_match.group(1))
            issue = issue_match.group(2).strip().upper()
            page_number = None
            page_title = ""
            continue
        page_match = PAGE_RE.match(line)
        if page_match:
            flush()
            if issue_number is None:
                continue
            page_number = int(page_match.group(1))
            page_title = page_match.group(2).strip().upper()
            continue
        if page_number is not None and line:
            body.append(line)
    flush()
    return blocks


def copy_map_for_volume(volume: dict[str, Any], manuscript: str) -> dict[str, str]:
    parsed = parse_manuscript(manuscript)
    by_position = {(block.issue_number, block.page_number): block for block in parsed}
    result: dict[str, str] = {}
    for page in volume["pages"]:
        key = (int(page["issue_number"]), int(page["page_number"]))
        block = by_position.get(key)
        if block is None:
            raise ValueError(f"missing manuscript copy for issue {key[0]} page {key[1]}")
        if block.issue != str(page["issue"]).upper():
            raise ValueError(f"issue mismatch for {page['page_id']}: {block.issue}")
        result[page["page_id"]] = block.text
    if len(result) != len(volume["pages"]):
        raise ValueError("copy map does not cover the complete volume")
    return result


def _wrap_text(text: str, font: str, size: float, width: float) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            candidate = word if not current else f"{current} {word}"
            if stringWidth(candidate, font, size) <= width:
                current = candidate
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        lines.append("")
    while lines and lines[-1] == "":
        lines.pop()
    return lines


def _fit_body(text: str, width: float, height: float) -> tuple[float, float, list[str]]:
    for size in (18, 17, 16, 15, 14, 13, 12, 11, 10):
        leading = size * 1.38
        lines = _wrap_text(text, "Times-Roman", size, width)
        if len(lines) * leading <= height:
            return float(size), float(leading), lines
    raise ValueError("copy block exceeds deterministic typography zone")


def _draw_asset(c: pdfcanvas.Canvas, path: Path, x: float, y: float, width: float, height: float) -> None:
    with Image.open(path) as image:
        iw, ih = image.size
    scale = min(width / iw, height / ih)
    draw_w, draw_h = iw * scale, ih * scale
    c.drawImage(str(path), x + (width - draw_w) / 2, y + (height - draw_h) / 2, draw_w, draw_h, mask="auto")


def assemble_volume_pdf(
    volume: dict[str, Any],
    manuscript_text: str,
    asset_dir: str | Path,
    output_pdf: str | Path,
    manifest_path: str | Path,
) -> dict[str, Any]:
    copy_map = copy_map_for_volume(volume, manuscript_text)
    assets = Path(asset_dir)
    output = Path(output_pdf)
    output.parent.mkdir(parents=True, exist_ok=True)

    page_width = float(volume["canvas"]["reader_width"])
    page_height = float(volume["canvas"]["reader_height"])
    silver = Color(0.73, 0.73, 0.71)
    dim_silver = Color(0.42, 0.42, 0.40)
    c = pdfcanvas.Canvas(str(output), pagesize=(page_width, page_height), pageCompression=1)
    records: list[dict[str, Any]] = []

    for page in volume["pages"]:
        c.setFillColor(black)
        c.rect(0, 0, page_width, page_height, stroke=0, fill=1)

        margin = 44.0
        header_y = page_height - 48.0
        c.setFillColor(silver)
        c.setFont("Courier", 13)
        c.drawString(margin, header_y, page["page_id"])
        c.drawCentredString(page_width / 2, header_y, f"PAGE {page['page_number']}")
        title = str(page["title"])
        c.drawRightString(page_width - margin, header_y, title)

        c.setFillColor(dim_silver)
        c.setFont("Courier", 10)
        c.drawString(margin, header_y - 24, f"{page['issue']} / {page['display_label']}")
        c.drawRightString(page_width - margin, header_y - 24, page["function_code"])

        asset_path = next(
            (candidate for ext in (".png", ".jpg", ".jpeg", ".webp")
             if (candidate := assets / f"{page['page_id']}{ext}").exists()),
            None,
        )
        image_x, image_y = margin, 365.0
        image_w, image_h = page_width - margin * 2, page_height - 500.0
        if asset_path is not None:
            _draw_asset(c, asset_path, image_x, image_y, image_w, image_h)
        else:
            c.setStrokeColor(dim_silver)
            c.setLineWidth(0.6)
            c.rect(image_x, image_y, image_w, image_h, stroke=1, fill=0)
            c.setFont("Courier", 11)
            c.drawCentredString(page_width / 2, image_y + image_h / 2, "VISUAL ASSET RESERVED - RENDER GATE CLOSED")

        body = copy_map[page["page_id"]]
        text_x, text_y, text_w, text_h = margin, 56.0, page_width - margin * 2, 260.0
        size, leading, lines = _fit_body(body, text_w, text_h)
        c.setFillColor(silver)
        c.setFont("Times-Roman", size)
        cursor = text_y + text_h
        for line in lines:
            cursor -= leading
            if line:
                c.drawString(text_x, cursor, line)

        c.setFillColor(dim_silver)
        c.setFont("Courier", 9)
        c.drawString(margin, 24, volume["volume_id"])
        c.drawRightString(page_width - margin, 24, "DETERMINISTIC TYPE LAYER")
        c.showPage()
        records.append({
            "page_id": page["page_id"],
            "asset": str(asset_path) if asset_path else None,
            "copy_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "body_font": "Times-Roman",
            "metadata_font": "Courier",
            "body_size": size,
            "body_leading": leading,
        })

    c.save()
    manifest = {
        "status": "ASSEMBLED",
        "volume_id": volume["volume_id"],
        "page_count": len(records),
        "output_pdf": str(output),
        "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "authoritative_text_in_image": False,
        "records": records,
    }
    dump_json(manifest, manifest_path)
    return manifest
