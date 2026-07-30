#!/usr/bin/env python3
"""Positive, negative, determinism, and clean-room tests."""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "pipeline_proof"
COMPILER = PROOF / "case19_readiness_compiler.py"
REQUIREMENTS = PROOF / "CASE_19_PIPELINE_REQUIREMENTS.json"
AUTHORIZATION = PROOF / "PIPELINE_PROOF_AUTHORIZATION.json"
REGISTRY = (
    ROOT
    / "deliverable"
    / "CL-ARCH-RECOVERY-001_RETURN_v1.1"
    / "03_CUSTODY"
    / "CASE_19_ASSET_RECORDS.json"
)
SOURCE_PACKET = (
    ROOT
    / "deliverable"
    / "CL-ARCH-RECOVERY-001_RETURN_v1.1"
    / "09_SOURCE_PACKET"
    / "CL-ARCH-RECOVERY-001_v1.1.zip"
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def invoke(
    requirements: Path,
    registry: Path,
    authorization: Path,
    source_packet: Path,
    workspace_root: Path,
    output: Path,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(COMPILER),
            "--requirements",
            str(requirements),
            "--registry",
            str(registry),
            "--authorization",
            str(authorization),
            "--source-packet",
            str(source_packet),
            "--workspace-root",
            str(workspace_root),
            "--output",
            str(output),
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    results = []
    with tempfile.TemporaryDirectory(prefix="cl-c19-proof-") as raw_tmp:
        tmp = Path(raw_tmp)

        baseline_a = tmp / "baseline-a.json"
        baseline_b = tmp / "baseline-b.json"
        run_a = invoke(REQUIREMENTS, REGISTRY, AUTHORIZATION, SOURCE_PACKET, ROOT, baseline_a)
        run_b = invoke(REQUIREMENTS, REGISTRY, AUTHORIZATION, SOURCE_PACKET, ROOT, baseline_b)
        baseline_pass = run_a.returncode == 0 and run_b.returncode == 0
        deterministic = baseline_pass and sha(baseline_a) == sha(baseline_b)
        receipt = json.loads(baseline_a.read_text(encoding="utf-8")) if baseline_pass else {}
        blocked_correctly = (
            receipt.get("ruling") == "PIPELINE_PROOF_PASS_FAIL_CLOSED"
            and receipt.get("manufacturing_eligibility") == "NOT_ELIGIBLE"
            and receipt.get("assembly_attempted") is False
            and len(receipt.get("blocked_components", [])) == 5
        )
        results.extend(
            [
                {"test": "baseline", "result": "PASS" if baseline_pass else "FAIL"},
                {"test": "deterministic_receipt", "result": "PASS" if deterministic else "FAIL"},
                {
                    "test": "correct_missing_component_block",
                    "result": "PASS" if blocked_correctly else "FAIL",
                },
            ]
        )

        bad_requirements = json.loads(REQUIREMENTS.read_text(encoding="utf-8"))
        bad_requirements["authority_gates"]["image_generation"] = "GRANTED"
        bad_req_path = tmp / "bad-authority.json"
        write_json(bad_req_path, bad_requirements)
        bad_auth = invoke(
            bad_req_path, REGISTRY, AUTHORIZATION, SOURCE_PACKET, ROOT, tmp / "bad-auth-out.json"
        )
        results.append(
            {
                "test": "illegal_authority_advance",
                "result": "PASS" if bad_auth.returncode == 2 else "FAIL",
            }
        )

        illegal_eligibility = json.loads(REQUIREMENTS.read_text(encoding="utf-8"))
        for component in illegal_eligibility["assembly_requirements"]:
            component["present"] = True
            component["observed_state"] = "FOUNDER_APPROVED"
        illegal_path = tmp / "illegal-eligibility.json"
        write_json(illegal_path, illegal_eligibility)
        illegal_run = invoke(
            illegal_path,
            REGISTRY,
            AUTHORIZATION,
            SOURCE_PACKET,
            ROOT,
            tmp / "illegal-out.json",
        )
        results.append(
            {
                "test": "illegal_assembly_advance",
                "result": "PASS" if illegal_run.returncode == 2 else "FAIL",
            }
        )

        bad_registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        bad_registry["assets"][0]["sha256"] = "0" * 64
        bad_registry_path = tmp / "bad-registry.json"
        write_json(bad_registry_path, bad_registry)
        tamper_run = invoke(
            REQUIREMENTS,
            bad_registry_path,
            AUTHORIZATION,
            SOURCE_PACKET,
            ROOT,
            tmp / "tamper-out.json",
        )
        results.append(
            {
                "test": "checksum_tamper",
                "result": "PASS" if tamper_run.returncode == 2 else "FAIL",
            }
        )

        clean_root = tmp / "clean-room"
        clean_root.mkdir()
        shutil.copytree(PROOF, clean_root / "pipeline_proof")
        shutil.copytree(ROOT / "nested" / "case19", clean_root / "nested" / "case19")
        (clean_root / "custody").mkdir()
        shutil.copy2(REGISTRY, clean_root / "custody" / REGISTRY.name)
        shutil.copy2(SOURCE_PACKET, clean_root / "custody" / SOURCE_PACKET.name)
        clean_run = subprocess.run(
            [
                sys.executable,
                str(clean_root / "pipeline_proof" / "case19_readiness_compiler.py"),
                "--requirements",
                str(clean_root / "pipeline_proof" / REQUIREMENTS.name),
                "--registry",
                str(clean_root / "custody" / REGISTRY.name),
                "--authorization",
                str(clean_root / "pipeline_proof" / AUTHORIZATION.name),
                "--source-packet",
                str(clean_root / "custody" / SOURCE_PACKET.name),
                "--workspace-root",
                str(clean_root),
                "--output",
                str(clean_root / "clean-room-receipt.json"),
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        clean_deterministic = (
            clean_run.returncode == 0
            and baseline_pass
            and sha(clean_root / "clean-room-receipt.json") == sha(baseline_a)
        )
        results.append(
            {
                "test": "clean_room",
                "result": "PASS" if clean_deterministic else "FAIL",
            }
        )

        passed = all(item["result"] == "PASS" for item in results)
        output = {
            "proof_id": "CL-C19-PIPELINE-PROOF-001",
            "result": "PASS" if passed else "FAIL",
            "tests": results,
            "baseline_receipt_sha256": sha(baseline_a) if baseline_pass else None,
            "clean_room_receipt_sha256": (
                sha(clean_root / "clean-room-receipt.json")
                if clean_run.returncode == 0
                else None
            ),
        }
        (PROOF / "TEST_RESULTS.json").write_text(
            json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        if baseline_pass:
            shutil.copy2(baseline_a, PROOF / "CASE_19_PIPELINE_PROOF_RECEIPT.json")

    print(
        "CL_C19_PIPELINE_PROOF_TESTS: "
        + ("PASS / FAIL_CLOSED / CLEAN_ROOM_REPRODUCIBLE" if passed else "FAIL")
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

