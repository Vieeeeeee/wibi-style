#!/usr/bin/env python3
"""验证极简导引、四格信息与四款字段路由。"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw


HERE = Path(__file__).resolve().parent
COMPOSITOR = HERE / "compose_ticket.py"
COMPILER = HERE / "compile_prompt.py"
FINISHER = HERE / "finish_ticket.py"
PRESETS = ["orbit-orange", "blossom-red", "sketch-black", "signal-coral"]


def make_fixture(path):
    image = Image.new("RGB", (1200, 900), "#D8D3C9")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 500, 1200, 900), fill="#52575B")
    draw.ellipse((770, 90, 1010, 330), fill="#F0D56B")
    for index, height in enumerate([430, 330, 520, 390, 470]):
        x = 80 + index * 220
        draw.rectangle((x, 500 - height, x + 150, 500), fill=(55 + index * 14, 72 + index * 9, 82 + index * 8))
    image.save(path)


def run(command):
    subprocess.run(command, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(HERE.parent.parent.parent / "04_自测"))
    args = parser.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    source = COMPOSITOR.read_text(encoding="utf-8")
    forbidden = ["Library/Fonts", "USER_FONTS", "make_photo_plate", "textured_paper", ".line((PHOTO_X"]
    found = [token for token in forbidden if token in source]
    if found:
        raise SystemExit("compose_ticket.py 仍含旧实现：" + ", ".join(found))

    photo = out_dir / "fixture-city-walk.png"
    data_path = out_dir / "fixture-ticket.json"
    make_fixture(photo)
    data = {
        "hero": "夏末散步",
        "title": "LATE SUMMER WALK",
        "kicker": "A CITY MEMORY TICKET",
        "subtitle": "风在楼与楼之间穿过",
        "serial": "VIE-0910-1740",
        "memory_mode": "scene-observation",
        "records": [
            {"label": "PLACE", "value": "西向街区"},
            {"label": "SCENE", "value": "夏末斜阳"},
            {"label": "KEEP", "value": "楼间的风"},
            {"kind": "graphic", "motif": "sun"},
        ],
        "subject_summary": "一个人在夏末傍晚穿过楼群之间的街道",
        "identity_anchors": ["单人步行", "背景建筑", "右上方低太阳"],
        "scene_facts": ["室外", "傍晚低角度光", "城市街道"],
        "crop_focus": [0.52, 0.50],
    }
    data_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    for preset in PRESETS:
        guide = out_dir / f"selftest-{preset}.png"
        run([
            sys.executable, str(COMPOSITOR),
            "--photo", str(photo),
            "--data", str(data_path),
            "--preset", preset,
            "--image-mode", "faithful-print",
            "--out", str(guide),
        ])
        with Image.open(guide) as image:
            guide_image_size = image.size
            if image.size != (2048, 769):
                raise SystemExit(f"{preset}: unexpected size {image.size}")

        prompt = out_dir / f"selftest-{preset}-prompt.md"
        run([
            sys.executable, str(COMPILER),
            "--photo", str(photo),
            "--guide", str(guide),
            "--data", str(data_path),
            "--preset", preset,
            "--image-mode", "faithful-print",
            "--out", str(prompt),
        ])
        compiled = prompt.read_text(encoding="utf-8")
        required = [data["hero"], data["title"], data["serial"]]
        if any(value not in compiled for value in required):
            raise SystemExit(f"{preset}: required route content missing")
        if not any(token in compiled for token in ["单排四格", "四个大格", "四个主格"]):
            raise SystemExit(f"{preset}: four-cell structure missing")
        if compiled.count("- record ") != 3 or compiled.count("- graphic cell:") != 1:
            raise SystemExit(f"{preset}: information band is not three records plus one graphic")
        if preset == "signal-coral":
            if '- kicker:' in compiled or '- subtitle:' in compiled:
                raise SystemExit("signal-coral: unsupported text tier leaked into exact copy")
        elif '- kicker:' not in compiled or '- subtitle:' not in compiled:
            raise SystemExit(f"{preset}: supported text tier missing")

        finished = out_dir / f"selftest-{preset}-finished.png"
        transparent = out_dir / f"selftest-{preset}-cutout.png"
        run([
            sys.executable, str(FINISHER),
            "--ticket", str(guide),
            "--out", str(finished),
            "--transparent-out", str(transparent),
        ])
        with Image.open(finished) as image:
            if image.size != guide_image_size:
                raise SystemExit(f"{preset}: finished canvas size changed")
            if image.getpixel((0, 0)) != (5, 5, 5):
                raise SystemExit(f"{preset}: black presentation background missing")
        with Image.open(transparent) as image:
            if image.mode != "RGBA":
                raise SystemExit(f"{preset}: cutout is not RGBA")
            alpha = image.getchannel("A")
            if alpha.getpixel((0, 0)) != 0 or alpha.getpixel((image.width // 2, image.height // 2)) != 255:
                raise SystemExit(f"{preset}: cutout alpha mask failed")

    print(json.dumps({"ok": True, "presets": PRESETS, "out_dir": str(out_dir.resolve())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
