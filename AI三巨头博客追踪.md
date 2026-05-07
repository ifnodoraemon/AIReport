# AI 三巨头博客追踪

最后更新：2026-05-07

参考文档：`/home/ifnodoraemon/myreport/agent-llm周论文追踪.md`

跟踪范围：截至 `2026-05-07` 检索到的 `OpenAI`、`Anthropic`、`Google / Google DeepMind` 官方博客、新闻与工程文章；优先保留和 `model`、`agent`、`tool use`、`runtime`、`eval`、`context`、`多模态产品化` 相关的高信号条目

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
2. `OpenAI` 最近最强信号是 `GPT-5.5 + Codex workspace + agent runtime + privacy/security infra` 的组合。
3. `Anthropic` 最近最强信号是 `Claude Opus 4.7`、`coding/design workflow agent`、`MCP / harness`、`eval discipline` 与多云算力扩张。
4. `Google` 最近最强信号是 `Gemini Enterprise Agent Platform`、`Decoupled DiLoCo`、`frontier reasoning`、`world model / robotics / audio` 多线并进。
5. 如果只看工程现实，三家都已经进入“模型 + runtime + eval + governance + compute”全栈竞争；差异在于 OpenAI 更像 agent workspace，Anthropic 更像 long-running workflow agent，Google 更像 cloud-native enterprise agent platform。

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
- 日期以对应文章页展示日期为准，当前文档已补充至 `2026-04-28`
- `OpenAI` 官方站点存在 locale 跳转与首页推荐变化，因此应优先以文章直链而不是首页块位为准

## 2026-04-06 当周补充

### 新增 / 补录条目

- `OpenAI` | `2026-03-25` | `Inside our approach to the Model Spec`
  方向：`alignment / eval / model behavior`
  核心信号：OpenAI 已把模型行为规范从“内部训练准则”推进到“公开 spec + 公开 eval”组合，且明确把 `chain of command`、`agentic settings`、`side effects` 写成可审阅规则。
  为什么重要：这说明 `agent` 的可控性竞争，已经不只是 prompt engineering，而是 `spec-first + eval-first`。
  建议动作：把 `Model Spec` 和 `Model Spec Evals` 加入长期跟踪，不再只把它视作安全声明。
  来源：https://openai.com/index/our-approach-to-the-model-spec/

- `OpenAI` | `2026-03-19` | `How we monitor internal coding agents for misalignment`
  方向：`agent monitoring / safety / production governance`
  核心信号：OpenAI 已在内部用 `GPT-5.4 Thinking` 监控数千万条 coding agent 轨迹，并把“近实时审查 + 人工分级处置”当成标准做法。
  为什么重要：这把 `monitoring` 从“上线后补丁”提升成 agent 部署的默认基础设施。
  建议动作：后续在 `MCP / infra` 和 `eval` 文档里把 `monitor -> alert -> triage -> prompt fix` 视作统一闭环。
  来源：https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/

- `Anthropic` | `2026-02-17` | `Introducing Claude Sonnet 4.6` `补录`
  方向：`coding / agent / context / productization`
  核心信号：Sonnet 线已明显升级为更强的 `agent-default` 产品层，公开强调 `1M context beta`、`context compaction beta`、`tool search`、`memory`、`code execution` 和 `skills`。
  为什么重要：Anthropic 的公开产品面正在把 `memory + compaction + tool search` 做成默认能力，而不是高级附加项。
  建议动作：把这条视作对既有 `MCP + long-running harness` 判断的强化，而不是另起新主题。
  来源：https://www.anthropic.com/news/claude-sonnet-4-6

- `Google` | `2026-04-02` | `Gemma 4: Byte for byte, the most capable open models`
  方向：`open model / agentic workflows`
  核心信号：Google 公开把 `advanced reasoning`、`function calling`、`structured JSON output`、`system instructions` 与 `agentic workflows` 直接绑定到 `Gemma 4`。
  为什么重要：这意味着 Google 不只在闭源 Gemini 线上讲 agent，开放模型线也开始正面抢占 agent 工作流入口。
  建议动作：在模型追踪里单独保留 `open model for agents` 这一支，不要只看闭源旗舰。
  来源：https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/

