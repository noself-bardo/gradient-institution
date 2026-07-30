#!/usr/bin/env python3
"""Fail-closed validator for the bounded Case 19 component-production packet."""

from __future__ import annotations

import hashlib
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SVG_NS = "{http://www.w3.org/2000/svg}"

REQUIRED = [
    ROOT / "00_CONTROL" / "COMPONENT_PRODUCTION_AUTHORIZATION.json",
    ROOT / "01_ARTIFACT" / "CASE19_ARTIFACT_MASTER_v1.0.svg",
    ROOT / "01_ARTIFACT" / "CASE19_ARTIFACT_REVIEW_v1.0.png",
    ROOT / "01_ARTIFACT" / "CASE19_ARTIFACT_MASTER_NOTES_v1.0.md",
    ROOT / "02_COPY" / "CASE19_FOUR_PAGE_COPY_v1.0.md",
    ROOT / "03_TYPOGRAPHY" / "CASE19_PAGE_01_TYPE_v1.0.svg",
    ROOT / "03_TYPOGRAPHY" / "CASE19_PAGE_02_TYPE_v1.0.svg",
    ROOT / "03_TYPOGRAPHY" / "CASE19_PAGE_03_TYPE_v1.0.svg",
    ROOT / "03_TYPOGRAPHY" / "CASE19_PAGE_04_TYPE_v1.0.svg",
    ROOT / "04_LAYOUT" / "CASE19_LAYOUT_SPEC_v1.0.json",
    ROOT / "05_REVIEW" / "CASE19_TYPOGRAPHY_CONTACT_SHEET_v1.0.png",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    raise RuntimeError(message)


def validate() -> dict:
    for path in REQUIRED:
        if not path.is_file() or path.stat().st_size == 0:
            fail(f"missing or empty required file: {path.relative_to(ROOT)}")

    auth = json.loads((ROOT / "00_CONTROL" / "COMPONENT_PRODUCTION_AUTHORIZATION.json").read_text())
    if auth["assembly_authority"] != "CLOSED":
        fail("assembly authority advanced")
    if auth["production_authority"] != "BOUNDED_CASE19_COMPONENTS_ONLY":
        fail("component authority is not properly bounded")

    layout = json.loads((ROOT / "04_LAYOUT" / "CASE19_LAYOUT_SPEC_v1.0.json").read_text())
    if layout["assembly_authority"] != "CLOSED":
        fail("layout specification advanced assembly")
    if layout["inherited_standard"]["canvas_pixels_600ppi"] != [3750, 4950]:
        fail("locked canvas geometry changed")
    if layout["inherited_standard"]["trim_pixels_600ppi"] != [3600, 4800]:
        fail("locked trim geometry changed")
    if len(layout["pages"]) != 4:
        fail("layout specification does not contain exactly four pages")

    artifact = ET.parse(ROOT / "01_ARTIFACT" / "CASE19_ARTIFACT_MASTER_v1.0.svg").getroot()
    if artifact.findall(f".//{SVG_NS}text"):
        fail("artifact master contains semantic typography")
    if artifact.findall(f".//{SVG_NS}image"):
        fail("artifact master embeds raster imagery")
    ids = {node.attrib.get("id") for node in artifact.iter() if node.attrib.get("id")}
    for required_id in {"plank", "grain", "wear", "cut-cavity", "cut-edges"}:
        if required_id not in ids:
            fail(f"artifact editable group absent: {required_id}")

    typography_files = sorted((ROOT / "03_TYPOGRAPHY").glob("CASE19_PAGE_*_TYPE_v1.0.svg"))
    if len(typography_files) != 4:
        fail("expected exactly four typography SVGs")
    for path in typography_files:
        root = ET.parse(path).getroot()
        if root.attrib.get("viewBox") != "0 0 3750 4950":
            fail(f"typography geometry changed: {path.name}")
        if root.findall(f".//{SVG_NS}image"):
            fail(f"typography SVG embeds imagery: {path.name}")
        families = {
            node.attrib["font-family"]
            for node in root.findall(f".//{SVG_NS}text")
            if "font-family" in node.attrib
        }
        if not families or not families.issubset({"Source Serif 4", "IBM Plex Mono"}):
            fail(f"noncanonical font declared in {path.name}: {sorted(families)}")

    with Image.open(ROOT / "01_ARTIFACT" / "CASE19_ARTIFACT_REVIEW_v1.0.png") as im:
        if im.size != (1600, 1000):
            fail(f"artifact review dimensions changed: {im.size}")

    forbidden = [
        ROOT / "ASSEMBLED_PAGE.png",
        ROOT / "ASSEMBLED_PAGE.pdf",
        ROOT / "FINAL_RELEASE.pdf",
    ]
    if any(path.exists() for path in forbidden):
        fail("unauthorized assembly or release artifact detected")

    records = []
    for path in REQUIRED:
        records.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )

    return {
        "packet_id": "CL-C19-COMPONENT-PRODUCTION-001",
        "result": "PASS_FAIL_CLOSED",
        "component_state": "FOUNDER_REVIEW_CANDIDATE",
        "required_files_verified": len(records),
        "artifact_editable": True,
        "artifact_contains_semantic_text": False,
        "typography_layers_verified": 4,
        "canonical_fonts_declared": ["Source Serif 4", "IBM Plex Mono"],
        "assembly_attempted": False,
        "manufacturing_eligibility": "PENDING_FOUNDER_COMPONENT_REVIEW",
        "broader_production_authority": "CLOSED",
        "files": records,
    }


def main() -> int:
    try:
        result = validate()
    except Exception as exc:
        print(f"CL_C19_COMPONENT_PRODUCTION: FAIL_CLOSED: {exc}", file=sys.stderr)
        return 2
    output = ROOT / "00_CONTROL" / "COMPONENT_VALIDATION_RECEIPT.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("CL_C19_COMPONENT_PRODUCTION: PASS_FAIL_CLOSED / FOUNDER_REVIEW_REQUIRED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
