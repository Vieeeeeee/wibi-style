#!/usr/bin/env python3
"""把照片和票根文字排成只表达位置、字量与层级的中性结构导引图。"""

import argparse
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent.parent
SANS = ROOT / "assets/fonts/NotoSansSC-VF.ttf"
with open(ROOT / "design-system/presets.json", "r", encoding="utf-8") as fh:
    DESIGN_SYSTEM = json.load(fh)

SIZE = (DESIGN_SYSTEM["canvas"]["width"], DESIGN_SYSTEM["canvas"]["height"])
PHOTO_X = DESIGN_SYSTEM["canvas"]["photo_x"]
PRESETS = DESIGN_SYSTEM["presets"]
INK = "#343434"


def font(size, weight=400):
    face = ImageFont.truetype(str(SANS), max(6, round(size)))
    try:
        face.set_variation_by_axes([float(weight)])
    except (AttributeError, OSError, ValueError):
        pass
    return face


def cover_crop(image, target, focus):
    image = ImageOps.exif_transpose(image).convert("RGB")
    tw, th = target
    scale = max(tw / image.width, th / image.height)
    resized = image.resize(
        (math.ceil(image.width * scale), math.ceil(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    cx, cy = focus[0] * resized.width, focus[1] * resized.height
    left = round(min(max(cx - tw / 2, 0), resized.width - tw))
    top = round(min(max(cy - th / 2, 0), resized.height - th))
    return resized.crop((left, top, left + tw, top + th))


def fit_font(draw, text, max_width, start, minimum, weight):
    for size in range(start, minimum - 1, -2):
        face = font(size, weight)
        box = draw.textbbox((0, 0), text, font=face)
        if box[2] - box[0] <= max_width:
            return face
    return font(minimum, weight)


def draw_vertical_text(canvas, text, xy, size=22):
    if not text:
        return
    face = font(size, 450)
    box = face.getbbox(text)
    layer = Image.new("RGBA", (box[2] - box[0] + 20, box[3] - box[1] + 20), (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((10, 10 - box[1]), text, font=face, fill=INK)
    layer = layer.rotate(90, expand=True)
    canvas.alpha_composite(layer, xy)


def draw_text_route(canvas, data, preset):
    draw = ImageDraw.Draw(canvas)
    hero = str(data.get("hero", ""))
    title = str(data.get("title", ""))
    kicker = str(data.get("kicker", ""))
    subtitle = str(data.get("subtitle", ""))
    serial = str(data.get("serial", ""))

    hero_face = fit_font(draw, hero, 1100, 164, 72, 760)

    if preset == "signal-coral":
        draw.text((720, 190), hero, font=hero_face, fill=INK, anchor="ma")
        draw.text((720, 422), title, font=font(34, 520), fill=INK, anchor="ma")
        draw_vertical_text(canvas, serial, (1366, 54))
        return

    if preset == "orbit-orange":
        draw_vertical_text(canvas, kicker, (52, 52), 18)
        draw.text((720, 176), hero, font=hero_face, fill=INK, anchor="ma")
        draw.text((720, 382), title, font=font(36, 520), fill=INK, anchor="ma")
        draw.text((720, 448), subtitle, font=font(24, 430), fill=INK, anchor="ma")
        draw_vertical_text(canvas, serial, (1366, 54))
        return

    draw.text((720, 48), kicker, font=font(18, 450), fill=INK, anchor="ma")
    draw.text((720, 124), title, font=font(38, 520), fill=INK, anchor="ma")
    draw.text((720, 210), hero, font=hero_face, fill=INK, anchor="ma")
    draw.text((720, 448), subtitle, font=font(24, 430), fill=INK, anchor="ma")
    if preset == "sketch-black":
        draw_vertical_text(canvas, serial, (52, 52))


def draw_info_band(canvas, data, preset):
    draw = ImageDraw.Draw(canvas)
    columns = [64, 382, 706, 1056, 1402]
    top, bottom = 556, 714
    draw.line((columns[0], top, columns[-1], top), fill=INK, width=2)
    draw.line((columns[0], bottom, columns[-1], bottom), fill=INK, width=2)
    for x in columns[1:-1]:
        draw.line((x, top, x, bottom), fill=INK, width=2)

    records = [item for item in data.get("records", [])[:4] if isinstance(item, dict)]
    records += [{}] * (4 - len(records))
    for index, item in enumerate(records):
        x = columns[index] + 18
        if item.get("kind") == "graphic":
            if preset == "blossom-red":
                serial = str(data.get("serial", ""))
                draw.text((x, top + 18), serial, font=font(15, 420), fill=INK)
            continue
        draw.text((x, top + 18), str(item.get("label", "")), font=font(14, 400), fill=INK)
        draw.text((x, top + 62), str(item.get("value", "")), font=font(24, 500), fill=INK)


def compose(photo, data, preset):
    canvas = Image.new("RGBA", SIZE, "#F5F5F3")
    crop = cover_crop(photo, (SIZE[0] - PHOTO_X, SIZE[1]), data.get("crop_focus", [0.5, 0.5]))
    crop = ImageEnhance.Contrast(ImageOps.grayscale(crop)).enhance(0.65).convert("RGB")
    canvas.paste(crop, (PHOTO_X, 0))
    draw_text_route(canvas, data, preset)
    draw_info_band(canvas, data, preset)
    return canvas


def main():
    parser = argparse.ArgumentParser(description="生成不预制视觉风格的票根结构导引图")
    parser.add_argument("--photo", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--preset", required=True, choices=sorted(PRESETS))
    parser.add_argument("--image-mode", default="faithful-print", choices=["faithful-print", "artistic-redraw"])
    parser.add_argument("--out", required=True)
    parser.add_argument("--scale", type=int, default=1, choices=[1, 2, 3])
    args = parser.parse_args()

    with open(args.data, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict) or not str(data.get("title", "")).strip():
        raise SystemExit("JSON 必须包含非空 title")
    focus = data.get("crop_focus", [0.5, 0.5])
    if not isinstance(focus, list) or len(focus) != 2 or not all(isinstance(v, (int, float)) and 0 <= v <= 1 for v in focus):
        raise SystemExit("crop_focus 必须是 0–1 之间的 [x, y]")

    photo = Image.open(args.photo)
    canvas = compose(photo, data, args.preset)
    if args.scale > 1:
        canvas = canvas.resize((SIZE[0] * args.scale, SIZE[1] * args.scale), Image.Resampling.LANCZOS)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(out, quality=95)
    print(json.dumps({"out": str(out.resolve()), "size": canvas.size, "preset": args.preset}, ensure_ascii=False))


if __name__ == "__main__":
    main()
