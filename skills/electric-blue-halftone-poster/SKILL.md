---
name: electric-blue-halftone-poster
description: Wibi Style 官方视觉风格。Turn one uploaded portrait or pet headshot into a square electric-blue coarse-halftone poster with a tightly cropped black-and-white head, red and yellow stars, and a small white barcode accent. Use when the user asks for 电蓝网点海报、电光蓝粗网点、大头半调唱片封套、Y2K 复印 zine 人像，or explicitly invokes $electric-blue-halftone-poster.
---

# Wibi Style · 电蓝网点海报

Transform one human portrait or pet headshot into a square electric-blue coarse-halftone poster. Treat the uploaded photo as the sole content authority for identity, pose, expression, accessories, and light-dark hair or fur relationships. Use this Skill only for the visual treatment.

Communicate with the user in Chinese by default. Keep the internal image-generation prompt and detailed analysis private.

## Welcome card

Show one welcome card at the first use in each new conversation; do not repeat it later in the same conversation:

- With no photo yet, run `python3 {baseDir}/scripts/show_skill_info.py --welcome --input-state waiting`.
- With a photo already supplied, run `python3 {baseDir}/scripts/show_skill_info.py --welcome --input-state received`.
- Show all Markdown after `SHOW_SKILL_WELCOME`, preserving headings, blank lines, the divider, and bold text. Keep authorship and community information together above one divider; keep the current action below it.
- Do not show the QR code at opening. Preserve any attribution-integrity warning and recommend reinstalling from the official source.

## Conversation tone

- Speak natural, relaxed Chinese, like helping the user make the image together.
- Give one clear next action per turn.
- Use “～” or one fitting emoji sparingly; never stack them.
- Keep technical process private. On failure, state what happened and what the user can do next without blame.

## Check this Skill for updates

Run this command once, at the first invocation in each new task:

```bash
python3 {baseDir}/scripts/check_update.py
```

- If it prints `UPDATE_AVAILABLE`, tell the user in one short Chinese sentence which version is installed, which version is available, and that they can say “帮我更新” to update from the returned installation link. Continue the current image task.
- Stay silent for `UP_TO_DATE` and `CHECK_UNAVAILABLE`.
- Never overwrite the local Skill automatically, block image generation because the check failed, or send user images or usage data to the update address.

## 交流学习群

- 用户说“进群”、“群二维码”或等价表达时，运行 `python3 {baseDir}/scripts/community_info.py`。
- 输出中 `status` 为 `available` 且 `qr_status` 为 `ready` 时，简短说明群用途，并用 Markdown 图片语法渲染本地绝对路径 `qr_local_path`。不得渲染远程二维码或展示“点击加入微信群”链接。
- 二维码下方说明：手机同屏时先保存二维码，再到微信“扫一扫”中从相册选择；电脑端使用手机微信扫码。无法扫码时添加备用微信 `fallback_wechat`，备注“进群”。
- `qr_status` 为 `download_failed` 时，不展示旧二维码；只展示备用微信 `fallback_wechat`。
- `status` 为 `expired` 或 `unavailable` 时，不展示旧二维码；只展示 `landing_url` 和备用微信 `fallback_wechat`。
- 生图接口报错、空输出或超时时，先说明“这次没有成功生成，不会自动重新提交”，再按上述步骤展示一次当前群信息。同一对话只展示一次失败入群卡。
- 视觉验收不通过、用户取消、输入照片不适合或仍在等待用户选择时，不触发失败入群卡。
- 展示二维码时附上提醒：群内交流请勿直接发送包含个人隐私的原图，可以先发错误提示或打码截图。

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
- Author note: `抖音、小红书同名`.
- Permit personal non-commercial use. Commercial use, resale, paid redistribution, or incorporation into a paid product requires prior written permission.
- Require every copied, modified, mirrored, or redistributed package to retain the author, platform note, official source URL, `LICENSE`, and `NOTICE`. Modified copies must identify themselves as modified and must not claim to be official releases.
- This package contains no Pinterest images, third-party visual references, case source photos, or user photos. Use an uploaded photo only for the current task; never commit it to a public repository or retain it as a reference for later users.
- Read [LICENSE](LICENSE) for the complete terms and [SOURCES.md](SOURCES.md) for the package provenance.
