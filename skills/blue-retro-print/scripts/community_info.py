#!/usr/bin/env python3
"""Read the current Wibi community entry from the official repository."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_CONFIG_URL = "https://raw.githubusercontent.com/Vieeeeeee/wibi-style/main/community.json"
FALLBACK = {
    "schema_version": 1,
    "status": "unavailable",
    "name": "威比 😌 AIGC 学习群",
    "description": "Skill 安装、选图、生图问题和新风格内测",
    "landing_url": "https://github.com/Vieeeeeee/wibi-style#加入交流群",
    "fallback_wechat": "Wibi2077",
    "social_handle": "@威比 Hunter Wei.",
    "social_note": "抖音、小红书同名",
}
REQUIRED_FIELDS = (
    "schema_version",
    "revision",
    "name",
    "description",
    "join_url",
    "qr_image_url",
    "valid_until",
    "landing_url",
    "fallback_wechat",
    "social_handle",
    "social_note",
)


def _is_expired(value: str) -> bool:
    expires_at = datetime.fromisoformat(value)
    if expires_at.tzinfo is None:
        raise ValueError("valid_until must include a timezone")
    return datetime.now(timezone.utc) > expires_at.astimezone(timezone.utc)


def load_community(timeout: float = 3.0) -> dict[str, object]:
    config_url = os.environ.get("WIBI_COMMUNITY_CONFIG_URL", DEFAULT_CONFIG_URL)
    parsed = urllib.parse.urlsplit(config_url)
    separator = "&" if parsed.query else "?"
    checked_url = (
        f"{config_url}{separator}checked_at={int(time.time())}"
        if parsed.scheme in {"http", "https"}
        else config_url
    )
    request = urllib.request.Request(
        checked_url,
        headers={"User-Agent": "wibi-style-community/1", "Cache-Control": "no-cache"},
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if payload.get("schema_version") != 1:
            raise ValueError("unsupported community schema")
        for field in REQUIRED_FIELDS:
            if not payload.get(field):
                raise ValueError(f"missing community field: {field}")
        for field in ("join_url", "qr_image_url", "landing_url"):
            if urllib.parse.urlsplit(payload[field]).scheme != "https":
                raise ValueError(f"community URL must use https: {field}")
        result = dict(payload)
        result["status"] = "expired" if _is_expired(str(payload["valid_until"])) else "available"
        if result["status"] == "expired":
            result.pop("join_url", None)
            result.pop("qr_image_url", None)
        return result
    except (
        OSError,
        ValueError,
        KeyError,
        TypeError,
        json.JSONDecodeError,
        urllib.error.URLError,
    ) as error:
        result = dict(FALLBACK)
        result["reason"] = type(error).__name__
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Show the current Wibi AIGC community entry")
    parser.add_argument("--timeout", type=float, default=3.0)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    result = load_community(timeout=args.timeout)
    encoded = json.dumps(result, ensure_ascii=False, sort_keys=True)
    if args.as_json:
        print(encoded)
    else:
        print("SHOW_COMMUNITY_INFO")
        print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
