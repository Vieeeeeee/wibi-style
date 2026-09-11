#!/usr/bin/env python3
"""将某一票根预设的完整 Prompt、照片分析和逐字文案合并成一次 image_gen 调用包。"""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
with open(ROOT / "design-system/presets.json", "r", encoding="utf-8") as fh:
    SYSTEM = json.load(fh)

TEXT_ROUTES = {
    "orbit-orange": ["hero", "title", "kicker", "subtitle", "serial"],
    "blossom-red": ["hero", "title", "kicker", "subtitle", "serial"],
    "sketch-black": ["hero", "title", "kicker", "subtitle", "serial"],
    "signal-coral": ["hero", "title", "serial"],
}

ROUTE_NOTES = {
    "orbit-orange": "kicker 替换参考票左侧竖排文字；serial 位于照片前的竖排票号槽；hero、title 与 subtitle 构成中央层级。",
    "blossom-red": "kicker 与 title 位于 Hero 上方；subtitle 位于 Hero 下方；serial 与照片提取图案共享第四格。",
    "sketch-black": "kicker 与 title 位于 Hero 上方；subtitle 位于 Hero 下方；serial 替换参考票左侧竖排票号。",
    "signal-coral": "只保留中文 hero、英文 title 和 serial；英文 title 使用 Hero 下方唯一的辅助标题槽，不显示 kicker 或 subtitle。",
}


def resolved(path):
    return str(Path(path).expanduser().resolve())


def compact_list(value):
    if not value:
        return "未额外指定"
    if isinstance(value, list):
        return "；".join(str(item) for item in value)
    return str(value)


def main():
    parser = argparse.ArgumentParser(description="编译定制票根的一次生成 Prompt")
    parser.add_argument("--photo", required=True, help="用户内容照片")
    parser.add_argument("--guide", required=True, help="compose_ticket.py 产出的排版导引图")
    parser.add_argument("--data", required=True)
    parser.add_argument("--preset", required=True, choices=sorted(SYSTEM["presets"]))
    parser.add_argument("--image-mode", default="faithful-print", choices=["faithful-print", "artistic-redraw"])
    parser.add_argument("--style-reference", help="选中的原始印刷风格参考；默认使用项目本地参考")
    parser.add_argument("--out", required=True, help="完整 Prompt 文本")
    parser.add_argument("--manifest-out", help="包含三张输入图与 Prompt 的 JSON 调用包")
    args = parser.parse_args()

    with open(args.data, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not str(data.get("title", "")).strip():
        raise SystemExit("JSON 必须包含非空 title")

    preset = SYSTEM["presets"][args.preset]
    template = (ROOT / preset["prompt"]).read_text(encoding="utf-8")
    local_reference = (ROOT / preset["local_style_reference"]).resolve()
    style_reference = Path(args.style_reference).expanduser().resolve() if args.style_reference else local_reference
    missing = [path for path in [Path(args.photo), Path(args.guide), style_reference] if not path.is_file()]
    if missing:
        raise SystemExit("缺少输入图：" + "，".join(str(path) for path in missing))

    mode_text = {
        "faithful-print": "图像方式为忠实印刷化：不重新设计人物、建筑、食物或场景，仅将用户照片裁切并转译为该预设的印刷图版。",
        "artistic-redraw": "图像方式为艺术化重绘：用该预设的线条和块面重绘用户照片，但主体数量、身份锚点、姿态、物件和场景方向不变，不新增照片中没有的内容。",
    }[args.image_mode]
    exact_lines = [f'- {key}: "{data[key]}"' for key in TEXT_ROUTES[args.preset] if data.get(key) not in (None, "")]
    for item in data.get("records", []):
        if isinstance(item, dict) and item.get("kind") == "graphic":
            exact_lines.append(f'- graphic cell: motif "{item.get("motif", "photo-derived mark")}"')
        elif isinstance(item, dict) and item.get("label") and item.get("value"):
            exact_lines.append(f'- record {item["label"]}: "{item["value"]}"')
    exact = "\n".join(exact_lines)
    hierarchy = ""
    if data.get("hero"):
        hierarchy = "中文 Hero 是全票最大文字和唯一文字焦点；英文 title 仅作辅助，保持明显尺度差。排版导引中的字体只是位置与字量占位，最终字形由图像模型根据所选票根参考自行设计。Hero 可以选择性呈现窄压、缺墨、墨边波动、轻微重影或基线误差，保持准确可读并形成印刷年代感；信息格使用更克制的功能字形，与 Hero 明显区分。底部固定四个大格，每格只承担一个角色，其中最多一格使用与照片有关的简洁图案。票面与照片依靠纸色和图版密度自然交界，不出现贯穿全高的竖分割线。"
    context = f"""

## 本次照片分析

- 画面摘要：{data.get('subject_summary', '以用户内容照片为准')}
- 必须保留的身份锚点：{compact_list(data.get('identity_anchors'))}
- 已确认场景事实：{compact_list(data.get('scene_facts'))}
- 纪念信息模式：{data.get('memory_mode', 'scene-observation')}
- {mode_text}
- {hierarchy}
- 本预设字段路由：{ROUTE_NOTES[args.preset]}

## 逐字文案

{exact}

排版导引图中的文字与上述逐字文案是同一份内容。完成图只出现这些文字，所有字符逐字保持，将原始印刷风格参考的字形性格和印刷残缺应用到导引图的文字上。一次完成全部构图、照片转译、排字与纸墨质感。
"""
    prompt = template.rstrip() + context
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(prompt + "\n", encoding="utf-8")

    manifest = {
        "preset": args.preset,
        "image_mode": args.image_mode,
        "referenced_image_paths": [str(style_reference), resolved(args.photo), resolved(args.guide)],
        "reference_roles": ["原始票根编辑底图", "用户内容照片", "排版导引图"],
        "prompt_path": str(out.resolve()),
        "prompt": prompt,
    }
    manifest_path = Path(args.manifest_out) if args.manifest_out else out.with_suffix(".json")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"prompt": str(out.resolve()), "manifest": str(manifest_path.resolve()), "preset": args.preset}, ensure_ascii=False))


if __name__ == "__main__":
    main()
