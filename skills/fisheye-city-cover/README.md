# Wibi Style · 鱼眼城市海报

把一张人物、合照、街拍或旅行照片做成 3:4 Y2K 强鱼眼城市杂志海报：真实 8–12mm 鱼眼畸变、液态铬银城市标题、三种可选背景、旧 CCD / MiniDV 质感和断续 RGB 信号横条。

当前版本：`v0.13.4`

作者：`@威比 Hunter Wei.`（抖音、小红书同名）

官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/fisheye-city-cover`

## 安装

在 Codex 中发送：

```text
请安装这个 Skill；安装完成后，运行包内 `scripts/show_skill_info.py --always`，并把输出的 Skill 信息完整展示给我：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/fisheye-city-cover
```

安装器只下载这一款 Skill，不会下载仓库中的其他风格。每个新对话第一次使用时会展示两段式 Markdown 欢迎卡。

## 使用

上传一张照片后说：

```text
使用 $fisheye-city-cover 处理这张照片
```

如果你还没有选择风格和拍摄地点，Skill 会轻松地问你：

```text
我们先挑一个海报气质吧～ 黑银、靛蓝、复古粉，你更喜欢哪一种？✨

这张照片是在哪里拍的呀？告诉我城市或地点就好，我会把它变成海报上的大标题～
```

回复风格和城市后直接生成，不再增加第二轮确认。也可以一开始就说完整：

```text
使用 $fisheye-city-cover 处理这张照片，选择靛蓝，城市是东京
```

如果同一条消息已经包含风格和城市，Skill 不会重复询问。城市、省份或地区名都可以作为用户指定标题，例如 `东京 → TOKYO`、`香港 → HONG KONG`、`云南 → YUNNAN`。

## 三种独立风格

| 选择 | 背景 | 文字 |
| --- | --- | --- |
| 黑银 | 近黑、炭黑包裹背景 | 液态铬银标题与银色小字 |
| 靛蓝 | 一眼可见的中深灰调靛蓝 | 液态铬银标题与银色小字 |
| 复古粉 | 干净清透的草莓牛奶粉、珠光果冻粉 | 液态铬银标题与银色小字 |

三种风格使用完全独立的完整模板，不在一次生成中混色。

## 共同规格

| 项目 | 规格 |
| --- | --- |
| 比例 | 3:4 竖图 |
| 内容 | 原照片决定全部人物、动作、服装、道具、背景和构图 |
| 鱼眼 | 真实 8–12mm 光学畸变；中心近大远小、周边直线弯曲、空间卷曲，不能只是圆形裁切 |
| 版式 | 用户所选背景色、液态铬银大标题、银色底部小字 |
| 底部文字 | 3–5 组全大写英文短语；窄体科技、扩展体或 Y2K 仪表字体，带字距、粗细、字号、分栏和线框层级设计 |
| 质感 | CCD / MiniDV / CRT、硬直闪、扫描线、JPEG 损伤 |
| 信号元素 | 少量细窄、断续的横向 RGB tracking 彩条 |
| 默认工具 | Codex 内置图片生成工具 |

Skill 每次固定携带一张内置鱼眼版式参考。参考只定义鱼眼结构、标题规模、边框、底部信息层级和旧数码质感，不提供人物、服装、道具、品牌、Logo、原文字或背景。鱼眼圆内部只使用原图已有画面，不向照片边界外扩画；3:4 新增空间由海报背景和文字承担。

## 成图示例

以下均为本 Skill 的实际生成结果，只展示成图，不包含用户原图、Before / After 对比图或运行参考。

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/fisheye-city-cover-v0.13.4/docs/fisheye-city-cover/examples/example-01.png" alt="深圳黑银鱼眼城市海报" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/fisheye-city-cover-v0.13.4/docs/fisheye-city-cover/examples/example-02.png" alt="香港黑银鱼眼城市海报" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/fisheye-city-cover-v0.13.4/docs/fisheye-city-cover/examples/example-03.png" alt="成都靛蓝鱼眼城市海报" width="30%" />
  <br />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/fisheye-city-cover-v0.13.4/docs/fisheye-city-cover/examples/example-04.png" alt="杭州清透粉鱼眼城市海报" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/fisheye-city-cover-v0.13.4/docs/fisheye-city-cover/examples/example-05.png" alt="新加坡清透粉鱼眼城市海报" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/fisheye-city-cover-v0.13.4/docs/fisheye-city-cover/examples/example-06.png" alt="北京三人合照鱼眼城市海报" width="30%" />
</p>

## 更新与隐私

每个新任务第一次使用时会只读检查这一款 Skill 是否有新版本。发现更新时只提醒，不自动覆盖本地文件；网络不可用不阻断生成，也不会上传用户照片或使用数据。

用户照片只用于当前任务，不进入安装包、公开仓库或后续用户的参考集。

想交流 Skill 安装、选图、生图问题或参加新风格内测，可以在使用时回复“进群”。Skill 会从官方仓库下载当前二维码并通过本地图片展示；不会提供无法从普通浏览器直接入群的链接。二维码过期或网络不可用时不会展示旧图。

## 使用与授权

原创 Skill 规则与 Prompt 适配仅限个人非商业使用；商业使用请先联系作者。复制、修改、转发、镜像或重新打包时，必须保留作者、抖音/小红书同名备注、官方仓库地址、`LICENSE` 和 `NOTICE`。公开分享生成结果时欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

内置版式参考已由用户于 2026-08-14 确认为公开素材并授权随本 Skill 分发。来源路径、SHA-256 和运行职责见 [`SOURCES.md`](SOURCES.md)。