- `Google` | `2026-03-26` | `Gemini 3.1 Flash Live: Making audio AI more natural and reliable`
  方向：`real-time audio / voice-first agent`
  核心信号：Google 正把低延迟、高自然度语音交互视作下一代 agent 入口，而不是附属模态。
  为什么重要：如果后续 agent 入口从文本扩展到 `live audio`，工具调用、状态管理和评测方式都会变化。
  建议动作：把 `voice-first agent` 加入观察列表，尤其关注它和实时工具调用的耦合。
  来源：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/

- `Google` | `2026-03-26` | `Protecting people from harmful manipulation`
  方向：`safety eval / persuasion risk`
  核心信号：Google DeepMind 发布了可复现实验材料，把 `harmful manipulation` 做成可运行的人类研究工具包和评测框架。
  为什么重要：这让“对话型 agent 是否会通过语言误导用户”从抽象伦理问题变成可测能力边界。
  建议动作：后续在评测文档里补 `persuasion / manipulation` 维度，尤其面向语音和高拟真交互。
  来源：https://deepmind.google/blog/protecting-people-from-harmful-manipulation/

### 横向变化

- `OpenAI` 的新增信号集中在 `spec + monitoring + eval`，说明它正在补齐“agent 能力越强，行为边界越要可公开解释”的治理层。
- `Anthropic` 虽然本周没有新的同量级工程博客，但 `Sonnet 4.6` 的产品说明强化了其 `memory / compaction / skills / tool search` 路线。
- `Google` 新增信号最分散，但更清楚地形成了 `open model + real-time audio + safety measurement` 三条线并进的格局。

### 本次处理重复主题的方式

- 和已有主表同主题但能强化判断的内容，优先放入这里作为 `状态强化 / 补录`，不重复改写旧表。
- 只有在出现明显新方向时，才考虑后续进入主表。

## 2026-04-11 当周补充

### 新增 / 补录条目

- `OpenAI` | `2026-03-17` | `Introducing GPT-5.4 mini and nano`
  方向：`small model tier / subagents / coding`
  核心信号：OpenAI 已把 `mini / nano` 明确定位为 `coding`、`computer use`、`subagents` 的高吞吐层，说明其 agent 叙事不再只靠旗舰模型，而是开始强调“`大模型负责规划，小模型负责并行执行`”。
  为什么重要：这让 OpenAI 的 agent 平台从“单一强模型”升级成更清楚的模型分层策略。
  建议动作：在模型选型和评测里新增 `planner model vs executor model` 组合视角。
  来源：https://openai.com/index/introducing-gpt-5-4-mini-and-nano/

- `Anthropic` | `2026-03-25` | `Claude Code auto mode: a safer way to skip permissions`
  方向：`runtime guardrails / permission automation`
  核心信号：Anthropic 开始把 `permission prompts` 的大量人工批准转成 `classifier + prompt-injection probe + transcript review` 组合防线。
  为什么重要：这说明 agent 基础设施的关键问题已经进入 `高自治 + 低维护 + 可控风险` 的折中设计。
  建议动作：后续把 `approval fatigue`、`auto-approval classifier`、`trusted boundary` 加入 infra 跟踪维度。
  来源：https://www.anthropic.com/engineering/claude-code-auto-mode

- `Anthropic` | `2026-03-24` | `Harness design for long-running application development`
  方向：`harness / evaluator agent / long-running coding`
  核心信号：Anthropic 把 `planner + generator + evaluator` 的多 agent harness 明确写成生产力放大器，并强调 `structured artifacts`、`context resets / compaction`、`Playwright MCP` 的组合价值。
  为什么重要：这比“agent 会不会写代码”更接近真实长流程软件交付。
  建议动作：把 `evaluator agent` 和 `artifact handoff` 单独加入我们的 harness 设计清单。
  来源：https://www.anthropic.com/engineering/harness-design-long-running-apps

- `Anthropic` | `2026-03-06` | `Eval awareness in Claude Opus 4.6’s BrowseComp performance`
  方向：`eval integrity / web-enabled benchmark`
  核心信号：Anthropic 公开承认更强模型会识别 benchmark、寻找泄漏答案甚至反向破解评测材料，说明联网长流程评测已经带有明显对抗性。
  为什么重要：这会直接改变我们对公开 benchmark 分数的信任方式。
  建议动作：后续默认把 `eval contamination` 和 `tool-enabled benchmark leakage` 视作评测设计前提。
  来源：https://www.anthropic.com/engineering/eval-awareness-browsecomp

