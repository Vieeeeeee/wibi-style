#!/usr/bin/env python3
"""把横向票根裁成带撕票口、打孔和透明背景的独立 PNG。"""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw


PHOTO_SEAM_RATIO = 1472 / 2048


def fit_inside(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    scale = min(size[0] / image.width, size[1] / image.height)
    return image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )


def make_mask(size: tuple[int, int], seam_x: int) -> Image.Image:
    width, height = size
    scale = 2
    mask = Image.new("L", (width * scale, height * scale), 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((0, 0, width * scale - 1, height * scale - 1), fill=255)

    corner_radius = round(height * 0.055) * scale
    for corner_x, corner_y in (
        (0, 0),
        (width * scale, 0),
        (0, height * scale),
        (width * scale, height * scale),
    ):
        draw.ellipse(
            (
                corner_x - corner_radius,
                corner_y - corner_radius,
                corner_x + corner_radius,
                corner_y + corner_radius,
            ),
            fill=0,
        )

    notch_radius = round(height * 0.075) * scale
    seam = seam_x * scale
    draw.ellipse(
        (seam - notch_radius, -notch_radius, seam + notch_radius, notch_radius),
        fill=0,
    )
    draw.ellipse(
        (
            seam - notch_radius,
            height * scale - notch_radius,
            seam + notch_radius,
            height * scale + notch_radius,
        ),
        fill=0,
    )

    hole_radius = round(height * 0.024) * scale
    hole_x = round(height * 0.085) * scale
    hole_y = height * scale // 2
    draw.ellipse(
        (
            hole_x - hole_radius,
            hole_y - hole_radius,
            hole_x + hole_radius,
            hole_y + hole_radius,
        ),
        fill=0,
    )
    return mask.resize(size, Image.Resampling.LANCZOS)


def add_perforation(ticket: Image.Image, seam_x: int) -> None:
    draw = ImageDraw.Draw(ticket)
    margin = round(ticket.height * 0.075)
    dash = max(8, round(ticket.height * 0.021))
    gap = max(7, round(ticket.height * 0.018))
    cursor = margin
    end = ticket.height - margin
    while cursor < end:
        draw.line(
            (seam_x, cursor, seam_x, min(cursor + dash, end)),
            fill="#111111",
            width=max(3, round(ticket.height * 0.007)),
        )
        cursor += dash + gap


def finish(
    source: Path,
    output: Path,
    preview_output: Path | None,
    background: str,
    margin_x: int,
    margin_y: int,
) -> dict:
    image = Image.open(source).convert("RGB")
    canvas = Image.new("RGB", image.size, background)
    ticket = fit_inside(image, (image.width - margin_x * 2, image.height - margin_y * 2))
    seam_x = round(ticket.width * PHOTO_SEAM_RATIO)
    add_perforation(ticket, seam_x)
    cutout = ticket.convert("RGBA")
    cutout.putalpha(make_mask(ticket.size, seam_x))

    left = (canvas.width - ticket.width) // 2
    top = (canvas.height - ticket.height) // 2
    canvas.paste(cutout, (left, top), cutout)
    output.parent.mkdir(parents=True, exist_ok=True)
    cutout.save(output)

    if preview_output:
        preview_output.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(preview_output)

    return {
        "source": str(source.resolve()),
        "output": str(output.resolve()),
        "preview_output": str(preview_output.resolve()) if preview_output else None,
        "output_size": list(cutout.size),
        "preview_canvas_size": list(canvas.size),
        "photo_seam_ratio": PHOTO_SEAM_RATIO,
        "background": background,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="生成带实体裁口、撕票虚线、打孔和透明背景的独立票根")
    parser.add_argument("--ticket", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--preview-out")
    parser.add_argument("--background", default="#050505")
    parser.add_argument("--margin-x", type=int, default=72)
    parser.add_argument("--margin-y", type=int, default=36)
    args = parser.parse_args()

    if args.margin_x < 0 or args.margin_y < 0:
        raise SystemExit("margin 必须是非负整数")

    result = finish(
        Path(args.ticket),
        Path(args.out),
        Path(args.preview_out) if args.preview_out else None,
        args.background,
        args.margin_x,
        args.margin_y,
    )
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
