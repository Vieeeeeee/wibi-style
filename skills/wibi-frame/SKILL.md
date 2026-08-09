---
name: wibi-frame
description: Analyze a user photo, propose three high-value close-up events in Chinese, wait for the user to choose, then generate a 9:16 vintage flat-comic composition with a small geometric frame, a large internal detail, a natural frame breakout, and coordinated color fusion. Use for single-image tests, guided style transfer, approved batch work, and post-generation quality control.
---

# Wibi Frame Manga

## Operating contract

- Communicate with the user in Chinese by default. Keep internal analysis and generation prompts private.
- Use the Codex built-in image-generation tool by default. Use Lovart only when the user explicitly requests it.
- Process one photo at a time unless the user explicitly authorizes batch work.
- Treat a newly uploaded photo as content authority. References define visual treatment; layout guides define geometry only.
- Preserve every substantive prompt revision and generated version. Never overwrite an earlier result.
- Keep raw generations, failed versions, and repaired intermediates as private local records. Do not render, link, or otherwise surface them to the user unless the user explicitly asks to see process work or a specific earlier version.

## Interaction state

### 1. New photo: propose the crop before generating

Inspect the full photo and propose exactly three distinct close-up events. Rank the strongest option as A and mark it as recommended. This turn is text-only: do not call an image-generation tool and do not produce concept sketches.

Use this Chinese response pattern:

```text
我从照片里找到了三个适合放大的局部：

A. <具体局部 + 关系>（推荐，<一句理由>）
B. <具体局部 + 关系>（<一句特点>）
C. <具体局部 + 关系>（<一句特点>）

回复 A、B 或 C；也可以说“按推荐来”。
```

The choice locks only the enlarged source region. Frame geometry, breakout direction, palette, and color fusion remain open until generation.

### 2. Selection received: generate one result

Proceed when the user selects A, B, or C; describes one candidate in natural language; chooses a different precise region; or says “按推荐来”, “你决定”, or “直接做”. Use A when the user delegates the decision.

If the user already specifies a precise crop in the initial request, skip the candidate turn and generate directly. If several photos arrive without batch authorization, ask which photo to process first.

### 3. Feedback and batch behavior

- Feedback without a new generation request: acknowledge it, update the working interpretation, and wait. Do not generate again.
- Approved batch: present candidates per photo unless the user authorizes “全部按推荐来”. Track every case independently.
- Default selected-case budget: one initial generation. Use one additional targeted regeneration only when automatic optimization or batch optimization has already been authorized. Never hide an extra generation call.
- A tool error, empty output, or timeout is a generation failure. Stop instead of silently retrying, changing model, or changing quality.

## Visual objective

Create a small framed scene inside a large field of flat color. Maintain two simultaneous scales:

- the framed scene occupies only about 30–40% of the canvas along its dominant axis;
- the chosen detail is enlarged inside that frame and reaches its edges.

A valid close-up can be described as “one specific part + one visual relationship”, such as fingers exposing an earring, noodles touching the mouth, a palm covering one eye, or a shoe crossing a border. Preserve identifiers unique to the source photo. A centered full face, reduced half-body portrait, or miniature full figure indicates failed distillation.

## Distill the source image

1. Read the complete action, pose, object interaction, occlusion, and distinctive accessories.
2. Build three candidates from different parts, scales, or relationships. Do not relabel the same crop three times.
3. Rank by source specificity, contact or occlusion clarity, silhouette strength, thumbnail legibility, color potential, and surprise value.
4. Prefer the strongest recognizable relationship. For a quiet frontal portrait, two eyes with brow and hairline may be stronger than an artificially isolated ear or environmental fragment.
5. After selection, lock a real tight crop from the source. Preserve angle, contact points, occlusion order, finger direction, object position, accessory structure, and the chosen expression. Do not reconstruct cropped-away anatomy or scenery.

Candidate labels must be concrete, for example:

- one eye + blue hair clip + crossing hair;
- mouth corner + noodle contact + chopstick tip;
- green nails + chopsticks + bowl rim;
- ear + earring + hair pressed against the ear;
- shoe + ankle tattoo + skirt hem.