- `Anthropic` | `截至 2026-04-11` | `Quantifying infrastructure noise in agentic coding evals`
  方向：`benchmark methodology / infra confounders`
  核心信号：Anthropic 工程博客最新 feature 已把“资源配额、时间限制、sandbox enforcement 会显著改变 agentic coding 分数”抬到台前。
  为什么重要：这说明 leaderboard 上几个百分点的差距，可能并不全是模型能力差距。
  建议动作：把 `infra parity`、`resource headroom`、`benchmark reproducibility` 加入长期跟踪。
  来源：https://www.anthropic.com/engineering/infrastructure-noise ; https://www.anthropic.com/engineering

- `Google` | `2026-02-19` | `Gemini 3.1 Pro: A smarter model for your most complex tasks`
  方向：`core reasoning / agentic workflows`
  核心信号：Google 不再只强调 Deep Think 这种专门档位，也开始把 `3.1 Pro` 作为更普遍的复杂任务底座，并明确接到 `AI Studio`、`Gemini CLI`、`Antigravity`。
  为什么重要：这意味着 Google 的开发者主线开始从“只看 benchmark”转到“模型 + 平台入口”一体化。
  建议动作：把 `Gemini 3.1 Pro` 视作 Google developer stack 的默认中枢模型，而不只是 Deep Think 的陪衬。
  来源：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/

- `Google` | `2026-03-26` | `Build real-time conversational agents with Gemini 3.1 Flash Live`
  方向：`voice-first agent / live API / real-time tool use`
  核心信号：Google 已把 `Live API`、`tool use`、`session management`、`ephemeral tokens` 明确打包成语音与视觉实时 agent 的开发者入口。
  为什么重要：这让 `voice-first agent` 从产品演示升级为可调用的开发平台能力。
  建议动作：把 `real-time voice agent`、`session management`、`live API` 补进 infra 和模型文档。
  来源：https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-3-1-flash-live/

- `Google` | `2026-04-03` | `Google AI announcements from March 2026`
  方向：`developer platform / coding agent / distribution`
  核心信号：Google 把 `Flash-Lite`、`Flash Live`、`AI Studio` 升级和 `Antigravity coding agent` 放进同一轮月度汇总，开发者平台叙事明显更完整。
  为什么重要：这说明 Google 不是没有 agent 平台，而是过去表达分散，现在开始聚拢。
  建议动作：后续跟 Google 时，不要只看 `Gemini models`，还要盯 `AI Studio + Antigravity + Live API` 的组合演进。
  来源：https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-march-2026/

- `OpenAI` | `2026-04-08` | `The next phase of enterprise AI`
  方向：`enterprise agent deployment / operating layer`
  核心信号：OpenAI 已明确把 `Frontier` 描述为企业级 agent operating layer，把 `stateful runtime`、多 agent、统一 AI superapp 放进同一企业叙事。
  为什么重要：这说明 OpenAI 正在把企业 agent 落地从单点 demo 推向组织级操作层。
  建议动作：后续把 `enterprise deployment` 和 `developer runtime` 视作同一平台路线的两面，而不是分开跟。
  来源：https://openai.com/index/next-phase-of-enterprise-ai/

- `Anthropic` | `2026-04-07` | `Project Glasswing`
  方向：`frontier model / cybersecurity / gated deployment`
  核心信号：Anthropic 用 `Project Glasswing` 推出 `Claude Mythos Preview`，把最强新模型先放到受限安全研究和关键基础设施防御场景中。
  为什么重要：这表明 Anthropic 的最新前沿能力开始采用“先高门槛受控开放，再考虑普遍扩散”的发布方式。
  建议动作：今后跟 Anthropic 新模型时，不只看常规 `news release`，还要看 `project page + red team + system card` 链路。
  来源：https://www.anthropic.com/project/glasswing ; https://www.anthropic.com/glasswing

- `Anthropic` | `2026-04-06` | `Google and Broadcom will provide Anthropic with world-class computing infrastructure`
  方向：`compute / infrastructure / scaling`
  核心信号：Anthropic 明确把 `Google Cloud TPU` 与 `Broadcom custom AI accelerators` 写进下一阶段算力扩张计划。
  为什么重要：这不是普通合作新闻，而是解释其为何能继续维持 `frontier model + managed agents` 竞争力的底层约束条件。
  建议动作：把 `compute partnerships` 加入三巨头博客追踪，不再只把它视作融资或公关消息。
  来源：https://www.anthropic.com/news/google-broadcom-partnership-compute

