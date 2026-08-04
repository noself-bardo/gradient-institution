from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Protocol

from .io import dump_json
from .qc import inspect_image


class RenderAuthorizationError(RuntimeError):
    pass


@dataclass(frozen=True)
class RenderReceipt:
    asset_id: str
    adapter: str
    status: str
    source_path: str
    accepted_path: str | None
    sha256: str
    qc: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class RendererAdapter(Protocol):
    adapter_id: str

    def materialize(self, compiled: dict[str, Any], output_dir: str | Path) -> dict[str, Any]: ...


def require_render_authorization(compiled: dict[str, Any]) -> None:
    if not bool(compiled.get("render_authorized")):
        raise RenderAuthorizationError("volume is not APPROVED_FOR_RENDER")


class ManifestRendererAdapter:
    """Fail-closed adapter that emits provider-neutral job packets only.

    It never contacts an image service. Production execution requires a future
    provider adapter and a compiled volume with render_authorized=true.
    """

    adapter_id = "manifest-renderer-v1"

    def materialize(self, compiled: dict[str, Any], output_dir: str | Path) -> dict[str, Any]:
        destination = Path(output_dir)
        destination.mkdir(parents=True, exist_ok=True)
        jobs = destination / "jobs"
        jobs.mkdir(exist_ok=True)
        for packet in compiled["render_packets"]:
            dump_json(packet, jobs / f"{packet['asset_id']}.json")
        index = {
            "adapter": self.adapter_id,
            "volume_id": compiled["volume_id"],
            "render_authorized": bool(compiled["render_authorized"]),
            "page_count": compiled["page_count"],
            "compiled_sha256": compiled["compiled_sha256"],
            "execution_status": "BLOCKED" if not compiled["render_authorized"] else "READY",
            "blockers": [] if compiled["render_authorized"] else ["APPROVED_FOR_RENDER"],
        }
        dump_json(index, destination / "render-plan.json")
        return index


def ingest_rendered_asset(
    packet: dict[str, Any],
    source_image: str | Path,
    accepted_dir: str | Path,
    receipt_path: str | Path,
) -> RenderReceipt:
    source = Path(source_image)
    validation = packet["validation"]
    canvas = {
        "master_width": packet["canvas"]["width"],
        "master_height": packet["canvas"]["height"],
    }
    qc = inspect_image(source, validation, canvas)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    accepted_path: Path | None = None
    status = "REJECTED"
    if qc.passed:
        target_dir = Path(accepted_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
        accepted_path = target_dir / f"{packet['asset_id']}{source.suffix.lower()}"
        shutil.copy2(source, accepted_path)
        status = "ACCEPTED"
    receipt = RenderReceipt(
        asset_id=packet["asset_id"],
        adapter="external-result-ingest-v1",
        status=status,
        source_path=str(source),
        accepted_path=str(accepted_path) if accepted_path else None,
        sha256=digest,
        qc=qc.to_dict(),
    )
    dump_json(receipt.to_dict(), receipt_path)
    return receipt