## Route references and layout assets

Choose one primary reference from `assets/references/`. It controls close-up density, crop rhythm, border interaction, line treatment, and color organization. It does not supply people, props, text, or decorative content.

| Selected event | Primary reference candidates |
| --- | --- |
| Eyes, mouth, or hands around the face | `01`, `05`, `06`, `08`, `09`, `10`, `17` |
| Hand-to-object contact | `01`, `07`, `10`, `15` |
| Legs, shoes, neckline, jewelry, or clothing | `11`, `12`, `13`, `14`, `16` |
| Segmented crop rhythm only | `02`, `03` |
| Rare full-head exception with smoke or headwear | `04` |

Read each input by role:

- source photo: subject, pose, interaction, and internal-geometry authority;
- primary visual reference: style and crop-density authority;
- layout guide: frame shape, size, and placement authority only.

## Select the frame

Use a recognizable geometric window:

- rectangle for horizontal eye-mouth relationships, face-and-hand events, object contact, or vertical garment crops;
- square for a single eye, compact gestures, or tight makeup details;
- slanted quadrilateral for directional profiles, tools, or diagonal gaze;
- diamond for centered earrings, symmetrical gestures, or centered makeup.

A shallow, wide rectangular frame is the most failure-resistant composition, but it is not the automatic default for every image. Select it only when the event has a genuinely horizontal reading direction. Let the crop direction and center of gravity determine the frame.

Use the 14 guides in `assets/layout-guides/`:

- horizontal: `横向小框.png`, `横向小框_居中宽.png`, `横向小框_偏下.png`;
- segmented: `错位双横框.png`, only for two source-supported information bands;
- compact: `正方形小框.png`, `正方形小框_偏上.png`, `正方形小框_偏右.png`;
- diagonal: `斜四边形小框.png`, `斜四边形小框_反向.png`;
- centered: `菱形小框.png`, `菱形小框_双层.png`;
- vertical: `窄竖框.png`, `窄竖框_偏右.png`;
- no visible frame: `纯色鼠尾草底.png`, only when subject edges or color contrast still make the crop boundary intelligible.

Treat guide colors as placeholders. Decide composition first; derive the final palette independently from the source and primary reference.

## Design the boundary and palette

### Natural frame breakout

Prefer one credible breakout. Let the model choose the source-supported element, crossed edge, and extension length. Hair, smoke, noodles, straps, hems, arms, hands, legs, shoes, or tools are valid only when their original direction supports the crossing.

Keep the chosen close-up even when another crop would break out more easily. At the crossing, the subject sits in front and fully hides that segment of the border. Resume the border on both sides of the subject. Use a contained frame only when no continuous source element can cross naturally.

### Color fusion

Prefer one connection color already present in the selected crop. When that exact color reaches the frame edge, use the same value outside the frame and remove only the border segment at the true color contact. Preserve enough straight edges and corners for the original frame shape to remain legible.

Use one clear breakout and one color-fusion contact when the source supports both. They may occupy different edges or cooperate in one direction. Keep the outer field as one uniform matte color without gradients, vignettes, halos, or patch-like cleanup shapes.

## Visual language

Use a vintage American-comic and old-print graphic language:

- thick, decisive black outer contours that remain legible at phone-thumbnail size;
- sparse internal lines limited to expression, joints, folds, and contact points;
- large black shadow masses and clear negative space;
- three to five matte flat colors with at most one hard-edged shadow per region;
- restrained halftone, hatching, or paper grain used only as print character;
- simplified material cues with minimal highlights.

Build identity through silhouette, expression, accessories, action, and local structure. If fine lines or texture dominate the thumbnail, regenerate with heavier contours, fewer internal marks, and larger tonal masses.

## Generation plan

Plan in two internal design passes; do not interpret them as two mandatory tool calls.

1. Establish the selected close-up at large scale, preserving source geometry, contact, and the intended breakout path.
2. Place that locked event into the selected guide, scale the complete framed unit to 30–40% of the canvas along its dominant axis, and resolve the outer color field and color-fusion contact.

The generation prompt for the current photo must specify:

