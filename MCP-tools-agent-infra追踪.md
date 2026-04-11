# MCP / Tools / Agent Infra 追踪

最后更新：2026-04-11

参考文档：`/home/ifnodoraemon/myreport/AI三巨头博客追踪.md`、`/home/ifnodoraemon/myreport/agent-llm周GitHub热点追踪.md`

跟踪范围：近期与 `MCP`、`tool use`、`code execution`、`sandbox`、`agent runtime`、`context compaction`、`skills`、`stateful execution` 相关的高信号工程进展

## 目的

这份文件作为长期维护的 agent 基础设施记录，用于：

- 追踪 `MCP` 是否正在成为事实标准
- 追踪 agent 从“会回答”转向“能执行”的关键工程层
- 记录 `runtime`、`sandbox`、`state`、`skills`、`handoff` 的公开最佳实践
- 帮助我们判断哪些基础设施已经进入产品主线，哪些还只是概念包装

## 相关页面

详见 `wiki/` 中的长期基础设施与对比页：

- [wiki/companies/openai-agent-stack.md](/home/ifnodoraemon/myreport/wiki/companies/openai-agent-stack.md)
- [wiki/companies/anthropic-agent-stack.md](/home/ifnodoraemon/myreport/wiki/companies/anthropic-agent-stack.md)
- [wiki/companies/google-agent-stack.md](/home/ifnodoraemon/myreport/wiki/companies/google-agent-stack.md)
- [wiki/concepts/context-engineering.md](/home/ifnodoraemon/myreport/wiki/concepts/context-engineering.md)
- [wiki/comparisons/openai-vs-anthropic-agent-stack.md](/home/ifnodoraemon/myreport/wiki/comparisons/openai-vs-anthropic-agent-stack.md)

## 当前判断

当前最值得关注的高信号主题：

1. `MCP` 已经不再只是 Anthropic 生态内的话题，而是在走向跨平台标准。
2. `shell + container + code execution + sandbox` 正在变成 agent 平台的默认能力边界。
3. `skills`、`compaction`、`progress notes`、`handoff artifacts` 说明长时任务的核心问题已经转向上下文管理和任务接力。
4. 近期工程优先级应继续偏 `harness-first + context-first + observability-first`。

## 跟踪表

| 来源 | 日期 | 条目 | 方向 | 核心信号 | 与我们的相关性 | 优先级 | 建议动作 | 来源链接 |
|---|---|---|---|---|---|---|---|---|
| OpenAI | 2026-03-11 | Responses API with a computer environment | Runtime / shell / container | `shell tool`、`hosted container`、`skills`、`compaction` 被打包为 agent 基础设施 | 这是我们设计可执行 agent runtime 的直接参考 | P0 | 抽象成内部清单：`shell`、`container`、`state`、`compaction`、`skills` | https://openai.com/index/equip-responses-api-computer-environment/ |
| OpenAI | 2026-02-11 | Harness engineering | Harness / repo design | 强调 `AGENTS.md`、系统化 docs、可验证任务流，说明 repo 结构本身已经是 agent 能力的一部分 | 对我们如何维护 agent-friendly 文档仓库很有参考意义 | P0 | 继续把仓库文档结构做成 agent 可读、可更新的形式 | https://openai.com/index/harness-engineering/ |
| OpenAI | 2026-02-27 | Stateful Runtime Environment for Agents | Stateful execution / enterprise deployment | 真正难点被定义为 `state`、`workflow`、`governance`、`long-horizon execution` | 对企业级或长期运行 agent 的架构判断很重要 | P1 | 单独跟 `stateful runtime`，避免只讨论模型 API | https://openai.com/index/introducing-the-stateful-runtime-environment-for-agents-in-amazon-bedrock/ |
| Anthropic | 2025-12-09 | MCP donated to Agentic AI Foundation | 协议 / 标准 / 生态 | `MCP` 从厂商倡议升级到基金会治理，是连接层标准化的核心信号 | 直接影响工具接入和跨平台兼容判断 | P0 | 默认把 `MCP-compatible` 作为长期重要维度 | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation |
| Anthropic | 2025-11-04 | Code execution with MCP | MCP / code execution | 相比大量直接 tool call，写代码调用工具可能更高效、更省上下文 | 对复杂工作流和成本控制很相关 | P0 | 跟踪“代码执行代理”是否会成为比 function calling 更强的默认范式 | https://www.anthropic.com/engineering/code-execution-with-mcp |
| Anthropic | 2025-11-26 | Effective harnesses for long-running agents | Long-running agents / handoff | `progress notes`、`feature list`、`init.sh` 这类工件说明 handoff 是核心能力，不是附属细节 | 对长时任务和多轮接力式 agent 非常关键 | P0 | 在内部任务流设计里显式引入 handoff artifact 概念 | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| GitHub 热点 | 2026-03-25 | deepagents / OpenViking / claude-mem / plugins | Harness / context / skills / memory | 开源热点已经验证：`runtime`、`context database`、`cross-session memory`、`plugin distribution` 正在产品化 | 说明基础设施竞争已经从模型层外溢到工具层和上下文层 | P0 | 把这些项目作为工程侧对照样本持续跟踪 | https://github.com/trending |

