#!/usr/bin/env python3
import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "04_REFERENCE" / "CASE_19_REFERENCE_IMPLEMENTATION.json"
MACHINE = ROOT / "01_CONTRACT" / "PRODUCTION_STATE_MACHINE.json"

REQUIRED_VIEWS = ("full_evidence", "alternate_or_construction", "macro_or_detail")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def view_valid(view):
    if view.get("state") == "NOT_APPLICABLE":
        return bool(view.get("justification")) and view.get("founder_approved") is True
    return (
        view.get("state") == "FOUNDER_APPROVED"
        and bool(view.get("filename"))
        and len(view.get("sha256", "")) == 64
        and view.get("contains_typography") is False
        and view.get("role") == "PRIMARY_FORENSIC_MASTER"
    )


def validate(record):
    blockers = []
    if record.get("source_custody", {}).get("state") != "VALIDATED":
        blockers.append("SOURCE_CUSTODY_NOT_VALIDATED")
    if record.get("specification", {}).get("state") != "FROZEN":
        blockers.append("SPECIFICATION_NOT_FROZEN")
    if record.get("witness", {}).get("state") not in {
        "VERIFIED_SOURCE_LOCKED", "WITNESS_ABSENT"
    }:
        blockers.append("WITNESS_STATE_UNRESOLVED")
    objects = record.get("objects") or []
    if not objects:
        blockers.append("OBJECT_REGISTER_MISSING")
    for obj in objects:
        views = obj.get("views", {})
        for key in REQUIRED_VIEWS:
            if key not in views or not view_valid(views[key]):
                blockers.append(f"{obj.get('object_id','UNKNOWN')}:{key}:INVALID")
        if obj.get("founder_disposition") != "APPROVED":
            blockers.append(f"{obj.get('object_id','UNKNOWN')}:ARTIFACT_NOT_APPROVED")
    components = record.get("components", {})
    for key in ("copy", "svg_typography", "layout"):
        if components.get(key) != "APPROVED":
            blockers.append(f"COMPONENT_{key.upper()}_NOT_APPROVED")
    if components.get("provenance") != "COMPLETE":
        blockers.append("PROVENANCE_INCOMPLETE")
    assembly = record.get("assembly", {})
    if assembly.get("state") != "COMPLETE" or assembly.get("pages") != 4:
        blockers.append("ASSEMBLY_INCOMPLETE")
    if assembly.get("text_is_editable") is not True:
        blockers.append("TEXT_NOT_EDITABLE")
    if assembly.get("artifact_layers_are_separate") is not True:
        blockers.append("ARTIFACT_LAYERS_NOT_SEPARATE")
    qc = record.get("qc", {})
    if qc.get("structural") != "PASS":
        blockers.append("STRUCTURAL_QC_NOT_PASS")
    if qc.get("rendered_visual") != "PASS":
        blockers.append("RENDERED_VISUAL_QC_NOT_PASS")
    if qc.get("true_polarity_reviewed") is not True:
        blockers.append("TRUE_POLARITY_NOT_REVIEWED")
    return blockers


def main():
    reference = load(REFERENCE)
    machine = load(MACHINE)
    baseline = validate(reference)
    tests = {"baseline_case19_reference": baseline == []}

    mutations = {}
    r = copy.deepcopy(reference)
    r["objects"] = []
    mutations["missing_object_register"] = r

    r = copy.deepcopy(reference)
    del r["objects"][0]["views"]["full_evidence"]
    mutations["missing_full_evidence"] = r

    r = copy.deepcopy(reference)
    r["objects"][0]["views"]["full_evidence"]["role"] = "SECONDARY_DIAGRAM"
    mutations["vector_substitution"] = r

    r = copy.deepcopy(reference)
    r["objects"][0]["founder_disposition"] = "PENDING"
    mutations["artifact_not_founder_approved"] = r

    r = copy.deepcopy(reference)
    r["assembly"]["text_is_editable"] = False
    mutations["image_baked_text"] = r

    r = copy.deepcopy(reference)
    r["qc"]["rendered_visual"] = "NOT_RUN"
    mutations["missing_rendered_visual_qc"] = r

    for name, record in mutations.items():
        tests[name] = len(validate(record)) > 0

    expected_terminal = machine.get("terminal_nonproduction_state")
    tests["terminal_state_matches_reference"] = (
        reference.get("state") == expected_terminal
    )
    tests["publication_not_implied"] = "publication" in machine.get("not_implied", [])
    tests["other_case_authority_not_implied"] = (
        "production authority for another case" in machine.get("not_implied", [])
    )

    result = "PASS_FAIL_CLOSED" if all(tests.values()) else "FAIL"
    output = {"result": result, "tests": tests, "baseline_blockers": baseline}
    print(json.dumps(output, indent=2))
    return 0 if result == "PASS_FAIL_CLOSED" else 1


if __name__ == "__main__":
    sys.exit(main())
