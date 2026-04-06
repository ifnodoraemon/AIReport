# AI 关键人物追踪

最后更新：2026-04-06

参考文档：`/home/ifnodoraemon/myreport/AI三巨头博客追踪.md`、`/home/ifnodoraemon/myreport/模型发布追踪.md`、`/home/ifnodoraemon/myreport/MCP-tools-agent-infra追踪.md`

跟踪范围：截至 `2026-04-06` 检索到的 AI 关键人物 `个人官网 / 官方博客 / 公司新闻页 / X`；优先选择能持续释放 `模型路线`、`agent infra`、`开发者生态`、`安全治理`、`world model` 高信号的人

## 目的

这份文件用于：

- 补齐“只看公司，不看关键人物”的信息盲区
- 区分谁在输出 `公司路线信号`，谁在输出 `技术范式信号`
- 把 `X` 纳入快信号层，但不让它替代官网确认
- 建立一份适合长期维护的关键人物名单

## 来源分层

### 一级来源

- `个人官网`
- `公司官方博客`
- `公司 newsroom / press`
- `研究机构官方页面`

这些来源用于确认：

- 真正发布了什么
- 日期是什么
- 是否已经从想法变成正式动作

### 二级来源

- `本人 X`
- `公司官号 X`

这些来源用于捕捉：

- 更早的路线信号
- 新概念和新术语
- 演讲、访谈、招聘、预告

默认规则：

- `官网已确认`：最高优先级
- `X + 官网双确认`：很值得跟
- `仅 X 信号`：可以记录，但要明确标注，避免过度解读

## 当前判断

当前最值得跟的人，不一定是“最有名”的人，而是：

1. 能影响 `frontier model / agent / infra / safety / world model` 主线的人
2. 有稳定公开输出入口的人
3. 其公开动作能直接映射到产品、研究或工程优先级的人

## 推荐追踪名单

### P0：建议周更

| 人物 | 当前角色 | 为什么值得跟 | 最近公开动态 | X 是否值得盯 | 核心信号 | 主要来源 |
|---|---|---|---|---|---|---|
| Sam Altman | OpenAI CEO | 看 `OpenAI` 的顶层路线：模型、平台、算力、商业化如何一起推进 | `2026-03-31` OpenAI 宣布新一轮 `1220 亿美元` 融资；`2026-03-05` 发布 `GPT-5.4` | 值得；`X` 上的信号常比官网更早，但必须回到官网核实 | 当前最强信号不是单模型升级，而是 `compute + distribution + Codex + agent platform` 联动 | https://openai.com/index/accelerating-the-next-phase-ai/ ; https://openai.com/index/introducing-gpt-5-4/ ; https://x.com/sama |
| Dario Amodei | Anthropic CEO | 看 `Anthropic` 如何把 `安全 + agent + 政策接口` 绑成一条线 | `2026-03-31` 与澳大利亚政府签署 AI 安全与研究 MOU；`2026-03-11` 推出 `Anthropic Institute` | 值得，但更适合跟 `Anthropic` 官方渠道，因为正式动作多在官网先落地 | Anthropic 仍在把 `frontier capability`、`safety research`、`policy interface` 一起推进 | https://www.anthropic.com/news/australia-MOU?id=19234 ; https://www.anthropic.com/news/the-anthropic-institute?s=09 ; https://www.anthropic.com/news |
| Demis Hassabis | Google DeepMind CEO | 看 `Google DeepMind` 的研究顶层叙事，尤其是 `AGI -> science -> world models` | 截至 `2026-04-06`，`DeepMind` 平台侧最新高信号已推进到 `2026-04` 的 `Gemma 4`；可稳定确认的个人署名高信号仍以 `2026-03-10` 的 `AlphaGo impact` 为主 | 值得；他的 `X` 往往会提前给出产品方向和个人判断，但当前仍应优先看官方页 | Google 正在持续把 `AGI / science / open models` 三条线并行推进 | https://deepmind.google/blog/10-years-of-alphago/ ; https://deepmind.google/blog/ ; https://deepmind.google/models/gemma/gemma-4/ ; https://x.com/demishassabis |
| Andrew Ng | DeepLearning.AI Founder | 看 `开发者生态`、`课程扩散`、`工程范式普及`，这条线对实际落地很重要 | `2026-04-03` The Batch 明确强调 `voice UI` 将快速普及；`2026-04-28` 至 `2026-04-29` 将主持 `AI Dev 26 x SF`；`2026-03-06` The Batch 推出 `Context Hub` | 值得；更适合盯 `课程 / 会议 / 开发者工具` 线索 | 面向开发者的主线已经明显收敛到 `agentic AI`、`memory/context engineering`、`reliability/observability/security`，并开始更重视 `voice UI` | https://www.deeplearning.ai/the-batch/tag/the-batch/ ; https://ai-dev.deeplearning.ai/ ; https://x.com/AndrewYNg |
| Fei-Fei Li | World Labs Co-founder | 看 `spatial intelligence / world models / 3D interface`，这是容易被忽视但很关键的长期线 | `2026-03-03` World Labs 发布 `3D as code`；`2026-02-18` 宣布新融资；`2026-01-21` 推出 `World API` | 值得，但优先还是看 `World Labs` 官方博客，因为正式技术信号都在那边 | `world model` 正在从研究话题走向 API、接口和工作流 | https://www.worldlabs.ai/blog/3d-as-code ; https://www.worldlabs.ai/blog/funding-2026 ; https://www.worldlabs.ai/blog/announcing-the-world-api ; https://www.worldlabs.ai/blog |

