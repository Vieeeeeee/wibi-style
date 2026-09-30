#!/usr/bin/env python3
"""Show the install card or the two-section per-conversation welcome card."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from community_info import load_community


REQUIRED_FILES = (
    "README.md",
    "SKILL.md",
    "LICENSE",
    "NOTICE",
    "manifest.json",
    "scripts/community_info.py",
)
AUTHOR = "@威比 Hunter Wei."
AUTHOR_NOTE = "抖音、小红书同名"


def main() -> int:
    parser = argparse.ArgumentParser(description="Show Wibi Style Skill information")
    parser.add_argument("--always", action="store_true", help="show even if this installed copy was shown before")
    parser.add_argument("--welcome", action="store_true", help="show the two-section welcome card")
    parser.add_argument(
        "--input-state",
        choices=("waiting", "received"),
        default="waiting",
        help="choose the next-action copy shown in the welcome card",
    )
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    manifest_path = skill_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    official_source = manifest.get("official_source", manifest.get("install_url", ""))

    required_text = (AUTHOR, AUTHOR_NOTE, official_source)
    missing: list[str] = []
    for name in REQUIRED_FILES:
        path = skill_dir / name
        if not path.is_file():
            missing.append(name)
            continue
        text = path.read_text(encoding="utf-8")
        if name in {"README.md", "SKILL.md", "LICENSE", "NOTICE", "manifest.json"}:
            for value in required_text:
                if value and value not in text:
                    missing.append(f"{name}:{value}")

    if args.welcome:
        welcome = manifest.get("welcome", {})
        next_lines = welcome.get(args.input_state)
        if not isinstance(next_lines, list) or not next_lines:
            print("WELCOME_CONFIG_INCOMPLETE")
            return 1
        print("SHOW_SKILL_WELCOME")
        print()
        print(f"### {manifest['name']}")
        print()
        print(f"**Visual Skill by {AUTHOR}**  ")
        print(AUTHOR_NOTE)
        print()
        print("如果你也喜欢研究好玩的 AI 视觉 Skill，可以回复 **「进群」**，来一起交流～")
        print()
        print("---")
        print()
        print("#### 现在开始")
        print()
        for index, line in enumerate(next_lines):
            suffix = "  " if index < len(next_lines) - 1 else ""
            print(f"{line}{suffix}")
        if missing:
            print()
            print("署名完整性：不完整，建议从官方来源重新安装")
        return 0

    fingerprint_source = (
        manifest_path.read_bytes()
        + str(manifest_path.stat().st_ino).encode("ascii")
        + str(manifest_path.stat().st_mtime_ns).encode("ascii")
    )
    fingerprint = hashlib.sha256(fingerprint_source).hexdigest()
    state_dir = Path.home() / ".codex" / "wibi-style" / "author-card-state"
    state_path = state_dir / f"{manifest['slug']}.json"
    previous = {}
    try:
        previous = json.loads(state_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    if not args.always and not missing and previous.get("fingerprint") == fingerprint:
        print("AUTHOR_CARD_ALREADY_SHOWN")
        return 0

    print("SHOW_SKILL_INFO")
    print(f"名称：{manifest['name']}（{manifest['slug']}）")
    print(f"版本：{manifest['version']}")
    print(f"作者：{AUTHOR}（{AUTHOR_NOTE}）")
    print(f"官方来源：{official_source}")
    print(f"安装路径：{skill_dir}")
    community = load_community(timeout=2.0)
    print(f"交流学习群：**{community['name']}**")
    print(f"可以交流：{community['description']}")
    print("获取当前群二维码：回复“进群”")
    print(f"稳定入口：{community['landing_url']}")
    if missing:
        print("署名完整性：不完整，建议从官方来源重新安装")
    else:
        print("署名完整性：通过")
        state_dir.mkdir(parents=True, exist_ok=True)
        state_path.write_text(
            json.dumps({"fingerprint": fingerprint, "version": manifest["version"]}, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
