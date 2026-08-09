from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .canonical import sha256_bytes


TEXT_EXTENSIONS = {".txt", ".md", ".markdown"}
STRUCTURED_EXTENSIONS = {".json", ".jsonl", ".csv"}
SUPPORTED_EXTENSIONS = TEXT_EXTENSIONS | STRUCTURED_EXTENSIONS


class IntakeError(ValueError):
    pass


@dataclass(frozen=True)
class CapturedSource:
    source_id: str
    relative_path: str
    media_type: str
    byte_count: int
    sha256: str
    extraction_status: str
    normalized_text: str | None

    def inventory_record(self) -> dict[str, Any]:
        return {
            "source_id": self.source_id,
            "relative_path": self.relative_path,
            "media_type": self.media_type,
            "byte_count": self.byte_count,
            "sha256": self.sha256,
            "extraction_status": self.extraction_status,
        }


def _normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def _extract_text(path: Path, raw: bytes) -> str | None:
    suffix = path.suffix.lower()
    if suffix in TEXT_EXTENSIONS:
        return _normalize_newlines(raw.decode("utf-8-sig"))
    if suffix == ".json":
        value = json.loads(raw.decode("utf-8-sig"))
        return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)
    if suffix == ".jsonl":
        records = [json.loads(line) for line in raw.decode("utf-8-sig").splitlines() if line.strip()]
        return "\n".join(json.dumps(item, ensure_ascii=False, sort_keys=True) for item in records)
    if suffix == ".csv":
        rows = list(csv.reader(raw.decode("utf-8-sig").splitlines()))
        return "\n".join(" | ".join(cell.strip() for cell in row) for row in rows)
    return None


def capture_sources(source_root: Path) -> list[CapturedSource]:
    root = source_root.resolve()
    if not root.is_dir():
        raise IntakeError(f"source_root is not a directory: {source_root}")
    files = sorted((path for path in root.rglob("*") if path.is_file()), key=lambda p: p.relative_to(root).as_posix())
    if not files:
        raise IntakeError("source_root contains no files")
    captured: list[CapturedSource] = []
    for index, path in enumerate(files, start=1):
        raw = path.read_bytes()
        normalized = _extract_text(path, raw)
        captured.append(
            CapturedSource(
                source_id=f"SRC-{index:04d}",
                relative_path=path.relative_to(root).as_posix(),
                media_type=path.suffix.lower().lstrip(".") or "binary",
                byte_count=len(raw),
                sha256=sha256_bytes(raw),
                extraction_status="EXTRACTED" if normalized is not None else "EXTRACTION_REQUIRED",
                normalized_text=normalized,
            )
        )
    return captured
