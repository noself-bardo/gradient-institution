from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from typing import Any

LEGACY_GATE_PATTERN = re.compile(r"\bINTIFADA\b|IMAGE GENERATION NOT AUTHORIZED|IMAGE GATE CLOSED", re.I)
FUNCTION_CODES = ["RELIC_ENTRY", "WITNESS_RECORD", "SYSTEM_TRANSLATION", "ARCHIVE_DISPOSITION"]


class CompileError(ValueError):
    pass


def canonical_json(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_object(data: Any) -> str:
    return hashlib.sha256(canonical_json(data).encode("utf-8")).hexdigest()


def _strip_legacy_gate(text: str) -> str:
    lines = [line for line in text.splitlines() if not LEGACY_GATE_PATTERN.search(line)]
    return "\n".join(lines).strip()


def validate_invariants(volume: dict[str, Any]) -> None:
    pages = volume.get("pages", [])
    if len(pages) == 0 or len(pages) % 4 != 0:
        raise CompileError("A volume must contain a non-zero multiple of four pages")
    seen: set[str] = set()
    grouped: dict[int, list[dict[str, Any]]] = {}
    for page in pages:
        page_id = page["page_id"]
        if page_id in seen:
            raise CompileError(f"Duplicate page ID: {page_id}")
        seen.add(page_id)
        grouped.setdefault(int(page["issue_number"]), []).append(page)
        if page["function_code"] not in FUNCTION_CODES:
            raise CompileError(f"Unknown function code on {page_id}: {page['function_code']}")
    for issue_number, issue_pages in grouped.items():
        ordered = sorted(issue_pages, key=lambda item: int(item["page_number"]))
        if [page["page_number"] for page in ordered] != [1, 2, 3, 4]:
            raise CompileError(f"Issue {issue_number:02d} does not contain pages 1-4 exactly")
        if [page["function_code"] for page in ordered] != FUNCTION_CODES:
            raise CompileError(f"Issue {issue_number:02d} violates CCR-CL-003 function order")


def compile_render_packet(volume: dict[str, Any], page: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    canvas = deepcopy(volume["canvas"])
    qc = deepcopy(profile["qc"])
    visual = deepcopy(profile["visual"])
    overrides = deepcopy(page.get("render_overrides", {}))

    source_prompt = _strip_legacy_gate(page["source_prompt"])
    source_negative = _strip_legacy_gate(page["source_negative_prompt"])
    enforced_prompt = (
        f"{source_prompt}\n\n"
        "EXECUTION LOCK: render as a flat Crisis Liturgies archival plate on a full matte-black canvas. "
        "Translate every material, including paper or ivory, into the approved metallic-silver tonal family. "
        "Do not generate authoritative typography; reserve clean layout zones for deterministic compositing. "
        "No white, cream, beige, gray-paper, or transparent background. No photographic lighting, cast shadow, vignette, or page mockup."
    )
    enforced_negative = (
        f"{source_negative}, white background, off-white canvas, cream background, beige background, "
        "gray paper background, aged paper canvas, transparent background, page mockup, cinematic lighting, "
        "cast shadow, vignette, photorealistic scene, lifestyle scene, authoritative body text, fake typography"
    )

    packet = {
        "schema_version": "1.0.0",
        "asset_id": page["page_id"],
        "volume_id": volume["volume_id"],
        "issue_number": page["issue_number"],
        "page_number": page["page_number"],
        "function_code": page["function_code"],
        "display_label": page["display_label"],
        "title": page["title"],
        "approval": {
            "volume_state": volume["state"],
            "render_authorized": bool(volume["render_authorization"]["authorized"]),
        },
        "canvas": canvas,
        "visual": {
            **visual,
            "human_presence": overrides.get("human_presence", {"mode": "none"}),
            "material_translation_terms": overrides.get("material_translation_terms", []),
            "allow_environment": bool(overrides.get("allow_environment", False)),
            "allow_cast_shadow": False,
            "allow_transparency": False,
        },
        "prompt": enforced_prompt,
        "negative_prompt": enforced_negative,
        "typography": {
            "authoritative_text_allowed": False,
            "composition_stage": "layout",
            "reserved_zones": ["header", "footer", "copy-field"],
        },
        "validation": qc,
        "repair_policy": deepcopy(profile["repair_policy"]),
        "source": {
            "prompt_sha256": hashlib.sha256(page["source_prompt"].encode("utf-8")).hexdigest(),
            "page_spec_sha256": sha256_object(page),
        },
    }
    packet["packet_sha256"] = sha256_object(packet)
    return packet


def compile_volume(volume: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    validate_invariants(volume)
    packets = [compile_render_packet(volume, page, profile) for page in volume["pages"]]
    compiled = {
        "volume_id": volume["volume_id"],
        "state": volume["state"],
        "render_authorized": bool(volume["render_authorization"]["authorized"]),
        "page_count": len(packets),
        "profile": volume["release_profile"],
        "volume_spec_sha256": sha256_object(volume),
        "render_packets": packets,
    }
    compiled["compiled_sha256"] = sha256_object(compiled)
    return compiled
