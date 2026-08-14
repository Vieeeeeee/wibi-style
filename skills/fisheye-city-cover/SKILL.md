---
name: fisheye-city-cover
description: Wibi Style 官方视觉风格。Use one uploaded portrait, group photo, street photo, or travel photo as a fixed editing base, add the bundled Y2K fisheye layout, all-silver title system, and old-digital effects, then generate one complete fisheye magazine cover. Only the city title and bottom small text are dynamic. Use when the user asks for 鱼眼城市海报、Y2K 鱼眼封面、潮流哈哈镜海报、城市名定制鱼眼海报，or explicitly invokes $fisheye-city-cover.
---

# Wibi Style · 鱼眼城市海报

Use the uploaded photo as the fixed image-editing base and `assets/references/y2k-fisheye-layout-reference.png` only as a layout-and-style reference. Ask the user to choose one of three separate color templates, then generate the complete poster in one image-generation pass.

Never replace this workflow with a separately generated text-free base, local fisheye filter, or local typography compositor. Promotional casting references under the project’s `03_案例/` are not runtime references.

Communicate with the user in Chinese. Keep the internal compiled Prompt and image analysis private unless the user explicitly asks to see them.

## Show author card after installation

Run this command before the update check at the first invocation in each new task:

```bash
python3 {baseDir}/scripts/show_skill_info.py
```

- If it prints `SHOW_SKILL_INFO`, show its name, version, author, same-name platforms, official source, installation path, and attribution-integrity result to the user as a compact Chinese `Skill 信息` card. Then continue to the input gate below.
- Stay silent for `AUTHOR_CARD_ALREADY_SHOWN`.
- If attribution integrity is incomplete, preserve the warning and recommend reinstalling from the official source. Do not repair or overwrite files automatically.
- The original author line is `@威比 Hunter Wei.（抖音、小红书同名）`. The official source is `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/fisheye-city-cover`. Keep both, `LICENSE`, and `NOTICE` with every copied, modified, mirrored, or redistributed package.

## Check this Skill for updates

Run this command once, after the author-card check at the first invocation in each new task:

```bash
python3 {baseDir}/scripts/check_update.py
```

- If it prints `UPDATE_AVAILABLE`, tell the user in one short Chinese sentence which version is installed, which version is available, and that they can say “帮我更新” to update from the returned installation link. Continue the current task.
- Stay silent for `UP_TO_DATE` and `CHECK_UNAVAILABLE`.
- Never overwrite the local Skill automatically, block image generation because the check failed, or send user images or usage data to the update address.

## 交流学习群

- 用户说“进群”、“群二维码”或同义表达时，运行 `python3 {baseDir}/scripts/community_info.py`。
- 输出中 `status` 为 `available` 时，简短说明群用途，展示 `join_url`，并用 Markdown 图片语法渲染 `qr_image_url`。
- `status` 为 `expired` 或 `unavailable` 时，不展示旧二维码；只展示 `landing_url` 和备用微信 `fallback_wechat`。
- 生图接口报错、空输出或超时时，先说明“这次没有成功生成，不会自动重新提交”，再按上述步骤展示一次当前群信息。同一对话只展示一次失败入群卡。
- 视觉验收不通过、用户取消、照片不适合或仍在等待用户选择时，不触发失败入群卡。
- 展示二维码时提醒：群内交流请勿直接发送包含个人隐私的原图，可以先发错误提示或打码截图。

## Photo, style, and city gate

Before compiling or generating anything, establish exactly one user photo, one user-selected style, and one user-provided city or place title.

1. If there is no photo, ask naturally: `先发一张你想做成海报的照片给我吧～` Then stop.
2. If several photos arrive without explicit batch authorization, ask naturally: `这几张都很适合呀～ 这次想先从哪一张开始？` Then stop.
3. Accept these style names and obvious equivalents: `黑银`, `靛蓝`, or `复古粉`. Do not select a style from the photo, gender, clothing, or city.
4. If both style and city are missing, ask with this friendly wording:

   `我们先挑一个海报气质吧～ 黑银、靛蓝、复古粉，你更喜欢哪一种？✨`

   `这张照片是在哪里拍的呀？告诉我城市或地点就好，我会把它变成海报上的大标题～`

   Stop after these questions and do not generate yet.
