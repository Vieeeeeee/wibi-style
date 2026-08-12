#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
FILES=("README.md","SKILL.md","LICENSE","NOTICE","manifest.json"); AUTHOR="@威比 Hunter Wei."; NOTE="抖音、小红书同名"
def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--always",action="store_true"); args=parser.parse_args(); root=Path(__file__).resolve().parents[1]; manifest_path=root/"manifest.json"; manifest=json.loads(manifest_path.read_text(encoding="utf-8")); source=manifest["official_source"]; missing=[]
    for name in FILES:
        path=root/name
        if not path.is_file(): missing.append(name); continue
        text=path.read_text(encoding="utf-8")
        for value in (AUTHOR,NOTE,source):
            if value not in text: missing.append(f"{name}:{value}")
    fingerprint=hashlib.sha256(manifest_path.read_bytes()+str(manifest_path.stat().st_ino).encode()+str(manifest_path.stat().st_mtime_ns).encode()).hexdigest(); state_dir=Path.home()/".codex"/"wibi-style"/"author-card-state"; state=state_dir/f"{manifest['slug']}.json"
    try: previous=json.loads(state.read_text(encoding="utf-8"))
    except (FileNotFoundError,json.JSONDecodeError): previous={}
    if not args.always and not missing and previous.get("fingerprint")==fingerprint: print("AUTHOR_CARD_ALREADY_SHOWN"); return 0
    print("SHOW_SKILL_INFO"); print(f"名称：{manifest['name']}（{manifest['slug']}）"); print(f"版本：{manifest['version']}"); print(f"作者：{AUTHOR}（{NOTE}）"); print(f"官方来源：{source}"); print(f"安装路径：{root}"); print("署名完整性：不完整，建议从官方来源重新安装" if missing else "署名完整性：通过")
    if not missing: state_dir.mkdir(parents=True,exist_ok=True); state.write_text(json.dumps({"fingerprint":fingerprint,"version":manifest["version"]},ensure_ascii=False)+"\n",encoding="utf-8")
    return 0
if __name__ == "__main__": raise SystemExit(main())
