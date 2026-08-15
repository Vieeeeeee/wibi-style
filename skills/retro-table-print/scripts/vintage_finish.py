#!/usr/bin/env python3
"""把一张干净的数字生成图收尾成旧杂志印刷的质感。

复古感的来源是光学解析力有限和印刷网点吃掉高频，不是滤镜色。
所以这一步只动解析力、颗粒和动态范围，不动色相和饱和度。

强度默认自动：先量当前图的锐度，再搜一个能落进目标区间的强度。
不同图像模型出图的锐度差很多（实测同一张原片，一个模型的锐度是另一个的两倍多），
写死强度换个模型就废，所以这里自己量自己调。

用法：
    python3 vintage_finish.py 输入图 [--out 输出图] [--strength auto|0.7]

缺少 Pillow 时打印 VINTAGE_FINISH_SKIPPED 并正常退出，不阻断出图。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# 目标区间来自本项目 8 张已验收成片的实测（指标见 measure_sharpness）。
TARGET_LOW = 16.5
TARGET_HIGH = 22.5
TARGET_AIM = 19.5
METRIC_HEIGHT = 1200      # 量之前统一缩到这个高度，保证不同尺寸可比

REFERENCE_HEIGHT = 1600   # 下面几个参数是在这个高度上标定的，实际按比例缩放
BLUR_RADIUS = 1.1
GRAIN_SIGMA = 4.5
HALFTONE_AMPLITUDE = 3
BLACK_POINT = 12          # 印刷暗部抬起来，不到纯黑
WHITE_POINT = 238         # 印刷高光压下去，不到纯白


def measure_sharpness(image) -> float:
    """拉普拉斯响应的标准差。数值越大越锐。"""
    from PIL import Image, ImageFilter, ImageStat
    width, height = image.size
    probe = image.resize((max(1, int(width * METRIC_HEIGHT / height)), METRIC_HEIGHT), Image.LANCZOS)
    laplacian = probe.convert("L").filter(
        ImageFilter.Kernel((3, 3), [0, 1, 0, 1, -4, 1, 0, 1, 0], scale=1, offset=128)
    )
    return ImageStat.Stat(laplacian).stddev[0]


def apply_finish(image, strength: float):
    from PIL import Image, ImageChops, ImageFilter

    if strength <= 0:
        return image
    width, height = image.size
    scale = height / REFERENCE_HEIGHT   # 参数随分辨率缩放，换尺寸观感一致

    # 1. 有限解析力：降采样再放回原尺寸，高频细节一去不返
    divisor = 1 + 2 * strength
    if divisor > 1.05:
        small = image.resize((max(1, int(width / divisor)), max(1, int(height / divisor))), Image.LANCZOS)
        image = small.resize((width, height), Image.BICUBIC)

    # 2. 光学柔化
    radius = BLUR_RADIUS * strength * scale
    if radius > 0.05:
        image = image.filter(ImageFilter.GaussianBlur(radius))

    # 3. 印刷网点：小方块平铺，成本低且是规则纹理
    amplitude = max(1, round(HALFTONE_AMPLITUDE * strength))
    tile_size = 4
    tile = Image.new("L", (tile_size, tile_size))
    tile.putdata([128 + amplitude if (x + y) % 2 == 0 else 128 - amplitude
                  for y in range(tile_size) for x in range(tile_size)])
    halftone = Image.new("L", (width, height))
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            halftone.paste(tile, (x, y))
    image = ImageChops.add(image, halftone.convert("RGB"), scale=1, offset=-128)

    # 4. 胶片颗粒
    noise = Image.effect_noise((width, height), GRAIN_SIGMA * strength).convert("RGB")
    image = ImageChops.add(image, noise, scale=1, offset=-128)

    # 5. 印刷动态范围：暗部抬起、高光压住，不出现纯黑纯白
    black = BLACK_POINT * strength
    white = 255 - (255 - WHITE_POINT) * strength
    span = white - black
    return image.point([round(black + value * span / 255) for value in range(256)] * 3)


def auto_strength(image) -> tuple[float, float, list[str]]:
    """二分搜一个能把锐度压进目标区间的强度。"""
    trace = []
    raw = measure_sharpness(image)
    trace.append(f"原图 {raw:.2f}")
    if raw <= TARGET_HIGH:
        return 0.0, raw, trace          # 本来就够柔，不用动

    low, high, best, best_metric = 0.0, 1.5, 1.0, None
    for _ in range(5):
        mid = (low + high) / 2
        metric = measure_sharpness(apply_finish(image, mid))
        trace.append(f"强度 {mid:.2f} → {metric:.2f}")
        if best_metric is None or abs(metric - TARGET_AIM) < abs(best_metric - TARGET_AIM):
            best, best_metric = mid, metric
        if abs(metric - TARGET_AIM) <= 1.5:
            return mid, metric, trace    # 够居中就停，落在区间边沿不算够好
        if metric > TARGET_HIGH:
            low = mid                    # 还太锐，加大强度
        else:
            high = mid                   # 过头了，减小强度
    return best, best_metric, trace


def main() -> int:
    parser = argparse.ArgumentParser(description="旧杂志印刷质感收尾")
    parser.add_argument("image", type=Path)
    parser.add_argument("--out", type=Path, help="默认在原文件名后加 _vintage")
    parser.add_argument("--strength", default="auto",
                        help="auto（默认，自己量自己调）或 0 到 1.5 的数字")
    args = parser.parse_args()

    try:
        from PIL import Image
    except ImportError:
        print("VINTAGE_FINISH_SKIPPED reason=pillow_not_installed")
        print("这一步需要 Pillow。可以运行 pip3 install Pillow 后重试；跳过不影响已生成的图片。")
        return 0

    if not args.image.is_file():
        print(f"VINTAGE_FINISH_FAILED reason=file_not_found path={args.image}")
        return 1

    try:
        image = Image.open(args.image).convert("RGB")
    except Exception as error:
        print(f"VINTAGE_FINISH_FAILED reason=cannot_open_image detail={type(error).__name__}")
        print(f"这个文件读不出图片：{args.image}")
        return 1

    if str(args.strength).lower() == "auto":
        strength, metric, trace = auto_strength(image)
        print("[auto] " + " | ".join(trace))
        if strength == 0:
            print(f"VINTAGE_FINISH_SKIPPED reason=already_soft metric={metric:.2f}")
            print("这张图本来就够柔，不需要收尾。")
            return 0
    else:
        try:
            strength = max(0.0, min(1.5, float(args.strength)))
        except ValueError:
            print(f"VINTAGE_FINISH_FAILED reason=bad_strength value={args.strength}")
            return 1
        if strength == 0:
            print("VINTAGE_FINISH_SKIPPED reason=strength_zero")
            return 0
        metric = None

    result = apply_finish(image, strength)
    final_metric = measure_sharpness(result)

    destination = args.out or args.image.with_name(f"{args.image.stem}_vintage{args.image.suffix or '.jpg'}")
    save_kwargs = {"quality": 95} if destination.suffix.lower() in {".jpg", ".jpeg"} else {}
    try:
        result.save(destination, **save_kwargs)
    except Exception as error:
        print(f"VINTAGE_FINISH_FAILED reason=cannot_save detail={type(error).__name__}")
        print(f"写不进这个位置：{destination}")
        return 1
    print(f"VINTAGE_FINISH_OK out={destination} strength={strength:.2f} "
          f"metric={final_metric:.2f} target={TARGET_LOW}-{TARGET_HIGH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