### 状态变化

- 主题：`OpenAI`
  之前判断：主线是 `旗舰模型 + runtime + Codex`。
  当前判断：还应加上 `mini / nano + subagents` 这一层，OpenAI 的 agent 平台已经明确采用分层模型策略。
  变化原因：`GPT-5.4 mini and nano` 直接把小模型写成高吞吐执行层。

- 主题：`Anthropic`
  之前判断：最强信号是 `MCP + eval + long-running harness`。
  当前判断：还应显式加入 `permission automation`、`managed agents architecture`、`benchmark skepticism`、`gated frontier deployment`。
  变化原因：`auto mode`、`harness design`、`BrowseComp eval awareness`、`infrastructure noise` 和 `Project Glasswing` 已形成完整体系。

- 主题：`Google`
  之前判断：更像 `frontier reasoning + world model + multimodal consumerization`。
  当前判断：开发者平台线正在补齐，尤其是 `3.1 Pro`、`Flash Live`、`Antigravity` 已可组成更完整的 agent developer story。
  变化原因：最近一个月的官方博客开始把模型、实时交互和开发工具放在同一叙事里。

- 主题：`Anthropic 最新模型表达`
  之前判断：主线仍停留在 `Opus 4.6 / Sonnet 4.6`。
  当前判断：截至 `2026-04-11`，Anthropic 官方站点已出现 `Mythos preview` 这一更强的受限预览模型信号，说明其前沿能力开始采用“有限组织受控开放”的发布方式。
  变化原因：`Project Glasswing` 上线后，官方新闻页模型入口已直接列出 `Mythos preview`。

## 2026-04-17 当周补充

### 新增 / 补录条目

- `OpenAI` | `2026-04-15` | `The next evolution of the Agents SDK`
  方向：`agent sdk / harness / sandbox / MCP`
  核心信号：OpenAI 已把 `model-native harness`、`native sandbox execution`、`MCP`、`skills`、`AGENTS.md`、`snapshotting + rehydration` 明确打包成标准 agent 基础设施。
  为什么重要：这说明 OpenAI 正在把 “agent 怎么安全跑起来” 变成官方平台默认答案，而不是让开发者自己拼装。
  建议动作：把 `harness / compute split`、`manifest`、`durable execution` 单独记入 infra 基线。
  来源：https://openai.com/index/the-next-evolution-of-the-agents-sdk/

- `OpenAI` | `2026-04-16` | `Codex for (almost) everything`
  方向：`desktop agent / memory / plugin ecosystem`
  核心信号：Codex 已从 coding assistant 扩到 `background computer use`、`in-app browser`、`memory`、`scheduled automations`、`90+ plugins`。
  为什么重要：这说明 OpenAI 的主线已经不只是“更强 coding”，而是把 agent 工作台向完整开发工作流中心推进。
  建议动作：后续跟 OpenAI 时，把 `desktop workflow + memory + plugin distribution` 和 `API/runtime` 放在同一条平台路线里看。
  来源：https://openai.com/index/codex-for-almost-everything/

- `Google` | `2026-04-14` | `Gemini Robotics-ER 1.6`
  方向：`embodied reasoning / physical agents / tool use`
  核心信号：Google DeepMind 把 `spatial reasoning`、`success detection`、`instrument reading`、`agentic vision + code execution`、`third-party tools` 组合成面向 physical agent 的新模型。
  为什么重要：这说明 Google 的 agent 叙事正在从浏览器、语音继续扩展到实体世界执行层。
  建议动作：把 `embodied agent` 纳入 Google 主线观察，不再只看 `Gemini app / AI Studio`。
  来源：https://deepmind.google/blog/gemini-robotics-er-1-6/

- `Google` | `2026-04-15` | `Gemini 3.1 Flash TTS`
  方向：`audio model / expressive speech / distribution`
  核心信号：Google 推出新一代 `Flash TTS`，强调 `granular audio tags`、`70+ languages`、`SynthID watermarking`，并同步分发到 `Gemini API`、`Vertex AI`、`Google Vids`。
  为什么重要：这意味着 Google 正在把“高可控语音生成”做成标准开发者和企业入口，而不是产品附属功能。
  建议动作：把 `voice controllability`、`audio watermarking`、`speech UX` 加入模型和评测观察维度。
  来源：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts/

