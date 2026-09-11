# 票根信息数据

排版脚本读取 UTF-8 JSON。用户只提供一份内容，预设负责把字段映射到各自能够容纳的文字槽。

```json
{
  "hero": "夏末未归",
  "title": "STILL OUT IN LATE SUMMER",
  "kicker": "A CITY MEMORY TICKET",
  "subtitle": "风在楼与楼之间穿过",
  "serial": "VIE-0910-1740",
  "memory_mode": "scene-observation",
  "records": [
    {"label": "PLACE", "value": "北向窗边"},
    {"label": "SCENE", "value": "夏末斜阳"},
    {"label": "KEEP", "value": "想留住这束光"},
    {"kind": "graphic", "motif": "sun"}
  ],
  "subject_summary": "一个人在夏末傍晚穿过楼群之间的街道",
  "identity_anchors": ["单人步行", "背景三栋建筑", "右上方低太阳", "深色地面"],
  "scene_facts": ["室外", "傍晚低角度光", "城市街道"],
  "crop_focus": [0.50, 0.45]
}
```

## 填写规则

- `hero`：按 [intake.md 的纪念文字层级](intake.md#纪念文字层级) 生成中文记忆索引。
- `title`：按 Hero 的同一瞬间生成简短英文辅助标题；它在所有预设中保留，但位置由预设决定。
- `kicker` 与 `subtitle`：可选短句。预设没有对应文字槽时自动省略，不挤进其他位置。
- `serial`：不超过二十个英文大写字母、数字和连字符；位置由预设决定。
- `records`：固定四格。前三格使用简短英文 `label` 与中文 `value`；第四格使用 `kind: graphic` 与照片相关的 `motif`。
- `memory_mode`：使用 `fact-archive`、`scene-observation` 或 `personal-memory`。
- `subject_summary`、`identity_anchors` 与 `scene_facts`：约束模型保留照片事实。
- `crop_focus`：0–1 之间的 `[x, y]`，用于把主体保留在右侧窄图窗。

需要精确日期、地点或人物信息时，把它们写入四格记录；不再维护一组固定票务字段。