### P1：建议双周或月更

| 人物 | 当前角色 | 为什么值得跟 | 最近公开动态 | X 是否值得盯 | 核心信号 | 主要来源 |
|---|---|---|---|---|---|---|
| Andrej Karpathy | Eureka Labs Founder | 看 `技术解释力`、`如何理解 agent/harness/context engineering`，而不是公司级 roadmap | `2026-04-04` 新建 gist `llm-wiki.md`；`2026-03-13` `microgpt.py` 仍在活跃更新；`2026-02-25` 在 `X` 上明确谈到让工作 `testable / observable / legible` 才能把 agent 放进更长循环 | 非常值得；他最近最有信息量的公开输出已经转到 `gist + X` | 这是“高频高信号 gist/X，低频官网”的典型对象 | https://gist.github.com/karpathy?direction=desc&sort=updated ; https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f ; https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95 ; https://x.com/karpathy/status/2026738848420737474 |
| Ilya Sutskever | Safe Superintelligence Inc. Co-founder | 公开输出极少，但任何新动作都可能代表长期研究方向变化 | 截至 `2026-04-06`，`SSI` 官网公开信息仍强调“单一目标是 safe superintelligence”，未见高频产品化更新 | 若有官方 `X` 或访谈，值得跟；但日常噪音很多，建议低频扫 | 这是“低频但一旦更新就高信号”的观察对象 | https://ssi.inc/ |

## 为什么先跟这几位

### 1. 他们覆盖了当前最关键的几条主线

- `Sam Altman`：平台、算力、产品整合
- `Dario Amodei`：安全、agent、政策接口
- `Demis Hassabis`：AGI 研究叙事、science、world model
- `Andrew Ng`：开发者生态、教育扩散、工程范式
- `Fei-Fei Li`：spatial intelligence、world models、3D interface
- `Karpathy / Ilya`：低频但高密度的长期范式信号

### 2. `X` 现在确实应该纳入

- 很多真正的“新想法”先出现在 `X`
- 特别是 `Karpathy`、`Sam`、`Demis` 这类人物，`X` 往往比官网更早释放方向变化
- 但只看 `X` 容易把“试探性表达”误当成“正式路线”

所以当前默认建议是：

- `人物思想变化`：优先看 `X`
- `正式产品动作`：优先看官网
- `仓库记录`：尽量写成 `X 信号 -> 官网确认 -> 对我们的影响`

## 候选扩展名单

后续如果要扩大覆盖范围，可以再补：

- `Yann LeCun`：更适合跟 `open science / alternative AGI views`
- `Jensen Huang`：更适合跟 `AI infra / chips / system economics`
- `Mark Zuckerberg`：更适合跟 `open-weight strategy`
- `Jeff Dean`：更适合跟 `Google 基础研究与系统层`

## 建议追踪方式

### 每周

- 看 `OpenAI / Anthropic / DeepMind / World Labs / DeepLearning.AI` 官方博客与新闻页
- 扫一遍关键人物和公司官号的 `X`
- 只保留真的改变方向判断的动作

### 每两周

