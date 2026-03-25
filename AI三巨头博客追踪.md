# AI 三巨头博客追踪

最后更新：2026-03-25

参考文档：`/home/ifnodoraemon/myreport/agent-llm周论文追踪.md`

跟踪范围：截至 `2026-03-25` 检索到的 `OpenAI`、`Anthropic`、`Google / Google DeepMind` 官方博客、新闻与工程文章；优先保留和 `model`、`agent`、`tool use`、`runtime`、`eval`、`context`、`多模态产品化` 相关的高信号条目

## 目的

这份文件作为长期维护的博客追踪记录，用于：

- 跟踪 `OpenAI / Anthropic / Google` 最近公开表达的 AI 主线
- 区分哪些是 `模型发布`，哪些是 `agent 基础设施`、`开发者平台`、`评测方法学`、`多模态产品化`
- 判断三家在工程落地方向上的趋同与分化
- 记录这些博客信号对我们工作的实际影响
- 为后续每周更新提供统一模板

## 当前判断

当前最值得关注的高信号主题：

1. 三家都已经从“单模型能力”转向“`agent + tool + workflow`”叙事，但落点不同。
2. `OpenAI` 最近最强信号不是单点模型参数，而是 `agent runtime`、`computer environment`、`tool search`、`Codex / agent harness`。
3. `Anthropic` 最近最强信号是 `coding agent`、`MCP 标准化`、`长时任务 harness`、`agent eval 方法学`。
4. `Google` 最近最强信号是 `frontier reasoning + 成本分层 + world model + 多模态创作产品化`，技术面更宽，开发者工作流集中度稍低于 OpenAI / Anthropic。
5. 如果只看工程现实，`OpenAI / Anthropic` 更像在竞争“开发者 agent 操作系统”；`Google` 更像在同时推进“研究前沿 + 平台分发 + 消费级多模态入口”。

## 跟踪表

