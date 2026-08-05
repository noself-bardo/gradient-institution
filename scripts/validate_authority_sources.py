"""Validate source-reference completeness and authority resolution ordering."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> dict:
    return json.loads((ROOT / "00_CONTROL" / path).read_text(encoding="utf-8"))

def main() -> int:
    errors: list[str] = []
    sources = read("SOURCE_ACCESS_REGISTER.yaml")["sources"]
    required = {"source_system", "source_title", "stable_source_id", "source_path_or_url",
                "inspected_at", "authority_scope", "verification_method"}
    source_ids = set()
    for source in sources:
        source_ids.add(source.get("source_id"))
        missing = required - set(source)
        if missing:
            errors.append(f"{source.get('source_id')}: missing {sorted(missing)}")
    authority = read("AUTHORITY_REGISTER.yaml")
    expected = ["explicit_human_ratification", "current_general_constitutional_law",
                "project_local_constitution_or_production_law",
                "explicit_supersession_and_continuity_records",
                "current_project_control_or_closure_records",
                "canonical_repository_evidence", "historical_and_secondary_sources"]
    if authority.get("resolution_order") != expected:
        errors.append("authority resolution order does not match required precedence")
    if len(source_ids) != len(sources):
        errors.append("duplicate source_id")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"PASS: {len(sources)} complete source records; authority precedence is valid")
    return 0

if __name__ == "__main__":
    sys.exit(main())
