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
    "SOURCES.md",
    "manifest.json",
    "scripts/show_skill_info.py",
    "scripts/community_info.py",
    "references/community.md",
)


class SkillsIntegrityTest(unittest.TestCase):
    @property
    def skill_dirs(self) -> list[Path]:
        dirs = [p for p in sorted(SKILLS_DIR.iterdir()) if p.is_dir() and not p.name.startswith(".")]
        self.assertGreater(len(dirs), 0, "Skills collection must not be empty")
        return dirs

    def test_all_skills_have_required_structure(self) -> None:
        for skill_dir in self.skill_dirs:
            slug = skill_dir.name
            for filename in REQUIRED_FILES:
                target = skill_dir / filename
                self.assertTrue(target.is_file(), f"{slug} is missing required file: {filename}")

            manifest_path = skill_dir / "manifest.json"
            self.assertTrue(manifest_path.is_file(), f"{slug} is missing manifest.json")
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest.get("slug"), slug, f"Manifest slug mismatch in {slug}")
            self.assertTrue(manifest.get("version"), f"Missing version in {slug}")
            self.assertTrue(manifest.get("name"), f"Missing name in {slug}")
            self.assertTrue(manifest.get("author"), f"Missing author in {slug}")
            self.assertTrue(manifest.get("welcome"), f"Missing welcome in {slug}")
            self.assertIsInstance(manifest.get("license"), str, f"Manifest license must be string in {slug}")
            self.assertTrue(manifest.get("license"), f"Missing license in {slug}")

    def test_readme_catalogs_match_discovered_skills(self) -> None:
        readme_en = (ROOT / "README.md").read_text(encoding="utf-8")
        readme_zh = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        legacy_en = (ROOT / "README.en.md").read_text(encoding="utf-8")

        for skill_dir in self.skill_dirs:
            slug = skill_dir.name
            anchor = f"skills/{slug}/"
            self.assertIn(anchor, readme_en, f"{slug} missing from README.md catalog")
            self.assertIn(anchor, readme_zh, f"{slug} missing from README.zh-CN.md catalog")
            self.assertIn(anchor, legacy_en, f"{slug} missing from README.en.md catalog")

    def test_license_consistency_and_package_self_containment(self) -> None:
        for skill_dir in self.skill_dirs:
            slug = skill_dir.name
            license_text = (skill_dir / "LICENSE").read_text(encoding="utf-8")

            # Must contain attribution and source
            self.assertIn("@威比 Hunter Wei.", license_text, f"{slug} LICENSE missing author")
            self.assertIn("抖音、小红书同名", license_text, f"{slug} LICENSE missing platform note")
            self.assertIn(f"skills/{slug}", license_text, f"{slug} LICENSE missing official source URL")

            # Must contain full text of MIT for tooling
            self.assertIn("Permission is hereby granted, free of charge", license_text, f"{slug} LICENSE missing MIT grant")
            self.assertIn("without restriction", license_text, f"{slug} LICENSE missing MIT terms")
            self.assertIn("MIT License", license_text, f"{slug} LICENSE missing MIT label")

            # Must contain full text of Personal Non-Commercial for design/prompts
            self.assertIn("personal, non-commercial", license_text, f"{slug} LICENSE missing non-commercial grant")
            self.assertIn("Commercial use", license_text, f"{slug} LICENSE missing commercial reservation")

            # Check SOURCES.md: scripts must be marked MIT, not non-commercial
            sources_text = (skill_dir / "SOURCES.md").read_text(encoding="utf-8")
            self.assertIn("MIT License", sources_text, f"{slug} SOURCES.md missing MIT declaration for scripts")

            # Check manifest license
            manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertIn("MIT", manifest["license"], f"{slug} manifest license missing MIT reference")
            self.assertIn("NonCommercial", manifest["license"], f"{slug} manifest license missing NonCommercial reference")

    def test_bundled_references_exist_on_disk(self) -> None:
        for skill_dir in self.skill_dirs:
            slug = skill_dir.name
            manifest = json.loads((skill_dir / "manifest.json").read_text(encoding="utf-8"))
            for ref in manifest.get("references", []):
                ref_file = ref.get("file")
                if ref_file:
                    target = skill_dir / ref_file
                    self.assertTrue(target.is_file(), f"{slug} referenced file does not exist: {ref_file}")


if __name__ == "__main__":
    unittest.main()
