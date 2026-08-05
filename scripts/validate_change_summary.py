"""Validate baseline counts and reject duplicate source/branch accounting."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> dict:
    return json.loads((ROOT / "00_CONTROL" / path).read_text(encoding="utf-8"))

def main() -> int:
    matrix = read("PORTFOLIO_MATRIX.yaml")
    sources = read("SOURCE_ACCESS_REGISTER.yaml")["sources"]
    errors: list[str] = []
    summary = matrix["change_summary"]
    rows = matrix["records"]
    split_rows = sum(len(item["candidate_ids"]) for item in summary["records_split"])
    crisis_rows = len([row for row in rows if row["legacy_id"] == "GRAD-009"])
    if split_rows != crisis_rows:
        errors.append("split change summary does not account for all Crisis Liturgies candidates")
    source_ids = [source["source_id"] for source in sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source IDs would cause duplicate source counting")
    branch_ids = [record.get("branch_id") for record in read("SUPERSESSION_REGISTER.yaml")["records"]
                  if record.get("branch_id")]
    if len(branch_ids) != len(set(branch_ids)):
        errors.append("duplicate branch IDs in supersession register")
    if summary["records_combined"] or summary["records_deferred"]:
        errors.append("unexpected combined or deferred records; update intake report and validator deliberately")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print("PASS: change-summary counts and source/branch accounting are consistent")
    return 0

if __name__ == "__main__":
    sys.exit(main())