5. If only the style is missing, ask naturally:

   `我们先挑一个海报气质吧～ 黑银、靛蓝、复古粉，你更喜欢哪一种？✨`

   Stop after this question and do not generate yet.
6. If only the city or place is missing, ask naturally:

   `这张照片是在哪里拍的呀？告诉我城市或地点就好，我会把它变成海报上的大标题～`

   Stop after this question. Do not infer the city from buildings, signs, metadata, or visual appearance, and do not generate yet.
7. If the same message already contains a style and a city or place, do not ask again. Accept city, province, region, or other user-chosen place labels such as `东京`, `香港`, or `云南`.
8. After the user answers, convert the supplied label to its conventional uppercase English title when unambiguous, for example `东京 → TOKYO` and `香港 → HONG KONG`. If the user already supplied English, preserve its wording and uppercase it. Never replace the user's place with a more specific or different location.
9. Do not add a second confirmation turn. Once the photo, style, and city are present and the user has asked to make the poster, create three to five concise, non-factual, `UPPERCASE ENGLISH` atmosphere phrases for `{SMALL_TEXT}` from the visible scene. Each phrase should contain two to four English words. If the user supplied Chinese small text, translate its meaning into concise English; use conventional English or romanization for proper place names. Do not invent dates, coordinates, venues, events, rankings, or brands. Then generate one image directly.

## Input contract

- Process one user photo at a time unless the user explicitly authorizes a batch.
- Always carry exactly two runtime images: the current user photo and `assets/references/y2k-fisheye-layout-reference.png`.
- Identify their roles by visual content, not attachment order. The real photo is the sole authority for people, props, actions, and the entire scene/background. The bundled poster supplies only fisheye optics, curved headline scale, dark frame, typography hierarchy, CCD/DV texture, chrome glow, and bottom information layout.
- Do not copy the reference people, group identity, clothing, furniture, speakers, rabbit mark, album name, track list, brand, logo, or exact wording.
- Never use the reference room, speakers, computers, monitors, desks, chairs, walls, or other furniture to complete or replace the user photo's background. Bend and restyle only the background actually present in the user photo, even when it is simple.
- Apply a strict prop-presence gate: an object may appear only when it is visible in the user photo. A lighter or flame must remain when present and must never be invented when absent. Do not invent a cigarette, microphone, handheld device, or foreground prop to strengthen the fisheye effect.
- Apply the same closed-set rule to pose and clothing. Never invent a visible arm, hand, V sign, pointing gesture, open palm, or other pose that is absent from the user photo. Preserve sleeve length, neckline, garment category, layers, body coverage, and visible skin exactly; short sleeves remain short and unseen hands remain unseen.
- Preserve the user photo’s people, count, identity, faces, makeup, hair, clothing, body coverage, pose, gestures, interaction, accessories, scene, and essential composition.
- The required user-facing controls are the style choice and city or place title. Optional small text is accepted when the user supplies it; otherwise the Skill generates only non-factual atmosphere phrases from the visible scene. The bottom small text must always be concise uppercase English.
- Preserve the meaning of user-supplied wording. Keep supplied English wording where possible; translate supplied Chinese into concise English and normalize it to uppercase. Never invent real coordinates, dates, venues, rankings, event claims, or brands.
- When the photo, style, and city gate is satisfied and the user has clearly asked to generate, make one image directly. Stop after an error, empty output, timeout, or failed visual gate. Never retry automatically.

## Separate style templates

Select exactly one complete template from the user's choice:

- `黑银` → [references/styles/black-silver.md](references/styles/black-silver.md)
- `靛蓝` → [references/styles/indigo.md](references/styles/indigo.md)
- `复古粉` → [references/styles/retro-pink.md](references/styles/retro-pink.md)

Never mix colors or partial instructions across templates. `references/style-prompt.md` remains a backward-compatible alias of the black-silver template.

Do not dynamically redesign or narrate the photo. Treat the uploaded image as one fixed editing base. Do not compile a case-specific description of the person, action, clothing, props, or background.

