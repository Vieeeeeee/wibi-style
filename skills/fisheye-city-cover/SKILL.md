---
name: fisheye-city-cover
description: Wibi Style 官方视觉风格。Use one uploaded portrait, group photo, street photo, or travel photo as a fixed editing base, add the bundled Y2K fisheye layout, all-silver title system, and old-digital effects, then generate one complete fisheye magazine cover. Only the city title and bottom small text are dynamic. Use when the user asks for 鱼眼城市海报、Y2K 鱼眼封面、潮流哈哈镜海报、城市名定制鱼眼海报，or explicitly invokes $fisheye-city-cover.
---

# Wibi Style · 鱼眼城市海报

Use the uploaded photo as the fixed image-editing base and `assets/references/y2k-fisheye-layout-reference.png` only as a layout-and-style reference. Ask the user to choose one of three separate color templates, then generate the complete poster in one image-generation pass.

Never replace this workflow with a separately generated text-free base, local fisheye filter, or local typography compositor. Promotional casting references under the project’s `03_案例/` are not runtime references.

Communicate with the user in Chinese. Keep the internal compiled Prompt and image analysis private unless the user explicitly asks to see them.

## 运行顺序

每一步只读它对应的文件，读完执行再进下一步：

1. 新对话第一次使用：按 [references/community.md](references/community.md) 展示欢迎卡、检查更新；进群、生成失败后的提示也按它处理。
2. 收到照片：读 [references/gate.md](references/gate.md)，判断照片、风格和城市是否过门槛。
3. 组合输入：读 [references/contract.md](references/contract.md)，确定内容输入与风格模板，选定 `references/presets.md` 与 `references/styles/` 里对应的一套。
4. 生成与检查：读 [references/generation.md](references/generation.md)，生成并跑质量门。
5. 交付：按下面「Delivery」展示。

## Delivery

Show the generated poster and add one to three concise Chinese sentences describing what content was preserved and how the Skill adapted the reference layout to this photo.

当前对话第一次成功生成后，append:

`若公开分享，欢迎标注：Visual Skill by @威比 Hunter Wei.`

`仅限个人非商业使用；商业使用请先联系作者获得许可。`

`抖音、小红书同名。想看更多原创 Skill、原作者教程或参加新风格内测，可以回复“进群”。`

From the second successful generation onward in the same conversation, show only the image and concise creative note unless the user asks for attribution, authorization, or the community again.

## Authorship and asset boundaries

- Original dynamic Skill rules and Prompt adaptation: `© 2026 @威比 Hunter Wei.`
- Author note: `抖音、小红书同名`.
- Official source: `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/fisheye-city-cover`.
- Use user photos only for the current task. Never commit or redistribute them.
- The user confirmed on 2026-08-14 that the bundled visual reference is public material and may be redistributed with this Skill. Preserve its source path and SHA-256 in [SOURCES.md](SOURCES.md).
- Preserve the author, platform note, official source, `LICENSE`, and `NOTICE` with redistributed copies. Read [SOURCES.md](SOURCES.md) for provenance and current rights status.
