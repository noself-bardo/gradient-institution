from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from cl_corpus.canonical import sha256_bytes, sha256_object
from cl_corpus.orchestrator import run_intake
from cl_corpus.schema import validate_instance


ROOT = Path(__file__).resolve().parents[1]
SIM = ROOT / "simulations" / "CL-CORPUS-SIM-001"
FIXED_TIME = "2026-08-04T20:00:00Z"


class CorpusTests(unittest.TestCase):
    def test_intake_contract_validates(self) -> None:
        config = json.loads((SIM / "intake.json").read_text(encoding="utf-8"))
        validate_instance(config, ROOT / "schemas" / "intake.schema.json")

    def test_cold_simulation_emits_single_canonical_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            report = run_intake(SIM / "intake.json", output, created_at=FIXED_TIME)
            self.assertEqual(report["status"], "HANDOFF_READY")
            self.assertEqual(report["current_state"], "AWAITING_CONVERSION_ARCHITECT")
            handoff = json.loads((output / "handoff.json").read_text(encoding="utf-8"))
            validate_instance(handoff, ROOT / "schemas" / "handoff.schema.json")
            self.assertEqual(handoff["package_class"], "CL-CORPUS-HANDOFF-1.0.0")
            self.assertEqual(handoff["intended_recipient"], "CL-CONV-001")
            self.assertEqual(len(handoff["source_inventory"]), 3)
            self.assertTrue(all(value is False for value in handoff["production_gates"].values()))
            self.assertFalse(report["render_authorized"])

    def test_cold_simulation_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first"
            second = Path(tmp) / "second"
            run_intake(SIM / "intake.json", first, created_at=FIXED_TIME)
            run_intake(SIM / "intake.json", second, created_at=FIXED_TIME)
            for name in ["handoff.json", "normalized-corpus.txt", "run-report.json", "MANIFEST.sha256", "custody-receipt.json"]:
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes(), name)

    def test_manifest_checksums_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            run_intake(SIM / "intake.json", output, created_at=FIXED_TIME)
            for line in (output / "MANIFEST.sha256").read_text(encoding="ascii").splitlines():
                digest, name = line.split("  ", 1)
                self.assertEqual(digest, sha256_bytes((output / name).read_bytes()), name)

    def test_committed_cold_receipt_matches_fixture(self) -> None:
        receipt = (ROOT / "control" / "CL-CORPUS-SIM-001_COLD_SIMULATION_RECEIPT.md").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            report = run_intake(SIM / "intake.json", output, created_at=FIXED_TIME)
            handoff = json.loads((output / "handoff.json").read_text(encoding="utf-8"))
            custody = json.loads((output / "custody-receipt.json").read_text(encoding="utf-8"))
            expected = [
                report["source_inventory_sha256"],
                handoff["corpus"]["sha256"],
                handoff["handoff_sha256"],
                custody["files"]["handoff.json"],
                custody["package_manifest_sha256"],
            ]
            for digest in expected:
                self.assertIn(digest, receipt)

    def test_handoff_hash_excludes_only_its_own_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            run_intake(SIM / "intake.json", output, created_at=FIXED_TIME)
            handoff = json.loads((output / "handoff.json").read_text(encoding="utf-8"))
            digest = handoff.pop("handoff_sha256")
            self.assertEqual(digest, sha256_object(handoff))

    def test_missing_consent_fails_closed_and_emits_no_handoff(self) -> None:
        config = json.loads((SIM / "intake.json").read_text(encoding="utf-8"))
        config["authority"]["processing_consent_recorded"] = False
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            config_path = tmp_path / "intake.json"
            config["source_root"] = str((SIM / "raw").resolve())
            config_path.write_text(json.dumps(config), encoding="utf-8")
            output = tmp_path / "out"
            report = run_intake(config_path, output, created_at=FIXED_TIME)
            self.assertEqual(report["status"], "BLOCKED")
            self.assertIn("PROCESSING_CONSENT_REQUIRED", report["blockers"])
            self.assertFalse((output / "handoff.json").exists())

    def test_recorded_consent_requires_record_identifier(self) -> None:
        config = json.loads((SIM / "intake.json").read_text(encoding="utf-8"))
        config["authority"]["consent_record"] = None
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            config_path = tmp_path / "intake.json"
            config["source_root"] = str((SIM / "raw").resolve())
            config_path.write_text(json.dumps(config), encoding="utf-8")
            with self.assertRaises(ValueError):
                run_intake(config_path, tmp_path / "out", created_at=FIXED_TIME)

    def test_sensitive_intake_requires_handling_protocol(self) -> None:
        config = json.loads((SIM / "intake.json").read_text(encoding="utf-8"))
        config["privacy"]["classification"] = "HIGHLY_SENSITIVE"
        config["privacy"]["handling_protocol"] = None
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            config_path = tmp_path / "intake.json"
            config["source_root"] = str((SIM / "raw").resolve())
            config_path.write_text(json.dumps(config), encoding="utf-8")
            report = run_intake(config_path, tmp_path / "out", created_at=FIXED_TIME)
            self.assertIn("SENSITIVE_HANDLING_PROTOCOL_REQUIRED", report["blockers"])

    def test_unextracted_binary_blocks_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "raw"
            source.mkdir()
            (source / "memo.wav").write_bytes(b"RIFF-simulation")
            config = json.loads((SIM / "intake.json").read_text(encoding="utf-8"))
            config["source_root"] = "raw"
            config_path = tmp_path / "intake.json"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            output = tmp_path / "out"
            report = run_intake(config_path, output, created_at=FIXED_TIME)
            self.assertIn("SOURCE_EXTRACTION_REQUIRED", report["blockers"])
            self.assertFalse((output / "handoff.json").exists())

    def test_third_party_material_requires_handling_protocol(self) -> None:
        config = json.loads((SIM / "intake.json").read_text(encoding="utf-8"))
        config["privacy"]["contains_third_party_material"] = True
        config["privacy"]["handling_protocol"] = None
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            config_path = tmp_path / "intake.json"
            config["source_root"] = str((SIM / "raw").resolve())
            config_path.write_text(json.dumps(config), encoding="utf-8")
            report = run_intake(config_path, tmp_path / "out", created_at=FIXED_TIME)
            self.assertIn("THIRD_PARTY_HANDLING_PROTOCOL_REQUIRED", report["blockers"])


if __name__ == "__main__":
    unittest.main()
