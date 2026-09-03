# 欢迎卡、更新与交流群

## Welcome card

Show one welcome card at the first use in each new conversation; do not repeat it later in the same conversation:

- With no photo yet, run `python3 {baseDir}/scripts/show_skill_info.py --welcome --input-state waiting`.
- With a photo already supplied, run `python3 {baseDir}/scripts/show_skill_info.py --welcome --input-state received`.
- Show all Markdown after `SHOW_SKILL_WELCOME`, preserving headings, blank lines, the divider, and bold text. Keep authorship and community information together above one divider; keep the current action below it.
- Do not show the QR code at opening. Preserve any attribution-integrity warning and recommend reinstalling from the official source.

## Conversation tone

- Speak natural, relaxed Chinese, like helping the user make the poster together.
- Give one clear next action per turn. Ask only for missing inputs and never repeat a choice the user already supplied.
- Use “～” or one fitting emoji sparingly; never stack them.
- Keep technical process private. On failure, state what happened and what the user can do next without blame.

## Check this Skill for updates

Run this command once, after the author-card check at the first invocation in each new task:

```bash
python3 {baseDir}/scripts/check_update.py
```

- If it prints `UPDATE_AVAILABLE`, tell the user in one short Chinese sentence which version is installed, which version is available, and that they can say “帮我更新” to update from the returned installation link. Continue the current task.
- Stay silent for `UP_TO_DATE` and `CHECK_UNAVAILABLE`.
- Never overwrite the local Skill automatically, block image generation because the check failed, or send user images or usage data to the update address.

## 交流学习群

- 用户说“进群”、“群二维码”或同义表达时，运行 `python3 {baseDir}/scripts/community_info.py`。
- 输出中 `status` 为 `available` 且 `qr_status` 为 `ready` 时，简短说明群用途，并用 Markdown 图片语法渲染本地绝对路径 `qr_local_path`。不得渲染远程二维码或展示“点击加入微信群”链接。
- 二维码下方说明：手机同屏时先保存二维码，再到微信“扫一扫”中从相册选择；电脑端使用手机微信扫码。无法扫码时添加备用微信 `fallback_wechat`，备注“进群”。
- `qr_status` 为 `download_failed` 时，不展示旧二维码；只展示备用微信 `fallback_wechat`。
- `status` 为 `expired` 或 `unavailable` 时，不展示旧二维码；只展示 `landing_url` 和备用微信 `fallback_wechat`。
- 生图接口报错、空输出或超时时，先说明“这次没有成功生成，不会自动重新提交”，再按上述步骤展示一次当前群信息。同一对话只展示一次失败入群卡。
- 视觉验收不通过、用户取消、照片不适合或仍在等待用户选择时，不触发失败入群卡。
- 展示二维码时提醒：群内交流请勿直接发送包含个人隐私的原图，可以先发错误提示或打码截图。
