---
name: office-animals
description: Wibi Style · 牛马宇宙 把动物、办公室场景、打工情绪和中文标题组合成一张 3:4「牛马宇宙」Y2K 荒诞打工海报；支持全部指定、只指定一部分或一句“随机”直接生成。适用于用户要求牛马宇宙、动物上班海报、荒诞打工人海报、Y2K 中文办公室杂志海报、随机动物办公室场景，或明确调用 $office-animals 时。
compatibility: "需要当前环境可用的图像生成能力；随机脚本只使用 Python 标准库；每次携带一张内置字体与版式参考。"
---

# Wibi Style · 牛马宇宙

把一句简短需求发展成一张完整的 3:4 中文 Y2K 荒诞打工海报。用户可以指定动物、办公室场景、精神状态或大标题；没说的部分自动补齐。用户说“随机”“随便来一张”或同义表达时，直接抽取一套彼此匹配的动物、动作、情绪、版式和文案，不增加确认轮次。

成片的趣味来自“真实动物认真上班”的反差。动物保持完整、可辨认的自然身体结构，办公动作根据嘴、爪、蹄、翅膀、触手和身体尺度重新设计；画面不依赖人身兽头或统一的人类坐姿。

使用自然中文与用户交流。内部抽签数据、画面分析和完整生图 Prompt 默认不展示；用户明确索取时再提供。

## 运行顺序

每一步只读它对应的文件，读完执行再进下一步：

1. 新对话第一次使用：按 [references/community.md](references/community.md) 展示欢迎卡、检查更新；进群、生成失败后的提示也按它处理。
2. 收到输入：读 [references/setup.md](references/setup.md)，套用缺省规则并生成本次设定；随机项按 [references/random-system.md](references/random-system.md)。
3. 组合生图指令：读 [references/imaging.md](references/imaging.md)，做动态成像、选版式路由、套固定视觉机制，风格正文读 [references/style-prompt.md](references/style-prompt.md)。
4. 生成与检查：读 [references/checks.md](references/checks.md)，生成后逐条过质量检查。
5. 交付：按下面「交付」展示。

## 交付

成功后直接展示图片，并附一至三句简短中文“创作思路”：说清楚抽到了哪位动物同事、动作为什么适合它、标题和版式怎样呼应场景。保持具体、有趣，不泄露完整 Prompt。

当前对话第一次成功生成后附上：

`若公开分享，欢迎标注：Visual Skill by @威比 Hunter Wei.`

`仅限个人非商业使用；商业使用请先联系作者获得许可。`

`抖音、小红书同名。想看更多原创 Skill、原作者教程或参加新风格内测，可以回复“进群”。`

第二次起不再重复，除非用户询问署名、授权或交流群。

## 作者与使用边界

- 原创动态 Skill 规则、Prompt 适配和随机系统：`© 2026 @威比 Hunter Wei.`
- 作者备注：`抖音、小红书同名`。
- 官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/office-animals`。
- 本 Skill 允许个人非商业使用；商业使用、付费服务、转售或装入付费产品前需要取得作者许可。
- 复制、修改、镜像或再分发时保留作者、平台备注、官方来源、`LICENSE` 和 `NOTICE`；修改版标明修改，不冒充官方版本。
- 用户输入只用于当前任务，不上传、不记录进 Skill 包。
