from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT if (ROOT / "RELEASE_MANIFEST_v1.0.json").exists() else ROOT / "releases" / "CL-BUILDER-1.0"
SOURCE = RELEASE / "source"
if SOURCE.exists():
    sys.path.insert(0, str(SOURCE))
else:
    sys.path.insert(0, str(ROOT))

from cl_builder.compiler import compile_volume
from cl_builder.io import load_structured


class ReleaseDistributionTests(unittest.TestCase):
    def test_required_release_files_exist(self) -> None:
        required = {
            "README.md",
            "RELEASE_NOTES_v1.0.md",
            "QUICKSTART_v1.0.md",
            "AUTHORITY_AND_SCOPE_v1.0.md",
            "CL-METHOD-001_v1.0.md",
            "PRODUCTION_WORKFLOW_v1.0.md",
            "HUMAN_GATES_v1.0.md",
            "RENDER_AUTHORIZATION_PROTOCOL_v1.0.md",
            "BOUNDED_REPAIR_PROTOCOL_v1.0.md",
            "QC_STANDARD_v1.0.md",
            "DETERMINISTIC_ASSEMBLY_STANDARD_v1.0.md",
            "CUSTODY_AND_CHECKSUM_PROTOCOL_v1.0.md",
            "REFERENCE_FIXTURE_REGISTER_v1.0.json",
            "RELEASE_MANIFEST_v1.0.json",
            "CHECKSUMS_v1.0.sha256",
        }
        self.assertEqual(set(), {name for name in required if not (RELEASE / name).exists()})

    def test_reference_register_locks_all_three_fixtures(self) -> None:
        register = json.loads((RELEASE / "REFERENCE_FIXTURE_REGISTER_v1.0.json").read_text())
        self.assertEqual(
            ["CL-REF-001", "CL-REF-002", "CL-REF-003"],
            [fixture["reference_id"] for fixture in register["fixtures"]],
        )
        self.assertTrue(all(fixture["frozen"] for fixture in register["fixtures"]))

    def test_release_manifest_is_self_contained(self) -> None:
        manifest = json.loads((RELEASE / "RELEASE_MANIFEST_v1.0.json").read_text())
        self.assertEqual("CL-BUILDER-1.0", manifest["release_id"])
        self.assertTrue(manifest["self_contained"])
        self.assertEqual("CLOSED", manifest["render_gate"])

    def test_distribution_imports_without_repository_parent(self) -> None:
        result = subprocess.run(
            [sys.executable, "-c", "import cl_builder; print(cl_builder.__name__)"],
            cwd=SOURCE,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual("cl_builder", result.stdout.strip())

    def test_four_page_fixture_compiles(self) -> None:
        volume = load_structured(RELEASE / "examples" / "four-page-volume.json")
        profile = load_structured(RELEASE / "profiles" / "crisis-liturgies-expansion-v1.yaml")
        compiled = compile_volume(volume, profile)
        self.assertEqual(4, compiled["page_count"])
        self.assertFalse(compiled["render_authorized"])

    def test_four_page_preflight_passes_with_gate_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "preflight.json"
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "cl_builder.cli",
                    "preflight",
                    str(RELEASE / "examples" / "four-page-volume.json"),
                    "--output",
                    str(output),
                ],
                cwd=SOURCE,
                check=True,
                capture_output=True,
                text=True,
            )
            report = json.loads(output.read_text())
            self.assertEqual("PASS", report["status"])
            self.assertFalse(report["render_authorized"])
            self.assertEqual(4, report["page_count"])


if __name__ == "__main__":
    unittest.main()
