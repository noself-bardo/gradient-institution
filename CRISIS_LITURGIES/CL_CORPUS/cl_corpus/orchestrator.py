from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .canonical import canonical_json, sha256_bytes, sha256_object
from .intake import CapturedSource, IntakeError, capture_sources
from .schema import validate_instance


class OrchestrationError(ValueError):
    pass


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _read_config(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise OrchestrationError(f"invalid intake config: {exc}") from exc


def _admission_blockers(config: dict[str, Any], captured: list[CapturedSource]) -> list[str]:
    blockers: list[str] = []
    if not config["authority"]["submitter_authorized"]:
        blockers.append("SUBMITTER_AUTHORITY_REQUIRED")
    if not config["authority"]["processing_consent_recorded"]:
        blockers.append("PROCESSING_CONSENT_REQUIRED")
    elif not config["authority"]["consent_record"]:
        blockers.append("CONSENT_RECORD_REQUIRED")
    if config["privacy"]["classification"] in {"SENSITIVE", "HIGHLY_SENSITIVE"} and not config["privacy"]["handling_protocol"]:
        blockers.append("SENSITIVE_HANDLING_PROTOCOL_REQUIRED")
    if config["privacy"]["contains_third_party_material"] and not config["privacy"]["handling_protocol"]:
        blockers.append("THIRD_PARTY_HANDLING_PROTOCOL_REQUIRED")
    if any(source.extraction_status != "EXTRACTED" for source in captured):
        blockers.append("SOURCE_EXTRACTION_REQUIRED")
    return blockers


def _corpus_text(captured: list[CapturedSource]) -> str:
    sections: list[str] = []
    for source in captured:
        if source.normalized_text is None:
            continue
        sections.extend([
            f"=== {source.source_id} | {source.relative_path} | sha256:{source.sha256} ===",
            source.normalized_text,
            "",
        ])
    return "\n".join(sections).rstrip() + "\n"


def _handoff(config: dict[str, Any], captured: list[CapturedSource], corpus_sha256: str, created_at: str) -> dict[str, Any]:
    handoff = {
        "schema_version": "1.0.0",
        "package_class": "CL-CORPUS-HANDOFF-1.0.0",
        "corpus_id": config["corpus_id"],
        "title": config["title"],
        "created_at": created_at,
        "source_mode": config["source_mode"],
        "intended_recipient": "CL-CONV-001",
        "next_required_state": "CONVERSION_ARCHITECT_REVIEW",
        "authority": config["authority"],
        "privacy": config["privacy"],
        "declared_scope": config["declared_scope"],
        "source_inventory": [source.inventory_record() for source in captured],
        "corpus": {
            "normalized_filename": "normalized-corpus.txt",
            "sha256": corpus_sha256,
            "source_count": len(captured),
        },
        "production_gates": {
            "canon_authorized": False,
            "volume_spec_frozen": False,
            "builder_handoff_authorized": False,
            "render_authorized": False,
            "publication_authorized": False,
        },
        "prohibitions": [
            "NO_CANON_INFERENCE",
            "NO_VOLUME_SPEC_GENERATION",
            "NO_RENDERING",
            "NO_PUBLICATION",
            "NO_SOURCE_MUTATION",
        ],
    }
    handoff["handoff_sha256"] = sha256_object(handoff)
    return handoff


def run_intake(config_path: Path, output_dir: Path, *, created_at: str | None = None) -> dict[str, Any]:
    root = Path(__file__).resolve().parents[1]
    config = _read_config(config_path)
    validate_instance(config, root / "schemas" / "intake.schema.json")
    source_root = (config_path.parent / config["source_root"]).resolve()
    try:
        captured = capture_sources(source_root)
    except IntakeError as exc:
        raise OrchestrationError(str(exc)) from exc
    blockers = _admission_blockers(config, captured)
    timestamp = created_at or _utc_now()
    report: dict[str, Any] = {
        "schema_version": "1.0.0",
        "corpus_id": config["corpus_id"],
        "created_at": timestamp,
        "status": "BLOCKED" if blockers else "HANDOFF_READY",
        "current_state": "ADMISSION_BLOCKED" if blockers else "AWAITING_CONVERSION_ARCHITECT",
        "blockers": blockers,
        "source_count": len(captured),
        "source_inventory_sha256": sha256_object([source.inventory_record() for source in captured]),
        "render_authorized": False,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "run-report.json").write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    if blockers:
        return report

    corpus = _corpus_text(captured)
    corpus_sha = sha256_bytes(corpus.encode("utf-8"))
    handoff = _handoff(config, captured, corpus_sha, timestamp)
    validate_instance(handoff, root / "schemas" / "handoff.schema.json")
    (output_dir / "normalized-corpus.txt").write_text(corpus, encoding="utf-8", newline="\n")
    (output_dir / "handoff.json").write_text(json.dumps(handoff, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    checksums = {
        "handoff.json": sha256_bytes((output_dir / "handoff.json").read_bytes()),
        "normalized-corpus.txt": corpus_sha,
        "run-report.json": sha256_bytes((output_dir / "run-report.json").read_bytes()),
    }
    checksum_text = "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items()))
    (output_dir / "MANIFEST.sha256").write_text(checksum_text, encoding="ascii", newline="\n")
    package_receipt = {
        "package_class": "CL-CORPUS-HANDOFF-1.0.0",
        "corpus_id": config["corpus_id"],
        "created_at": timestamp,
        "files": checksums,
        "package_manifest_sha256": sha256_bytes(checksum_text.encode("ascii")),
        "final_state": "AWAITING_CONVERSION_ARCHITECT",
        "render_gate": "CLOSED",
    }
    (output_dir / "custody-receipt.json").write_text(canonical_json(package_receipt) + "\n", encoding="utf-8", newline="\n")
    return report
