#!/usr/bin/env python3
"""Check this installed Wibi Style Skill against its public manifest."""

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


SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:[-+].*)?$")


def version_key(value: str) -> tuple[int, int, int]:
    match = SEMVER.fullmatch(value)
    if not match:
        raise ValueError(f"invalid semantic version: {value}")
    return tuple(int(part) for part in match.groups())


def main() -> int:
    parser = argparse.ArgumentParser(description="Check for a newer Wibi Style Skill release")
    parser.add_argument("--timeout", type=float, default=3.0)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    manifest_path = Path(__file__).resolve().parents[1] / "manifest.json"
    local = json.loads(manifest_path.read_text(encoding="utf-8"))
    remote_url = os.environ.get("WIBI_STYLE_UPDATE_MANIFEST", local["update_manifest_url"])
    if not remote_url:
        result = {
            "status": "CHECK_UNAVAILABLE",
            "slug": local.get("slug", "unknown"),
            "reason": "not_published",
        }
        if args.as_json:
            print(json.dumps(result, ensure_ascii=False))
        else:
            print(f"CHECK_UNAVAILABLE reason={result['reason']}")
        return 0
    parsed_url = urllib.parse.urlsplit(remote_url)
    separator = "&" if parsed_url.query else "?"
    checked_url = (
        f"{remote_url}{separator}checked_at={int(time.time())}"
        if parsed_url.scheme in {"http", "https"}
        else remote_url
    )
    request = urllib.request.Request(
        checked_url,
        headers={"User-Agent": "wibi-style-update-check/1", "Cache-Control": "no-cache"},
    )

    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            remote = json.loads(response.read().decode("utf-8"))
        if remote.get("slug") != local.get("slug"):
            raise ValueError("remote manifest slug does not match local skill")
        current = local["version"]
        latest = remote["version"]
        status = "UPDATE_AVAILABLE" if version_key(latest) > version_key(current) else "UP_TO_DATE"
        result = {
            "status": status,
            "slug": local["slug"],
            "current": current,
            "latest": latest,
            "install_url": remote.get("install_url", local["install_url"]),
        }
    except (OSError, ValueError, KeyError, json.JSONDecodeError, urllib.error.URLError) as error:
        result = {
            "status": "CHECK_UNAVAILABLE",
            "slug": local.get("slug", "unknown"),
            "reason": type(error).__name__,
        }

    if args.as_json:
        print(json.dumps(result, ensure_ascii=False))
    elif result["status"] == "UPDATE_AVAILABLE":
        print(
            "UPDATE_AVAILABLE "
            f"current={result['current']} latest={result['latest']} "
            f"install_url={result['install_url']}"
        )
    elif result["status"] == "UP_TO_DATE":
        print(f"UP_TO_DATE version={result['current']}")
    else:
        print(f"CHECK_UNAVAILABLE reason={result['reason']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
