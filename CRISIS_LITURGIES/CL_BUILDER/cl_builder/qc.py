from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


@dataclass(frozen=True)
class ImageQCResult:
    passed: bool
    width: int
    height: int
    expected_width: int
    expected_height: int
    black_coverage: float
    white_field_fraction: float
    foreground_coverage: float
    alpha_violation_fraction: float
    edge_black_coverage: float
    mean_channel_delta: float
    chroma_fraction: float
    failures: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def inspect_image(path: str | Path, validation: dict[str, Any], canvas: dict[str, Any]) -> ImageQCResult:
    image = Image.open(path).convert("RGBA")
    width, height = image.size
    array = np.asarray(image, dtype=np.int16)
    rgb = array[:, :, :3]
    alpha = array[:, :, 3]
    maximum = rgb.max(axis=2)
    minimum = rgb.min(axis=2)
    channel_delta = maximum - minimum

    black_tolerance = int(validation["black_rgb_tolerance"])
    white_threshold = int(validation["white_rgb_threshold"])
    chroma_threshold = int(validation.get("chroma_delta_threshold", 24))

    black_mask = maximum <= black_tolerance
    white_mask = minimum >= white_threshold
    alpha_mask = alpha < 255

    edge_width = max(1, int(min(width, height) * 0.02))
    edge_mask = np.zeros((height, width), dtype=bool)
    edge_mask[:edge_width, :] = True
    edge_mask[-edge_width:, :] = True
    edge_mask[:, :edge_width] = True
    edge_mask[:, -edge_width:] = True

    black_coverage = float(black_mask.mean())
    white_fraction = float(white_mask.mean())
    foreground_coverage = 1.0 - black_coverage
    alpha_fraction = float(alpha_mask.mean())
    edge_black_coverage = float(black_mask[edge_mask].mean())
    mean_channel_delta = float(channel_delta.mean())
    chroma_fraction = float((channel_delta > chroma_threshold).mean())

    failures: list[str] = []
    expected_width = int(canvas["master_width"])
    expected_height = int(canvas["master_height"])
    if (width, height) != (expected_width, expected_height):
        failures.append(f"dimensions {width}x{height} != {expected_width}x{expected_height}")
    if black_coverage < float(validation["minimum_black_coverage"]):
        failures.append("black coverage below minimum")
    if white_fraction > float(validation["maximum_white_field_fraction"]):
        failures.append("white field fraction above maximum")
    if foreground_coverage > float(validation["maximum_foreground_coverage"]):
        failures.append("foreground coverage above maximum")
    if alpha_fraction > float(validation["maximum_alpha_violation_fraction"]):
        failures.append("transparency detected")
    if edge_black_coverage < float(validation["minimum_edge_black_coverage"]):
        failures.append("edge contamination detected")
    if chroma_fraction > float(validation.get("maximum_chroma_fraction", 1.0)):
        failures.append("chromatic drift detected")
    if mean_channel_delta > float(validation.get("maximum_mean_channel_delta", 255.0)):
        failures.append("mean channel delta above maximum")

    return ImageQCResult(
        passed=not failures,
        width=width,
        height=height,
        expected_width=expected_width,
        expected_height=expected_height,
        black_coverage=round(black_coverage, 6),
        white_field_fraction=round(white_fraction, 6),
        foreground_coverage=round(foreground_coverage, 6),
        alpha_violation_fraction=round(alpha_fraction, 6),
        edge_black_coverage=round(edge_black_coverage, 6),
        mean_channel_delta=round(mean_channel_delta, 6),
        chroma_fraction=round(chroma_fraction, 6),
        failures=failures,
    )
