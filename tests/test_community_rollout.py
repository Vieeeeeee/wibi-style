from __future__ import annotations

from datetime import datetime, timezone, timedelta
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "community.json"

def get_installed_targets() -> dict[str, str]:
    targets: dict[str, str] = {}
    skills_dir = ROOT / "skills"
    for path in sorted(skills_dir.iterdir()):
        manifest_path = path / "manifest.json"
        if path.is_dir() and manifest_path.is_file():
            data = json.loads(manifest_path.read_text(encoding="utf-8"))
            targets[path.name] = data["version"]
    return targets


TARGETS = get_installed_targets()


def run_script(path: Path, *args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    merged = os.environ.copy()
    if env:
        merged.update(env)
    return subprocess.run(
        [sys.executable, str(path), *args],
        cwd=ROOT,
        env=merged,
        check=True,
        capture_output=True,
        text=True,
    )


class CommunityRolloutTest(unittest.TestCase):
    def setUp(self) -> None:
        self.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    def test_root_config_matches_readme_and_current_qr(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        self.assertIn(self.config["fallback_wechat"], readme)
        self.assertIn(self.config["fallback_wechat"], readme_zh)
        self.assertIn("README.zh-CN.md", readme)
        self.assertIn("README.md", readme_zh)
        self.assertTrue((ROOT / "assets/wechat-aigc-group-qr.jpg").is_file())
        expires_at = datetime.fromisoformat(self.config["valid_until"])
        self.assertIsNotNone(expires_at.tzinfo)

    def test_all_skills_share_the_local_qr_community_reader(self) -> None:
        digests = set()
        for slug in TARGETS:
            path = ROOT / "skills" / slug / "scripts" / "community_info.py"
            self.assertTrue(path.is_file())
            digests.add(hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertTrue(len(digests) <= 2)

    def test_available_community_output_and_opening_card(self) -> None:
        with tempfile.TemporaryDirectory() as home:
            env = {
                "HOME": home,
                "WIBI_COMMUNITY_CONFIG_URL": CONFIG_PATH.as_uri(),
            }
            for slug, version in TARGETS.items():
                scripts = ROOT / "skills" / slug / "scripts"
                author_card = run_script(scripts / "show_skill_info.py", "--always", env=env)
                self.assertIn("SHOW_SKILL_INFO", author_card.stdout)
                self.assertIn(f"版本：{version}", author_card.stdout)
                self.assertIn(f"**{self.config['name']}**", author_card.stdout)
                self.assertIn("回复“进群”", author_card.stdout)

    def test_all_welcome_cards_have_two_sections_and_contextual_actions(self) -> None:
        with tempfile.TemporaryDirectory() as home:
            env = {
                "HOME": home,
                "WIBI_COMMUNITY_CONFIG_URL": CONFIG_PATH.as_uri(),
            }
            for slug in TARGETS:
                skill_dir = ROOT / "skills" / slug
                manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
                script = skill_dir / "scripts" / "show_skill_info.py"
                waiting = run_script(script, "--welcome", "--input-state", "waiting", env=env).stdout
                received = run_script(script, "--welcome", "--input-state", "received", env=env).stdout
                for state, output in (("waiting", waiting), ("received", received)):
                    self.assertIn("SHOW_SKILL_WELCOME", output)
                    self.assertIn(f"### {manifest['name']}", output)
                    self.assertIn("**Visual Skill by @威比 Hunter Wei.**", output)
                    self.assertEqual(output.count("\n---\n"), 1)
                    brand, action = output.split("\n---\n")
                    self.assertIn("**「进群」**", brand)
                    self.assertNotIn("进群", action)
                    self.assertIn("#### 现在开始", action)
                    for line in manifest["welcome"][state]:
                        self.assertIn(line, action)
                    self.assertNotIn("安装路径：", output)

    def test_current_qr_is_downloaded_and_only_local_path_is_returned(self) -> None:
        script = ROOT / "skills" / "alt-manga-avatar" / "scripts" / "community_info.py"
        spec = importlib.util.spec_from_file_location("alt_manga_community_info", script)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        class Response:
            def __init__(self, body: bytes, url: str, content_type: str) -> None:
                self.body = body
                self.url = url
                self.headers = {
                    "Content-Length": str(len(body)),
                    "Content-Type": content_type,
                }

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def read(self, limit: int = -1) -> bytes:
                return self.body if limit < 0 else self.body[:limit]

            def geturl(self) -> str:
                return self.url

        active_config = dict(self.config)
        active_config["valid_until"] = (datetime.now(timezone.utc) + timedelta(days=30)).isoformat()
        config_body = json.dumps(active_config, ensure_ascii=False).encode("utf-8")
        qr_body = b"\xff\xd8\xff" + b"current-github-qr"
        qr_url = self.config["qr_image_url"]
        responses = [
            Response(config_body, module.DEFAULT_CONFIG_URL, "application/json"),
            Response(qr_body, qr_url, "image/jpeg"),
        ]
        with tempfile.TemporaryDirectory() as cache:
            with mock.patch.dict(os.environ, {"WIBI_COMMUNITY_CACHE_DIR": cache}):
                with mock.patch.object(module.urllib.request, "urlopen", side_effect=responses):
                    payload = module.load_community(download_qr=True)
            local_qr = Path(payload["qr_local_path"])
            self.assertTrue(local_qr.is_file())
            self.assertEqual(local_qr.read_bytes(), qr_body)

        self.assertEqual(payload["status"], "available")
        self.assertEqual(payload["qr_status"], "ready")
        self.assertNotIn("qr_image_url", payload)
        self.assertNotIn("join_url", payload)

    def test_expired_config_never_returns_stale_qr(self) -> None:
        expired = dict(self.config)
        expired["valid_until"] = "2000-01-01T00:00:00+08:00"
        with tempfile.TemporaryDirectory() as directory:
            fixture = Path(directory) / "expired.json"
            fixture.write_text(json.dumps(expired, ensure_ascii=False), encoding="utf-8")
            env = {"WIBI_COMMUNITY_CONFIG_URL": fixture.as_uri()}
            script = ROOT / "skills" / "wibi-frame" / "scripts" / "community_info.py"
            payload = json.loads(run_script(script, "--json", env=env).stdout)
        self.assertEqual(payload["status"], "expired")
        self.assertNotIn("qr_image_url", payload)
        self.assertNotIn("join_url", payload)
        self.assertEqual(payload["fallback_wechat"], "Wibi2077")

    def test_unavailable_config_has_safe_fallback(self) -> None:
        env = {"WIBI_COMMUNITY_CONFIG_URL": "file:///definitely-missing-wibi-community.json"}
        script = ROOT / "skills" / "diamond-kid-head-card" / "scripts" / "community_info.py"
        payload = json.loads(run_script(script, "--json", env=env).stdout)
        self.assertEqual(payload["status"], "unavailable")
        self.assertNotIn("qr_image_url", payload)
        self.assertEqual(payload["fallback_wechat"], "Wibi2077")

    def test_manifests_and_skill_policies_cover_all_public_skills(self) -> None:
        for slug, version in TARGETS.items():
            skill_dir = ROOT / "skills" / slug
            manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["version"], version)
            self.assertEqual(manifest["community"]["config_url"], self.config_url)
            self.assertIn(manifest["community"]["opening"], ("welcome-once-per-conversation", "summary-once"))
            self.assertEqual(
                manifest["community"]["qr_display"],
                "download-current-github-image-and-render-locally",
            )
            self.assertTrue(len(manifest["welcome"]["waiting"]) >= 1)
            self.assertTrue(len(manifest["welcome"]["received"]) >= 1)
            skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            community_ref = skill_dir / "references" / "community.md"
            combined_text = skill_text + ("\n" + community_ref.read_text(encoding="utf-8") if community_ref.is_file() else "")
            self.assertIn("## 交流学习群", combined_text)
            self.assertIn("同一对话只展示一次失败入群卡", combined_text)
            self.assertIn("当前对话第一次成功", combined_text)
            self.assertIn("--input-state waiting", combined_text)
            self.assertIn("--input-state received", combined_text)
            self.assertIn("qr_local_path", combined_text)
            self.assertNotIn("qr_image_url", combined_text)
            self.assertTrue("## 对话语气" in combined_text or "## Conversation tone" in combined_text)

    @property
    def config_url(self) -> str:
        return "https://raw.githubusercontent.com/Vieeeeeee/wibi-style/main/community.json"


if __name__ == "__main__":
    unittest.main()
