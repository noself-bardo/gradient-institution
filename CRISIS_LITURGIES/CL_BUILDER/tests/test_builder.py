from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

from cl_builder.compiler import CompileError, compile_volume
from cl_builder.io import load_structured
from cl_builder.qc import inspect_image
from cl_builder.schema import validate_instance


ROOT = Path(__file__).resolve().parents[1]
VOLUME_PATH = ROOT / "volumes" / "CL-EV-001" / "volume.yaml"
PROFILE_PATH = ROOT / "profiles" / "crisis-liturgies-expansion-v1.yaml"


class BuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.volume = load_structured(VOLUME_PATH)
        cls.profile = load_structured(PROFILE_PATH)

    def test_volume_and_page_schema(self) -> None:
        validate_instance(self.volume, ROOT / "schemas", "volume")
        self.assertEqual(len(self.volume["pages"]), 48)
        for page in self.volume["pages"]:
            validate_instance(page, ROOT / "schemas", "page")

    def test_compiler_emits_48_packets_and_strips_legacy_gate(self) -> None:
        compiled = compile_volume(self.volume, self.profile)
        self.assertEqual(compiled["page_count"], 48)
        for packet in compiled["render_packets"]:
            validate_instance(packet, ROOT / "schemas", "render-packet")
            self.assertNotIn("INTIFADA", packet["prompt"])
            self.assertNotIn("IMAGE GATE", packet["prompt"])
            self.assertEqual(packet["canvas"]["background_hex"], "#000000")
            self.assertFalse(packet["typography"]["authoritative_text_allowed"])

    def test_invariant_function_order_is_enforced(self) -> None:
        invalid = copy.deepcopy(self.volume)
        invalid["pages"][0]["function_code"] = "ARCHIVE_DISPOSITION"
        with self.assertRaises(CompileError):
            compile_volume(invalid, self.profile)

    def test_render_authorization_remains_closed(self) -> None:
        compiled = compile_volume(self.volume, self.profile)
        self.assertFalse(compiled["render_authorized"])
        self.assertEqual(self.volume["render_authorization"]["status"], "NOT_APPROVED_FOR_RENDER")

    def test_partial_human_presence_is_bounded(self) -> None:
        modes = {page["render_overrides"]["human_presence"]["mode"] for page in self.volume["pages"]}
        self.assertIn("partial_evidence", modes)
        for page in self.volume["pages"]:
            hp = page["render_overrides"]["human_presence"]
            self.assertFalse(hp["identifiable"])
            self.assertFalse(hp["cinematic"])
            self.assertTrue(hp["subordinate_to_relic"])

    def test_black_field_qc_pass_and_white_field_fail(self) -> None:
        canvas = {**self.volume["canvas"], "master_width": 300, "master_height": 400}
        qc = self.profile["qc"]
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            passing = Image.new("RGB", (canvas["master_width"], canvas["master_height"]), (0, 0, 0))
            draw = ImageDraw.Draw(passing)
            draw.rectangle((120, 150, 180, 250), fill=(175, 175, 175))
            pass_path = tmp_path / "pass.png"
            passing.save(pass_path)
            pass_result = inspect_image(pass_path, qc, canvas)
            self.assertTrue(pass_result.passed, pass_result.failures)

            failing = Image.new("RGB", (canvas["master_width"], canvas["master_height"]), (255, 255, 255))
            fail_path = tmp_path / "fail.png"
            failing.save(fail_path)
            fail_result = inspect_image(fail_path, qc, canvas)
            self.assertFalse(fail_result.passed)
            self.assertIn("white field fraction above maximum", fail_result.failures)


if __name__ == "__main__":
    unittest.main()
