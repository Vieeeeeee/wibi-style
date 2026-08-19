# Wibi Style · 童年大头卡贴

**Visual Skill by @威比 Hunter Wei.**
抖音、小红书同名

把照片做成儿童纯大头卡贴：只保留一颗完整的头，干净悬浮在纯色底上，边缘像一张精心切割的贴纸。

进门先读图，自动分两条路：

- **儿童老照片** → 甜版·钻牙萌娃。重拍式重建成明亮可爱的现代儿童棚拍，原片明显露齿时把每颗牙面密铺满钻；五种背景可选，默认白色。
- **当代自拍** → 酷版·童年酷照。把本人反推成 5–8 岁的样子，骨相五官照着你走，配上潮童装饰；男孩走墨镜银饰冷色水钻，女孩走糖果色小花亮片。

判断完直接开工并告诉你走的哪一版，随时可以让它换另一版。

<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/kid-head-card-v1.0.1/docs/kid-head-card/examples/example-01.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/kid-head-card-v1.0.1/docs/kid-head-card/examples/example-02.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/kid-head-card-v1.0.1/docs/kid-head-card/examples/example-03.png" width="30%" />
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/kid-head-card-v1.0.1/docs/kid-head-card/examples/example-04.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/kid-head-card-v1.0.1/docs/kid-head-card/examples/example-05.png" width="30%" />
  <img src="https://raw.githubusercontent.com/Vieeeeeee/wibi-style/kid-head-card-v1.0.1/docs/kid-head-card/examples/example-06.png" width="30%" />
</p>

上排为甜版·钻牙萌娃，下排为酷版·童年酷照。

## 安装

```text
请安装这个 Skill：
https://github.com/Vieeeeeee/wibi-style/tree/main/skills/kid-head-card
```

安装器只下载这一款 Skill。装完不用做别的，第一次调用时它会自己打招呼并告诉你下一步。

## 使用

发一张照片，然后：

```text
使用 $kid-head-card 处理这张照片。
```

不用自己说要哪一版，它会先看图再告诉你。想指定也可以直接说「走钻牙萌娃」或「走童年酷照」。

只有一种情况它会先问你：清晰的当代照片但主体本来就是小孩——这时两条路都成立，它会给你两个选项。

## 适合什么照片

- 甜版：单人儿童老照片，正面或轻微侧脸，脸和头发大致可辨；褪色、颗粒、轻微折痕都能用。
- 酷版：单人正脸或近正脸的当代自拍，手机原图即可；戴眼镜、化妆、染发都行，会先剥掉再重建。
- 两版都不适合：侧脸过大、遮挡大半张脸、多人合影、严重模糊。

## 关于旧版

本包由 `diamond-kid-head-card` 扩展而来，甜版规则与之等价。旧包保留在仓库中并指向这里，不再单独更新。已经装了旧包的话，装上本包即可，两者可以并存。

## 更新

每次使用时会只读查询公开 `manifest.json`。发现新版只提示当前版、最新版和安装地址，不自动覆盖本地文件，不上传你的照片或使用数据；网络不可用时不影响生图。

## 交流学习群

回复「进群」获取当前群二维码。群内交流请不要直接发送包含个人隐私的原图，可以先发错误提示或打码截图。

## 授权

作者固定为 `@威比 Hunter Wei.`（抖音、小红书同名），官方来源固定为 `https://github.com/Vieeeeeee/wibi-style/tree/main/skills/kid-head-card`。

仅限个人非商业使用；商业使用请先联系作者获得许可。公开分享时欢迎标注：`Visual Skill by @威比 Hunter Wei.`

复制、修改、镜像、重新打包或再分发时必须保留作者、平台备注、官方来源、`LICENSE` 和 `NOTICE`；修改版必须说明修改，不得冒充官方版本。

本包不含案例照片、用户照片或第三方视觉参考。你的照片只用于当次任务。
