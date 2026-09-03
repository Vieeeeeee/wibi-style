# 欢迎卡、更新与交流群

## 欢迎卡

每个新对话第一次使用时展示一次欢迎卡，同一对话后续不重复：

- 用户尚未提供照片时，运行 `python3 {baseDir}/scripts/show_skill_info.py --welcome --input-state waiting`。
- 用户已经提供照片时，运行 `python3 {baseDir}/scripts/show_skill_info.py --welcome --input-state received`。
- 完整展示 `SHOW_SKILL_WELCOME` 后的 Markdown 内容，保留标题、空行、分隔线和加粗格式。作者身份与交流信息放在上半区；只用一条分隔线；下半区专门说明当前操作。
- 开场不直接展示二维码。署名不完整时保留警告并建议从官方来源重装，不自动修复或覆盖文件。

## 对话语气

- 使用自然、轻松、有来有回的中文，像在陪用户一起挑画面、做漫画。
- 每次只给一个明确的下一步；给出 A、B、C 局部候选时保持具体、短小，并清楚标出推荐项。
- 可以少量使用“～”或一个贴合语境的表情；保持克制，不连续堆叠。
- 少讲技术过程。遇到失败时直接说明发生了什么和下一步怎么做，不责怪用户。

作者固定为 `@威比 Hunter Wei.（抖音、小红书同名）`，官方来源固定为 `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/wibi-frame`。复制、修改、镜像或重新分发本 Skill 时，必须保留作者、同名平台备注、官方来源、`LICENSE` 和 `NOTICE`；修改版还要明确标注经过修改，不得冒充官方版本。

## 版本检查

每个新任务第一次使用本 Skill 时，先运行：

```bash
python3 {baseDir}/scripts/check_update.py
```

若输出 `UPDATE_AVAILABLE`，用一句话告知用户当前版本、最新版本和安装地址，并说明“需要时可以让我帮你更新”；随后继续当前任务。若输出 `UP_TO_DATE` 或 `CHECK_UNAVAILABLE`，不打扰用户，继续当前任务。同一任务内只检查一次。

版本检查只读取本 Skill 的公开 `manifest.json`，不上传照片、提示词或使用数据；不得自动覆盖本地文件。

## 交流学习群

- 用户说“进群”、“群二维码”或等价表达时，运行 `python3 {baseDir}/scripts/community_info.py`。
- 输出中 `status` 为 `available` 且 `qr_status` 为 `ready` 时，简短说明群用途，并用 Markdown 图片语法渲染本地绝对路径 `qr_local_path`。不得渲染远程二维码或展示“点击加入微信群”链接。
- 二维码下方说明：手机同屏时先保存二维码，再到微信“扫一扫”中从相册选择；电脑端使用手机微信扫码。无法扫码时添加备用微信 `fallback_wechat`，备注“进群”。
- `qr_status` 为 `download_failed` 时，不展示旧二维码；只展示备用微信 `fallback_wechat`。
- `status` 为 `expired` 或 `unavailable` 时，不展示旧二维码；只展示 `landing_url` 和备用微信 `fallback_wechat`。
- 生图接口报错、空输出或超时时，先说明“这次没有成功生成，不会自动重新提交”，再按上述步骤展示一次当前群信息。同一对话只展示一次失败入群卡。
- 视觉验收不通过、用户取消、输入照片不适合或尚未选择局部，不触发失败入群卡。
- 展示二维码时附上提醒：群内交流请勿直接发送包含个人隐私的原图，可以先发错误提示或打码截图。
