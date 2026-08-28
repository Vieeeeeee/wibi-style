#!/usr/bin/env python3
"""Draw a compatible animal-office poster brief using only the standard library."""

from __future__ import annotations

import argparse
import json
import random
import secrets


ANIMALS = {
    "paws": ["猫", "浣熊", "水豚", "兔子", "松鼠", "熊猫", "熊"],
    "grasping": ["猴子", "猩猩", "树懒"],
    "large_quadruped": ["牛", "马", "驴", "羊驼", "山羊", "鹿"],
    "bird": ["鹅", "鸭", "鸡", "鸽子", "猫头鹰", "鹈鹕"],
    "tentacles": ["章鱼"],
}

MOODS = [
    "周一宕机",
    "假装专业",
    "麻木但礼貌",
    "续命失败",
    "临下班来活",
    "指标发疯",
    "开会失焦",
    "摸鱼被抓",
]

MOOD_COPY = {
    "周一宕机": ["启动仍在继续", "精神暂未响应", "今日缓慢加载"],
    "假装专业": ["理解进行中", "结论暂时保留", "语气保持肯定"],
    "麻木但礼貌": ["情绪保持稳定", "礼貌继续在线", "意见稍后补充"],
    "续命失败": ["精神待充值", "状态仍未恢复", "请稍后再问"],
    "临下班来活": ["新任务已送达", "下班暂缓执行", "截止时间很近"],
    "指标发疯": ["目标继续上升", "数字保持活跃", "压力正在同步"],
    "开会失焦": ["重点已经飘走", "理解仍在路上", "会议继续进行"],
    "摸鱼被抓": ["页面切换失败", "工作突然恢复", "状态立刻正常"],
}

MOOD_KEYWORD_COPY = [
    (("懂", "听", "理解"), ["理解进行中", "重点正在消化", "问题暂不发言"]),
    (("困", "睡", "累"), ["睡意正在上升", "精神保持离线", "状态缓慢恢复"]),
    (("急", "赶", "迟"), ["时间正在减少", "步伐保持镇定", "任务优先处理"]),
    (("崩", "疯", "压力"), ["压力正在同步", "情绪暂时稳定", "问题继续增加"]),
    (("摸鱼", "偷懒"), ["页面切换失败", "工作突然恢复", "状态立刻正常"]),
    (("麻木", "礼貌"), ["情绪保持稳定", "礼貌继续在线", "意见稍后补充"]),
    (("咖啡", "续命"), ["精神待充值", "状态仍未恢复", "请稍后再问"]),
    (("下班", "来活"), ["新任务已送达", "下班暂缓执行", "截止时间很近"]),
]

AUXILIARY_COPY = [
    "今日待办",
    "任务进行中",
    "稍后回复",
    "继续跟进",
    "保持在线",
    "进度同步",
    "结论待定",
    "等待确认",
    "备注已更新",
    "优先处理",
    "反馈已收到",
    "今日有效",
]

MICRO_COPY = [
    "状态栏",
    "进度栏",
    "备注栏",
    "待办栏",
    "观察记录",
    "任务清单",
    "本日进度",
    "工作样本",
]

COPY_COUNTS = {
    "headline-photo": {"core": 5, "auxiliary": 5, "micro": 3},
    "full-bleed-editorial": {"core": 5, "auxiliary": 6, "micro": 4},
    "cutout-motion": {"core": 5, "auxiliary": 4, "micro": 2},
}

