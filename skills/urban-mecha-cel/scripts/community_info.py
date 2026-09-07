#!/usr/bin/env python3
"""Read the current Wibi community entry from the official repository."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
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
MAX_QR_BYTES = 5 * 1024 * 1024
OFFICIAL_QR_HOST = "raw.githubusercontent.com"
OFFICIAL_QR_PATH_PREFIX = "/Vieeeeeee/wibi-style/"


def _is_expired(value: str) -> bool:
    expires_at = datetime.fromisoformat(value)
    if expires_at.tzinfo is None:
        raise ValueError("valid_until must include a timezone")
    return datetime.now(timezone.utc) > expires_at.astimezone(timezone.utc)


def _download_qr(url: str, revision: str, timeout: float) -> str:
    parsed = urllib.parse.urlsplit(url)
    if (
        parsed.scheme != "https"
        or parsed.hostname != OFFICIAL_QR_HOST
        or not parsed.path.startswith(OFFICIAL_QR_PATH_PREFIX)
    ):
        raise ValueError("QR image must come from the official GitHub repository")

    separator = "&" if parsed.query else "?"
    checked_url = f"{url}{separator}checked_at={int(time.time())}"
    request = urllib.request.Request(
        checked_url,
        headers={"User-Agent": "wibi-style-community/2", "Cache-Control": "no-cache"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        final = urllib.parse.urlsplit(response.geturl())
        if (
            final.scheme != "https"
            or final.hostname != OFFICIAL_QR_HOST
            or not final.path.startswith(OFFICIAL_QR_PATH_PREFIX)
        ):
            raise ValueError("QR download redirected outside the official GitHub repository")
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_QR_BYTES:
            raise ValueError("QR image is too large")
        data = response.read(MAX_QR_BYTES + 1)

    if len(data) > MAX_QR_BYTES:
        raise ValueError("QR image is too large")
    if data.startswith(b"\xff\xd8\xff"):
        extension = ".jpg"
    elif data.startswith(b"\x89PNG\r\n\x1a\n"):
        extension = ".png"
    else:
        raise ValueError("QR download is not a JPEG or PNG image")

    safe_revision = re.sub(r"[^A-Za-z0-9._-]+", "-", revision).strip("-.") or "current"
    digest = hashlib.sha256(data).hexdigest()[:12]
    cache_root = Path(
        os.environ.get(
            "WIBI_COMMUNITY_CACHE_DIR",
            Path.home() / ".codex" / "wibi-style" / "community-cache",
        )
    ).expanduser()
    cache_root.mkdir(parents=True, exist_ok=True)
    target = cache_root / f"{safe_revision}-{digest}{extension}"
    temporary = cache_root / f".{target.name}.download"
    temporary.write_bytes(data)
    os.replace(temporary, target)
    return str(target.resolve())


def load_community(timeout: float = 3.0, download_qr: bool = False) -> dict[str, object]:
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
        elif download_qr:
            try:
                result["qr_local_path"] = _download_qr(
                    str(payload["qr_image_url"]),
                    str(payload["revision"]),
                    timeout,
                )
                result["qr_status"] = "ready"
            except (OSError, ValueError, urllib.error.URLError) as error:
                result["qr_status"] = "download_failed"
                result["qr_reason"] = type(error).__name__
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

    result = load_community(timeout=args.timeout, download_qr=True)
    encoded = json.dumps(result, ensure_ascii=False, sort_keys=True)
    if args.as_json:
        print(encoded)
    else:
        print("SHOW_COMMUNITY_INFO")
        print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
