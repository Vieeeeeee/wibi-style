# Wibi Style · 牛马宇宙

把动物同事送进办公室：指定动物、场景、精神状态或大标题，也可以一句“随机”抽出一套动作成立的 Y2K 中文荒诞打工海报。

当前版本：`v1.1.0`

作者：`@威比 Hunter Wei.`（抖音、小红书同名）

官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/office-animals`

## 安装

在 Codex 中发送：

```text
请安装这个 Skill：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/office-animals
```

## 展示图

以下六张全部是本 Skill 的实际生成结果，不包含任何手工制作或项目既有素材。

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/office-animals-v1.1.0/docs/office-animals/examples/example-01.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/office-animals-v1.1.0/docs/office-animals/examples/example-02.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/office-animals-v1.1.0/docs/office-animals/examples/example-03.png" width="30%" />
  <br />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/office-animals-v1.1.0/docs/office-animals/examples/example-04.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/office-animals-v1.1.0/docs/office-animals/examples/example-05.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/office-animals-v1.1.0/docs/office-animals/examples/example-06.png" width="30%" />
</p>

## 怎么玩

四个信息都可以指定，也都可以留空：

```text
使用 $office-animals 做一张：水豚在周会上假装听懂，标题“收到但没懂”。
```

```text
使用 $office-animals，随机动物，场景是深夜加班。
```

```text
使用 $office-animals，全部随机。
```

```text
使用 $office-animals，先给我三个设定，不生图。
```

用户明确提供的部分会原样保留，空着的部分才随机。随机系统会先匹配动物身体能力与办公动作，再选择版式和标题，因此每次得到的是一个成立的小情境。每次还会携带一张内置字体与版式参考，只学习红色手工拼字、蓝色边注层级和低清直闪气质，不提供动物、场景和文案。

## 固定风格

| 项目 | 规格 |
| --- | --- |
| 比例 | 3:4 竖版 |
| 主体 | 一只完整、可辨认的真实动物 |
| 场景 | 工位、周会、咖啡机、打印区、述职、闸机、前台、走廊或深夜办公室 |
| 摄影 | 1999–2004 低清数码直闪、荧光灯、轻微 JPEG 损伤与旧印刷颗粒 |
| 标题 | 朱红 `#C40D0A` 超大中文展示字 |
| 边注 | 深钴蓝 `#102C91`，按场景生成核心、辅助、微型三层中文；分别使用粗宋、中宋、细宋，不同版式约 11–15 组 |
| 纸色 | 暖灰纸白 `#E3DEDA` |
| 轮廓 | 动物外沿朱红编辑剪贴描边 |

## 三种版式

- 工位、咖啡机、打印区和夜班使用上标题、下照片的 `headline-photo`。
- 周会、述职、汇报和前台使用满版杂志信息框的 `full-bleed-editorial`。
- 闸机、走廊和电梯使用留白更大的 `cutout-motion`。

## 当前验证状态

水豚周会经过六轮受控迭代定版；随后随机生成浣熊、猩猩、鹿、鹅和章鱼，覆盖五个动物家族、五个场景与三种版式。红色手工拼字、粗宋／中宋／细宋三层边注、蓝字贴器物走线和参考内容隔离均成立；标题按词义断行、不追加多余标点，同一组蓝字在整张图中只出现一次。随机脚本、欢迎卡与更新查询只使用 Python 标准库，不联网上传任何用户数据。

## 内置参考职责

`assets/references/y2k-office-typography-reference.png` 只负责：

- 红色中文标题的手工剪纸式字形；
- 蓝色宋体、黑体、窄体小字的自由混排；
- 低清数码直闪、红色剪贴描边和早期中文 DTP 气质。

动物、场景、动作、道具、标题和边注文案全部由本次动态设定决定。参考中的牛、绿色桌面、显示器、键鼠、Photoshop 画面和原文字不会进入新图。

## 更新与隐私

每个新任务第一次使用时会只读检查这一款 Skill 是否有新版本。发现更新时只提醒，不自动覆盖本地文件；网络不可用不阻断生成，也不会上传用户输入或使用数据。

## 使用与授权

原创 Skill 规则、Prompt 适配和随机系统仅限个人非商业使用；商业使用请先联系作者。复制、修改、转发、镜像或重新打包时，必须保留作者、抖音/小红书同名备注、官方仓库地址、`LICENSE` 和 `NOTICE`。公开分享生成结果时欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```
