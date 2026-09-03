# Input contract and style templates

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
