from __future__ import annotations

import hashlib
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
from PIL import Image


@dataclass(frozen=True)
class CalibrationPage:
    file: str
    width: int
    height: int
    black_coverage: float
    white_field_fraction: float
    foreground_coverage: float
    edge_black_coverage: float
    mean_channel_delta: float
    chroma_fraction: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inspect_calibration_page(path: str | Path, qc: dict[str, Any]) -> CalibrationPage:
    source = Path(path)
    image = Image.open(source).convert("RGB")
    array = np.asarray(image, dtype=np.int16)
    maximum = array.max(axis=2)
    minimum = array.min(axis=2)
    channel_delta = maximum - minimum

    black_tolerance = int(qc["black_rgb_tolerance"])
    white_threshold = int(qc["white_rgb_threshold"])
    chroma_threshold = int(qc.get("chroma_delta_threshold", 24))

    black_mask = maximum <= black_tolerance
    white_mask = minimum >= white_threshold
    height, width = maximum.shape
    edge_width = max(1, int(min(width, height) * 0.02))
    edge_mask = np.zeros((height, width), dtype=bool)
    edge_mask[:edge_width, :] = True
    edge_mask[-edge_width:, :] = True
    edge_mask[:, :edge_width] = True
    edge_mask[:, -edge_width:] = True

    black_coverage = float(black_mask.mean())
    return CalibrationPage(
        file=source.name,
        width=width,
        height=height,
        black_coverage=round(black_coverage, 8),
        white_field_fraction=round(float(white_mask.mean()), 8),
        foreground_coverage=round(1.0 - black_coverage, 8),
        edge_black_coverage=round(float(black_mask[edge_mask].mean()), 8),
        mean_channel_delta=round(float(channel_delta.mean()), 6),
        chroma_fraction=round(float((channel_delta > chroma_threshold).mean()), 8),
    )


def _distribution(values: Iterable[float]) -> dict[str, float]:
    array = np.asarray(list(values), dtype=float)
    return {
        "min": round(float(array.min()), 8),
        "p05": round(float(np.percentile(array, 5)), 8),
        "median": round(float(np.median(array)), 8),
        "p95": round(float(np.percentile(array, 95)), 8),
        "max": round(float(array.max()), 8),
    }


def derive_thresholds(pages: list[CalibrationPage], base_qc: dict[str, Any]) -> dict[str, Any]:
    min_black = min(page.black_coverage for page in pages)
    max_white = max(page.white_field_fraction for page in pages)
    max_foreground = max(page.foreground_coverage for page in pages)
    min_edge = min(page.edge_black_coverage for page in pages)
    max_delta = max(page.mean_channel_delta for page in pages)
    max_chroma = max(page.chroma_fraction for page in pages)

    return {
        "black_rgb_tolerance": int(base_qc["black_rgb_tolerance"]),
        "white_rgb_threshold": int(base_qc["white_rgb_threshold"]),
        "minimum_black_coverage": round(max(0.0, math.floor((min_black - 0.02) * 100) / 100), 2),
        "maximum_white_field_fraction": round(max(0.0015, math.ceil(max_white * 10000) / 10000 + 0.0005), 4),
        "maximum_foreground_coverage": round(min(1.0, math.ceil((max_foreground + 0.02) * 100) / 100), 2),
        "maximum_alpha_violation_fraction": 0.0,
        "minimum_edge_black_coverage": round(max(0.0, math.floor((min_edge - 0.005) * 1000) / 1000), 3),
        "chroma_delta_threshold": int(base_qc.get("chroma_delta_threshold", 24)),
        "maximum_chroma_fraction": round(max(0.003, math.ceil(max_chroma * 1000) / 1000), 3),
        "maximum_mean_channel_delta": round(max(9.0, math.ceil(max_delta * 2) / 2 + 0.5), 1),
    }


def calibrate_directory(
    image_dir: str | Path,
    base_qc: dict[str, Any],
    source_document: str | Path | None = None,
) -> dict[str, Any]:
    directory = Path(image_dir)
    files = sorted(
        path for path in directory.iterdir()
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
    )
    if not files:
        raise ValueError(f"no calibration images found in {directory}")

    pages = [inspect_calibration_page(path, base_qc) for path in files]
    dimensions = sorted({(page.width, page.height) for page in pages})
    report: dict[str, Any] = {
        "status": "PASS",
        "corpus_page_count": len(pages),
        "dimensions": [{"width": width, "height": height} for width, height in dimensions],
        "metrics": {
            "black_coverage": _distribution(page.black_coverage for page in pages),
            "white_field_fraction": _distribution(page.white_field_fraction for page in pages),
            "foreground_coverage": _distribution(page.foreground_coverage for page in pages),
            "edge_black_coverage": _distribution(page.edge_black_coverage for page in pages),
            "mean_channel_delta": _distribution(page.mean_channel_delta for page in pages),
            "chroma_fraction": _distribution(page.chroma_fraction for page in pages),
        },
        "recommended_qc": derive_thresholds(pages, base_qc),
        "pages": [page.to_dict() for page in pages],
    }
    if source_document is not None:
        source = Path(source_document)
        report["source_document"] = {
            "file": source.name,
            "sha256": _sha256(source),
        }
    return report
