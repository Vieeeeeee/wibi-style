# Wibi Style · 地下试镜skill

把一张清晰人像照片做成纯白背景的三联"模特资料卡"：同一个人原地转身的三个定格——完整侧脸转向画面左侧、正面直视喊叫、完整侧脸镜像转向画面右侧——用九十年代模特试镜宝丽来快照式的机顶直闪硬光拍摄，清冷未修图质感。

当前版本：`v1.1.4`

作者：`@威比 Hunter Wei.`（抖音、小红书同名）

## 成图示例

以下均为本 Skill 的实际生成结果，仅展示成图，不包含用户原始照片。

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/underground-audition-v1.1.4/docs/underground-audition/examples/example-01.png" alt="地下试镜skill成图示例 1" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/underground-audition-v1.1.4/docs/underground-audition/examples/example-02.png" alt="地下试镜skill成图示例 2" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/underground-audition-v1.1.4/docs/underground-audition/examples/example-03.png" alt="地下试镜skill成图示例 3" width="30%" />
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/underground-audition-v1.1.4/docs/underground-audition/examples/example-04.png" alt="地下试镜skill成图示例 4" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/underground-audition-v1.1.4/docs/underground-audition/examples/example-05.png" alt="地下试镜skill成图示例 5" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/underground-audition-v1.1.4/docs/underground-audition/examples/example-06.png" alt="地下试镜skill成图示例 6" width="30%" />
</p>

手机壁纸的两套背景色预设（纸白 / 深炭黑，logo 颜色自动跟随适配）：

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/underground-audition-v1.1.4/docs/underground-audition/bg-preset-demo.png" alt="纸白与深炭黑两套壁纸背景色对比" width="60%" />
</p>

## 安装

在 Codex 中发送：

```text
请安装这个 Skill：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/underground-audition
```

安装器只下载这一款 Skill，不会下载仓库中的其他风格。这款 Skill 没有随包的视觉参考图，只包含规则文本和排版脚本；安装完成后会展示名称、版本、作者、同名平台、官方来源和安装路径。

作者卡会简短介绍"威比 😌 AIGC 学习群"；回复"进群"可从官方仓库读取当前入群链接和二维码。真实生图接口报错、空输出或超时时，也会在停止自动重试后展示一次当前入群信息。

每个新任务第一次使用时会查询这一款有没有新版本；只在发现更新时提醒，不自动覆盖本地文件，也不上传用户照片。

## 使用

上传一张照片后说：

```text
使用 $underground-audition 处理这张照片
```

Skill 会先看一遍照片、确认适合这套风格，再生成一张三联转身照。**生成后会自动核对转身角度、镜像关系和表情是否成立**——如果左右两张没有真的转到完整九十度、或者中间那张不像在喊叫，Skill 会展示当时的结果、说明具体哪里不对，并问你要不要再出一张；**只有你明确同意，才会重新生成，绝不擅自多跑一次**。

默认交付小红书方图；检查通过后 Skill 会主动问一句要不要顺便出一张手机壁纸尺寸，背景色可以选纸白（默认，偏暖的白，不是纯白）或深炭黑，logo 颜色会自动跟着背景换。也可以直接说"给我锁屏版，黑色背景"一步到位。除了方图和锁屏，还有一档 3:4 竖版（1536×2048），说一句「要 3:4 竖版」就能拿到。

## 适合的照片

- 单人、正面或半侧的半身或大头照，五官清楚、发型轮廓明确；
- 戴眼镜、连帽衫、卷发、短发、长直发、耳饰都已经过测试；
- 不适合：多人合影、全身远景、脸部过小或严重模糊的照片——缩小后会丢掉辨识度。

## 视觉规格

| 项目 | 规格 |
| --- | --- |
| 比例 | 1:1（另提供 3:4 与手机锁屏画幅） |
| 尺寸 | 小红书方图 2048×2048；3:4 方图 1536×2048；锁屏 1290×2796 |
| 格式 | PNG |
| 背景色 | 纸白 `#F7F5F0`（默认）/ 深炭黑 `#0A0A0A`，logo 颜色自动跟随背景适配 |
| 结构 | 三张 3:4 竖版照片横排在画布上，下方合成 WIBI 品牌标记 |
| 拍法 | 机顶直闪硬光的宝丽来试镜快照，清冷未修图质感 |
| 生成后检查 | 自动核对转身角度与表情；不通过只询问是否重出，不自动重试 |
| 生图能力 | 使用当前环境已经可用的工具或模型，针对 GPT Image 2 调校验证 |

在线体验更多风格：[威比风格实验室](https://style.abdc.online)

## 使用与授权

原创 Skill 规则仅限个人非商业使用；商业使用请先联系作者获得许可。复制、修改、转发、镜像或重新打包本 Skill 时，必须完整保留作者、抖音/小红书同名备注、官方仓库地址、`LICENSE` 和 `NOTICE`。公开分享生成结果时欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

本包不包含案例原图或用户照片，也没有随包分发的视觉参考图——这套风格完全依赖文字规则驱动，生成阶段不携带任何图片。包内唯一随包的图片资产是 `assets/brand/logo_wibi_skill.png`，作者原创的 WIBI 品牌标记，只在出图之后由排版脚本贴上，不参与生成、不是风格参考。README 展示的成图位于仓库 `docs/`，不随单款 Skill 安装。完整范围见 [`LICENSE`](LICENSE) 与 [`SOURCES.md`](SOURCES.md)。