SCENES = {
    "spreadsheet": {
        "label": "表格工位",
        "families": ["paws", "grasping", "bird", "tentacles"],
        "layout": "headline-photo",
        "action": "守在电脑前盯住一张密集表格，屏幕里有几格醒目的红色提示，姿态像已经看了很久仍在假装计算",
        "headlines": ["表格又活了", "数据正在渡劫", "今天也很会算"],
        "side_copy": ["单元格观察", "任务加载中", "公式保持沉默"],
    },
    "meeting": {
        "label": "周会现场",
        "families": ["paws", "grasping", "large_quadruped", "bird", "tentacles", "other"],
        "layout": "full-bleed-editorial",
        "action": "处在会议桌最显眼的位置，认真望向发言方向，面前只有一页没有看懂的会议资料",
        "headlines": ["收到等于没懂", "会开完了事呢", "重点我已错过"],
        "side_copy": ["会议观察", "重点已错过", "发言保持简短"],
    },
    "coffee": {
        "label": "咖啡续命",
        "families": ["paws", "grasping", "bird", "tentacles"],
        "layout": "headline-photo",
        "action": "守着办公室咖啡机和一只白色杯子，正以符合自身身体结构的方式等待这杯咖啡恢复工作能力",
        "headlines": ["咖啡续命失败", "先活着再上班", "这杯不够救我"],
        "side_copy": ["续命申请", "精神待充值", "浓度仍然不够"],
    },
    "printer": {
        "label": "打印机卡纸",
        "families": ["paws", "grasping", "bird", "tentacles"],
        "layout": "headline-photo",
        "action": "与一台吐出半截纸的打印机僵持，正用嘴、爪、翅膀或触手中真正拥有的部位处理卡纸",
        "headlines": ["它又卡住了", "纸比我先崩", "设备情绪稳定"],
        "side_copy": ["设备观察", "纸张拒绝配合", "稍后仍要再试"],
    },
    "turnstile": {
        "label": "门禁冲刺",
        "families": ["large_quadruped", "bird", "paws", "other"],
        "layout": "cutout-motion",
        "action": "正赶向办公室闸机或打卡机，身体朝前形成明确运动方向，工牌轻微晃动",
        "headlines": ["又迟到了", "打卡正在冲刺", "门禁认识我吗"],
        "side_copy": ["打卡记录", "通道即将关闭", "步伐保持镇定"],
    },
    "review": {
        "label": "绩效述职",
        "families": ["paws", "grasping", "large_quadruped", "bird", "tentacles", "other"],
        "layout": "full-bleed-editorial",
        "action": "面对一份绩效表、投影或资料册接受认真审视，姿态克制，眼神已经开始游离",
        "headlines": ["述职像在渡劫", "绩效正在加载", "优点稍后补充"],
        "side_copy": ["绩效观察", "优点正在整理", "表达保持积极"],
    },
    "overtime": {
        "label": "深夜加班",
        "families": ["paws", "grasping", "large_quadruped", "bird", "tentacles", "other"],
        "layout": "headline-photo",
        "action": "独自守着发光的电脑屏幕，周围工位已经空了，只有荧光灯和桌面文件还醒着",
        "headlines": ["今晚别睡了", "下班只是传说", "夜班正在续费"],
        "side_copy": ["夜班记录", "工位仍然在线", "睡意暂不受理"],
    },
    "presentation": {
        "label": "KPI 汇报",
        "families": ["paws", "grasping", "large_quadruped", "bird", "tentacles", "other"],
        "layout": "full-bleed-editorial",
        "action": "位于投影或白板旁，以符合自身身体结构的姿态展示一组很难解释的数据",
        "headlines": ["这页谁做的", "数据很有精神", "KPI自由生长"],
        "side_copy": ["汇报现场", "趋势保持想象", "问题稍后回答"],
    },
    "reception": {
        "label": "前台接线",
        "families": ["paws", "grasping", "bird", "tentacles"],
        "layout": "full-bleed-editorial",
        "action": "守在前台电话、访客本和接待台旁，正在处理一件自己也不清楚该转给谁的事情",
        "headlines": ["您好我也不会", "请稍等我先慌", "工位无人接听"],
        "side_copy": ["接线记录", "正在寻找同事", "问题暂未归属"],
    },
    "elevator": {
        "label": "电梯偶遇",
        "families": ["paws", "grasping", "large_quadruped", "bird", "other"],
        "layout": "cutout-motion",
        "action": "带着工牌或一份薄文件等在电梯门口，和旁边空荡的走廊形成安静又尴尬的停顿",
        "headlines": ["别聊工作好吗", "电梯还没到", "假装没有看见"],
        "side_copy": ["走廊观察", "话题正在回避", "楼层仍在上升"],
    },
}

ALIASES = {
    "表格": "spreadsheet",
    "工位": "spreadsheet",
    "电脑": "spreadsheet",
    "周会": "meeting",
    "会议": "meeting",
    "咖啡": "coffee",
    "茶水间": "coffee",
    "打印": "printer",
    "卡纸": "printer",
    "闸机": "turnstile",
    "门禁": "turnstile",
    "打卡": "turnstile",
    "述职": "review",
    "绩效": "review",
    "加班": "overtime",
    "深夜": "overtime",
    "汇报": "presentation",
    "KPI": "presentation",
    "前台": "reception",
    "接线": "reception",
    "电梯": "elevator",
}


def animal_family(animal: str) -> str:
    for family, animals in ANIMALS.items():
        if animal in animals:
            return family
    return "other"


def resolve_scene(value: str | None) -> str | None:
    if not value:
        return None
    if value in SCENES:
        return value
    for alias, scene_id in ALIASES.items():
        if alias.lower() in value.lower():
            return scene_id
    return "custom"


def custom_layout(scene: str) -> str:
    if any(word in scene for word in ("闸机", "门禁", "走廊", "电梯", "赶", "冲")):
        return "cutout-motion"
    if any(word in scene for word in ("会议", "周会", "述职", "汇报", "前台", "路演")):
        return "full-bleed-editorial"
    return "headline-photo"


