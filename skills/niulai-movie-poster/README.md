# Wibi Style · 牛来电影海报

把一张横版照片做成《牛来》式低成本电影海报：真人手机照片负责场景、人数、姿势、衣服和道具，低清旧动画牛头负责头脸反差，朱砂红「牛来」毛笔片名和一枚朱红印章负责海报身份。

当前版本：`v1.0.2`

作者：`@威比 Hunter Wei.`（抖音、小红书同名）

官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/niulai-movie-poster`

## 安装

在 Codex 中发送：

```text
请安装这个 Skill：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/niulai-movie-poster
```

安装器只下载这一款 Skill，不会下载仓库中的其他风格。每个新对话第一次使用时会展示两段式 Markdown 欢迎卡。

## 人数路由

Skill 会先识别照片里清楚可替换的人数，再自动选择对应提示词和最少的角色参考：

| 人数 | 提示词 | 参考 |
|---|---|---|
| 1 人 | `references/prompts/01-single.md` | 黄色大牛 |
| 2 人 | `references/prompts/02-double.md` | 黄色大牛、橙色小牛 |
| 3 人 | `references/prompts/03-triple.md` | 黄色大牛、橙色小牛、黄色黑斑豹 |

## 使用

```text
使用 $niulai-movie-poster 把这张横版照片做成牛来电影海报。
```

默认只处理一张横版照片，输出 3:2 横版 PNG。照片内容优先：人数、场景、身体、衣服、手、道具、姿势和视线尽量保留；只替换头脸。竖版、四人以上、远景小人群或严重遮挡照片先换合适原图，或由用户明确允许裁切后再做。

## 成图方向

- 真人手机照片与低清旧动画头脸形成反差；
- 中文为主的电影海报，片名固定为“牛来”；
- 朱砂红粗毛笔字和朱红印章；
- 信息少而认真，不做商业大片、影展豪华版式或高级潮玩；
- 合照保留废片库式的近距离、不对称和偶然关系。

若公开分享，欢迎标注：`Visual Skill by @威比 Hunter Wei.`

仅限个人非商业使用；商业使用请先联系作者获得许可。复制、修改、镜像或再分发时请保留作者、平台备注、`LICENSE`、`NOTICE` 和来源说明。
