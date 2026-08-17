# Wibi Style · 钻牙萌娃大头

> **本款已并入 [Wibi Style · 童年大头卡贴](../kid-head-card/)（`kid-head-card`）。**
> 新包含同一套钻牙萌娃规则，另外支持把当代自拍反推成 5–8 岁的童年酷照，进门会自动判断走哪一版。
> 本包保留可用，但不再单独更新。

把一张单人儿童老照片重新拍摄式地转换成明亮、可爱的现代儿童摄影纯大头卡贴。只有原片明显露齿时才做细密满钻牙；闭嘴人物保持原表情。可选择暖白、复古大波点、柔和双色渐变、蜡笔手绘小星星或柔粉纯色背景。

当前版本：`v1.0.5`

作者：`@威比 Hunter Wei.`（抖音、小红书同名）

## 成图示例

以下均为本 Skill 的实际生成结果，只展示生成成品，不包含儿童老照片。

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/diamond-kid-head-card-v1.0.5/docs/diamond-kid-head-card/examples/example-01.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/diamond-kid-head-card-v1.0.5/docs/diamond-kid-head-card/examples/example-02.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/diamond-kid-head-card-v1.0.5/docs/diamond-kid-head-card/examples/example-03.png" width="30%" />
  <br />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/diamond-kid-head-card-v1.0.5/docs/diamond-kid-head-card/examples/example-04.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/diamond-kid-head-card-v1.0.5/docs/diamond-kid-head-card/examples/example-05.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/diamond-kid-head-card-v1.0.5/docs/diamond-kid-head-card/examples/example-06.png" width="30%" />
</p>

## 安装

在 Codex 中发送：

```text
请安装这个 Skill；安装完成后，运行包内 `scripts/show_skill_info.py --always`，并把输出的 Skill 信息完整展示给我：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/diamond-kid-head-card
```

安装器只下载这一款 Skill。每个新对话第一次使用时会展示两段式 Markdown 欢迎卡并只读查询更新。

回复“进群”会从官方仓库读取并下载当前二维码，再通过本地图片展示；不会提供无法从普通浏览器直接入群的链接。真实生图接口报错、空输出或超时时，也会在停止自动重试后展示一次当前入群信息。

## 使用

上传一张单人儿童照片后说：

```text
使用 $diamond-kid-head-card 处理这张照片，背景选 D 蜡笔手绘小星星。
```

若不指定背景，Skill 会询问 A–E 五种选项；用户说“默认”或“都行”时使用 A 暖白。Skill 使用当前环境已经可用的生图能力，每次生成一张 1:1 PNG。

## 关键规则

- 只保留完整头部、头发与头部配饰，没有脖子、肩膀、衣服、手或身体；
- 明显露齿时才在每颗可见牙面密铺细小钻石，闭嘴时不造牙；
- 老照片只定义人物身份，成品重建为明亮、清透的现代儿童棚拍；
- 一次只使用一种背景，蜡笔星星不得遮挡五官；
- 本款不需要运行参考图，生成时只携带用户上传的照片。

在线体验更多风格：[威比风格实验室](https://style.abdc.online)

## 使用与授权

原创 Skill 规则与提示词仅限个人非商业使用；商业使用请先联系作者。复制、修改、转发、镜像或重新打包时，必须保留 `@威比 Hunter Wei.`、抖音/小红书同名备注、官方来源、`LICENSE` 与 `NOTICE`。公开分享生成结果时欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/diamond-kid-head-card`。
