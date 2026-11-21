# 四平台搜索下拉词 Skill 统一入口

闲鱼、小红书、抖音、淘宝四个项目集中导航和安装。**保留独立源码仓库、项目名称和原链接**；本仓库提供目录与固定版本安装器，分别维护平台适配，不把四个平台当成统一接口。

| 平台 | 开源项目 | 安装后的 Skill 名 | 本次核对范围 |
| --- | --- | --- | --- |
| 闲鱼 | [xianyu-keyword-skill](https://github.com/dstmg/xianyu-keyword-skill) | `xianyu-keyword-skill` | 2026-11-21完成三词根真实两层采集与报告验收 |
| 小红书 | [xiaohongshu-keyword-skill](https://github.com/dstmg/xiaohongshu-keyword-skill) | `yao-geo-xiaohongshu` | 本次核对源码、许可证和固定版本下载；未重跑平台采集 |
| 抖音 | [douyin-keyword-skill](https://github.com/dstmg/douyin-keyword-skill) | `yao-geo-douyin` | 本次核对源码、许可证和固定版本下载；未重跑平台采集 |

| 淘宝 | [taobao-keyword-skill](https://github.com/dstmg/taobao-keyword-skill) | `taobao-keyword-skill` | 仅单词真实验证10条；默认人工输入，完整第二层未验收 |

## 各平台流程

闲鱼、小红书、抖音按各自Skill处理两层联想、逐次截图与JSON、路径和唯一词、Excel与持续研究报告。

**淘宝采用独立的保守流程**：默认用户手动输入，Agent观察留证及离线导出。明确授权的单词模式一批只查询一个词；两层计划只生成pending候选，不自动访问、换词或重试。它尚未通过完整第二层实测，不能按其他平台的批量流程运行。

需要支持浏览器操作和 SKILL.md 的 AI Agent、已登录的目标平台浏览器、Python 及各项目依赖。推荐按 [BrowserSkill官方安装指南](https://github.com/Tencent/BrowserSkill/blob/main/AGENT_INSTALL.md)准备 CLI、扩展和Agent技能；本仓库不分发第三方浏览器组件，不替用户登录。

下拉词不代表搜索量、热度、成交量或真实商业价值；路径多也不能证明需求更大。相同查询可以复用采集证据，相同词的不同来源路径仍应保留。遇登录、验证码或限制立即停止，由用户处理。

<a id="一次下载三个固定版本"></a>

## 一次下载四个固定版本

```powershell
git clone https://github.com/dstmg/search-keyword-skills.git
cd search-keyword-skills
python install.py --target "$env:USERPROFILE/.codex/skills"
```

若 Codex 使用自定义 CODEX_HOME，改为其 skills 目录。只装闲鱼可加 `--platform xianyu`；其他取值为 xiaohongshu、douyin、taobao。只装淘宝可用 `--platform taobao`。已有同名目录时会拒绝覆盖；不要为了安装删除用户自定义内容。

安装器使用 [catalog.json](catalog.json) 的40位 commit固定版本，检查提交、Skill名与MIT许可后复制，不改已有安装。安装后按各项目 requirements.txt 安装依赖，再重新打开Agent会话。离线环境可从各项目下载ZIP、解压并按其README导入；ZIP的主分支可能晚于此处固定版本。

宿主自动发现路径可能不同，其他Agent按其官方Skill目录导入。本次固定版本下载和Skill文件检查通过，不代表已经验证每个宿主的发现、执行或全部平台登录状态。

## 使用与持续积累

按平台调用安装后的Skill，例如：

> 用 $xianyu-keyword-skill 采集“万相台、workbuddy”的完整两层下拉词，私有保存截图和JSON，导出Excel并追加到我的闲鱼研究项目，完成有来源的运营解读。

小红书、抖音改用上表对应Skill名。四个平台分别使用各自页面适配、JSON格式和研究目录；不要混用选择器或把跨平台批次强行导入同一报告。需要跨平台比较时，另做清楚标注平台与采集时间的分析，不能直接把下拉数量当需求排名。

原始截图、研究批次和账号信息默认私有。公开素材先人工脱敏并核查来源授权；这里没有收录真实账号截图或真实采集包。

淘宝示例：

> 用 $taobao-keyword-skill 观察我手动输入的词，私有留证并生成报告；不要自动换词或扩层，出现验证或风险提示立即停止。

## 闲鱼本次结果

2026-11-21 Chrome + BrowserSkill 0.5.0：电商、万相台、workbuddy 共22次查询、47条来源路径、42个去重词、24张私有截图、0待采集。“电商”本次无下拉，不代表没有需求。详情见[闲鱼验证记录](https://github.com/dstmg/xianyu-keyword-skill/blob/main/reports/validation.md)。

## 许可与维护

本入口及安装器采用[MIT](LICENSE)。四个项目分别保留各自许可证与 Yao、dstmg 署名，版本和地址在 catalog.json 明列。安装器从原仓库下载源码，许可证不会授予平台截图、商标或第三方课程的分发权。原项目的更新在原仓库维护；本入口通过更新固定 commit来选择后续版本，不在运行时自动追最新版本。
