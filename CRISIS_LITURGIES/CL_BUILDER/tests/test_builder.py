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
PROFILE_PATH = ROOT / "profiles" / "crisis-liturgies-expansion-v1.yaml"
FUNCTIONS = ["RELIC_ENTRY", "WITNESS_RECORD", "SYSTEM_TRANSLATION", "ARCHIVE_DISPOSITION"]
LABELS = ["Encounter", "Mechanism / Witness", "Institution / Expansion", "Residue / Turn"]


def make_page(issue_number: int, page_number: int) -> dict:
    partial = issue_number == 1 and page_number == 1
    return {
        "page_id": f"CL-PM-I{issue_number:02d}-P{page_number}",
        "issue_number": issue_number,
        "issue": f"ISSUE {issue_number:02d}",
        "page_number": page_number,
        "display_label": LABELS[page_number - 1],
        "function_code": FUNCTIONS[page_number - 1],
        "title": f"PAGE {page_number}",
        "production_intent": "A controlled relic plate with meaningful negative space.",
        "source_prompt": "Create an archival plate. IMAGE GATE CLOSED. INTIFADA.",
        "source_negative_prompt": "white background, humanoid robot",
        "copy": {
            "source_document_id": "copy-source",
            "copy_register_id": "copy-register",
            "locked": True,
            "word_count": 20,
            "source_trace": "CONDITIONAL",
            "relic_status": "ACTIVE",
            "authoritative_text_in_image": False,
        },
        "render_overrides": {
            "human_presence": {
                "mode": "partial_evidence" if partial else "none",
                "identifiable": False,
                "cinematic": False,
                "subordinate_to_relic": True,
            },
            "material_translation_terms": ["mirror"],
            "allow_environment": False,
            "allow_cast_shadow": False,
            "allow_transparency": False,
        },
    }


def make_volume() -> dict:
    pages = [make_page(issue, page) for issue in range(1, 13) for page in range(1, 5)]
    return {
        "schema_version": "1.0.0",
        "volume_id": "CL-EV-001",
        "working_id": "CL-PM",
        "title": "THE PYGMALION MACHINE",
        "subtitle": "Projection, Artificial Intimacy, and the Mirror That Learned to Speak",
        "core_line": "AI is Pygmalion's mirror learning to speak.",
        "state": "BUILD_VALIDATED",
        "render_authorization": {
            "status": "NOT_APPROVED_FOR_RENDER",
            "authorized": False,
            "authorization_record": None,
        },
        "authority": {
            "canon": "Crisis Liturgies Canon v1.1",
            "generation_standard": "CL-GEN-STD-001 v1.0",
            "builder_amendment": "CCR-CL-002",
            "function_palette_amendment": "CCR-CL-003",
            "volume_ccr": "CL-PM_CANON_CHANGE_REPORT",
        },
        "release_profile": "crisis-liturgies-expansion-v1",
        "page_profile": {
            "name": "expansion-volume",
            "mapping": dict(zip(LABELS, FUNCTIONS)),
        },
        "canvas": {
            "master_width": 3750,
            "master_height": 4950,
            "reader_width": 1086,
            "reader_height": 1448,
            "orientation": "portrait",
            "background_hex": "#000000",
            "transparent_background": False,
        },
        "visual_doctrine": {
            "speaking_mirror_not_living_machine": True,
            "object_as_witness": True,
            "canvas": "matte_black",
            "ink_family": "metallic_silver_tonal",
            "max_foreground_coverage": 0.25,
            "authoritative_typography_stage": "layout",
            "prohibited_canvas_terms": ["white", "cream", "ivory", "transparent"],
        },
        "issues": [{"number": n, "title": f"ISSUE {n:02d}"} for n in range(1, 13)],
        "sources": [{"name": "fixture", "provider_id": "fixture", "sha256": None, "role": "test"}],
        "pages": pages,
    }


class BuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.volume = make_volume()
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