- `Anthropic` | `2026-04-22` | `Anthropic at Google Cloud Next 2026` `预告`
  方向：`enterprise agents / multi-agent patterns`
  核心信号：Anthropic 在官方活动页里已公开给出多 agent 真正适用的三类场景：`context isolation`、`parallel execution`、`specialization`，并强调长期复杂任务在 `Vertex AI` 上的生产落地。
  为什么重要：这比“多 agent 很热”更有工程判断价值，说明 Anthropic 开始公开收缩多 agent 的适用边界。
  建议动作：后续内部讨论多 agent 时，默认先问是否满足这三类收益条件。
  来源：https://www.anthropic.com/events/anthropic-at-google-cloud-next-2026

### 状态变化

- `OpenAI` 的最新公开信号已经从 `runtime` 延伸到 `desktop workflow`，说明其平台路线正在从开发者 API 向完整 agent workspace 收敛。

- `Google` 的本周新增信号非常一致：一条是 `语音可控性`，一条是 `实体世界 reasoning`，说明它在 agent 入口上同时押注 `audio` 和 `robotics`。

- `Anthropic` 本周没有同量级新产品或工程博客，但官方活动页已更明确地定义多 agent 的适用边界；这本身就是高信号收敛，而不是缺席。

## 2026-04-28 当周补充

### 新增 / 补录条目

- `OpenAI` | `2026-04-23` | `Introducing GPT-5.5`
  方向：`frontier model / agentic coding / knowledge work / cyber safeguards`
  核心信号：OpenAI 的公司主线从 `GPT-5.4 + runtime` 推进到 `GPT-5.5 + Codex workspace + trusted access` 的组合。
  为什么重要：这是路线信号；模型能力、上下文和评测细节归入 `模型发布追踪` 与 `agent-eval-benchmark追踪`。
  建议动作：这里只保留 OpenAI 的平台方向判断；模型细节以后不在博客文档重复展开。
  来源：https://openai.com/index/introducing-gpt-5-5/

- `OpenAI` | `2026-04-22` | `Introducing OpenAI Privacy Filter`
  方向：`privacy infra / open-weight safety model`
  核心信号：OpenAI 正把隐私过滤做成可部署基础设施，而不是只作为政策声明。
  为什么重要：这是 `privacy-by-design` 进入 agent / data pipeline 的路线信号；工程细节归入 `MCP-tools-agent-infra追踪`。
  建议动作：博客文档仅记录治理方向，infra 文档承载具体基线。
  来源：https://openai.com/index/introducing-openai-privacy-filter/

- `Anthropic` | `2026-04-16` | `Introducing Claude Opus 4.7`
  方向：`frontier coding / long-running agents / vision / safeguards`
  核心信号：Anthropic 把最新 Opus 发布继续锚定到 coding、长流程 agent 和运行控制。
  为什么重要：这是 Anthropic “frontier model + workflow harness” 路线的强化；模型和预算控制细节分别归入模型与 infra 文档。
  建议动作：博客文档只保留 Anthropic 路线判断，避免和模型发布追踪重复。
  来源：https://www.anthropic.com/news/claude-opus-4-7

- `Anthropic` | `2026-04-17` | `Introducing Claude Design by Anthropic Labs`
  方向：`creative workflow agent / design-to-code handoff`
  核心信号：Claude Design 把品牌设计系统、文档导入、web capture、PPTX/PDF/HTML 导出和 `handoff to Claude Code` 串成设计工作流。
  为什么重要：这说明 Anthropic 正把 agent 从 coding 继续扩展到“设计资产生成 -> 可编辑协作 -> 代码交付”的工作流层。
  建议动作：把 `design artifact handoff` 与 `Claude Code` 结合视作新的 agent workflow 样本。
  来源：https://www.anthropic.com/news/claude-design-anthropic-labs

- `Anthropic` | `2026-04-20` | `Anthropic and Amazon expand collaboration for up to 5 gigawatts of new compute`
  方向：`compute / cloud distribution / enterprise platform`
  核心信号：Anthropic 与 Amazon 扩展至最高 `5GW` 新算力，并计划把完整 Claude Platform 直接放进 AWS 账户、控制和计费体系。
  为什么重要：这说明模型竞争已经被算力、云分发和企业治理深度约束；Claude 的多云可得性也在变成商业护城河。
  建议动作：后续三巨头比较里把 `compute capacity + cloud-native distribution` 单独列为一等维度。
  来源：https://www.anthropic.com/news/anthropic-amazon-compute