After selecting the template, fill only two fields:

1. `{CITY_TITLE}`: the uppercase English title derived from the user's supplied city or place. Never infer it from the photo.
2. `{SMALL_TEXT}`: three to five uppercase English phrases, each two to four words. Keep user-supplied English where possible; translate user-supplied Chinese faithfully into concise English. Use conventional English or romanization for proper place names. Never place Chinese, Japanese, Korean, placeholder glyphs, or meaningless pseudo-English in the bottom information area.

Everything else stays fixed: preserve the uploaded image as a whole; add the selected background color, true strong fisheye optics, all-silver poster typography, bottom graphic hierarchy, and CCD/MiniDV/CRT finish. The bottom English must use designed typography rather than plain default body text: condensed techno grotesk, extended sans, or Y2K instrument lettering, with deliberate tracking, scale and weight contrast, modular columns, rules or frames, and clean baseline alignment. The fisheye circle may bend only content already visible in the user photo; the 3:4 extension belongs to poster background and typography, not photographic outpainting.

## Generation

Use the Codex built-in image-generation tool by default. Use Lovart only when the user explicitly requests Lovart.

Pass:

- the user photo as content input/edit target;
- `assets/references/y2k-fisheye-layout-reference.png` as the style-and-layout reference;
- the selected complete style template with only `{CITY_TITLE}` and `{SMALL_TEXT}` filled.

Request one complete `3:4` poster containing true photographic fisheye space, giant curved city headline, the selected enclosing background color, bottom metadata, and all optical/editorial effects in the same generation. The result itself is the Skill output.

## Quality gate

Approve only when all are true:

1. **Content fidelity:** Same subject count, recognizable identity, makeup, hair, clothing, pose, interaction, accessories, and scene as the user photo.
2. **Reference fidelity:** Clearly belongs to the original Y2K fisheye-poster family: giant circular lens space, huge curved compressed headline, selected wrapped background color, dense bottom editorial information, CCD/DV glow and low-fi future texture.
3. **Content separation:** No reference person, clothing, furniture, speaker, rabbit mark, brand, album identity, track name, or copied wording appears.
4. **Scene and prop fidelity:** The entire background comes from the user photo. No reference room, speaker, computer, monitor, desk, chair, or other scenery appears. Every foreground prop exists in the user photo; a lighter or flame is kept only when originally present.
5. **Pose and clothing fidelity:** No new arm, hand, V sign, pointing gesture, or pose appears. Sleeve length, neckline, garment structure, layers, body coverage, and visible skin match the user photo.
6. **True fisheye:** The circle is not merely a crop or mask. Faces remain readable while the nearest existing feature is visibly enlarged, peripheral straight lines curve, background space compresses toward the circle, and edges stretch naturally. Groups preserve every member and their relationship.
7. **Typography:** The main title is correct and immediately readable. All readable text follows the selected silver family. Bottom text contains only 3–5 clear uppercase English phrases and uses visibly designed narrow-techno, extended-sans, or Y2K-instrument typography with deliberate tracking, hierarchy, modular alignment, rules, frames, or subtle cut/outline/emboss details. Plain default body text, Chinese bottom text, placeholder glyphs, meaningless pseudo-English, unauthorized numbers, invented facts, or obvious gibberish fail this gate.
8. **Selected color:** Black-silver reads near-black, indigo reads visibly medium-dark indigo, and retro pink reads clean luminous pearl pink without dirty gray paper wear. Every readable text element remains silver, and the user photo is not tinted with the selected background color.
9. **Finish:** The design feels polished and intentional while clearly sourced from low-resolution 1999–2004 consumer imaging. At normal viewing size and in a face crop, verify limited detail, hard-flash clipping, low dynamic range, scanlines or interlace evidence, chroma bleed, signal noise, early JPEG damage, and CRT/print aging. Grain restricted to the border or top layer fails this gate.
10. **Originality:** No recognizable celebrity, artist, brand, album, mascot, logo, watermark, or platform mark is introduced.

If the result fails a core gate, explain the failure and stop. Create a new full Prompt version from this one, then wait for an explicit “再试一次” or equivalent before generating again.

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
