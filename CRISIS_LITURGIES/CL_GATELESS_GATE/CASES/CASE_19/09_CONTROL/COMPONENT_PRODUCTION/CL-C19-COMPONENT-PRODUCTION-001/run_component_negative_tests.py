#!/usr/bin/env python3
"""Negative tests for the bounded Case 19 component packet validator."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_REL = Path("00_CONTROL/validate_component_production.py")


def run(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / VALIDATOR_REL)],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def mutate_json(path: Path, key: str, value: object) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    data[key] = value
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    tests = []
    with tempfile.TemporaryDirectory(prefix="cl-c19-components-") as raw:
        tmp = Path(raw)

        baseline = tmp / "baseline"
        shutil.copytree(ROOT, baseline)
        tests.append({"test": "baseline", "pass": run(baseline).returncode == 0})

        missing = tmp / "missing"
        shutil.copytree(ROOT, missing)
        (missing / "02_COPY/CASE19_FOUR_PAGE_COPY_v1.0.md").unlink()
        tests.append({"test": "missing_component", "pass": run(missing).returncode == 2})

        assembly = tmp / "assembly"
        shutil.copytree(ROOT, assembly)
        (assembly / "ASSEMBLED_PAGE.png").write_bytes(b"forbidden")
        tests.append({"test": "illegal_assembly_artifact", "pass": run(assembly).returncode == 2})

        authority = tmp / "authority"
        shutil.copytree(ROOT, authority)
        mutate_json(
            authority / "00_CONTROL/COMPONENT_PRODUCTION_AUTHORIZATION.json",
            "assembly_authority",
            "GRANTED",
        )
        tests.append({"test": "illegal_authority_advance", "pass": run(authority).returncode == 2})

        font = tmp / "font"
        shutil.copytree(ROOT, font)
        svg = font / "03_TYPOGRAPHY/CASE19_PAGE_01_TYPE_v1.0.svg"
        svg.write_text(
            svg.read_text(encoding="utf-8").replace("Source Serif 4", "Arial", 1),
            encoding="utf-8",
        )
        tests.append({"test": "noncanonical_font", "pass": run(font).returncode == 2})

        embedded = tmp / "embedded"
        shutil.copytree(ROOT, embedded)
        svg = embedded / "01_ARTIFACT/CASE19_ARTIFACT_MASTER_v1.0.svg"
        svg.write_text(
            svg.read_text(encoding="utf-8").replace(
                "</svg>", '<image href="data:image/png;base64,AA=="/></svg>'
            ),
            encoding="utf-8",
        )
        tests.append({"test": "embedded_raster_in_master", "pass": run(embedded).returncode == 2})

    passed = all(item["pass"] for item in tests)
    result = {
        "packet_id": "CL-C19-COMPONENT-PRODUCTION-001",
        "result": "PASS" if passed else "FAIL",
        "tests": [
            {"test": item["test"], "result": "PASS" if item["pass"] else "FAIL"}
            for item in tests
        ],
    }
    (ROOT / "00_CONTROL/TEST_RESULTS.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        "CL_C19_COMPONENT_NEGATIVE_TESTS: "
        + ("PASS / FAIL_CLOSED" if passed else "FAIL")
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