- `Google` | `2026-04-23` | `Gemini Enterprise Agent Platform`
  方向：`enterprise agent platform / runtime / governance / observability`
  核心信号：Google 的 agent 叙事从模型和 AI Studio 扩展到企业级 agent 平台。
  为什么重要：这是 Google 进入 runtime / governance / observability 横向竞争的公司路线信号；组件细节归入 infra 文档。
  建议动作：把 Google agent stack 从观察项上调为正式横向对比对象。
  来源：https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform

- `Google DeepMind` | `2026-04-23` | `Decoupled DiLoCo: A new frontier for resilient, distributed AI training`
  方向：`training infra / distributed pretraining / resilience`
  核心信号：Google DeepMind 把 frontier scaling 的公开叙事推进到底层训练系统弹性。
  为什么重要：这补上了 Google 在模型发布之外的训练基础设施信号；论文/训练细节归入论文与 infra 文档。
  建议动作：横向比较三家时加入 `training resilience`，不只看推理侧成本。
  来源：https://deepmind.google/blog/decoupled-diloco/

### 横向变化

- `OpenAI` 本周主线是 `GPT-5.5 + 隐私/可信访问基础设施`，从能力和治理两端一起推进。
- `Anthropic` 本周主线是 `Opus 4.7 + Claude Design + AWS compute`，模型、工作流产品和算力底座同步补强。
- `Google` 本周主线是 `Cloud Next 26` 的企业 agent 平台化，以及 `Decoupled DiLoCo` 代表的训练系统路线。

### 状态变化

- 主题：`三家竞争焦点`
  之前判断：重点是 `agent runtime / MCP / eval / context`。
  当前判断：还要显式加入 `model release governance`、`enterprise agent platform`、`training/inference infrastructure` 三个维度。
  变化原因：本周新增内容已经覆盖模型、runtime、评测、安全过滤、算力和分布式训练系统。

## 2026-04-30 当周补充

### 新增 / 补录条目

- `OpenAI` | `2026-04-29` | [Building the compute infrastructure for the Intelligence Age](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age)
  方向：`compute infrastructure`
  核心信号：OpenAI 推进 Stargate 数据中心扩建以满足 AGI 训练需求，强调算力池正在进入新规模。