def choose_animal(rng: random.Random, scene_id: str) -> tuple[str, str]:
    scene = SCENES[scene_id]
    family = rng.choice(scene["families"])
    if family == "other":
        family = rng.choice(list(ANIMALS))
    animal = rng.choice(ANIMALS[family])
    return animal, family


def choose_scene(rng: random.Random, family: str) -> str:
    candidates = [
        scene_id
        for scene_id, scene in SCENES.items()
        if family in scene["families"] or "other" in scene["families"]
    ]
    return rng.choice(candidates)


def unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def select_copy(
    rng: random.Random,
    layout: str,
    core: list[str],
    mood: str,
) -> dict[str, list[str]]:
    counts = COPY_COUNTS[layout]
    core_copy = unique(core)[: counts["core"]]
    while len(core_copy) < counts["core"]:
        for fallback in ("今日状态", "任务进行中", "稍后回复", "继续跟进", "保持在线"):
            if fallback not in core_copy:
                core_copy.append(fallback)
                break

    matched_mood_copy = MOOD_COPY.get(mood, [])
    if not matched_mood_copy:
        for keywords, candidates in MOOD_KEYWORD_COPY:
            if any(keyword in mood for keyword in keywords):
                matched_mood_copy = candidates
                break
    mood_candidates = [value for value in matched_mood_copy if value not in core_copy]
    common_candidates = [value for value in AUXILIARY_COPY if value not in core_copy]
    rng.shuffle(mood_candidates)
    rng.shuffle(common_candidates)
    auxiliary_copy = unique(mood_candidates[:2] + common_candidates)[: counts["auxiliary"]]

    micro_candidates = [value for value in MICRO_COPY if value not in core_copy + auxiliary_copy]
    rng.shuffle(micro_candidates)
    micro_copy = micro_candidates[: counts["micro"]]
    return {
        "core": core_copy,
        "auxiliary": auxiliary_copy,
        "micro": micro_copy,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Draw one Y2K office-animal poster brief")
    parser.add_argument("--animal")
    parser.add_argument("--scene")
    parser.add_argument("--mood")
    parser.add_argument("--headline")
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    seed = args.seed if args.seed is not None else secrets.randbits(63)
    rng = random.Random(seed)
    scene_id = resolve_scene(args.scene)

    if args.animal:
        animal = args.animal.strip()
        family = animal_family(animal)
        if scene_id is None:
            scene_id = choose_scene(rng, family)
    elif scene_id and scene_id != "custom":
        animal, family = choose_animal(rng, scene_id)
    elif scene_id == "custom":
        family = rng.choice(list(ANIMALS))
        animal = rng.choice(ANIMALS[family])
    else:
        scene_id = rng.choice(list(SCENES))
        animal, family = choose_animal(rng, scene_id)

    mood = args.mood.strip() if args.mood else rng.choice(MOODS)

    if scene_id == "custom":
        scene_label = args.scene.strip()
        layout = custom_layout(scene_label)
        action = f"身处“{scene_label}”这个办公室场景，以符合{animal}真实身体结构的方式认真处理眼前工作，动作清楚且只使用它真正拥有的身体部位"
        headline = args.headline.strip() if args.headline else rng.choice(
            ["今天也在上班", "事情正在发生", "先把今天过完"]
        )
        core_copy = ["今日状态", mood, "场景观察", "任务进行中", "稍后继续"]
    else:
        scene = SCENES[scene_id]
        scene_label = scene["label"]
        layout = scene["layout"]
        action = scene["action"]
        headline = args.headline.strip() if args.headline else rng.choice(scene["headlines"])
        core_copy = ["今日状态", mood, *scene["side_copy"]]

    copy_tiers = select_copy(rng, layout, core_copy, mood)
    side_copy = copy_tiers["core"] + copy_tiers["auxiliary"] + copy_tiers["micro"]

    result = {
        "seed": seed,
        "animal": animal,
        "animal_family": family,
        "scene_id": scene_id,
        "scene": scene_label,
        "animal_behavior": action,
        "mood": mood,
        "layout_id": layout,
        "layout": {
            "headline-photo": "上部保留清楚的大标题区，办公室照片从中部向下展开，边注沿桌面、屏幕和动物轮廓组织",
            "full-bleed-editorial": "办公室环境满版铺开，大标题压住顶部，蓝色边注沿画面四周和动物轮廓形成杂志信息框",
            "cutout-motion": "动物动作成为剪贴主体，保留较大暖灰纸白，红描边、箭头和边注强化运动方向",
        }[layout],
        "headline": headline,
        "blue_copy": side_copy,
        "blue_copy_tiers": copy_tiers,
        "copy_density_target": len(side_copy),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