| 公司 | 日期 | 文章 | 方向 | 核心信号 | 与我们的相关性 | 优先级 | 建议动作 | 来源 |
|---|---|---|---|---|---|---|---|---|
| OpenAI | 2026-03-17 | Introducing GPT-5.4 | 模型 / tool use / knowledge work | `GPT-5.4` 把 coding、knowledge work、computer use、tool search 合到同一主线；说明 OpenAI 正在把“通用 agent 模型”变成默认产品层 | 如果我们关心长流程工作流与多工具 agent，这篇很重要 | P0 | 重点看 `tool search`、`agentic tool calling`、`GDPval` 这三块是否可映射到内部评测 | https://openai.com/index/introducing-gpt-5-4/ |
| OpenAI | 2026-03-11 | From model to agent: Equipping the Responses API with a computer environment | Agent runtime / execution environment | OpenAI 已明确把 `shell tool`、`hosted container`、`skills`、`compaction` 做成 agent 基础设施，而不是只给模型 API | 这直接关系到我们怎么做可执行、可持久、可恢复的 agent | P0 | 把文中 `shell + container + skills + compaction` 抽成内部 agent runtime 清单 | https://openai.com/index/equip-responses-api-computer-environment/ |
| OpenAI | 2026-02-11 | Harness engineering: leveraging Codex in an agent-first world | Harness / agent-first engineering | OpenAI 已在内部验证“`人类定义环境与反馈回路，agent 执行`”的工作方式；重点是 repo 结构、文档地图、可观测性、可验证性 | 对我们如何组织 agent-friendly repo、docs、QA 非常有参考价值 | P0 | 借鉴其 `AGENTS.md 只做目录、docs 做系统事实源` 的做法 | https://openai.com/index/harness-engineering/ |
| OpenAI | 2026-02-02 | Introducing the Codex app | 多 agent 工作台 / skills | OpenAI 已把“多 agent 并行”“skills”“安全沙箱”“项目级规则”产品化，说明交互层正在从 terminal 走向 agent command center | 如果我们看重 agent 使用体验，这篇是产品层强信号 | P1 | 关注 `multi-agent supervision` 和 `skills library` 的信息架构 | https://openai.com/index/introducing-the-codex-app/ |
| OpenAI | 2026-02-27 | Introducing the Stateful Runtime Environment for Agents in Amazon Bedrock | 企业 agent 部署 / stateful runtime | OpenAI 在公开强调：真正难的不是推理，而是 `state`、`workflow`、`governance`、`long-horizon execution` | 对企业级 agent 落地非常相关，尤其是有审批链、审计链的场景 | P1 | 把 `stateful runtime` 加入我们的长期跟踪主题，不要只盯模型能力 | https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/ |
| Anthropic | 2026-01-21 | Designing AI-resistant technical evaluations | 评测 / 招聘 / AI 时代基准失效 | Anthropic 直接给出一个现实信号：模型已经能在限时条件下击败大部分人类候选人，旧评测会失效 | 如果我们做内部评测或招聘作业设计，这篇非常重要 | P0 | 重新审视我们的 test / eval 是否已经被模型轻松穿透 | https://www.anthropic.com/engineering/AI-resistant-technical-evaluations |
| Anthropic | 2026-01-09 | Demystifying evals for AI agents | Agent eval 方法学 | Anthropic 把 agent eval 讲得很系统：`task / trial / grader / transcript`，并强调自动评测、生产监控、人审校准必须组合使用 | 这对我们建立 agent 评测体系是直接可用的 | P0 | 以这篇为蓝本，补一版内部 `agent eval` 术语表与最小框架 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| Anthropic | 2025-12-09 | Donating the Model Context Protocol and establishing the Agentic AI Foundation | 协议 / 生态 / 标准化 | `MCP` 已从 Anthropic 私有倡议升级到基金会治理，且 OpenAI、Google 等都在支持，说明连接层标准化已成事实主线 | 对工具连接、上下文注入、生态兼容性判断非常关键 | P0 | 默认把 `MCP` 当作必须长期跟踪的基础设施，不再视作短期潮流 | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation |
| Anthropic | 2025-11-26 | Effective harnesses for long-running agents | 长时 agent / harness | Anthropic 把长时 agent 的关键问题落到 `initializer agent`、`coding agent`、`progress notes`、`feature list`、`init.sh` 这些工程细节上 | 和我们做跨 context window 的 agent 设计强相关 | P0 | 借鉴其“显式留下下一轮可读工件”的模式设计任务交接机制 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| Anthropic | 2025-11-24 | Introducing Claude Opus 4.5 | 模型 / coding / agents | Anthropic 继续把 Claude 的最强卖点锚定在 `coding`、`agents`、`computer use`，不是泛聊天 | 如果我们评估 coding agent 供应商，这是一条核心信号 | P1 | 持续比较它与 OpenAI 在 `coding + agent` 叙事上的差异 | https://www.anthropic.com/news/claude-opus-4-5 |
| Anthropic | 2025-11-04 | Code execution with MCP: Building more efficient agents | MCP / tool use / code execution | Anthropic 明确指出：大量直接 tool call 会吃上下文，更优路线是“写代码来调用工具” | 这对 agent 成本、上下文利用率和复杂工作流设计很关键 | P1 | 关注“代码执行代理工具调用”是否比传统 function calling 更适合复杂任务 | https://www.anthropic.com/engineering/code-execution-with-mcp |
| Google | 2026-03-03 | Gemini 3.1 Flash-Lite: Built for intelligence at scale | 低成本模型 / 高吞吐 | Google 在明确做 `frontier` 之外，也在做“足够聪明但极致便宜和高吞吐”的分层模型；这是平台化的重要信号 | 如果我们要控制 agent 成本，这篇很值得跟 | P0 | 持续比较 `高吞吐小模型` 在分类、翻译、UI 生成、检索辅助中的可替代性 | https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-lite/ |
| Google | 2026-02-12 | Gemini 3 Deep Think: Advancing science, research and engineering | Frontier reasoning / science | Google 把 Deep Think 明确定位到 `science / research / engineering`，并用高难 benchmark 做背书 | 如果我们重视复杂推理与科研任务，这篇必须关注 | P0 | 跟踪其 `Humanity’s Last Exam`、`ARC-AGI-2`、`Codeforces` 等 benchmark 表达 | https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/ |
| Google | 2026-01-29 | Project Genie: Experimenting with infinite, interactive worlds | World model / interactive environment | Google 继续推进 `world model`，说明其 agent 视角不只停留在 browser / code，而是面向可交互环境建模 | 如果我们关注 embodied / simulation / training environment，这篇很重要 | P1 | 观察 world model 是否开始反向影响通用 agent 训练与评测 | https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/ |
| Google | 2026-02-18 | A new way to express yourself: Gemini can now create music | 多模态生成 / consumer productization | `Lyria 3 + Gemini app + SynthID` 表明 Google 在把生成模型快速产品化到消费者入口，同时补水印与验证能力 | 如果我们关心多模态产品面，这篇提供了产品化和内容可信度两条线索 | P1 | 跟踪 `生成能力 + 水印 / 验证` 是否成为 Google 的默认搭配 | https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/ |
| Google | 2026-03-10 | From games to biology and beyond: 10 years of AlphaGo’s impact | 研究叙事 / AGI 路线 | Google 在公开叙事里把 `AlphaGo -> AlphaFold -> AlphaProof / Deep Think / AlphaEvolve` 串成一条 AGI 路线 | 这有助于理解 Google 为什么同时押注 search、reasoning、science、world model | P1 | 把它当作 Google 顶层路线图解读，而不是普通纪念文章 | https://deepmind.google/blog/10-years-of-alphago/ |

## 横向观察

### 1. `Agent runtime` 已成为显性产品层

- `OpenAI`：`Responses API + shell + container + skills + compaction + stateful runtime`
- `Anthropic`：`Claude Code + harness + MCP + code execution + long-running agents`
- `Google`：开发者侧也在推进，但公开博客里更强的是 `reasoning models + world models + app surfaces`
- 结论：`runtime / environment / state / workflow` 已经不是“外围配套”，而是核心竞争点。

### 2. `Context / memory / handoff` 正从技巧变成工程学

