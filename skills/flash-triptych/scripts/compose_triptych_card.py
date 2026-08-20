#!/usr/bin/env python3
"""把「三联情绪模特卡」的生成图重新排版，并贴上 WIBI / skill 品牌标记。

图像模型只负责出三张照片，画面里不含任何文字——品牌标记是随包的固化素材
（assets/brand/logo_wibi_skill.png），每次贴同一张，不现场画字。同一张生成图
还能一次导出小红书方图和手机锁屏两种画幅，背景色也可以在纸白 / 深炭黑两套
预设间切换——logo 会按背景明暗自动换色，不需要另外准备两版素材。

用法:
  compose_triptych_card.py IN.png --preset xhs  --out OUT.png
  compose_triptych_card.py IN.png --preset lock --out OUT.png --bg black
  compose_triptych_card.py IN.png --preset lock --width 1179 --height 2556 --out OUT.png
"""
import argparse, pathlib, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 按平台常见路径找一款有 Bold / Light（或近似细体）字重的无衬线字体，只在
# --logo-mode code（备用画字模式，例如随包 logo 素材缺失时）下用得到。
FONT_CANDIDATES = [
    ("/System/Library/Fonts/HelveticaNeue.ttc", 1, 7),   # macOS
    ("/System/Library/Fonts/Helvetica.ttc", 1, 4),        # macOS 备选
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", None, None),  # Linux
    ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", None, None),  # Linux
    ("C:\\Windows\\Fonts\\arialbd.ttf", None, None),      # Windows
]
FONT_LIGHT_FALLBACKS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "C:\\Windows\\Fonts\\arial.ttf",
]

LOGO_ASSET = pathlib.Path(__file__).resolve().parent.parent / "assets/brand/logo_wibi_skill.png"

# 纸白不是纯 #FFFFFF，是印刷纸张常见的那种略暖的白；深炭黑也不是纯 #000000，
# 避免死黑在手机屏幕上过于生硬。
BG_PRESETS = {"paper": "#F7F5F0", "black": "#0A0A0A"}

PRESETS = {
    # 画布尺寸, 照片组占宽, 照片组顶端位置(占高), logo 中心(占高), logo_w = logo 占画布宽度比例
    "xhs":    dict(size=(2048, 2048), band_w=0.74, band_top=0.26, logo_y=0.865, logo_w=0.20, wibi=0.052),
    "xhs34":  dict(size=(1536, 2048), band_w=0.82, band_top=0.24, logo_y=0.875, logo_w=0.24, wibi=0.058),
    "lock":   dict(size=(1290, 2796), band_w=0.90, band_top=0.375, logo_y=0.825, logo_w=0.30, wibi=0.052),
}


def resolve_fonts():
    for path, bold_idx, light_idx in FONT_CANDIDATES:
        p = pathlib.Path(path)
        if not p.is_file():
            continue
        if bold_idx is not None:
            return path, bold_idx, path, light_idx
        for light in FONT_LIGHT_FALLBACKS:
            if pathlib.Path(light).is_file():
                return path, 0, light, 0
        return path, 0, path, 0
    sys.exit(
        "没有在常见路径找到系统无衬线字体（Helvetica Neue / DejaVu Sans / Liberation Sans / Arial 之一）。\n"
        "请安装其中一款，或修改本文件顶部 FONT_CANDIDATES 指向可用字体。"
    )


