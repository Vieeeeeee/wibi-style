# Wibi Style · 定制印刷票根

把一张人物、旅行、街景、建筑、食物或日常照片做成一张中英混排的私人纪念票根。Skill 会先理解画面，再写出属于这个瞬间的 Hero 文案，从四套印刷方向里选择一套，并在一次图片生成中完成照片制版、字形、纸张和油墨。

当前版本：`v1.1.0`

作者：`@威比 Hunter Wei.`（抖音、小红书同名）

官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/personalized-print-ticket`

## 安装

在 Codex 中发送：

```text
请安装这个 Skill：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/personalized-print-ticket
```

安装器只下载这一款 Skill。安装后会显示作者卡；新对话第一次调用时会提示你上传照片。

## 使用

上传一张照片后说：

```text
使用 $personalized-print-ticket 处理这张照片
```

你可以指定「橙黑活版」「粉纸朱红」「黑白手绘」或「珊瑚电影票」。没有指定时，Skill 会根据照片内容推荐；说“自动”或“给我惊喜”时会直接选择并生成。

## 它会做什么

1. 阅读照片里的主体、数量、姿态、物件、建筑和场景方向。
2. 从城市、天气、动作、光线或前后时刻中提炼 2–8 个汉字的 Hero 文案，并写一条自然英文标题。
3. 选择忠实印刷化或艺术化重绘，再匹配一套票根预设。
4. 用脚本生成准确文字和构图的排版导引图。
5. 把原始票根、用户照片和排版导引图交给当前环境可用的图片生成工具，一次完成整张票根。
6. 生成通过检查后，用代码沿照片副券边缘加入撕票虚线与缺口，并输出带四角裁口、侧边打孔的黑底展示图和透明裁切图。

城市名只在用户确认或画面证据足够明确时进入文案。照片决定人物与场景内容，内置参考只决定票根的结构、字形和纸墨方式。

## 四种印刷方向

| 选择 | 视觉特点 |
| --- | --- |
| 橙黑活版 `orbit-orange` | 暖白纸、黑色摄影制版、橙色标注和重型文化票字形 |
| 粉纸朱红 `blossom-red` | 淡粉纸、朱红单色版、超大标题和轻盈留白 |
| 黑白手绘 `sketch-black` | 暖白纸、黑色影印、线框标题和电影档案感 |
| 珊瑚电影票 `signal-coral` | 珊瑚红纸、近黑墨、宽幅标题和高密度照片版 |

## 成图示例

以下均为本 Skill 的实际生成结果，只展示生成成品，不包含用户原图、对比排版或运行参考。

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/personalized-print-ticket-v1.1.0/docs/personalized-print-ticket/examples/example-01.png" alt="香港雨未落橙黑票根" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/personalized-print-ticket-v1.1.0/docs/personalized-print-ticket/examples/example-02.png" alt="马尼拉的手势珊瑚票根" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/personalized-print-ticket-v1.1.0/docs/personalized-print-ticket/examples/example-03.png" alt="迎面风粉纸朱红票根" width="30%" />
  <br />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/personalized-print-ticket-v1.1.0/docs/personalized-print-ticket/examples/example-04.png" alt="一脸夏光橙黑票根" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/personalized-print-ticket-v1.1.0/docs/personalized-print-ticket/examples/example-05.png" alt="夜还没跑完黑白票根" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/personalized-print-ticket-v1.1.0/docs/personalized-print-ticket/examples/example-06.png" alt="雨停在伦敦橙黑票根" width="30%" />
</p>

## 输出与检查

默认先生成 `2048×769` 的横向窄票根，再输出同尺寸黑底裁切展示图和带透明通道的独立票根。裁切严格跟随照片副券边缘，包含四角裁口、上下撕票口、虚线和侧边打孔。Skill 同时保留原始横向票根、信息 JSON、完整生成 Prompt 和排版导引图；一次调用只生成一张，失败或视觉未通过时不会自动重试。

## 更新、隐私与社群

每个新任务第一次使用时只读检查这一款 Skill 是否有新版本；发现更新时只提醒，不自动覆盖本地文件。用户照片只用于当前任务，不进入安装包、公开仓库或后续用户的参考集。

想交流 Skill 安装、选图和生图问题，可以在使用时回复“进群”。Skill 会读取官方仓库的当前入口；二维码过期或下载失败时不会展示旧图。

## 使用与授权

原创 Skill 规则、排版脚本与 Prompt 适配仅限个人非商业使用；商业使用请先联系作者。复制、修改、转发、镜像或重新打包时，必须保留作者、抖音/小红书同名备注、官方仓库地址、`LICENSE` 和 `NOTICE`。公开分享生成结果时欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

四张运行参考由项目作者选择进入本次公开包，来源、SHA-256 与职责见 [`SOURCES.md`](SOURCES.md)。
