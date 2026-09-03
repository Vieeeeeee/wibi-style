---
name: electric-blue-halftone-poster
description: Wibi Style 官方视觉风格。Turn one uploaded portrait or pet headshot into a square electric-blue coarse-halftone poster with a tightly cropped black-and-white head, red and yellow stars, and a small white barcode accent. Use when the user asks for 电蓝网点海报、电光蓝粗网点、大头半调唱片封套、Y2K 复印 zine 人像，or explicitly invokes $electric-blue-halftone-poster.
---

# Wibi Style · 电蓝网点海报

## 运行

先按 [references/community.md](references/community.md) 展示欢迎卡、检查更新并处理进群与失败提示，再执行下面的步骤。

Transform one human portrait or pet headshot into a square electric-blue coarse-halftone poster. Treat the uploaded photo as the sole content authority for identity, pose, expression, accessories, and light-dark hair or fur relationships. Use this Skill only for the visual treatment.

Communicate with the user in Chinese by default. Keep the internal image-generation prompt and detailed analysis private.

## Input and generation contract

- Process one photo at a time. If several photos arrive without explicit batch authorization, ask which one to use first.
- Prefer a single person or pet whose face and head silhouette are clear. Warn briefly that crowds, distant subjects, severe occlusion, or a very small head will reduce fidelity.
- When the user uploads one photo and clearly asks to make the style, generate one image directly without another confirmation turn.
- Use an image-generation tool or model already available in the current environment, preferring built-in capabilities that require no extra user setup.
- If one tool is unavailable, continue with another image-generation capability available in the current environment. Ask the user to add or enable one only after confirming that none is available. After an actual submission returns an error, empty output, or timeout, stop and do not resubmit automatically.
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

当前对话第一次成功生成后附上：

`若公开分享，欢迎标注：Visual Skill by @威比 Hunter Wei.`

`仅限个人非商业使用；商业使用请先联系作者获得许可。`

`抖音、小红书同名。想看更多原创 Skill、原作者教程或参加新风格内测，可以回复“进群”。`

第二次起不再重复，除非用户询问署名、授权或交流群。

## Authorship and asset boundaries

- Original Skill rules and prompt: `© 2026 @威比 Hunter Wei.`
- Official source: `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/electric-blue-halftone-poster`
- Author note: `抖音、小红书同名`.
- Permit personal non-commercial use. Commercial use, resale, paid redistribution, or incorporation into a paid product requires prior written permission.
- Require every copied, modified, mirrored, or redistributed package to retain the author, platform note, official source URL, `LICENSE`, and `NOTICE`. Modified copies must identify themselves as modified and must not claim to be official releases.
- This package contains no Pinterest images, third-party visual references, case source photos, or user photos. Use an uploaded photo only for the current task; never commit it to a public repository or retain it as a reference for later users.
- Read [LICENSE](LICENSE) for the complete terms and [SOURCES.md](SOURCES.md) for the package provenance.