- 汇总一次 `X` 上反复出现、且被官网或产品动作印证的主题
- 删除纯情绪化、纯转发型低信号内容

### 每月

- 回看哪些 `X` 信号后来被官网确认了
- 调整我们对“谁是高信号人物”的名单

## 可执行入口清单

### X 账号清单

| 人物 / 机构 | X 入口 | 用途 | 优先级 |
|---|---|---|---|
| Sam Altman | https://x.com/sama | 看 OpenAI 顶层路线、融资、产品方向的早期信号 | P0 |
| Demis Hassabis | https://x.com/demishassabis | 看 DeepMind 研究主线、Gemini、science/world model 方向 | P0 |
| Andrew Ng | https://x.com/AndrewYNg | 看开发者生态、会议、课程、工具扩散 | P0 |
| Andrej Karpathy | https://x.com/karpathy | 看 agent、harness、research workflow、教育型最小实现 | P0 |
| OpenAI | https://x.com/OpenAI | 看正式发布、直播、预告 | P0 |
| Anthropic | https://x.com/AnthropicAI | 看正式发布、政策合作、研究博客转发 | P0 |
| Google DeepMind | https://x.com/GoogleDeepMind | 看研究发布、模型、science 方向 | P0 |
| World Labs | 若后续启用官方 X，再补入 | 当前优先看官网博客 | P1 |

### 官网 / 新闻页入口

| 人物 / 机构 | 入口 | 用途 | 优先级 |
|---|---|---|---|
| OpenAI News / Index | https://openai.com/index/ | 确认产品、模型、治理、研究正式发布 | P0 |
| Anthropic News | https://www.anthropic.com/news | 确认产品、安全、政策合作 | P0 |
| Google DeepMind Blog | https://deepmind.google/blog/ | 确认研究主线、模型、science 发布 | P0 |
| Google AI / Gemini | https://blog.google/innovation-and-ai/ | 确认 Gemini、Gemma、开发者工具 | P0 |
| DeepLearning.AI The Batch | https://www.deeplearning.ai/the-batch/tag/the-batch/ | 确认 Andrew Ng 侧的开发者生态和工具方向 | P0 |
| AI Dev | https://ai-dev.deeplearning.ai/ | 看会议议题是否变化，适合月更 | P1 |
| World Labs Blog | https://www.worldlabs.ai/blog | 确认 world model、3D interface、API 动作 | P0 |
| Karpathy Site | https://karpathy.ai/ | 低频官网归档入口 | P1 |
| SSI | https://ssi.inc/ | 低频但高信号的长期方向入口 | P1 |

### GitHub / Gist 入口

| 人物 / 机构 | 入口 | 用途 | 优先级 |
|---|---|---|---|
| Karpathy Gists | https://gist.github.com/karpathy?direction=desc&sort=updated | 当前 Karpathy 最新高信号主入口 | P0 |
| `llm-wiki.md` | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f | 看知识积累 / memory / wiki 化方向 | P0 |
| `microgpt.py` | https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95 | 看最小 LLM 实现与教学路线 | P1 |

### RSS / Feed 可用性

| 来源 | Feed 状态 | 备注 |
|---|---|---|
| Google Blog | 有公开 RSS | 页面内可见 RSS 入口，适合订阅 |
| DeepLearning.AI / The Batch | 可优先用页面归档；RSS 可后续补专门地址 | 当前用归档页已足够 |
| GitHub Gists | 可直接盯更新页；若后续需要自动化，可再补 Atom 方案 | 当前手动检查够用 |
| OpenAI / Anthropic / World Labs / SSI | 当前文档先按官网页面手动检查 | 不假设存在稳定公开 RSS，避免写错 |
| X | 无稳定官方 RSS | 默认手动检查 |

## 每周检查顺序

### 周一：先看正式发布

1. `OpenAI Index`
2. `Anthropic News`
3. `DeepMind Blog`
4. `Google AI / Gemini`
5. `World Labs Blog`

目的：

- 先确认有没有真正改变路线判断的新发布
- 避免一开始就被 `X` 噪音带偏

### 周二：再看关键人物 X

1. `sama`
2. `demishassabis`
3. `AndrewYNg`
4. `karpathy`
5. `OpenAI / Anthropic / GoogleDeepMind` 官号

筛选规则：

- 只记会改变判断的内容
- 纯转发、纯态度表达、纯活动宣传默认不记
- 如果只是 `X` 单条发言，先标成 `仅 X 信号`

