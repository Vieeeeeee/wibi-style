# Generation and quality gate

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