def detect_band(img, white=244):
    """找出生成图里三联照片所在的矩形，自动忽略底部空白或杂色。

    还会一并找出三张照片之间的内部空白缝（AI 生成图自带的白纸缝），
    返回它们在整条 band 里的局部 x 范围，供调用方在非白色背景下把这些
    缝改画成画布背景色，而不是让生成图里烤死的白色透出来。
    """
    a = np.array(img.convert("L"))
    ink = (a < white)
    rows = ink.sum(axis=1)
    segs, start = [], None
    for i, v in enumerate(rows):
        if v > 0 and start is None:
            start = i
        elif v == 0 and start is not None:
            segs.append((start, i)); start = None
    if start is not None:
        segs.append((start, len(rows)))
    if not segs:
        raise SystemExit("没找到照片区域，检查输入图是不是白底")
    top, bot = max(segs, key=lambda s: rows[s[0]:s[1]].sum())
    cols = ink[top:bot].sum(axis=0)
    nz = np.nonzero(cols)[0]
    l, r = int(nz[0]), int(nz[-1]) + 1
    gaps, in_gap, gap_start = [], False, None
    for x in range(l, r):
        v = cols[x]
        if v == 0 and not in_gap:
            in_gap, gap_start = True, x
        elif v > 0 and in_gap:
            in_gap = False
            gaps.append((gap_start - l, x - l))
    return l, top, r, bot, gaps


def trim_panel_edges(band, gaps, fill, trim=2):
    """深色背景下裁掉照片面板自带的近白色描边。"""
    panel_bounds = [0]
    for g0, g1 in gaps:
        panel_bounds.extend([g0, g1])
    panel_bounds.append(band.width)
    cleaned = Image.new("RGB", band.size, fill)
    for i in range(0, len(panel_bounds) - 1, 2):
        x0, x1 = panel_bounds[i], panel_bounds[i + 1]
        left = min(x0 + trim, x1 - 1)
        right = max(left + 1, x1 - trim)
        top = min(trim, band.height - 1)
        bottom = max(top + 1, band.height - trim)
        panel = band.crop((left, top, right, bottom))
        target_w = x1 - x0 - trim * 2
        target_h = band.height - trim * 2
        if target_w <= 0 or target_h <= 0:
            continue
        panel = panel.resize((target_w, target_h), Image.Resampling.LANCZOS)
        cleaned.paste(panel, (x0 + trim, top))
    return cleaned


def draw_tracked(draw, cx, y, text, font, tracking, fill="#000000"):
    w = [draw.textlength(c, font=font) for c in text]
    total = sum(w) + tracking * (len(text) - 1)
    x = cx - total / 2
    for c, cw in zip(text, w):
        draw.text((x, y), c, font=font, fill=fill)
        x += cw + tracking
    return total


def recolor_logo_for_bg(logo, bg_mode):
    """按背景明暗给 logo 素材换色。

    素材本身只有两类颜色：WIBI 的黑色网点、skill 手写体的蓝色。纸白背景下原样使用；
    深炭黑背景下把黑色网点整体反相成白色（蓝色手写体在黑底上对比度已经足够，不用变），
    这样只维护一份素材就能覆盖两种背景。
    """
    if bg_mode != "black":
        return logo
    a = np.array(logo).astype(np.int16)
    r, g, b, alpha = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    is_blue = (b - r > 40) & (b - g > 30)
    out = a.copy()
    out[..., 0] = np.where(is_blue, r, 255 - r)
    out[..., 1] = np.where(is_blue, g, 255 - g)
    out[..., 2] = np.where(is_blue, b, 255 - b)
    out[..., 3] = alpha
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), mode="RGBA")


def draw_logo_asset(canvas, cx, cy, target_w, bg_mode, asset_path=LOGO_ASSET):
    """贴随包的 logo 素材图（skill 手写体 + WIBI 半调网点），不现场生成或画字。

    素材已经抠透明底、裁到内容边界；这里只做按背景换色、等比缩放和居中定位。
    """
    logo = Image.open(asset_path).convert("RGBA")
    logo = recolor_logo_for_bg(logo, bg_mode)
    target_h = round(logo.height * target_w / logo.width)
    logo_r = logo.resize((target_w, target_h), Image.LANCZOS)
    canvas.paste(logo_r, (round(cx - target_w / 2), round(cy - target_h / 2)), logo_r)