### 周三：补看 GitHub / Gist

1. `Karpathy gists`
2. 其他确实出现高信号的个人或机构 GitHub 页面

筛选规则：

- 只保留能映射到 `memory / agent / eval / infra / world model` 主线的更新
- 代码小修小补不单独记

### 周四：交叉确认

1. 把周二的 `X` 信号回头对官网
2. 看有没有从“想法”转成“正式动作”
3. 给每条动态打标签：
   - `官网已确认`
   - `X + 官网双确认`
   - `仅 X 信号`

### 周五：写入仓库

1. 更新 [AI关键人物追踪.md](/home/ifnodoraemon/myreport/AI关键人物追踪.md)
2. 如果人物动态明显影响模型、infra、评测判断，再同步更新相关专题文档
3. 保持“少量高信号条目”，不做新闻堆积

## 最小周更清单

每周至少回答这 5 个问题：

1. `Sam / Dario / Demis` 有没有新的正式动作？
2. `Andrew Ng` 有没有把新的开发者主题推到课程、会议或工具层？
3. `Karpathy` 最近有没有新的 `gist` 或高信号 `X` 发言？
4. `Fei-Fei Li / World Labs` 有没有把 world model 往 API、产品或工作流推进？
5. 有没有人物信号需要反向更新 `模型 / infra / eval` 文档？

## 每周更新模板

每周更新时复制下面这段：

```md
## YYYY-MM-DD 当周

### 新增动态

- 人物：
  动作：
  来源级别：`官网已确认` / `X + 官网双确认` / `仅 X 信号`
  方向：
  为什么重要：
  对我们的影响：
  来源：

### 状态变化

- 人物：
  之前判断：
  当前判断：
  变化原因：

### 备注

- 
```

## 来源说明

- 优先使用 `个人官网`、`公司官方博客`、`研究机构官方页面`
- `X` 已纳入，但默认作为 `快信号层`，不是最终确认源
- 对于官方公开更新很少的人物，会明确标注“截至某日未见更新”，这属于基于官网可见内容的推断

## 2026-04-06 当周补充：X 快信号

### 新增动态

- 人物：`Andrej Karpathy`
  动作：`2026-04-04` 新建 gist `llm-wiki.md`
  来源级别：`官网已确认`
  方向：`knowledge accumulation / personal knowledge base / agent memory`
  为什么重要：这份 gist 直接攻击传统 `RAG` 的核心问题，即“每次问答都重新检索、没有累积”，转而主张把知识组织成一个能持续增长的 `LLM Wiki`。
  对我们的影响：这和仓库里已有的 `memory-first + context engineering` 主线高度一致，而且比单纯的向量库叙事更工程化。
  来源：https://gist.github.com/karpathy?direction=desc&sort=updated ; https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

- 人物：`Andrej Karpathy`
  动作：`2026-03-13` 更新 gist `microgpt.py`
  来源级别：`官网已确认`
  方向：`minimal LLM training / educational infrastructure`
  为什么重要：`microgpt.py` 仍在持续维护，说明他最近不仅在谈 agent 和知识组织，也在继续压缩“最小可理解 LLM 实现”这条教学与实验路线。
  对我们的影响：如果要跟 `Karpathy`，应该把 `gist` 视为一等来源，而不是只盯博客。
  来源：https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95

- 人物：`Andrej Karpathy`
  动作：`2026-03-07` 在 `X` 发布 `autoresearch` 最小化仓库；`2026-03-19` 相关社区开始扩展其并行实验模式
  来源级别：`仅 X 信号`
  方向：`agentic research / self-improving experimentation`
  为什么重要：这不是普通 demo，而是在公开推动“单卡、小仓库、可重复”的 agent 研究工作流。
  对我们的影响：如果后续想跟 `agent for research`，Karpathy 这条线值得长期盯，但目前更适合当作方向信号而不是稳定产品线。
  来源：https://x.com/karpathy ; https://x.com/skypilot_org/status/2034681533051855173

- 人物：`Andrej Karpathy`
  动作：`2026-02-25` 在 `X` 强调要把工作变得 `testable / observable / legible`，才能把 agent 放进更长循环
  来源级别：`仅 X 信号`
  方向：`harness engineering / observability`
  为什么重要：这和仓库里已有的 `runtime / eval / harness-first` 判断高度一致。
  对我们的影响：这类人物发言可以作为“工程范式变化”的早期指标。
  来源：https://x.com/karpathy/status/2026738848420737474