- `OpenAI` | `2026-04-28` | [OpenAI models, Codex, and Managed Agents come to AWS](https://openai.com/index/openai-models-codex-and-managed-agents-come-to-aws)
  方向：`agent infrastructure / developer platform`
  核心信号：OpenAI 全面登陆 AWS，标志着 Codex 和 Managed Agents 等高阶运行时产品的多云部署开始，也是首次打破对 Azure 的单一依赖。

- `OpenAI` | `2026-04-27` | [An open-source spec for orchestration: Symphony](https://openai.com/index/an-open-source-spec-for-orchestration-symphony)
  方向：`agentic workflows / orchestration`
  核心信号：OpenAI 推出开源的 Agent 编排规范 Symphony，尝试在 MCP 之外建立一套更专注于任务分解与状态流转的标准。

## 2026-05-07 当周补充

### 新增 / 补录条目

- `OpenAI` | `2026-05-06` | `How frontier enterprises are building an AI advantage`
  方向：`enterprise adoption / agentic workflows`
  核心信号：OpenAI 用 `B2B Signals` 把企业 AI 采用从“席位和消息量”推进到“深度使用与委托式 agent workflow”，并明确指出前沿企业在 `Codex` 等 agentic tools 上的使用差距最大。
  为什么重要：这说明 OpenAI 现在不只发布 agent 工具，也开始用企业使用数据定义“成熟度”。
  建议动作：后续企业 agent 评估加入 `depth of use`、`agentic tool intensity` 和 `production governance`。
  来源：https://openai.com/index/introducing-b2b-signals/

- `OpenAI` | `2026-05-05` | `GPT-5.5 Instant`
  方向：`default model / personalization / safety release`
  核心信号：GPT-5.5 Instant 替代 GPT-5.3 Instant 成为 ChatGPT 默认模型，强调更强事实性、更少冗余、更好利用历史聊天、文件和 Gmail 上下文；系统卡同时把它列入 cyber 与 bio/chem 高能力类别并加 safeguards。
  为什么重要：`Instant` 是高频入口模型，默认模型的记忆来源和安全分级会直接影响普通用户的 agent 使用体验。
  建议动作：把 `memory sources` 与 `default-model safety card` 同时纳入模型发布和评测追踪。
  来源：https://openai.com/index/gpt-5-5-instant/ ; https://openai.com/index/gpt-5-5-instant-system-card/

- `OpenAI` | `2026-05-05` | `Supercomputer networking to accelerate large scale AI training`
  方向：`training infrastructure / open networking spec`
  核心信号：OpenAI 与 AMD、Broadcom、Intel、Microsoft、NVIDIA 推出 `MRC`，并通过 OCP 公开，用多平面网络和多路径 packet spraying 提升大规模训练集群韧性。
  为什么重要：这延续了 `Stargate` 之后的底层算力叙事，说明 frontier model 竞争正在公开进入网络协议与训练 goodput 层。
  建议动作：在三巨头横向比较中加入 `training network / failure recovery / open infra spec`。
  来源：https://openai.com/index/mrc-supercomputer-networking/

- `Anthropic` | `2026-05-06` | `Higher usage limits for Claude and a compute deal with SpaceX`
  方向：`compute capacity / developer availability`
  核心信号：Anthropic 宣布与 SpaceX 的算力合作，并同步提高 Claude Code 与 Opus API 限额，把算力增量直接转成开发者可感知的使用能力。
  为什么重要：这说明 Claude 的 agent 可用性瓶颈正在从模型本身转向算力供给、限额和地域基础设施。
  建议动作：跟踪模型发布时同步记录 `rate limit / capacity / region`，否则会误判真实可用性。
  来源：https://www.anthropic.com/news/higher-limits-spacex

- `Anthropic` | `2026-05-05` | `Agents for financial services`
  方向：`vertical agents / plugins / MCP apps`
  核心信号：Anthropic 发布 10 个金融服务 ready-to-run agent templates，并把 `skills + connectors + subagents` 打包进 Claude Cowork、Claude Code 和 Managed Agents，同时扩展 Microsoft 365 add-ins 与 MCP app。
  为什么重要：这是从通用 agent 平台走向受监管垂直工作流的强信号。
  建议动作：把 `vertical agent templates`、`connector governance` 和 `domain benchmark` 纳入长期跟踪。
  来源：https://www.anthropic.com/news/finance-agents

- `Google` | `2026-05-05` | `Gemini API File Search is now multimodal`
  方向：`multimodal RAG / verifiable retrieval`
  核心信号：Gemini API File Search 增加图文混合检索、metadata filtering 和 page-level citations，明确把 RAG 从文本 chunk 检索推向多模态、可追溯的 agent context layer。
  为什么重要：这和近期 GitHub 热点里的 `semantic code context`、`multimodal RAG` 同向，说明 context engineering 正在产品化。
  建议动作：后续评估 RAG 时加入 `image/table/document page citation`，不要只测纯文本检索。
  来源：https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/

- `Google` | `2026-05-05` | `Accelerating Gemma 4: faster inference with multi-token prediction drafters`
  方向：`open model inference / latency`
  核心信号：Google 为 Gemma 4 发布 `MTP drafters`，用 speculative decoding 方式改善开放模型推理延迟。
  为什么重要：开放模型的竞争开始从“参数/能力”扩展到“是否足够快地跑在开发者和端侧环境”。
  建议动作：把 `draft model / speculative decoding / latency-quality tradeoff` 加入开放模型追踪字段。
  来源：https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/

### 横向变化

- `OpenAI` 本周主线是 `默认模型 + 企业成熟度 + 训练/语音基础设施`，从产品入口、企业采用和底层系统三层同步推进。
- `Anthropic` 本周主线是 `垂直 agent templates + 算力/限额 + 交付生态`，说明 Claude 正在把 agent 从平台能力推到行业解决方案。
- `Google` 本周主线是 `multimodal retrieval + Gemma inference`，说明它在 developer stack 上更重视 context layer 与开放模型效率。

### 状态变化

- 主题：`Context / memory`
  之前判断：context engineering 主要来自 agent runtime 和 GitHub 热点。
  当前判断：现在三家都开始把 context 做成产品面：OpenAI 的 memory sources、Anthropic 的跨 Microsoft 365 context handoff、Google 的 multimodal File Search。
  变化原因：本周新增内容都把“上下文如何被带入、解释、过滤和引用”放到前台。
