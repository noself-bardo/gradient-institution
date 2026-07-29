"""Validate the JSON-compatible YAML portfolio baseline."""
from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def load(name: str) -> dict:
    return json.loads((ROOT / "00_CONTROL" / name).read_text(encoding="utf-8"))

def main() -> int:
    matrix = load("PORTFOLIO_MATRIX.yaml")
    evidence = set(load("EVIDENCE_VOCABULARY.yaml")["evidence_labels"])
    statuses = set(load("STATUS_VOCABULARY.yaml")["status_labels"])
    sources = {s["source_id"] for s in load("SOURCE_ACCESS_REGISTER.yaml")["sources"]}
    errors: list[str] = []
    ids: set[str] = set()
    legacy_ids: set[str] = set()
    for row in matrix["records"]:
        for field in matrix["required_row_fields"]:
            if field not in row:
                errors.append(f"{row.get('candidate_id', '<missing>')}: missing {field}")
        candidate_id = row.get("candidate_id")
        if candidate_id in ids:
            errors.append(f"duplicate candidate_id: {candidate_id}")
        ids.add(candidate_id)
        legacy_ids.add(row.get("legacy_id"))
        if row.get("status") not in statuses:
            errors.append(f"{candidate_id}: invalid status")
        for source_ref in row.get("source_refs", []):
            if source_ref not in sources:
                errors.append(f"{candidate_id}: unknown source {source_ref}")
        for field, metadata in row.get("field_evidence", {}).items():
            if metadata.get("evidence_label") not in evidence:
                errors.append(f"{candidate_id}.{field}: invalid evidence label")
            if not metadata.get("source_refs") or "supersession_check" not in metadata:
                errors.append(f"{candidate_id}.{field}: incomplete field evidence")
            for source_ref in metadata.get("source_refs", []):
                if source_ref not in sources:
                    errors.append(f"{candidate_id}.{field}: unknown source {source_ref}")
    summary = matrix["change_summary"]
    if len(ids) != summary["candidate_records_created"]:
        errors.append("candidate_records_created does not match records")
    if len(legacy_ids) != summary["legacy_records_imported"]:
        errors.append("legacy_records_imported does not match distinct legacy IDs")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"PASS: {len(ids)} candidate rows; {len(legacy_ids)} legacy records; field evidence complete")
    return 0

if __name__ == "__main__":
    sys.exit(main())
