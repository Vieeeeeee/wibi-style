---
name: personalized-print-ticket
description: 把一张人物、风景、建筑、空间、食物或日常随拍制作成中英混排的定制印刷票根。先根据照片内容动态询问，再从四套票根 Prompt 中选一套；代码产出准确文字和构图的排版导引图，然后将导引图、用户照片和印刷风格参考共同交给图像模型，生成字形残缺、线条波动、纸墨颗粒更自然的完整票根。用于定制票根、电影票风格照片卡、旅行纪念票或日常瞬间票据。
---

# Wibi Style · 定制印刷票根

把用户照片变成一张完整的文化票据。代码是构图骨架和精确文字的导引，图像模型负责最终字形、线条、照片制版、纸张和油墨的统一印刷质感。

## 运行路由

1. 新对话第一次使用时按 [references/community.md](references/community.md) 展示欢迎卡并检查更新。
2. 收到照片后读 [references/intake.md](references/intake.md)，先分析画面，再决定是否需要询问。
3. 选定一种图像方式：`faithful-print` 忠实印刷化，或 `artistic-redraw` 艺术化重绘。一张票只用其中一种；选艺术化重绘时读 [references/artistic-redraw.md](references/artistic-redraw.md)。
4. 选定一套票根风格，读 [references/presets.md](references/presets.md)。用户没选时给出一个有理由的推荐；用户说“自动”或“给我惊喜”时直接选定。
5. 按 [references/ticket-data.md](references/ticket-data.md) 组织一份通用 JSON；脚本依据预设把字段映射到对应文字槽，并生成只表达位置、字量和层级的中性导引图：

```bash
python3 {baseDir}/scripts/compose_ticket.py \
  --photo 照片.png \
  --data 票根信息.json \
  --preset orbit-orange \
  --image-mode faithful-print \
  --out 排版导引图.png
```

6. 读选中的一份 [references/prompts](references/prompts) 完整 Prompt，再用 `scripts/compile_prompt.py` 注入照片分析和逐字文案。
7. 先用 `view_image` 查看选中的原始票根，再调用当前环境可用的图片生成工具走编辑路径。原始票根是编辑底图，保留其比例、排版、字形性格、线条和纸墨质感；用户内容照片只替换底图右侧原有图像；排版导引图只定义新文字和必要的区块适配。不使用“图一/图二”作为指令。
8. 每次只调用一次图片生成。按 [references/checks.md](references/checks.md) 检查身份、文字、构图、色版和整体印刷质感；不做局部修字、脚本覆盖或自动重试。未通过时保留本次结果并说明具体失败项，用户明确要求再试才开始新一轮。

## 四套风格

- `orbit-orange`：暖白纸，黑色照片版，橙色标注和信息线，重型文化活动票。
- `blossom-red`：淡粉纸与朱红单色版，超大标题和花形冲孔记号，情绪更轻松。
- `sketch-black`：暖白纸与黑色影印版，线框标题、手绘线稿与克制的电影档案感。
- `signal-coral`：珊瑚红纸与近黑墨，宽幅标题、衬线短句和高密度照片，情绪最强。

## 不变项

- 默认画布 `2048×769`，右侧图窗约占 `28%`；用户要求新尺寸时保持同一结构比例。
- 排版导引图是文字内容、位置和层级的权威；四种预设使用各自的字段路由，不强迫不同参考票容纳相同数量的文字层级。
- 排版导引图使用 Skill 内置通用字体，只表达字量、位置和层级；最终字形、年代感与印刷误差由图像模型根据当前预设设计。点阵票号由脚本从字形采样绘制。
- 自动填写时可以创作标题、短句和票务隐喻，不把无法确认的真实人名、精确地点或历史信息写成事实。
- 保留照片的主体、关系、姿态和场景锚点；裁切时优先保住人脸、建筑轮廓、食物主体或场景地标。
- 参考图只定义四套印刷逻辑，不复制其片名、引语、影片画面、等级标识、影院名或票号。
- 每次只生成一张成品。检查未通过时说明问题，重新生成图版需要用户确认。

## 交付

先展示成品，再用一到两句说明选用的风格、图像方式和保留的身份锚点。同时交付最终 PNG、信息 JSON 和本次完整 Prompt；排版导引图作为过程资产保留。

当前对话第一次成功生成后，附上：

`若公开分享，欢迎标注：Visual Skill by @威比 Hunter Wei.`

`仅限个人非商业使用；商业使用请先联系作者获得许可。`

`抖音、小红书同名。想看更多原创 Skill、原作者教程或参加新风格内测，可以回复“进群”。`

同一对话从第二次成功生成起只展示成品和简短创作说明；用户再次询问署名、授权或社群时按 [references/community.md](references/community.md) 处理。

## 作者与素材边界

- 原创动态规则、排版脚本与 Prompt 适配：`© 2026 @威比 Hunter Wei.`
- 作者备注：`抖音、小红书同名`。
- 官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/personalized-print-ticket`。
- 用户照片只用于当前任务，不进入安装包、公开仓库或后续用户的参考集。
- 四张运行参考由项目作者选择进入公开包，用于四套票根的版式、字形和纸墨职责；来源与 SHA-256 见 [SOURCES.md](SOURCES.md)。
- 再分发时保留作者、平台备注、官方来源、`LICENSE` 与 `NOTICE`。
