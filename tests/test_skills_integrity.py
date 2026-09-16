from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "NOTICE",
    "manifest.json",
    "scripts/show_skill_info.py",
    "scripts/community_info.py",
    "references/community.md",
)


class SkillsIntegrityTest(unittest.TestCase):
    def test_all_skills_have_required_structure(self) -> None:
        skill_dirs = [p for p in sorted(SKILLS_DIR.iterdir()) if p.is_dir()]
        self.assertEqual(len(skill_dirs), 31, "Repository should maintain exactly 31 skills")

        for skill_dir in skill_dirs:
            slug = skill_dir.name
            for filename in REQUIRED_FILES:
                target = skill_dir / filename
                self.assertTrue(target.is_file(), f"{slug} is missing required file: {filename}")

            manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest.get("slug"), slug, f"Manifest slug mismatch in {slug}")
            self.assertTrue(manifest.get("version"), f"Missing version in {slug}")
            self.assertTrue(manifest.get("name"), f"Missing name in {slug}")
            self.assertTrue(manifest.get("author"), f"Missing author in {slug}")
            self.assertTrue(manifest.get("welcome"), f"Missing welcome in {slug}")
            self.assertTrue(manifest.get("license"), f"Missing license in {slug}")


if __name__ == "__main__":
    unittest.main()
