"""Validate deterministic repository census and contradiction provenance."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(name: str) -> dict:
    return json.loads((ROOT / "00_CONTROL" / name).read_text(encoding="utf-8"))

def main() -> int:
    errors: list[str] = []
    census = read("REPOSITORY_SOURCE_INVENTORY.yaml")["supplemental_read_only_findings"]["deterministic_census"]
    top = census["files_by_top_level"]
    total = census["root_level_tracked_files"] + sum(top.values())
    if total != census["total_tracked_files_on_audit_branch"]:
        errors.append(f"census arithmetic {total} != {census['total_tracked_files_on_audit_branch']}")
    expected_total = (
        census["tracked_files_at_base"]
        + census.get("files_added_to_main_after_audit_base", 0)
        + census["files_added_on_audit_branch_before_current_pass"]
    )
    if expected_total != census["total_tracked_files_on_audit_branch"]:
        errors.append("base plus main additions plus audit additions census arithmetic does not balance")
    contradictions = read("CONTRADICTION_REGISTER.yaml")["records"]
    con2 = next((r for r in contradictions if r["record_id"] == "CON-002"), None)
    con3 = next((r for r in contradictions if r["record_id"] == "CON-003"), None)
    if not con2 or "SRC-GITHUB-AUDIT-20260729" not in con2["source_refs"]:
        errors.append("CON-002 lacks direct GitHub audit provenance")
    if not con3 or not any(ref.startswith("REPOSITORY_SOURCE_INVENTORY.yaml@") for ref in con3["source_refs"]):
        errors.append("CON-003 lacks direct repository-audit provenance")
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1
    print(f"PASS: census balances at {total} files; contradiction provenance is direct")
    return 0

if __name__ == "__main__":
    sys.exit(main())