1. selected event and exact crop boundaries;
2. source invariants: angle, contact, occlusion, direction, and accessory structure;
3. one primary reference and its assigned style role;
4. omitted content that must remain cropped away;
5. selected regular frame, placement, and target scale;
6. independently chosen palette, exact connection color, and border segment to remove;
7. one natural breakout path with the subject covering the crossed border;
8. vintage flat-comic line and shading treatment;
9. final 9:16 composition with no text, watermark, analysis, or comparison layout.

## Output specification

- Deliver `1440×2560` pixels, `9:16`, PNG.
- Request a 9:16 image and retain the highest-resolution source returned by the built-in tool.
- Treat the built-in tool result as an unapproved intermediate until the complete quality gate passes. During generation and repair, capture its saved path without presenting the raw image to the user.
- Perform crop cleanup and outer-field correction at source resolution.
- Resize once, at the end, directly to `1440×2560`; do not pass through intermediate sizes.
- Preserve PNG throughout. A final upscale can preserve the delivery dimensions but cannot create detail absent from the native result.
- Read the saved file dimensions before delivery. Reject any file that is not exactly `1440×2560`.

## Quality gate and repair policy

Check in this order:

1. **Event:** the first read is a specific local relationship, not a generic portrait.
2. **Source fidelity:** crop, pose, contact, occlusion, and object direction match the source.
3. **Scale:** the frame is small on the canvas while the selected detail remains large inside it.
4. **Geometry:** the frame is one of the approved regular shapes and remains legible.
5. **Boundary:** a credible breakout is used when available; the subject covers the crossed border.
6. **Color:** palette and layout were selected independently; an exact shared color fuses inside and outside when available.
7. **Style:** heavy contours and large tonal masses dominate over fine lines and noise.
8. **Background:** the connected outer field is a uniform flat color with clean edges and corners.
9. **Ratio lock:** local cleanup preserves the complete framed unit with identical width-to-height ratio, no clipped edge, and no change to the internal crop. Allow at most `0.5%` ratio drift from the generated unit.
10. **File:** PNG, exact `1440×2560`, undistorted 9:16.

Repair by failure class:

- Event, source fidelity, anatomy, contact, or comic style failure: preserve the failed version and use one targeted regeneration when authorized.
- Correct content with only frame scale, position, outer-field uniformity, or final-size issues: use safe local post-processing.
- Safe post-processing may uniformly scale the complete framed unit with the same factor on both axes, reposition it, replace only the connected outer field, remove outer artifacts, and perform the one final resize. It may not manually crop any framed-unit edge, distort its aspect ratio, redraw the subject, change the internal crop, move fingers or props, reorder occlusion, reconstruct anatomy, or place a border over a breakout subject.
- If the authorized targeted regeneration still fails, retain the best version locally, state the remaining issue in Chinese, and wait for the user. Show that version only when the user explicitly asks to see it.

For batches, apply the full gate independently to every photo. Report partial success accurately and retain all case-level versions.

## User-facing delivery

After generation, repair, and the complete quality gate, show only the single final approved image. Do not show raw tool output, failed generations, before-and-after comparisons, repaired intermediates, or alternate versions unless the user explicitly requests them. Then explain the selected local event, why it was worth enlarging, and how the frame and palette support it in two or three concise Chinese sentences. Do not expose candidate scoring or the internal generation prompt.

For the first two successful generations in a conversation, append:

`若公开分享，欢迎标注：Visual Skill by @威比 Hunter Wei.`

`仅限个人非商业使用；商业使用请先联系作者获得许可。`

Omit the repeated notice from the third successful generation onward unless the user asks about attribution or licensing.

## Distribution and authorship

The public package includes 17 visual-study references in `assets/references/`. Use them only for crop density, boundary logic, line treatment, and color organization. Do not copy their people, props, text, or decoration.

The original Skill logic and layout guides are for personal, non-commercial use. Commercial use requires prior permission from the author. Rights in bundled reference images remain with their respective rights holders; do not extract them for separate redistribution or commercial use.

The fixed author credit is `@威比 Hunter Wei.` The final period is part of the display name.
