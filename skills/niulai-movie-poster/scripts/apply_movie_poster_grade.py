#!/usr/bin/env python3
"""Apply a restrained cinematic film grade to 牛来 poster candidates.

The generated poster owns the composition, characters and copy. This script
only handles the finishing grade: film curve, cool shadows, warm highlights,
halation, grain and vignette. It intentionally keeps vermilion poster copy
clear and saturated.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


def smoothstep(value: np.ndarray) -> np.ndarray:
    return value * value * (3.0 - 2.0 * value)


def film_grade(image: Image.Image, strength: float, seed: int) -> Image.Image:
    rgb = np.asarray(image.convert("RGB"), dtype=np.float32) / 255.0
    original = rgb.copy()

    # Gentle filmic S-curve with a small lifted black point.
    curve_strength = 0.34 * strength
    graded = np.clip((rgb - 0.5) * (1.0 + curve_strength) + 0.5, 0.0, 1.0)
    graded = graded * (1.0 - 0.035 * strength) + 0.035 * strength

    luminance = (
        0.2126 * graded[..., 0]
        + 0.7152 * graded[..., 1]
        + 0.0722 * graded[..., 2]
    )
    shadows = 1.0 - smoothstep(np.clip((luminance - 0.18) / 0.52, 0.0, 1.0))
    highlights = smoothstep(np.clip((luminance - 0.42) / 0.52, 0.0, 1.0))

    # Teal/cool shadows and restrained warm highlights.
    graded[..., 0] -= 0.035 * strength * shadows
    graded[..., 1] += 0.008 * strength * shadows
    graded[..., 2] += 0.040 * strength * shadows
    graded[..., 0] += 0.045 * strength * highlights
    graded[..., 1] += 0.018 * strength * highlights
    graded[..., 2] -= 0.026 * strength * highlights

    # Slightly soften digital saturation while protecting vermilion copy.
    gray = (
        0.2126 * graded[..., 0]
        + 0.7152 * graded[..., 1]
        + 0.0722 * graded[..., 2]
    )[..., None]
    saturation = 1.0 - 0.08 * strength
    graded = gray + (graded - gray) * saturation

    # Preserve the poster's vermilion title and seal from becoming brown.
    red = original[..., 0]
    green = original[..., 1]
    blue = original[..., 2]
    red_mask = np.clip((red - green * 1.10) * 5.0, 0.0, 1.0)
    red_mask *= np.clip((red - blue * 1.08) * 5.0, 0.0, 1.0)
    graded = graded * (1.0 - 0.28 * red_mask[..., None]) + original * (
        0.28 * red_mask[..., None]
    )

    # Subtle red halation around bright practical lights and highlights.
    bright = np.clip((luminance - 0.70) / 0.30, 0.0, 1.0)
    bright_image = Image.fromarray(np.uint8(np.clip(bright * 255.0, 0, 255)))
    halation = np.asarray(
        bright_image.filter(ImageFilter.GaussianBlur(radius=8)), dtype=np.float32
    ) / 255.0
    graded[..., 0] += 0.030 * strength * halation
    graded[..., 1] += 0.008 * strength * halation

    # Fine grain, concentrated in midtones so text stays readable.
    rng = np.random.default_rng(seed)
    grain = rng.normal(0.0, 0.010 * strength, size=luminance.shape).astype(np.float32)
    grain_weight = 0.45 + 0.55 * (1.0 - np.abs(luminance - 0.5) * 2.0)
    graded += grain[..., None] * grain_weight[..., None]

    # Cinematic edge falloff, deliberately lighter than a heavy vignette.
    height, width = luminance.shape
    y, x = np.ogrid[:height, :width]
    dx = (x - width * 0.5) / (width * 0.5)
    dy = (y - height * 0.5) / (height * 0.5)
    distance = np.sqrt(dx * dx + dy * dy)
    edge = np.clip((distance - 0.42) / 0.78, 0.0, 1.0)
    graded *= (1.0 - 0.16 * strength * edge[..., None])

    # Keep the grade photographic instead of crushing the original scene.
    result = original * (1.0 - strength) + graded * strength
    return Image.fromarray(np.uint8(np.clip(result * 255.0 + 0.5, 0, 255)), "RGB")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--strength", type=float, default=0.82)
    parser.add_argument("--seed", type=int, default=20260816)
    args = parser.parse_args()

    if not 0.0 <= args.strength <= 1.0:
        raise SystemExit("--strength must be between 0 and 1")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for index, input_path in enumerate(args.inputs):
        output_path = args.out_dir / f"{input_path.stem}_cinema_grade_v1.png"
        with Image.open(input_path) as source:
            output = film_grade(source, args.strength, args.seed + index)
            output.save(output_path, format="PNG", optimize=True)
        print(output_path)


if __name__ == "__main__":
    main()