- 人物：`Sam Altman`
  动作：`2026-02-14` 在 `X` 评价“产生少量全新知识的能力”是值得认真对待的里程碑
  来源级别：`仅 X 信号`
  方向：`AI for science / knowledge creation`
  为什么重要：这类表态通常能反映 OpenAI 对下一阶段能力叙事的倾向。
  对我们的影响：后续应继续观察 OpenAI 是否把这条线扩展成正式产品或研究发布。
  来源：https://x.com/sama/status/2022729429710237977

- 人物：`Andrew Ng`
  动作：`2026-03-16` 在 `X` 继续推动 `Context Hub`，把它描述为让 coding agents 共享和获取最新 API 文档的基础工具
  来源级别：`X + 官网双确认`
  方向：`developer tools / context engineering`
  为什么重要：这是 `memory/context engineering` 正走向开发者基础设施的直接信号。
  对我们的影响：这进一步强化了“文档、context、agent 共享知识”是独立工程层的判断。
  来源：https://www.deeplearning.ai/the-batch/tag/the-batch/ ; https://x.com/AndrewYNg

- 人物：`Demis Hassabis`
  动作：截至 `2026-04-06`，未检索到比 `2026-03-10` DeepMind 官方博客更新更高信号、且可稳定验证的个人 `X` 新动作
  来源级别：`官网已确认`
  方向：`research roadmap`
  为什么重要：这说明 Demis 这条线当前更适合优先看 `DeepMind 官方博客`，而不是只盯个人 `X`
  对我们的影响：跟 Google DeepMind 时，仍应把官方研究发布作为主入口。
  来源：https://deepmind.google/blog/10-years-of-alphago/ ; https://x.com/demishassabis

### 状态变化

- 人物：`Karpathy`
  之前判断：更适合跟低频官网和长期范式。
  当前判断：他的最近高信号输出已经明显转向 `gist + X`，尤其要盯 `llm-wiki`、`microgpt`、`autoresearch`、`observability` 这四条线。
  变化原因：`2026-04-04` 新建 `llm-wiki.md` 和 `2026-04-06` 更新 `microgpt.py` 都比之前那版记录更新，也更贴近当前工作流主题。

- 人物：`Andrew Ng`
  之前判断：更偏课程与会议分发。
  当前判断：他也开始在 `X` 上为开发者工具和 context 基础设施放大声量，适合和官网一起跟。
  变化原因：`Context Hub` 同时在 The Batch 与 `X` 上形成了连续信号。

### 备注

- 当前 `X` 检索对部分账号可见性有限，因此人物最近动态优先记录“已找到且高信号”的内容，而不是硬凑每人一条。

## 2026-04-06 二次确认结论

### 有更新或需要修正的

- `Andrew Ng`：有更晚的官方更新，当前应以 `2026-04-03` The Batch 和 `2026-04-28/29` AI Dev 26 x SF 为最近公开动态。
- `Karpathy`：确实有比上一版更新的核心信号，但应以 `2026-04-04` 的 `llm-wiki.md` 为最新高信号主条目；`microgpt.py` 的可确认最近更新时间应修正为 `2026-03-13`，不应写成 `2026-04-06`。
- `Demis Hassabis`：个人署名高信号未明显晚于 `2026-03-10`，但 `Google DeepMind` 平台侧已推进到 `2026-04` 的 `Gemma 4`，这值得写进人物判断。

### 截至目前未发现更晚高信号公开动作的

- `Sam Altman`：截至 `2026-04-06`，仍以 `2026-03-31` 融资和 `2026-03-05` GPT-5.4 为最近两条最重要公开信号。
- `Dario Amodei`：截至 `2026-04-06`，仍以 `2026-03-31` 澳大利亚 MOU 和 `2026-03-11` Anthropic Institute 为最近高信号条目。
- `Fei-Fei Li / World Labs`：截至 `2026-04-06`，仍以 `2026-03-03` `3D as code` 为最近博客高信号更新，未见比它更晚的同级别公开动作。
- `Ilya Sutskever / SSI`：截至 `2026-04-06`，`SSI` 官网仍未出现更具体的新产品化或研究更新。
