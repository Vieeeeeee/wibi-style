# Contributing to Wibi Style

Thank you for your interest in contributing to Wibi Style! We welcome style contributions, bug reports, and tooling improvements.

## 1. Submitting Issues

- **Bug Reports**: If a Skill fails to install, reports missing files, or crashes during runtime checks, please open an issue on GitHub. Include the Skill name, error output, and Python environment details.
- **Style Feedback**: You are welcome to suggest new visual aesthetics or improvements to existing styling rules.

## 2. Adding or Updating a Visual Skill

Each Skill in `skills/<slug>/` is self-contained and must follow the repository's component-specific architecture:

1. **Required Files**:
   - `SKILL.md`: Complete agent runtime instructions.
   - `manifest.json`: Metadata schema (name, slug, version, author, license, welcome copy).
   - `LICENSE`: Self-contained component-specific license (MIT for code, Non-Commercial for prompts/design).
   - `NOTICE`: Author attribution and source notice.
   - `SOURCES.md`: Full provenance and licensing breakdown for all packaged files.
   - `README.md`: Per-skill documentation and installation snippet.
   - `references/community.md`: Welcome card and community handling rules.
   - `scripts/`: Runtime automation scripts (`check_update.py`, `show_skill_info.py`, `community_info.py`, and optional layout scripts).

2. **Asset Provenance & Copyright Rules**:
   - Any bundled reference images (`assets/references/`) or fonts (`assets/fonts/`) must include explicit provenance, SHA-256 digests, and authorization basis documented in `SOURCES.md`.
   - Never bundle third-party photographs without confirmed redistribution rights.
   - User photos are strictly ephemeral: never commit personal user photos or unverified source images.

3. **Versioning & Manifest**:
   - Follow Semantic Versioning (`1.0.0`, `1.0.1`, etc.).
   - Set `"license": "MIT AND LicenseRef-Wibi-Personal-NonCommercial-1.0"`.

## 3. Running Automated Tests

Before submitting a Pull Request, run the local test suite across all skills:

```bash
python3 -m unittest discover tests -v
```

The test suite validates:
- Structural integrity of every Skill package.
- Consistency between directory names, manifest slugs, and documentation catalogs.
- License consistency (MIT for scripts, Non-Commercial for prompts).
- Safe fallback behavior for community configuration.

All tests must pass cleanly.
