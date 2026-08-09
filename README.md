# Wibi Style

由 `@威比 Hunter Wei.` 制作和维护的视觉风格 Skill 仓库。

每个风格独立放在 `skills/<skill-name>/` 中，包含可直接读取的 `SKILL.md`、必要的构图模板和参考素材。后续新增风格继续沿用同一目录结构，互不混放。

仓库内的 `SKILL.md` 使用英文编写，以减少歧义和重复；Skill 实际运行时默认使用中文与用户沟通。

## 当前风格

| Skill | 说明 | 目录 |
| --- | --- | --- |
| `wibi-frame` | 先给出三个局部文字候选，用户选择后生成带自然越框与框内外同色融合的复古平面漫画特写 | [`skills/wibi-frame/`](skills/wibi-frame/) |

## 安装

将需要的风格文件夹完整复制到 Codex Skills 目录：

```bash
cp -R skills/wibi-frame ~/.codex/skills/
```

重新启动 Codex 后，可以直接说：

```text
使用 $wibi-frame 处理这张照片
```

## 使用与署名

若公开分享生成结果，欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

本仓库中的原创 Skill 逻辑与构图模板仅限个人非商业使用；商业使用请先联系作者获得许可。随 Skill 提供的参考图仅用于风格研究，其原始作品权利归各自权利人所有。
