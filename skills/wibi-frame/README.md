# Wibi 框景漫画

把普通照片里最值得看的局部，做成大面积纯色留白中的复古平面漫画特写。Skill 会先给出三个具体局部供你选择，再完成小框聚焦、自然越框和框内外同色连接。

当前版本：`v1.2.1`

作者：`@威比 Hunter Wei.`（抖音、小红书同名）

## 成图示例

以下均为本 Skill 的实际生成结果，仅展示成图，不包含用户原始照片。

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/wibi-frame-v1.2.1/docs/wibi-frame/examples/example-01.png" alt="面条与筷子局部成图" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/wibi-frame-v1.2.1/docs/wibi-frame/examples/example-02.png" alt="双眼局部成图" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/wibi-frame-v1.2.1/docs/wibi-frame/examples/example-03.png" alt="帽檐与眼神局部成图" width="30%" />
  <br />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/wibi-frame-v1.2.1/docs/wibi-frame/examples/example-04.png" alt="帽子与双手局部成图" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/wibi-frame-v1.2.1/docs/wibi-frame/examples/example-05.png" alt="西瓜与表情局部成图" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/wibi-frame-v1.2.1/docs/wibi-frame/examples/example-06.png" alt="侧脸与香烟局部成图" width="30%" />
</p>

## 安装

在 Codex 中发送：

```text
请安装这个 Skill；安装完成后，运行包内 `scripts/show_skill_info.py --always`，并把输出的 Skill 信息完整展示给我：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/wibi-frame
```

安装器只下载这一款 Skill，不会下载仓库中的其他风格。安装完成后会展示名称、版本、作者、同名平台、官方来源和安装路径；若安装器没有展示，第一次使用时会补展示一次。

旧 `v1.1` 没有更新检查，需要先按上面的地址手动更新一次。从 `v1.2.0` 起，每个新任务第一次使用时会查询这一款有没有新版本；只在发现更新时提醒，不自动覆盖本地文件，也不上传用户照片。

## 使用

上传一张照片后说：

```text
使用 $wibi-frame 处理这张照片
```

Skill 会先给出 A、B、C 三个不同的局部候选并推荐一个。回复选项或说“按推荐来”后，才会开始生成一张结果。批量处理需要你明确授权。

## 适合的照片

- 有清楚眼神、表情、手势或饰品关系的人像；
- 人与杯子、筷子、食物、眼镜等物件发生接触的照片；
- 服饰、腿鞋、珠宝或发型有独特轮廓的照片。

局部关系越具体，成图越有惊喜感。主体太远、严重模糊或看不清接触关系时，Skill 会先指出限制。

## 视觉规格

| 项目 | 规格 |
| --- | --- |
| 比例 | 9:16 竖图 |
| 尺寸 | 1440×2560 像素 |
| 格式 | PNG |
| 画风 | 复古平面漫画、粗轮廓、有限色盘 |
| 构图 | 局部放大、小框留白、自然越框、同色融框 |
| 默认工具 | Codex 内置图片生成工具 |

在线体验更多风格：[威比风格实验室](https://style.abdc.online)

## 使用与授权

原创 Skill 规则与原创构图卡仅限个人非商业使用；商业使用请先联系作者获得许可。复制、修改、转发、镜像或重新打包本 Skill 时，必须完整保留作者、抖音/小红书同名备注、官方仓库地址、`LICENSE` 和 `NOTICE`。公开分享生成结果时欢迎标注：

```text
Visual Skill by @威比 Hunter Wei.
```

本包没有打包 Pinterest 图片、第三方风格参考图、案例原图或用户照片。README 展示的六张成图位于仓库 `docs/`，不随单款 Skill 安装。完整范围见 [`LICENSE`](LICENSE) 与 [`SOURCES.md`](SOURCES.md)。
