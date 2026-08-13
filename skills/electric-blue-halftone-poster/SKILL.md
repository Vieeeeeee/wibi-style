---
name: electric-blue-halftone-poster
description: Wibi Style 官方视觉风格。Turn one uploaded portrait or pet headshot into a square electric-blue coarse-halftone poster with a tightly cropped black-and-white head, red and yellow stars, and a small white barcode accent. Use when the user asks for 电蓝网点海报、电光蓝粗网点、大头半调唱片封套、Y2K 复印 zine 人像，or explicitly invokes $electric-blue-halftone-poster.
---

# Wibi Style · 电蓝网点海报

Transform one human portrait or pet headshot into a square electric-blue coarse-halftone poster. Treat the uploaded photo as the sole content authority for identity, pose, expression, accessories, and light-dark hair or fur relationships. Use this Skill only for the visual treatment.

Communicate with the user in Chinese by default. Keep the internal image-generation prompt and detailed analysis private.

## Show author card after installation

Run this command before the update check at the first invocation in each new task:

```bash
python3 {baseDir}/scripts/show_skill_info.py
```

- If it prints `SHOW_SKILL_INFO`, show its name, version, author, same-name platforms, official source, installation path, and attribution-integrity result to the user as a compact Chinese “Skill 信息” card. Then continue the image task.
- Stay silent for `AUTHOR_CARD_ALREADY_SHOWN`.
- If attribution integrity is incomplete, preserve the warning and recommend reinstalling from the official source. Do not repair or overwrite files automatically.
- The original author line is `@威比 Hunter Wei.（抖音、小红书同名）`. The official source is `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/electric-blue-halftone-poster`. Keep both, `LICENSE`, and `NOTICE` with every copied, modified, mirrored, or redistributed package.

## Check this Skill for updates

Run this command once, at the first invocation in each new task:

```bash
python3 {baseDir}/scripts/check_update.py
```

- If it prints `UPDATE_AVAILABLE`, tell the user in one short Chinese sentence which version is installed, which version is available, and that they can say “帮我更新” to update from the returned installation link. Continue the current image task.
- Stay silent for `UP_TO_DATE` and `CHECK_UNAVAILABLE`.
- Never overwrite the local Skill automatically, block image generation because the check failed, or send user images or usage data to the update address.

## Input and generation contract

- Process one photo at a time. If several photos arrive without explicit batch authorization, ask which one to use first.
- Prefer a single person or pet whose face and head silhouette are clear. Warn briefly that crowds, distant subjects, severe occlusion, or a very small head will reduce fidelity.
- When the user uploads one photo and clearly asks to make the style, generate one image directly without another confirmation turn.
- Use the Codex built-in image-generation tool by default. Use Lovart only when the user explicitly requests it.
- Stop after a tool error, empty output, or timeout. Do not retry, switch models, or increase quality automatically.
- When the user gives feedback without requesting another generation, record the requested change and wait for an explicit “再做一张”, “重做”, or equivalent instruction.

## Workflow

1. Inspect the complete photo. Lock the subject identity, face or species structure, expression, head angle, hair or fur shape and light-dark relationship, and important glasses, hat, earrings, collar, or other accessories.
2. Read [references/style-prompt.md](references/style-prompt.md) for the complete visual specification.
3. Compile a photo-specific editing prompt. Preserve the photo's content relationships while applying the crop, black-white tonal structure, coarse halftone, electric-blue field, stars, and barcode treatment.
4. Pass only the user's photo as content input and request one square PNG. This package has no bundled visual reference and must not add network images.
5. Apply the quality gate below. If a core requirement fails, state the problem and stop. Regenerate only after the user authorizes another generation.

Do not expose the complete internal generation prompt or itemized visual analysis.

## Quality gate

Check every item before delivery:

1. **Identity:** The result still corresponds to the source. Preserve face shape or species traits, expression, head angle, accessories, and light-dark hair or fur relationships.
2. **Crop:** The head dominates the square. The top and side hair may touch or slightly cross the canvas, while the complete chin or lower muzzle remains visible. Shoulders and clothing must not compete with the head.
3. **Three-tone structure:** The face or head contains distinct pure-white highlights, countable coarse-dot midtones, and hard-edged solid-black shadows.
4. **Dot scale:** Large separated dots remain legible at phone-thumbnail size. Reject fine newspaper screening, uniform gray haze, or a full-image grain filter.
5. **Value fidelity:** Dark hair or fur remains dark; blond, bleached, white, or otherwise light areas stay light. Do not color the person or pet blue.
6. **Background:** Use one uniform saturated electric blue with crisp subject edges and no blue outline, halo, gradient, texture, or vignette.
7. **Graphic layer:** Place six red-and-yellow stars only in available blue space without obscuring critical facial features. Keep a small white decorative barcode and neutral text of no more than ten uppercase characters along the right side.
8. **File:** Deliver one square PNG with no frame, signature, platform mark, or recognizable brand.

## Delivery

Show the final image and add one or two concise Chinese sentences explaining which source traits were preserved and how the coarse halftone and electric-blue field organize the composition.

After the first two successful generations in the current conversation, append:

`若公开分享，欢迎标注：Visual Skill by @威比 Hunter Wei.`

`仅限个人非商业使用；商业使用请先联系作者获得许可。`

## Authorship and asset boundaries

- Original Skill rules and prompt: `© 2026 @威比 Hunter Wei.`
- Author note: `抖音、小红书同名`.
- Permit personal non-commercial use. Commercial use, resale, paid redistribution, or incorporation into a paid product requires prior written permission.
- Require every copied, modified, mirrored, or redistributed package to retain the author, platform note, official source URL, `LICENSE`, and `NOTICE`. Modified copies must identify themselves as modified and must not claim to be official releases.
- This package contains no Pinterest images, third-party visual references, case source photos, or user photos. Use an uploaded photo only for the current task; never commit it to a public repository or retain it as a reference for later users.
- Read [LICENSE](LICENSE) for the complete terms and [SOURCES.md](SOURCES.md) for the package provenance.
