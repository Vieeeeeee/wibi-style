# Wibi Style

**English** · [简体中文](README.md)

A collection of visual style Skills, made and maintained by `@威比 Hunter Wei.` — same handle on Douyin and Xiaohongshu.

**15 individually installable visual style Skills.** Pick one, upload a photo, and get that style back in Codex. You can also try them online at [Wibi Style Lab](https://style.abdc.online).

> For business partnerships, commercial licensing, or usage questions, add WeChat: `Wibi2077` (please mention why you're reaching out).

[![Wibi Style — 15 visual styles](assets/readme-style-overview.png)](https://style.abdc.online)

## Pick a style by your photo

| Your photo | Suggested styles |
| --- | --- |
| Selfies, avatars, close-up portraits | Electric Blue Halftone Poster, Bold Line Manga Avatar, Crayon Sketch Avatar, Dark Red & Black Cel Shade, Iridescent Long Exposure, Blue Retro Print |
| People, group shots, street or travel photos | Fisheye City Poster |
| Front-facing or close-up photos of kids | Diamond Grin Kid Portrait |
| People, pets, products, objects | Quirky Pop Doodle Sticker, Photo Perler Charm, Pixel Slice Stretch, Glitch Pixel Collage |
| City streets, architecture, travel photos | Clear Sky Urban Cel |
| Restaurant shots, food photos, full tables | Retro Table Magazine |
| You want to crop the most interesting part first | Framed Comic Panel (advanced, multi-step) |

## All styles

Click a name to see 6 real generated results, what photos it suits, and the install command for that style.

`Wibi Style ·` is a shared display prefix. The Skill name, GitHub path, and `$invocation-name` never carry it.

| Style | Skill | Works best with |
| --- | --- | --- |
| [Wibi Style · Framed Comic Panel](skills/wibi-frame/) | `wibi-frame` | Photos with clear eye contact, expression, gesture, or object relationships — crop first, then generate |
| [Wibi Style · Electric Blue Halftone Poster](skills/electric-blue-halftone-poster/) | `electric-blue-halftone-poster` | Single-person portraits or pet close-ups |
| [Wibi Style · Diamond Grin Kid Portrait](skills/diamond-kid-head-card/) | `diamond-kid-head-card` | Single-child photos where face, hair, or hat is recognizable |
| [Wibi Style · Quirky Pop Doodle Sticker](skills/quirky-pop-doodle-sticker/) | `quirky-pop-doodle-sticker` | People, pets, products, or props with a clear subject and memorable pose |
| [Wibi Style · Clear Sky Urban Cel](skills/clear-sky-urban-cel/) | `clear-sky-urban-cel` | City streets, architecture, travel documentary, transit, people in their environment |
| [Wibi Style · Photo Perler Charm](skills/photo-perler-charm/) | `photo-perler-charm` | People, pets, bouquets, food, and objects with clean silhouettes |
| [Wibi Style · Dark Red & Black Cel Shade](skills/dark-red-black-cel-shaded/) | `dark-red-black-cel-shaded` | Portraits with clear outlines that suit dramatic red-and-black lighting |
| [Wibi Style · Glitch Pixel Collage](skills/glitch-pixel-collage/) | `glitch-pixel-collage` | People, still life, or photos with distinct color layers |
| [Wibi Style · Bold Line Manga Avatar](skills/alt-manga-avatar/) | `alt-manga-avatar` | Front-facing or three-quarter selfies |
| [Wibi Style · Pixel Slice Stretch](skills/pixel-stretch/) | `pixel-stretch` | People, still life, or anything with a clear subject |
| [Wibi Style · Crayon Sketch Avatar](skills/art-print-poster/) | `art-print-poster` | Selfies with clear features and a memorable expression |
| [Wibi Style · Iridescent Long Exposure](skills/iridescent-long-exposure/) | `iridescent-long-exposure` | Close-ups or detail shots where you want a hazy, dreamlike mood |
| [Wibi Style · Blue Retro Print](skills/blue-retro-print/) | `blue-retro-print` | Portraits with clear outlines and expression |
| [Wibi Style · Fisheye City Poster](skills/fisheye-city-cover/) | `fisheye-city-cover` | Turning people, group shots, street or travel photos into a Y2K heavy-fisheye city cover |
| [Wibi Style · Retro Table Magazine](skills/retro-table-print/) | `retro-table-print` | Table photos where the dishes and vessels are readable — a full table or a single plate |

## Install and use in three steps

### 1. Pick a style

Open any style page above and copy its GitHub URL. Each one lives in its own directory, so only the style you pick gets installed.

### 2. Send the install command in Codex

Using Electric Blue Halftone Poster as an example:

```text
Please install this Skill. Once it's installed, run `scripts/show_skill_info.py --always` from the package and show me the full Skill info output:
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/electric-blue-halftone-poster
```

### 3. Start a new task, upload a photo, and call it

```text
Use $electric-blue-halftone-poster on this photo
```

For any other style, swap `$electric-blue-halftone-poster` for the Skill name from the table above.

## Language note

The style logic inside each `SKILL.md` is written in Chinese, and the models read it fine — you can talk to the Skill in English and it will answer you in English. What is still Chinese-only today: the welcome card and author card the Skill prints on first use, and the per-style README inside each package. Everything works; some of the text just won't be in your language yet. English versions of those are planned.

## Community

You're welcome to join the **威比 😌 AIGC 学习群** — a group for AI visual techniques, Skill usage questions, and new style previews.

[Join via WeChat](https://weixin.qq.com/g/AQYAAFCgkb4xsWUyI8RZ1eIfp48iPM_RN7O5DV_6BIEZLSEDGLmaHxMw1r2FlhGf), or scan this QR code in WeChat:

<a href="https://weixin.qq.com/g/AQYAAFCgkb4xsWUyI8RZ1eIfp48iPM_RN7O5DV_6BIEZLSEDGLmaHxMw1r2FlhGf"><img src="assets/wechat-aigc-group-qr.jpg" alt="Wibi AIGC study group QR code" width="360"></a>

> Heads up: this is a **WeChat group and the conversation is in Chinese**. It needs the WeChat app, so it may not be practical outside mainland China. If you can't join, [open an issue](https://github.com/Vieeeeeee/wibi-style/issues) instead — that works from anywhere.

> This QR code and link are valid until **August 20, 2026**. After that, add WeChat `Wibi2077` for a new invite.

Skills that support the group entry read the root [`community.json`](community.json) on demand and reference the same QR code above. Once the group link, expiry date, and `assets/wechat-aigc-group-qr.jpg` are updated, already-installed preview Skills will pick up the new entry on their next lookup. This lookup uploads no photos and no usage data.

## What's included and how updates work

Every style ships its own `SKILL.md`, runtime rules, prompt, version manifest, and whatever reference material or support files that style needs. Nothing is shared or mixed between styles.

The first time you call a style in a new task, it checks whether that one style has a new version — nothing else. It only tells you when a newer version exists; it never overwrites your local files, and it uploads no photos and no usage data.

## Use and attribution

When you share generated results publicly, please credit:

```text
Visual Skill by @威比 Hunter Wei.
```

The original Skill logic, prompts, and original composition templates in this repository are for **personal, non-commercial use only** — please contact the author for permission before any commercial use. If you copy, modify, redistribute, mirror, or repackage a style, you must keep the author credit, the Douyin/Xiaohongshu handle note, the official source link, `LICENSE`, and `NOTICE`. Modified versions must be clearly marked as modified and must not present themselves as official.

Each Skill's `SOURCES.md` states exactly which rights the package does and does not hold. A third-party image being publicly visible does not grant redistribution rights; material that hasn't cleared the copyright gate never goes into a new public install package.
