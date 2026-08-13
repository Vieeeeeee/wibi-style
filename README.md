# Wibi Style

由 `@威比 Hunter Wei.` 制作和维护的视觉风格 Skill 仓库，抖音、小红书同名。

当前收录 **13 款可独立安装的视觉风格 Skill**。选择一款、上传照片，即可在 Codex 中生成对应风格；也可以前往 [威比风格实验室](https://style.abdc.online) 在线体验。

> 商务合作、商业授权或使用咨询，请加微信：`Wibi2077`（添加时请备注来意）。

## 加入交流群

欢迎加入「威比 😌 AIGC 学习群」，交流 AI 视觉玩法、Skill 使用和新风格。

[点击加入微信群](https://weixin.qq.com/g/AQYAAFCgkb4xsWUyI8RZ1eIfp48iPM_RN7O5DV_6BIEZLSEDGLmaHxMw1r2FlhGf)，或用微信扫描下方二维码：

<a href="https://weixin.qq.com/g/AQYAAFCgkb4xsWUyI8RZ1eIfp48iPM_RN7O5DV_6BIEZLSEDGLmaHxMw1r2FlhGf"><img src="assets/wechat-aigc-group-qr.jpg" alt="威比 AIGC 学习群二维码" width="360"></a>

> 当前二维码和链接有效期至 2026 年 8 月 20 日；过期后请加微信 `Wibi2077` 获取新入口。

[![Wibi Style 13 款视觉风格总览](assets/readme-style-overview.png)](https://style.abdc.online)

## 按照片选风格

| 你的照片 | 推荐风格 |
| --- | --- |
| 自拍、头像、人物近景 | Wibi Style · 电蓝网点海报、Wibi Style · 粗线条漫画头像、Wibi Style · 蜡笔手绘头像、Wibi Style · 暗夜红黑赛璐璐、Wibi Style · 虹彩柔焦长曝光、Wibi Style · 蓝底复古印刷 |
| 儿童正脸或大头照 | Wibi Style · 钻牙萌娃大头 |
| 人物、宠物、产品或物件 | Wibi Style · 怪趣波普涂鸦贴纸、Wibi Style · 照片拼豆挂件、Wibi Style · 像素切片拉伸、Wibi Style · 乱码像素拼贴 |
| 城市街景、建筑、旅行照片 | Wibi Style · 晴空都市赛璐璐 |
| 想先挑选照片里最有意思的局部 | Wibi Style · 框景漫画（进阶、多步骤） |

## 全部风格

点击名称可查看 6 张实际生成结果、适合的照片和该款安装指令。

`Wibi Style ·` 是统一展示前缀；英文 Skill 名、GitHub 地址和 `$调用名` 保持不变，旧用法继续有效。

| 中文名 | Skill | 适合的照片 |
| --- | --- | --- |
| [Wibi Style · 框景漫画](skills/wibi-frame/) | `wibi-frame` | 有清楚眼神、表情、手势或物件关系的照片；先选局部，再生成 |
| [Wibi Style · 电蓝网点海报](skills/electric-blue-halftone-poster/) | `electric-blue-halftone-poster` | 单人人像或宠物大头照 |
| [Wibi Style · 钻牙萌娃大头](skills/diamond-kid-head-card/) | `diamond-kid-head-card` | 脸部、头发或帽子大致可辨的单人儿童照片 |
| [Wibi Style · 怪趣波普涂鸦贴纸](skills/quirky-pop-doodle-sticker/) | `quirky-pop-doodle-sticker` | 主体清楚、动作和轮廓有记忆点的人物、宠物、产品或道具 |
| [Wibi Style · 晴空都市赛璐璐](skills/clear-sky-urban-cel/) | `clear-sky-urban-cel` | 城市街道、建筑、旅行纪实、交通设施和环境人物 |
| [Wibi Style · 照片拼豆挂件](skills/photo-perler-charm/) | `photo-perler-charm` | 人物、宠物、花束、食物和轮廓清晰的物件 |
| [Wibi Style · 暗夜红黑赛璐璐](skills/dark-red-black-cel-shaded/) | `dark-red-black-cel-shaded` | 轮廓清楚、适合戏剧性红黑光影的人物照片 |
| [Wibi Style · 乱码像素拼贴](skills/glitch-pixel-collage/) | `glitch-pixel-collage` | 人物、静物或色彩层次明确的照片 |
| [Wibi Style · 粗线条漫画头像](skills/alt-manga-avatar/) | `alt-manga-avatar` | 正面或半侧脸自拍 |
| [Wibi Style · 像素切片拉伸](skills/pixel-stretch/) | `pixel-stretch` | 主体清楚的人物、静物或其他照片 |
| [Wibi Style · 蜡笔手绘头像](skills/art-print-poster/) | `art-print-poster` | 五官清楚、表情有记忆点的自拍 |
| [Wibi Style · 虹彩柔焦长曝光](skills/iridescent-long-exposure/) | `iridescent-long-exposure` | 想要朦胧氛围的人物近景或局部特写 |
| [Wibi Style · 蓝底复古印刷](skills/blue-retro-print/) | `blue-retro-print` | 轮廓和神态清楚的人物照片 |

## 三步安装和使用

### 1. 选择一款

打开上方任意一款的页面，复制它的 GitHub 地址。每款都放在独立目录中，只会安装你选择的这一款。

### 2. 在 Codex 中发送安装指令

以“电蓝网点海报”为例：

```text
请安装这个 Skill；安装完成后，运行包内 `scripts/show_skill_info.py --always`，并把输出的 Skill 信息完整展示给我：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/electric-blue-halftone-poster
```

### 3. 新开一个任务，上传照片后调用

```text
使用 $electric-blue-halftone-poster 处理这张照片
```

调用其他风格时，将 `$electric-blue-halftone-poster` 换成列表中的对应 Skill 名称。

## 包含内容与更新

每款风格都有独立的 `SKILL.md`、运行规则、提示词、版本清单，以及该款需要的参考素材或支持文件。各款互不混放。

每个新任务第一次调用时，只查询当前使用的这一款是否有新版本；发现新版才提示，不自动覆盖本地文件，也不上传用户照片或使用数据。

## 使用与署名

公开分享生成结果时，欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

本仓库中的原创 Skill 逻辑、提示词与原创构图模板仅限个人非商业使用；商业使用请先联系作者获得许可。复制、修改、转发、镜像或重新打包某款 Skill 时，必须保留作者、抖音/小红书同名备注、官方来源、`LICENSE` 与 `NOTICE`；修改版必须明确标注经过修改，不得冒充官方版本。

每款 Skill 的 `SOURCES.md` 会分别说明本包拥有和不拥有的内容权利。第三方图片公开可见不代表获得再分发许可，未通过版权门的素材不会加入新的公开安装包。