## 横向观察

### 1. `MCP` 正在成为连接层主线

- `Anthropic` 提供治理信号
- `OpenAI` 提供平台接入信号
- 开源生态开始围绕 `skills / plugins / MCP` 聚集

### 2. `Runtime` 是当前最真实的 agent 护城河

- 仅有 function calling 已经不够
- `shell`、`container`、`code execution`、`sandbox`、`state` 更接近真实生产系统

### 3. 长时任务关键在 `context management`

- `compaction`
- `progress notes`
- `skills`
- `handoff artifacts`

这些能力决定 agent 能不能在长流程里稳定工作。

## 当前优先级

### P0

- 跟踪 `MCP` 标准化与生态扩张
- 跟踪 `runtime / shell / container / sandbox`
- 跟踪 `long-running harness` 与 `handoff`

### P1

- 跟踪 `stateful execution` 和企业部署能力
- 跟踪 `plugin / skills` 是否形成更稳定的分发模式

## 近期建议动作

### 本周

- 把现有博客和 GitHub 条目统一映射到同一套基础设施标签
- 定义内部最小 agent infra 清单：`tool use`、`runtime`、`state`、`context`、`observability`

### 未来两周

- 对比 `MCP`、`function calling`、`code execution` 三种工具接入方式的适用边界
- 明确哪些能力是必须在平台层实现，哪些可以留给具体 agent

## 每周更新模板

每周更新时复制下面这段：

```md
## YYYY-MM-DD 当周

### 新增条目

- 条目：
  方向：
  核心信号：
  为什么重要：
  建议动作：

### 状态变化

- 主题：
  之前判断：
  当前判断：
  变化原因：

### 工程启发

- 启发：
  对我们的影响：

### 备注

- 
```

## 来源说明

- 优先使用官方博客、官方文档和高信号开源项目主页
- 这份文档关注的是 `工程基础设施信号`，不是模型效果榜单

## 2026-04-06 当周补充

### 新增条目

- 条目：`OpenAI Model Spec + Model Spec Evals`
  方向：`behavior spec / eval infrastructure`
  核心信号：OpenAI 已把模型行为规范和场景化 eval 绑定发布，明确要用它们发现 `model behavior` 与 `spec` 的偏差。
  为什么重要：这意味着 agent infra 的一部分已经变成“如何把行为边界写成可测规范”。
  建议动作：后续内部 infra 设计不要只做 tool/runtime，也要给 `spec -> eval -> incident` 留接口。
  来源：https://openai.com/index/our-approach-to-the-model-spec/

- 条目：`How we monitor internal coding agents for misalignment`
  方向：`production monitoring / governance`
  核心信号：OpenAI 把对内部 coding agent 的 `full-trajectory monitoring`、分级告警和人工复核做成常态化流程。
  为什么重要：真实的长时 agent 平台，最终都会碰到 `observability + policy enforcement + incident response`。
  建议动作：把 `trajectory logging`、`severity levels`、`human escalation` 补入内部最小 infra 清单。
  来源：https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/

- 条目：`Claude Sonnet 4.6 product updates` `补录`
  方向：`context compaction / tool search / code execution / MCP surface`
  核心信号：Anthropic 已在公开产品说明里把 `context compaction beta`、`memory`、`tool search`、`code execution` 和 `Excel MCP connectors` 放到同一层说明。
  为什么重要：这说明 `MCP` 和 `memory` 已开始进入更普通用户可感知的产品层，而不是只在工程博客里存在。
  建议动作：把 `connector portability` 和 `compaction` 一起纳入长期 infra 维度。
  来源：https://www.anthropic.com/news/claude-sonnet-4-6

- 条目：`GitHub 周榜：hermes-agent / oh-my-claudecode / oh-my-openagent / compound-engineering-plugin / honcho / agent-framework`
  方向：`open-source infra signal`
  核心信号：本周热点把 `stateful agent`、`multi-agent orchestration`、`plugin portability`、`memory library`、`deploy framework` 同时推上来。
  为什么重要：开源侧正在把 infra 抽象从单一 product wrapper 升级为更清楚的分层组件。
  建议动作：后续优先比较它们的分层方式，而不是只比较 stars。
  来源：https://github.com/trending/python?since=weekly ; https://github.com/trending/typescript?since=weekly

### 状态变化

- 主题：`MCP`
  之前判断：MCP 正在成为连接层主线。
  当前判断：MCP 不只在协议层推进，也开始渗透到具体产品入口和插件生态兼容层。
  变化原因：Anthropic 在产品说明中已直接把 `MCP connectors` 暴露给 Excel 等工作流场景。

