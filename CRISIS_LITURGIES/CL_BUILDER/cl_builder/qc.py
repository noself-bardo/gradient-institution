from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

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
    failures: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _is_black(pixel: tuple[int, int, int], tolerance: int) -> bool:
    return max(pixel) <= tolerance


def _is_white(pixel: tuple[int, int, int], threshold: int) -> bool:
    return min(pixel) >= threshold


def inspect_image(path: str | Path, validation: dict[str, Any], canvas: dict[str, Any]) -> ImageQCResult:
    image = Image.open(path).convert("RGBA")
    width, height = image.size
    getter = getattr(image, "get_flattened_data", image.getdata)
    pixels = list(getter())
    total = max(len(pixels), 1)
    black_tolerance = int(validation["black_rgb_tolerance"])
    white_threshold = int(validation["white_rgb_threshold"])

    rgb = [(r, g, b) for r, g, b, _ in pixels]
    black_count = sum(_is_black(p, black_tolerance) for p in rgb)
    white_count = sum(_is_white(p, white_threshold) for p in rgb)
    alpha_violations = sum(a < 255 for _, _, _, a in pixels)

    edge_width = max(1, int(min(width, height) * 0.02))
    edge_pixels: list[tuple[int, int, int]] = []
    rgba = image.load()
    for y in range(height):
        for x in range(width):
            if x < edge_width or x >= width - edge_width or y < edge_width or y >= height - edge_width:
                r, g, b, _ = rgba[x, y]
                edge_pixels.append((r, g, b))
    edge_black_count = sum(_is_black(p, black_tolerance) for p in edge_pixels)

    black_coverage = black_count / total
    white_fraction = white_count / total
    foreground_coverage = 1.0 - black_coverage
    alpha_fraction = alpha_violations / total
    edge_black_coverage = edge_black_count / max(len(edge_pixels), 1)

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
        failures=failures,
    )
