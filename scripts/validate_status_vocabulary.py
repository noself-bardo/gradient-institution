"""Validate status and evidence vocabulary definitions and their use."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> dict:
    return json.loads((ROOT / "00_CONTROL" / path).read_text(encoding="utf-8"))

def main() -> int:
    evidence = read("EVIDENCE_VOCABULARY.yaml")["evidence_labels"]
    statuses = read("STATUS_VOCABULARY.yaml")["status_labels"]
    required_evidence = {"DIRECT_SOURCE_VERIFIED", "SECONDARY_BASELINE", "INFERRED",
                         "INCOMPLETE", "INACCESSIBLE", "DISPUTED",
                         "SUPERSEDED_HISTORICAL_RECORD", "VOID_FOR_PRODUCTION",
                         "PENDING_HUMAN_GATE", "TEMPORAL_DIFFERENCE",
                         "METADATA_INCONSISTENCY"}
    errors = []
    if required_evidence - set(evidence):
        errors.append(f"missing evidence labels: {sorted(required_evidence - set(evidence))}")
    if "IMPORTED_CANDIDATE" not in statuses:
        errors.append("missing IMPORTED_CANDIDATE status")
    if any(not description for description in list(evidence.values()) + list(statuses.values())):
        errors.append("vocabulary descriptions must not be empty")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"PASS: {len(evidence)} evidence labels and {len(statuses)} status labels")
    return 0

if __name__ == "__main__":
    sys.exit(main())
