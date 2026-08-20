# 来源与版权

| 内容 | 来源 | 版权状态 |
| --- | --- | --- |
| `SKILL.md`、`references/style-prompt.md` | 三联情绪模特卡项目的真实案例迭代：17 轮 Prompt 版本（v1–v17），在 4 位测试对象（女生、戴眼镜男生、卷发男生、短发男生）上反复验证 | © 2026 @威比 Hunter Wei.，按本包 LICENSE 授权 |
| `assets/brand/logo_wibi_skill.png` | 作者原创设计并生成的 WIBI 品牌标记（WIBI 半调网点 + skill 手写体，SHA-256 见 `manifest.json.rights.original_assets`），只在出图后由排版脚本贴上，不参与生成、不是风格参考图 | © 2026 @威比 Hunter Wei.，按本包 LICENSE 授权 |
| `scripts/compose_triptych_card.py` | 为本项目原创编写的排版脚本，负责识别生成图中的照片区域、重排到目标画幅、贴上品牌标记素材并按背景明暗自动换色，支持纸白/深炭黑两套背景预设 | © 2026 @威比 Hunter Wei.，按本包 LICENSE 授权 |
| `scripts/check_update.py` | 为 Wibi Style 独立编写的无遥测更新检查 | © 2026 @威比 Hunter Wei.，按本包 LICENSE 授权 |
| `scripts/show_skill_info.py` | 安装后作者卡、欢迎卡与署名完整性检查 | © 2026 @威比 Hunter Wei.，按本包 LICENSE 授权 |
| `scripts/community_info.py` | 只读获取官方仓库的当前交流群入口，不上传照片或使用数据 | © 2026 @威比 Hunter Wei.，按本包 LICENSE 授权 |
| `NOTICE` | 作者、同名平台和官方来源声明 | © 2026 @威比 Hunter Wei.，必须随再分发副本保留 |

本包不包含案例原图、用户照片，也不携带任何随包分发的视觉参考图——生成阶段完全依赖 `references/style-prompt.md` 中的文字规则驱动，`manifest.json` 的 `references` 字段为空数组。随包唯一的图片资产是作者原创的品牌标记 `assets/brand/logo_wibi_skill.png`，只在生成之后的排版环节使用，见上表。

运行时上传的照片只用于用户当次任务；本 Skill 不把照片写入 GitHub，也不把照片发送给版本检查地址。

仓库 `docs/flash-triptych/examples/` 展示六张实际生成结果，只供 README 展示风格效果，不随单款 Skill 安装；这六张已从本包版本 `1.1.0` 的真实验收结果中选定（见 README），`manifest.json` 的 `gallery.status` 标记为 `ready_pending_publish`，正式推送仓库前的最后一步是把本地已选定的图片上传到 `docs/flash-triptych/examples/`。

作者：`@威比 Hunter Wei.`（抖音、小红书同名）。官方来源：`https://github.com/Vieeeeeee/wibi-style/tree/main/skills/flash-triptych`。