- 主题：`runtime`
  之前判断：`shell / container / sandbox / state` 是默认能力边界。
  当前判断：还需要显式补上 `monitoring / triage / policy enforcement`，否则长时运行不可控。
  变化原因：OpenAI 的内部监控文章把这块直接公开化了。

### 工程启发

- 启发：`spec`、`runtime`、`monitoring` 三者正在收敛成一套系统，而不是各自独立。
  对我们的影响：后续如果只做工具层，不做行为规范和异常处置，会留下明显缺口。

## 2026-04-11 当周补充

### 新增条目

- 条目：`Claude Code auto mode`
  方向：`permission automation / safety guardrails`
  核心信号：Anthropic 已把 `classifier`、`prompt-injection probe`、`trusted boundary` 组合成运行时自动审批机制。
  为什么重要：这比单纯的“是否 sandbox”更接近真实生产 agent 的自治边界设计。
  建议动作：把 `auto approval`、`transcript classifier`、`approval fatigue` 加入我们的最小 infra 术语表。
  来源：https://www.anthropic.com/engineering/claude-code-auto-mode

- 条目：`Harness design for long-running application development`
  方向：`multi-agent harness / evaluator loop / handoff`
  核心信号：Anthropic 明确把 `planner + generator + evaluator`、`Playwright MCP`、`structured artifact handoff` 作为长流程软件交付的有效模式。
  为什么重要：这说明前沿 coding agent 的关键竞争点已从“会不会写代码”转向“能否在多小时流程中稳定交付”。
  建议动作：把 `evaluator agent` 和 `artifact-based handoff` 纳入内部基线设计。
  来源：https://www.anthropic.com/engineering/harness-design-long-running-apps

- 条目：`Scaling Managed Agents: Decoupling the brain from the hands`
  方向：`managed agents / session-harness-sandbox split`
  核心信号：Anthropic 开始把 `session`、`harness`、`sandbox` 明确虚拟化成稳定接口，强调 `brain / hands / session` 解耦、凭证隔离和可恢复长时执行。
  为什么重要：这是一篇非常强的“agent infra 不是 prompt orchestration，而是系统设计”信号。
  建议动作：后续对 runtime 架构的记录，默认分成 `context store`、`orchestration loop`、`execution environment` 三层来比较。
  来源：https://www.anthropic.com/engineering/managed-agents

- 条目：`Quantifying infrastructure noise in agentic coding evals`
  方向：`infra measurement / benchmark rigor`
  核心信号：Anthropic 已把 `resource headroom`、`sandbox enforcement`、`time budget` 是否一致，视作 agentic coding benchmark 的一等变量。
  为什么重要：这意味着 infra 团队配置本身会改变 leaderboard 结果，评测和基础设施已不可分。
  建议动作：今后记录 benchmark 结果时，附带记录资源与 sandbox 条件，不再只记录分数。
  来源：https://www.anthropic.com/engineering/infrastructure-noise ; https://www.anthropic.com/engineering

- 条目：`Google AI Studio / Antigravity / Gemini Live API`
  方向：`developer platform / live agent runtime`
  核心信号：Google 已把 `Antigravity coding agent`、`Live API`、`session management`、`function calling` 明确写入开发者叙事。
  为什么重要：Google 的 agent infra 过去表达偏散，这轮开始出现更完整的平台化入口。
  建议动作：把 `Google developer agent stack` 从观察项上调到正式比较对象。
  来源：https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-march-2026/ ; https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-3-1-flash-live/

- 条目：`OpenAI enterprise operating layer`
  方向：`enterprise agent deployment / unified agent stack`
  核心信号：OpenAI 已把 `Frontier`、`stateful runtime`、`unified AI superapp`、`company-wide agents` 写成同一企业平台叙事。
  为什么重要：这说明 `runtime` 在 OpenAI 这边已经不只是开发者能力，而是企业级操作层。
  建议动作：后续比较平台路线时，把 `developer runtime` 和 `enterprise runtime` 分开记，但放在同一架构图里。
  来源：https://openai.com/index/next-phase-of-enterprise-ai/

### 状态变化

- 主题：`runtime`
  之前判断：`shell / container / sandbox / state` 是默认能力边界。
  当前判断：还必须显式补上 `permission automation` 和 `session-harness-sandbox` 的架构拆分。
  变化原因：Anthropic 最近两篇工程文章把这两点都公开化了。

- 主题：`评测与基础设施的关系`
  之前判断：评测是 runtime 的旁路能力。
  当前判断：在 agentic coding 里，评测、资源配额、sandbox enforcement 已变成同一系统的不同切面。
  变化原因：`infrastructure noise` 文章直接证明了 infra 配置会改变 benchmark 结果。
