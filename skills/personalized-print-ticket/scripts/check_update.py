#!/usr/bin/env python3
"""从官方 GitHub Raw 地址只读检查当前 Skill 版本。"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
OFFICIAL_HOST = "raw.githubusercontent.com"
OFFICIAL_PATH_PREFIX = "/Vieeeeeee/wibi-style/"
MAX_MANIFEST_BYTES = 256 * 1024


def version_key(version: str) -> tuple[int, int, int]:
    if not SEMVER.fullmatch(version):
        raise ValueError("invalid semantic version")
    return tuple(int(part) for part in version.split("."))


def checked_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname != OFFICIAL_HOST
        or not parsed.path.startswith(OFFICIAL_PATH_PREFIX)
        or parsed.username
        or parsed.password
        or parsed.port not in (None, 443)
    ):
        raise ValueError("update manifest must use the official GitHub Raw path")
    return url


def read_remote_manifest(url: str, timeout: float) -> dict:
    request = urllib.request.Request(
        checked_url(url),
        headers={"User-Agent": "personalized-print-ticket-update-checker"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        checked_url(response.geturl())
        declared_length = response.headers.get("Content-Length")
        if declared_length and int(declared_length) > MAX_MANIFEST_BYTES:
            raise ValueError("update manifest is too large")
        raw = response.read(MAX_MANIFEST_BYTES + 1)
        if len(raw) > MAX_MANIFEST_BYTES:
            raise ValueError("update manifest is too large")
    payload = json.loads(raw.decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("update manifest must be a JSON object")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    parser.add_argument("--timeout", type=float, default=5.0, help="网络超时秒数")
    args = parser.parse_args()

    package_dir = Path(__file__).resolve().parents[1]
    local_manifest = json.loads((package_dir / "manifest.json").read_text(encoding="utf-8"))
    current = local_manifest["version"]
    slug = local_manifest["slug"]
    manifest_url = os.environ.get(
        "WIBI_STYLE_UPDATE_MANIFEST",
        local_manifest["update_manifest_url"],
    )

    try:
        remote_manifest = read_remote_manifest(manifest_url, args.timeout)
        latest = remote_manifest["version"]
        status = "UPDATE_AVAILABLE" if version_key(latest) > version_key(current) else "UP_TO_DATE"
        result = {
            "status": status,
            "slug": slug,
            "current": current,
            "latest": latest,
            "checked_at": int(time.time()),
        }
    except (KeyError, ValueError, json.JSONDecodeError, urllib.error.URLError) as error:
        result = {
            "status": "CHECK_UNAVAILABLE",
            "slug": slug,
            "reason": type(error).__name__,
        }

    if args.json:
        print(json.dumps(result, ensure_ascii=False))
    elif result["status"] == "UPDATE_AVAILABLE":
        print(f"发现新版本：{result['current']} → {result['latest']}")
    elif result["status"] == "UP_TO_DATE":
        print(f"当前已是最新版：{result['current']}")
    else:
        print("暂时无法检查更新。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