- `OpenAI` 在强调 `compaction`、`skills`、`container context`
- `Anthropic` 在强调 `progress notes`、`feature list`、`init.sh`、`effective harness`
- `Google` 更少从 workflow 工程角度表达，但在 `1M context`、`world model`、`reasoning` 上给出了另一条路径
- 结论：博客层的公开表达已经强验证论文文档里的 `memory-first / context-first` 主线

### 3. `评测` 正从研究话题升级为产品生死线

- `Anthropic` 是三家里在 `agent eval` 上最系统、最直接的
- `OpenAI` 也在 `AgentKit / Evals / GDPval / tool search` 中持续强化评测与可观测性
- `Google` 更偏 benchmark 驱动，尤其是顶级 reasoning benchmark
- 结论：后续如果我们只看“模型更强”而不看“评测更稳”，会误判趋势

### 4. `MCP` 已经接近事实标准

- `Anthropic` 把 `MCP` 捐给基金会是最大信号
- `OpenAI` 在 Responses API 中明确支持远程 MCP server
- Google 也出现在支持方名单中
- 结论：面向外部工具与内部系统的连接层，后续默认优先关注 `MCP-compatible` 生态

### 5. 三家的差异正在变清楚

- `OpenAI`：更像 `agent platform + runtime + knowledge work`
- `Anthropic`：更像 `coding agent + MCP + eval discipline`
- `Google`：更像 `frontier reasoning + world model + multimodal consumerization`

## 与论文追踪的对应关系

### 1. `Memory / context` 被博客信号进一步坐实

- 论文文档里已经把 `memory` 和 `context` 定成高优先级。
- 博客侧现在出现的是工程化版本：
- `OpenAI`：`compaction`、`container context`、`skills`
- `Anthropic`：`long-running harness`、`handoff artifacts`
- `Google`：`长上下文 + world model`
- 这说明这条线已经不只是 benchmark 话题。

### 2. `评测` 从论文 benchmark 转为部署必要条件

- `Anthropic` 的两篇 eval 文章说明：agent 能力越强，评测越不能停留在单轮 prompt 级别。
- `OpenAI` 也在用 `tool search`、`GDPval`、`Codex`、`Evals` 把评测嵌进平台。
- 这和论文文档中的“长流程、主观质量、真实任务评测”主线高度一致。

### 3. `Agent` 的重点已从 orchestration 转向 execution environment

- 论文里强调 `agentic RL`、`memory`、`control`、`evaluation`。
- 博客里更落地的表达已经变成：`shell`、`container`、`runtime`、`harness`、`skills`、`state`
- 这意味着近期工程优先级应继续偏 `harness-first / context-first`，而不是盲目转向复杂训练路线。

## 当前优先级

### P0

- 跟踪 `OpenAI` 的 `agent runtime / Responses API / Codex harness`
- 跟踪 `Anthropic` 的 `agent eval / MCP / long-running harness`
- 跟踪 `Google` 的 `Deep Think / Flash-Lite / 推理与成本分层`

### P1

- 跟踪 `OpenAI` 的 `Codex app / stateful runtime / GPT-5.4`
- 跟踪 `Anthropic` 的 `Claude Opus 4.5 / code execution with MCP`
- 跟踪 `Google` 的 `Project Genie / Lyria 3 / AlphaGo -> AGI 叙事`

### P2

- 继续观察 `world model` 是否开始和通用 agent workflow 更紧密收敛
- 继续观察 `consumer multimodal app` 是否会反哺 developer platform

## 近期建议动作

### 本周

- 先把三家的博客条目统一打上标签：`model`、`agent`、`runtime`、`eval`、`context`、`multimodal`
- 补一份内部最小对照表：`OpenAI vs Anthropic vs Google` 在 `tool use / state / eval / skills / MCP` 上分别做到了什么
- 重点细读三篇：`OpenAI runtime`、`Anthropic evals`、`Google Deep Think`

### 未来两周

- 把博客追踪和论文追踪做映射，判断哪些主题是“研究热、工程冷”，哪些已经进入产品主线
- 建立固定周更节奏：每周只保留 `3-6` 篇新增高信号条目，不做资讯堆积

### 本月

- 明确我们更要跟的是：`developer agent stack`、`企业 agent deployment`，还是 `frontier reasoning / multimodal`
- 当前默认建议：优先跟 `developer agent stack + eval + context engineering`

## 每周更新模板

每周更新时复制下面这段：

```md
## YYYY-MM-DD 当周

### OpenAI

- 新文章：
  方向：
  核心信号：
  建议动作：

### Anthropic

- 新文章：
  方向：
  核心信号：
  建议动作：

### Google

- 新文章：
  方向：
  核心信号：
  建议动作：

### 横向变化

- 共同主题：
  对我们的影响：

- 分化主题：
  对我们的影响：

### 状态变化

- 主题：
  之前判断：
  当前判断：
  变化原因：

### 备注

- 
```

## 来源说明

- 仅使用三家官方站点页面：`openai.com`、`anthropic.com`、`blog.google / deepmind.google`
- 日期以对应文章页展示日期为准，统一按 `2026-03-25` 检索结果整理
- `OpenAI` 官方站点存在 locale 跳转与首页推荐变化，因此应优先以文章直链而不是首页块位为准

