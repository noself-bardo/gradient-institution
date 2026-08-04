from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw
from pypdf import PdfReader

from cl_builder.compiler import CompileError, compile_volume
from cl_builder.io import load_structured
from cl_builder.qc import inspect_image
from cl_builder.schema import validate_instance


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "profiles" / "crisis-liturgies-expansion-v1.yaml"
CALIBRATION_REPORT = ROOT / "references" / "CL-IV" / "CL-IV_CALIBRATION_v0.2.json"
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

            chromatic = Image.new("RGB", (canvas["master_width"], canvas["master_height"]), (0, 0, 0))
            draw = ImageDraw.Draw(chromatic)
            draw.rectangle((90, 120, 210, 280), fill=(180, 20, 20))
            chroma_path = tmp_path / "chroma.png"
            chromatic.save(chroma_path)
            chroma_result = inspect_image(chroma_path, qc, canvas)
            self.assertFalse(chroma_result.passed)
            self.assertIn("chromatic drift detected", chroma_result.failures)


class EngineeringStageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.volume = make_volume()
        cls.profile = load_structured(PROFILE_PATH)

    def test_committed_calibration_report_matches_profile(self) -> None:
        report = json.loads(CALIBRATION_REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["corpus_page_count"], 48)
        self.assertEqual(report["source_document"]["sha256"], "168e2c958b55cbc9f3641f16110dbd5c21789a6908e2830587206c54799f41fe")
        recommended = report["recommended_qc"]
        for key in (
            "minimum_black_coverage",
            "maximum_white_field_fraction",
            "maximum_foreground_coverage",
            "minimum_edge_black_coverage",
            "maximum_chroma_fraction",
            "maximum_mean_channel_delta",
        ):
            self.assertEqual(self.profile["qc"][key], recommended[key], key)

    def test_calibration_accepts_volume_iv_reference_corpus(self) -> None:
        from cl_builder.calibration import calibrate_directory

        corpus = Path('/tmp/cliv_native')
        if not corpus.exists():
            self.skipTest('external Volume IV reference corpus not mounted')
        report = calibrate_directory(corpus, self.profile['qc'])
        self.assertEqual(report['corpus_page_count'], 48)
        recommended = report['recommended_qc']
        self.assertLessEqual(recommended['minimum_black_coverage'], 0.35)
        self.assertLessEqual(recommended['maximum_white_field_fraction'], 0.002)
        self.assertGreaterEqual(recommended['minimum_edge_black_coverage'], 0.995)
        for image in sorted(corpus.glob('*.jpg')):
            result = inspect_image(image, self.profile['qc'], {'master_width': 1086, 'master_height': 1448})
            self.assertTrue(result.passed, f"{image.name}: {result.failures}")

    def test_manifest_renderer_stays_fail_closed(self) -> None:
        from cl_builder.renderer import ManifestRendererAdapter, RenderAuthorizationError, require_render_authorization

        compiled = compile_volume(self.volume, self.profile)
        with tempfile.TemporaryDirectory() as tmp:
            index = ManifestRendererAdapter().materialize(compiled, tmp)
            self.assertEqual(index['execution_status'], 'BLOCKED')
            self.assertEqual(len(list((Path(tmp) / 'jobs').glob('*.json'))), 48)
        with self.assertRaises(RenderAuthorizationError):
            require_render_authorization(compiled)

    def test_manuscript_parser_and_deterministic_pdf_assembly(self) -> None:
        from cl_builder.assembly import assemble_volume_pdf, copy_map_for_volume

        mini = copy.deepcopy(self.volume)
        mini['pages'] = mini['pages'][:4]
        mini['issues'] = mini['issues'][:1]
        mini['canvas'] = {**mini['canvas'], 'reader_width': 540, 'reader_height': 720}
        manuscript_parts = [f"ISSUE 01 — {mini['pages'][0]['issue']}"]
        for page in mini['pages']:
            manuscript_parts.extend([
                f"PAGE {page['page_number']} — {page['title']}",
                f"Locked deterministic copy for {page['page_id']}. The image renderer does not own this sentence.",
            ])
        manuscript = '\n\n'.join(manuscript_parts)
        copy_map = copy_map_for_volume(mini, manuscript)
        self.assertEqual(len(copy_map), 4)
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            output = tmp_path / 'proof.pdf'
            manifest_path = tmp_path / 'manifest.json'
            manifest = assemble_volume_pdf(mini, manuscript, tmp_path / 'assets', output, manifest_path)
            self.assertEqual(manifest['page_count'], 4)
            self.assertTrue(output.exists())
            self.assertGreater(output.stat().st_size, 1000)
            self.assertTrue(manifest_path.exists())
            validate_instance(manifest, ROOT / "schemas", "assembly-manifest")
            reader = PdfReader(str(output))
            self.assertEqual(len(reader.pages), 4)
            self.assertIn("Locked deterministic copy", reader.pages[0].extract_text())

    def test_external_result_ingest_writes_valid_receipt(self) -> None:
        from cl_builder.renderer import ingest_rendered_asset

        compiled = compile_volume(self.volume, self.profile)
        packet = copy.deepcopy(compiled["render_packets"][0])
        packet["canvas"]["width"] = 300
        packet["canvas"]["height"] = 400
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            image = Image.new("RGB", (300, 400), (0, 0, 0))
            ImageDraw.Draw(image).rectangle((120, 150, 180, 250), fill=(175, 175, 175))
            image_path = tmp_path / "render.png"
            image.save(image_path)
            receipt_path = tmp_path / "receipt.json"
            receipt = ingest_rendered_asset(packet, image_path, tmp_path / "accepted", receipt_path)
            self.assertEqual(receipt.status, "ACCEPTED")
            validate_instance(receipt.to_dict(), ROOT / "schemas", "render-receipt")
            self.assertTrue(receipt_path.exists())


class ProvenMethodRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.method = load_structured(ROOT / "method" / "CL-METHOD-001.yaml")
        cls.fixtures = json.loads((ROOT / "references" / "golden" / "CL-METHOD-001_REGRESSION_FIXTURES_v1.0.json").read_text(encoding="utf-8"))

    def test_method_lock_has_three_distinct_references(self) -> None:
        refs = self.fixtures["references"]
        self.assertEqual([r["reference_id"] for r in refs], ["CL-REF-001", "CL-REF-002", "CL-REF-003"])
        self.assertEqual({r["issue"] for r in refs}, {"MIRROR", "IVORY", "REFUSAL"})
        self.assertEqual(sum(r["page_count"] for r in refs), 12)
        self.assertEqual(refs[0]["repair_count"], 1)
        self.assertEqual(refs[1]["repair_count"], 0)
        self.assertEqual(refs[2]["repair_count"], 2)
        self.assertEqual([r["id"] for r in self.method["references"]], [r["reference_id"] for r in refs])

    def test_method_keeps_renderer_visual_only(self) -> None:
        self.assertTrue(self.method["renderer"]["visual_only"])
        self.assertFalse(self.method["renderer"]["authoritative_text_allowed"])
        self.assertEqual(self.method["canvas"]["background_hex"], "#000000")
        self.assertFalse(self.method["canvas"]["transparency_allowed"])
        self.assertEqual(self.method["repair"]["scope"], "page_bounded")
        self.assertTrue(self.method["repair"]["preserve_accepted_pages"])

    def test_method_preserves_four_page_function_order(self) -> None:
        self.assertEqual(self.method["page_functions"], FUNCTIONS)

    def test_ivory_reference_qc_remains_inside_locked_envelope(self) -> None:
        for page_id, metrics in self.fixtures["ivory_qc"].items():
            self.assertEqual(metrics["status"], "PASS", page_id)
            self.assertGreaterEqual(metrics["black_coverage"], 0.65, page_id)
            self.assertLessEqual(metrics["white_coverage"], 0.01, page_id)
            self.assertGreaterEqual(metrics["edge_black_coverage"], 0.85, page_id)
            self.assertEqual(metrics["dimensions"], "1086x1448")

    def test_frozen_proof_hashes_are_present(self) -> None:
        for ref in self.fixtures["references"]:
            digest = ref["proof_pdf_sha256"]
            self.assertIsInstance(digest, str)
            self.assertEqual(len(digest), 64)
            int(digest, 16)

    def test_refusal_cover_is_separate_from_canonical_function_order(self) -> None:
        refusal = self.fixtures["refusal"]
        cover = refusal["cover"]
        self.assertEqual(cover["classification"], "ISSUE_COVER")
        self.assertFalse(cover["canonical_page_function_member"])
        functions = [page["function"] for page in refusal["interior_pages"].values()]
        self.assertEqual(functions, FUNCTIONS)
        self.assertEqual(refusal["canonical_function_order"], FUNCTIONS)
        self.assertEqual(len(refusal["interior_pages"]), 4)

    def test_refusal_cover_density_exception_is_narrow_and_isolated(self) -> None:
        refusal = self.fixtures["refusal"]
        density = self.method["density"]
        exception = density["cover_exceptions"]["CL-REF-003"]
        self.assertEqual(exception["applies_only_to"], refusal["cover"]["page_id"])
        self.assertEqual(exception["classification"], "ISSUE_COVER")
        self.assertFalse(exception["canonical_page_function_member"])
        self.assertGreater(refusal["cover"]["foreground_coverage"], density["interior_maximum_foreground_coverage"])
        self.assertLessEqual(refusal["cover"]["foreground_coverage"], exception["maximum_foreground_coverage"])
        self.assertGreaterEqual(refusal["cover"]["black_coverage"], exception["minimum_black_coverage"])
        for page in refusal["interior_pages"].values():
            self.assertGreaterEqual(page["black_coverage"], density["interior_minimum_black_coverage"])
            self.assertLessEqual(page["foreground_coverage"], density["interior_maximum_foreground_coverage"])

    def test_refusal_qc_preserves_black_edges_and_zero_chroma_transparency(self) -> None:
        refusal = self.fixtures["refusal"]
        pages = [refusal["cover"], *refusal["interior_pages"].values()]
        for page in pages:
            self.assertGreater(page["black_coverage"], 0.0)
            self.assertEqual(page["edge_black_coverage"], 1.0)
            self.assertEqual(page["chroma_fraction"], 0.0)
            self.assertEqual(page["alpha_violation_fraction"], 0.0)
            self.assertLessEqual(page["white_coverage"], 0.01)

    def test_refusal_typography_and_svg_editability_are_owned_deterministically(self) -> None:
        refusal = self.fixtures["refusal"]
        typography = refusal["typography"]
        svg = refusal["editable_svg"]
        self.assertEqual(typography["owner"], "deterministic_layout")
        self.assertFalse(typography["authoritative_text_in_renderer"])
        self.assertTrue(svg["required"])
        self.assertTrue(svg["all_named_layers"])
        self.assertTrue(svg["all_live_text"])
        self.assertTrue(svg["all_vector_tonal_paths"])
        self.assertEqual(svg["embedded_raster_image_nodes"], 0)
        self.assertEqual(len(svg["path_nodes"]), 5)
        self.assertEqual(len(svg["named_layers"]), 5)
        self.assertTrue(all(count > 0 for count in svg["path_nodes"]))
        self.assertTrue(all(count > 0 for count in svg["named_layers"]))

    def test_refusal_package_manifest_and_checksums_are_locked(self) -> None:
        package = self.fixtures["refusal"]["package"]
        self.assertEqual(package["proof_page_count"], 5)
        self.assertEqual(package["checksum_entry_count"], 16)
        self.assertEqual(package["checksum_mismatch_count"], 0)
        for key in (
            "proof_pdf_sha256",
            "package_zip_sha256",
            "package_manifest_sha256",
            "qc_manifest_sha256",
            "checksums_sha256",
        ):
            digest = package[key]
            self.assertEqual(len(digest), 64, key)
            int(digest, 16)
        ref = next(item for item in self.fixtures["references"] if item["reference_id"] == "CL-REF-003")
        self.assertEqual(ref["proof_pdf_sha256"], package["proof_pdf_sha256"])
        self.assertEqual(ref["package_zip_sha256"], package["package_zip_sha256"])

    def test_refusal_does_not_authorize_unrelated_rendering(self) -> None:
        authorization = self.fixtures["refusal"]["render_authorization"]
        self.assertEqual(authorization["authorized_issue"], "CL-EV-001-I02")
        self.assertFalse(authorization["unrelated_issues_authorized"])
        self.assertFalse(authorization["full_volume_authorized"])
        self.assertEqual(self.method["founder_gates"], ["BOUNDED_RENDER_AUTHORIZATION", "COMPLETED_ISSUE_PROOF_REVIEW"])


if __name__ == "__main__":
    unittest.main()
