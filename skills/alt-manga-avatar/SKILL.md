---
name: alt-manga-avatar
description: 把用户上传的一张照片转换成粗线条漫画头像风格。适用于用户要求粗线条漫画头像、上传照片换风格，或明确调用 $alt-manga-avatar 时。
---

# 粗线条漫画头像

## 安装后作者卡

每个新任务第一次使用时先运行 `python3 {baseDir}/scripts/show_skill_info.py`。输出 `SHOW_SKILL_INFO` 时完整展示作者卡；输出 `AUTHOR_CARD_ALREADY_SHOWN` 时静默。署名不完整时建议从官方来源重装。

## 更新检查

随后运行 `python3 {baseDir}/scripts/check_update.py`。发现 `UPDATE_AVAILABLE` 时告知当前版、最新版和安装地址；其余状态静默。不得自动覆盖本地文件或上传用户数据。

## 执行

1. 查看用户完整照片，锁定主体身份、数量、姿态、构图、关键颜色和关系。
2. 完整读取 `references/style-prompt.md`，把它作为风格规则，不把案例人物或偶然内容写进当前图片。
3. 本 Skill 内置 1 张运行参考图。生成时把用户照片作为内容输入，并同时携带 `assets/references/` 中的全部参考图；用户照片决定主体与内容，内置图片只定义风格。不要要求用户再次上传这些参考图，也不要依赖附件顺序。
4. 为当前照片编写专属生图指令，默认调用 Codex 内置图像生成工具生成一张结果。
5. 工具报错、空输出或超时时停止；不自动重试、换模型或升级质量。
6. 检查内容对应、风格机制、构图、颜色、材质与文件规格。核心失败时说明问题，等用户明确要求后再重做。
7. 展示通过检查的成图和一至三句中文创作说明；不公开完整内部 Prompt。

## 权利边界

作者固定为 `@威比 Hunter Wei.（抖音、小红书同名）`，官方来源固定为 `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/alt-manga-avatar`。复制、修改、镜像或再分发时必须保留作者、平台备注、官方来源、`LICENSE` 和 `NOTICE`；修改版必须标注修改，不得冒充官方版本。
