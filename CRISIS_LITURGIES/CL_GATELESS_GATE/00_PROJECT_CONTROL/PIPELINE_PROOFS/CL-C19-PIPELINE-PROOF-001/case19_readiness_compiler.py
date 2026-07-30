#!/usr/bin/env python3
"""Deterministic Case 19 readiness compiler.

This program verifies the frozen custody inputs and evaluates whether the
component contract permits assembly. It never creates, transforms, assembles,
or renders production assets.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path


NORMAL_STATES = [
    "DISCOVERED",
    "REGISTERED",
    "VERIFIED",
    "ELIGIBLE",
    "PRODUCED",
    "QC_PASSED",
    "FOUNDER_APPROVED",
    "ASSEMBLY_ELIGIBLE",
]


class ProofFailure(RuntimeError):
    pass


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProofFailure(f"Cannot read valid JSON: {path}: {exc}") from exc


def resolve_zip_member(names: set[str], container_path: str) -> str:
    if "::" not in container_path:
        raise ProofFailure(f"Asset is not registered inside the source packet: {container_path}")
    requested = container_path.split("::", 1)[1]
    matches = [name for name in names if name == requested or name.endswith("/" + requested)]
    if len(matches) != 1:
        raise ProofFailure(
            f"Expected exactly one source-packet member for {requested}; found {len(matches)}"
        )
    return matches[0]


def state_satisfies(observed: str, required: str) -> bool:
    if observed not in NORMAL_STATES or required not in NORMAL_STATES:
        return observed == required
    return NORMAL_STATES.index(observed) >= NORMAL_STATES.index(required)


def compile_receipt(
    requirements_path: Path,
    registry_path: Path,
    authority_path: Path,
    source_packet_path: Path,
    workspace_root: Path,
) -> dict:
    requirements = load_json(requirements_path)
    registry = load_json(registry_path)
    authorization = load_json(authority_path)

    if requirements.get("mode") != "READINESS_ONLY_NO_ASSEMBLY":
        raise ProofFailure("Proof mode must remain READINESS_ONLY_NO_ASSEMBLY")
    if authorization.get("production_authority") != "CLOSED_EXCEPT_CONTROL_PLANE_PROOF":
        raise ProofFailure("Pipeline-proof authorization boundary is missing or illegally changed")
    if authorization.get("authorized_by") != "Steven, Founder":
        raise ProofFailure("Founder authorization identity is missing")

    forbidden_grants = {
        key: value
        for key, value in requirements["authority_gates"].items()
        if key != "pipeline_proof_control_plane" and value != "NOT_GRANTED"
    }
    if forbidden_grants:
        raise ProofFailure(f"Illegal production authority advance: {sorted(forbidden_grants)}")
    if requirements["authority_gates"].get("pipeline_proof_control_plane") != "GRANTED":
        raise ProofFailure("Control-plane proof authority is not granted")

    spec = requirements["frozen_specification"]
    spec_path = workspace_root / spec["path"]
    if not spec_path.is_file():
        raise ProofFailure(f"Frozen specification missing: {spec_path}")
    observed_spec_sha = sha256_file(spec_path)
    if observed_spec_sha != spec["sha256"]:
        raise ProofFailure("Frozen specification checksum mismatch")

    if not source_packet_path.is_file():
        raise ProofFailure(f"Sealed source packet missing: {source_packet_path}")

    assets = registry.get("assets")
    if not isinstance(assets, list):
        raise ProofFailure("Custody registry has no assets array")
    by_id = {}
    for asset in assets:
        asset_id = asset.get("asset_id")
        if not asset_id or asset_id in by_id:
            raise ProofFailure(f"Missing or duplicate asset ID: {asset_id}")
        by_id[asset_id] = asset

    required_ids = requirements["custody_requirements"]["required_asset_ids"]
    quarantined_ids = requirements["custody_requirements"]["quarantined_asset_ids"]
    expected_ids = set(required_ids + quarantined_ids)
    if set(by_id) != expected_ids:
        missing = sorted(expected_ids - set(by_id))
        unregistered = sorted(set(by_id) - expected_ids)
        raise ProofFailure(
            f"Custody registry coverage mismatch; missing={missing}; unexpected={unregistered}"
        )

    custody_checks = []
    with zipfile.ZipFile(source_packet_path) as archive:
        names = set(archive.namelist())
        for asset_id in sorted(expected_ids):
            asset = by_id[asset_id]
            member = resolve_zip_member(names, asset["container_path"])
            payload = archive.read(member)
            observed_sha = sha256_bytes(payload)
            observed_bytes = len(payload)
            if observed_sha != asset["sha256"]:
                raise ProofFailure(f"Checksum mismatch for {asset_id}")
            if observed_bytes != asset["bytes"]:
                raise ProofFailure(f"Byte-count mismatch for {asset_id}")
            if asset_id in required_ids and asset["status"] != "VERIFIED":
                raise ProofFailure(f"Required asset {asset_id} is not VERIFIED")
            if asset_id in quarantined_ids and asset["status"] != "QUARANTINED":
                raise ProofFailure(f"Expected quarantined asset {asset_id} changed state")
            custody_checks.append(
                {
                    "asset_id": asset_id,
                    "status": asset["status"],
                    "sha256": observed_sha,
                    "bytes": observed_bytes,
                }
            )

    approved_tx_id = requirements["custody_requirements"]["approved_transcription_asset_id"]
    approved_tx_authority = requirements["custody_requirements"][
        "approved_transcription_authority_id"
    ]
    approved_tx = by_id.get(approved_tx_id)
    if not approved_tx or approved_tx.get("authority_record_id") != approved_tx_authority:
        raise ProofFailure("Approved transcription treatment authority link is broken")

    blocked_components = []
    ready_components = []
    for component in requirements["assembly_requirements"]:
        present = component.get("present") is True
        observed = component.get("observed_state")
        required = component.get("required_state")
        if present and state_satisfies(observed, required):
            ready_components.append(component["component_id"])
        else:
            blocked_components.append(
                {
                    "component_id": component["component_id"],
                    "label": component["label"],
                    "present": present,
                    "observed_state": observed,
                    "required_state": required,
                }
            )

    manufacturing_eligibility = "ELIGIBLE" if not blocked_components else "NOT_ELIGIBLE"
    if manufacturing_eligibility == "ELIGIBLE":
        raise ProofFailure(
            "This proof is not authorized to assemble; an eligible manifest must enter a separate gate"
        )

    receipt = {
        "proof_id": requirements["proof_id"],
        "case_id": requirements["case_id"],
        "case_title": requirements["case_title"],
        "compiler_mode": requirements["mode"],
        "authorization_id": authorization["authorization_id"],
        "frozen_specification": {
            "sha256": observed_spec_sha,
            "state": spec["state"],
        },
        "source_packet": {
            "sha256": sha256_file(source_packet_path),
            "registered_assets_verified": len(custody_checks),
        },
        "custody_checks": custody_checks,
        "ready_components": ready_components,
        "blocked_components": blocked_components,
        "manufacturing_eligibility": manufacturing_eligibility,
        "assembly_attempted": False,
        "creative_actions_performed": [],
        "production_gates": requirements["authority_gates"],
        "ruling": "PIPELINE_PROOF_PASS_FAIL_CLOSED",
        "founder_review_gate": "READY",
        "recommended_disposition": "ACCEPT_PIPELINE_PROOF_AND_OPEN_BOUNDED_COMPONENT_PRODUCTION",
    }
    if receipt["ruling"] != requirements["expected_ruling"]:
        raise ProofFailure("Unexpected proof ruling")
    if manufacturing_eligibility != requirements["expected_manufacturing_eligibility"]:
        raise ProofFailure("Unexpected manufacturing eligibility")
    return receipt


def canonical_json(value: dict) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--requirements", required=True, type=Path)
    parser.add_argument("--registry", required=True, type=Path)
    parser.add_argument("--authorization", required=True, type=Path)
    parser.add_argument("--source-packet", required=True, type=Path)
    parser.add_argument("--workspace-root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        receipt = compile_receipt(
            args.requirements,
            args.registry,
            args.authorization,
            args.source_packet,
            args.workspace_root,
        )
    except ProofFailure as exc:
        print(f"CL_C19_PIPELINE_PROOF: FAIL_CLOSED: {exc}", file=sys.stderr)
        return 2

    rendered = canonical_json(receipt)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print("CL_C19_PIPELINE_PROOF: PASS_FAIL_CLOSED / MANUFACTURING_NOT_ELIGIBLE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
