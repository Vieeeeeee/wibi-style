from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "community.json"
TARGETS = {
    "diamond-kid-head-card": "1.0.3",
    "wibi-frame": "1.3.5",
}


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
        self.assertIn(self.config["join_url"], readme)
        self.assertIn("assets/wechat-aigc-group-qr.jpg", readme)
        self.assertIn(self.config["fallback_wechat"], readme)
        self.assertTrue((ROOT / "assets/wechat-aigc-group-qr.jpg").is_file())
        expires_at = datetime.fromisoformat(self.config["valid_until"])
        self.assertIsNotNone(expires_at.tzinfo)
        self.assertGreater(expires_at.astimezone(timezone.utc), datetime.now(timezone.utc))

    def test_two_skills_share_the_same_community_reader(self) -> None:
        digests = set()
        for slug in TARGETS:
            path = ROOT / "skills" / slug / "scripts" / "community_info.py"
            self.assertTrue(path.is_file())
            digests.add(hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertEqual(len(digests), 1)

    def test_available_community_output_and_opening_card(self) -> None:
        with tempfile.TemporaryDirectory() as home:
            env = {
                "HOME": home,
                "WIBI_COMMUNITY_CONFIG_URL": CONFIG_PATH.as_uri(),
            }
            for slug, version in TARGETS.items():
                scripts = ROOT / "skills" / slug / "scripts"
                community = run_script(scripts / "community_info.py", "--json", env=env)
                payload = json.loads(community.stdout)
                self.assertEqual(payload["status"], "available")
                self.assertEqual(payload["qr_image_url"], self.config["qr_image_url"])

                author_card = run_script(scripts / "show_skill_info.py", "--always", env=env)
                self.assertIn("SHOW_SKILL_INFO", author_card.stdout)
                self.assertIn(f"版本：{version}", author_card.stdout)
                self.assertIn(self.config["name"], author_card.stdout)
                self.assertIn("回复“进群”", author_card.stdout)

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

    def test_manifests_and_skill_policies_are_scoped_to_two_targets(self) -> None:
        for slug, version in TARGETS.items():
            skill_dir = ROOT / "skills" / slug
            manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["version"], version)
            self.assertEqual(manifest["community"]["config_url"], self.config_url)
            skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("## 交流学习群", skill_text)
            self.assertIn("同一对话只展示一次失败入群卡", skill_text)
            self.assertIn("当前对话第一次成功", skill_text)

    @property
    def config_url(self) -> str:
        return "https://raw.githubusercontent.com/Vieeeeeee/wibi-style/main/community.json"


if __name__ == "__main__":
    unittest.main()
