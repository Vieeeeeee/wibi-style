# Wibi Style

由 `@威比 Hunter Wei.` 制作和维护的视觉风格 Skill 仓库；抖音、小红书同名。

每个风格独立放在 `skills/<skill-name>/` 中，包含可直接读取的 `SKILL.md`、必要的原创构图模板和支持文件。后续新增风格继续沿用同一目录结构，互不混放。

## 当前风格

| Skill | 说明 | 目录 |
| --- | --- | --- |
| `wibi-frame` | 先给出三个局部文字候选，用户选择后生成带自然越框与框内外同色融合的复古平面漫画特写 | [`skills/wibi-frame/`](skills/wibi-frame/) |
| `electric-blue-halftone-poster` | 把单人人像或宠物大头照做成电光蓝粗网点半调唱片海报 | [`skills/electric-blue-halftone-poster/`](skills/electric-blue-halftone-poster/) |

## 安装

在 Codex 中发送所需风格的独立 GitHub 地址。例如只安装电蓝网点海报：

```text
请安装这个 Skill：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/electric-blue-halftone-poster
```

安装器只下载这个风格目录，不会把其他 Skill 一起下载。推荐在安装指令中同时要求安装代理运行包内 `scripts/show_skill_info.py --always`，这样安装完成后会立即展示作者卡。安装完成后新开一个任务，再直接说：

```text
使用 $electric-blue-halftone-poster 处理这张照片
```

每款新发布的 Skill 都有独立版本清单。每个新任务第一次调用时只查询这一款的远端版本；发现新版才提示，不自动覆盖本地文件，也不上传用户照片或使用数据。

## 使用与署名

若公开分享生成结果，欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

本仓库中的原创 Skill 逻辑、提示词与原创构图模板仅限个人非商业使用；商业使用请先联系作者获得许可。复制、修改、转发、镜像或重新打包某款 Skill 时，必须保留作者、抖音/小红书同名备注、官方来源、`LICENSE` 与 `NOTICE`；修改版必须明确标注经过修改，不得冒充官方版本。每款 Skill 的 `SOURCES.md` 会分别说明本包拥有和不拥有的内容权利。第三方图片公开可见不代表获得再分发许可，未通过版权门的素材不会加入新的公开安装包。
