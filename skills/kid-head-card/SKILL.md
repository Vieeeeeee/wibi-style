---
name: kid-head-card
description: Wibi Style 官方视觉风格。把照片做成儿童纯大头卡贴，只保留头部、干净悬浮在纯色底上。进门先读图分两条路：儿童老照片走「钻牙萌娃」，重建成明亮可爱的现代儿童棚拍并在露齿时做满钻牙；当代自拍走「童年酷照」，把本人反推成 5–8 岁并加潮童装饰。当用户要求童年大头、萌娃大头贴、钻牙大头、把自拍变成小时候的样子，或明确调用 $kid-head-card 时使用。
---

# Wibi Style · 童年大头卡贴

两种玩法共用同一个视觉骨架：**一颗完整的头悬浮在干净纯色底上，没有脖子、肩膀和身体，边缘像一张精心切割的贴纸。** 区别在于原片是什么，以及往哪个方向做。

| | 甜版·钻牙萌娃 | 酷版·童年酷照 |
| --- | --- | --- |
| 输入 | 儿童老照片 | 当代自拍（多为成年人） |
| 做什么 | 重拍式重建成明亮可爱的现代儿童棚拍，露齿时做满钻牙 | 把本人反推成 5–8 岁，加潮童装饰 |
| 背景 | 五选一，默认白色 | 固定浅灰白 |

## 运行顺序

每一步只读它对应的文件，读完执行再进下一步：

1. 新对话第一次使用：按 [references/community.md](references/community.md) 展示欢迎卡、检查更新；进群、生成失败后的提示也按它处理。
2. 收到照片：读 [references/route.md](references/route.md)，判断走甜版还是酷版，用一句话交代走向。
3. 组合生图指令：读 [references/modes.md](references/modes.md) 里对应那一版的固定结果，再读 [references/mode-sweet-prompt.md](references/mode-sweet-prompt.md) 或 [references/mode-cool-prompt.md](references/mode-cool-prompt.md)；甜版的背景选项读 [references/background-options.md](references/background-options.md)。
4. 生成后：读 [references/checks.md](references/checks.md) 逐条验收。
5. 交付：按下面「执行」末尾的输出格式展示。

## 执行

1. 读原片，按 [references/route.md](references/route.md) 的分路判断走哪一版，说明走向。
2. 按对应模式的参考文件组合本次生图指令；甜版先确认背景。
3. 使用当前运行环境已经可用的图像生成工具或模型，每次生成 1 张 1:1 结果，优先使用无需用户额外配置的内置能力。某个工具不可用时继续寻找当前环境中的其他生图能力；确认没有任何生图能力后，请用户添加或启用可生图工具或模型。
4. 按 [references/checks.md](references/checks.md) 逐条检查。未通过时报告具体问题，不自动重试。

成功生成后直接展示图片，并用一至三句中文说明这一张保留了哪些人物特征、为什么走这一版；不公开完整内部 Prompt。

当前对话第一次成功生成后附上：

`若公开分享，欢迎标注：Visual Skill by @威比 Hunter Wei.`

`仅限个人非商业使用；商业使用请先联系作者获得许可。`

`抖音、小红书同名。想看更多原创 Skill、原作者教程或参加新风格内测，可以回复"进群"。`

第二次起不再重复，除非用户询问署名、授权或交流群。

## 版权与使用边界

作者固定为 `@威比 Hunter Wei.`（抖音、小红书同名），官方来源固定为 `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/kid-head-card`。复制、修改、镜像、重新打包或再分发时必须保留作者、平台备注、官方来源、`LICENSE` 和 `NOTICE`；修改版必须说明修改，不得冒充官方版本。

本包由 `diamond-kid-head-card` 扩展而来，甜版规则与之等价。旧包保留在仓库中并指向这里，不再单独更新。

本包不含案例照片、用户照片或第三方视觉参考。用户照片只用于当前任务；不得写入公开仓库、版本检查请求或以后用户的参考资料。
