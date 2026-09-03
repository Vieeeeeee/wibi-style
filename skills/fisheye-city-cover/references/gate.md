# Photo, style, and city gate

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
