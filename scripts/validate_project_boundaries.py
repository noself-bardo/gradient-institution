"""Prevent a parent candidate from inheriting a child candidate's status."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    matrix = json.loads((ROOT / "00_CONTROL" / "PORTFOLIO_MATRIX.yaml").read_text(encoding="utf-8"))
    rows = {row["candidate_id"]: row for row in matrix["records"]}
    errors: list[str] = []
    for row in rows.values():
        parent_id = row.get("parent_candidate_id")
        if parent_id:
            parent = rows.get(parent_id)
            if not parent:
                errors.append(f"{row['candidate_id']}: parent does not exist")
            elif parent["status"] != "IMPORTED_CANDIDATE" and parent["status"] == row["status"]:
                errors.append(f"{row['candidate_id']}: parent status appears inherited")
    crisis = [row for row in rows.values() if row["legacy_id"] == "GRAD-009"]
    expected = {"CAND-009A", "CAND-009B", "CAND-009C", "CAND-009D", "CAND-009E", "CAND-009F"}
    if {row["candidate_id"] for row in crisis} != expected:
        errors.append("Crisis Liturgies boundary split is incomplete or changed without validator update")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"PASS: {len(crisis)} Crisis Liturgies candidate boundaries; no inherited child status")
    return 0

if __name__ == "__main__":
    sys.exit(main())
