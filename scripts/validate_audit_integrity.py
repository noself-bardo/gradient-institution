"""Validate audit inventories and historical-source boundaries."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(name: str) -> dict:
    return json.loads((ROOT / "00_CONTROL" / name).read_text(encoding="utf-8"))

def main() -> int:
    errors: list[str] = []
    notion = read("NOTION_SOURCE_INVENTORY.yaml")
    repo = read("REPOSITORY_SOURCE_INVENTORY.yaml")
    matrix = read("PORTFOLIO_MATRIX.yaml")
    ids = [p["page_id"] for p in notion["pages"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate Notion page IDs")
    required = {"page_id", "title", "url", "authority_scope", "status", "supports", "supersession"}
    for page in notion["pages"]:
        missing = required - set(page)
        if missing:
            errors.append(f"{page.get('page_id')}: missing retrieval metadata {sorted(missing)}")
    candidate_ids = {r["candidate_id"] for r in matrix["records"]}
    for page in notion["pages"]:
        unknown = set(page["supports"]) - candidate_ids
        if unknown:
            errors.append(f"{page['page_id']}: unknown candidate refs {sorted(unknown)}")
    if any(p["evidence"] == "DIRECT_SOURCE_VERIFIED" and "Drive" in p["path"] for p in repo["material_sources"]):
        errors.append("inaccessible Drive path represented as directly verified")
    source_text = (ROOT / "00_CONTROL" / "SOURCE_ACCESS_REGISTER.yaml").read_text(encoding="utf-8")
    if "agent-a617894e" in source_text or "/home/workspace" in source_text:
        errors.append("absolute private runtime path represented as canonical source")
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1
    print(f"PASS: {len(ids)} direct Notion records, {len(repo['material_sources'])} repository sources, no private-path or Drive-evidence violation")
    return 0

if __name__ == "__main__":
    sys.exit(main())
