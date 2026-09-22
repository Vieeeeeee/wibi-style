#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, json, os, re, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path
SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:[-+].*)?$")
def key(value):
    match = SEMVER.fullmatch(value)
    if not match: raise ValueError(value)
    return tuple(int(part) for part in match.groups())
def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--timeout", type=float, default=3.0); parser.add_argument("--json", action="store_true", dest="as_json"); args = parser.parse_args()
    path = Path(__file__).resolve().parents[1] / "manifest.json"; local = json.loads(path.read_text(encoding="utf-8")); url = os.environ.get("WIBI_STYLE_UPDATE_MANIFEST", local["update_manifest_url"])
    parsed = urllib.parse.urlsplit(url); checked = f"{url}{'&' if parsed.query else '?'}checked_at={int(time.time())}" if parsed.scheme in {"http", "https"} else url
    try:
        request = urllib.request.Request(checked, headers={"User-Agent":"wibi-style-update-check/1","Cache-Control":"no-cache"})
        with urllib.request.urlopen(request, timeout=args.timeout) as response: payload = json.loads(response.read().decode("utf-8"))
        remote = json.loads(base64.b64decode(payload["content"]).decode("utf-8")) if parsed.netloc == "api.github.com" and payload.get("encoding") == "base64" else payload
        if remote.get("slug") != local.get("slug"): raise ValueError("slug")
        status = "UPDATE_AVAILABLE" if key(remote["version"]) > key(local["version"]) else "UP_TO_DATE"
        result = {"status":status,"slug":local["slug"],"current":local["version"],"latest":remote["version"],"install_url":remote.get("install_url",local["install_url"])}
    except (OSError, ValueError, KeyError, json.JSONDecodeError, urllib.error.URLError) as error:
        result = {"status":"CHECK_UNAVAILABLE","slug":local.get("slug","unknown"),"reason":type(error).__name__}
    print(json.dumps(result, ensure_ascii=False) if args.as_json else (f"UPDATE_AVAILABLE current={result['current']} latest={result['latest']} install_url={result['install_url']}" if result["status"] == "UPDATE_AVAILABLE" else (f"UP_TO_DATE version={result['current']}" if result["status"] == "UP_TO_DATE" else f"CHECK_UNAVAILABLE reason={result['reason']}")))
    return 0
if __name__ == "__main__": raise SystemExit(main())