def draw_logo(canvas, cx, cy, wibi_px, ink="#000000"):
    """旧版代码画字备用方案：随包 logo 素材缺失时才会走到这里。"""
    d = ImageDraw.Draw(canvas)
    bold_path, bold_idx, light_path, light_idx = resolve_fonts()
    f_wibi = ImageFont.truetype(bold_path, wibi_px, index=bold_idx)
    tracking = wibi_px * 0.09

    small = max(7, int(wibi_px * 0.19))
    f_small = ImageFont.truetype(light_path, small, index=light_idx)
    track_small = small * 0.80
    gap = wibi_px * 0.155

    small_block_h = small * 1.3
    wibi_visual_h = wibi_px * 1.0
    block_h = small_block_h + gap + wibi_visual_h
    y = cy - block_h / 2

    draw_tracked(d, cx, y, "SKILL", f_small, track_small, ink)
    draw_tracked(d, cx, y + small_block_h + gap, "WIBI", f_wibi, tracking, ink)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("--preset", default="xhs", choices=list(PRESETS))
    p.add_argument("--out", required=True)
    p.add_argument("--width", type=int)
    p.add_argument("--height", type=int)
    p.add_argument("--bg", default="paper", choices=list(BG_PRESETS),
                   help="背景色预设：paper=纸白（默认，非纯白）；black=深炭黑。logo 颜色随之自动适配")
    p.add_argument("--paper", help="自定义背景色 hex，覆盖 --bg 预设")
    p.add_argument("--band-width", type=float, help="照片组占画布宽度的比例，覆盖预设")
    p.add_argument("--logo-mode", default="asset", choices=["asset", "code"],
                   help="asset（默认）=贴随包 logo 素材图；code=旧版代码实时画字，仅素材缺失时用")
    p.add_argument("--logo-asset", default=str(LOGO_ASSET), help="asset 模式下的素材图路径")
    p.add_argument("--logo-scale", type=float, default=1.0, help="logo 整体缩放")
    p.add_argument("--logo-y", type=float, help="logo 中心占画布高度的比例，覆盖预设")
    args = p.parse_args()

    cfg = dict(PRESETS[args.preset])
    W, H = cfg["size"]
    if args.width:  W = args.width
    if args.height: H = args.height
    band_w = args.band_width or cfg["band_w"]
    bg_hex = args.paper or BG_PRESETS[args.bg]

    src = Image.open(args.src).convert("RGB")
    l, t, r, b, gaps = detect_band(src)
    band = src.crop((l, t, r, b))
    if args.bg == "black":
        # 黑底会放大模型成片自带的白色面板边缘；先裁边，再补黑色缝隙。
        band = trim_panel_edges(band, gaps, bg_hex)

    target_w = round(W * band_w)
    target_h = round(band.height * target_w / band.width)
    scale = target_w / band.width
    band = band.resize((target_w, target_h), Image.LANCZOS)

    canvas = Image.new("RGB", (W, H), bg_hex)
    px, py = (W - target_w) // 2, round(H * cfg["band_top"])
    canvas.paste(band, (px, py))
    if bg_hex.upper() != "#FFFFFF":
        # 三张照片之间是生成图自带的白纸缝，非纯白背景下要改画成画布背景色，
        # 否则这几条白缝会在深色或非白背景上突兀地透出来。
        cd = ImageDraw.Draw(canvas)
        for g0, g1 in gaps:
            cd.rectangle([px + g0 * scale, py, px + g1 * scale, py + target_h], fill=bg_hex)
    logo_y = args.logo_y or cfg["logo_y"]
    ink = "#FFFFFF" if args.bg == "black" and not args.paper else "#000000"
    if args.logo_mode == "asset" and pathlib.Path(args.logo_asset).is_file():
        logo_w = round(W * cfg["logo_w"] * args.logo_scale)
        draw_logo_asset(canvas, W / 2, H * logo_y, logo_w, args.bg, args.logo_asset)
    else:
        wibi_px = round(W * cfg["wibi"] * args.logo_scale)
        draw_logo(canvas, W / 2, H * logo_y, wibi_px, ink)

    pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.out)
    print(f"{args.out}  {W}×{H}  bg={args.bg}({bg_hex})  照片区 {r-l}×{b-t} -> {target_w}×{target_h}")


if __name__ == "__main__":
    main()
