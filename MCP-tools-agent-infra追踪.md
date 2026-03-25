# MCP / Tools / Agent Infra 追踪

最后更新：2026-03-25

参考文档：`/home/ifnodoraemon/myreport/AI三巨头博客追踪.md`、`/home/ifnodoraemon/myreport/agent-llm周GitHub热点追踪.md`

跟踪范围：近期与 `MCP`、`tool use`、`code execution`、`sandbox`、`agent runtime`、`context compaction`、`skills`、`stateful execution` 相关的高信号工程进展

## 目的

这份文件作为长期维护的 agent 基础设施记录，用于：

- 追踪 `MCP` 是否正在成为事实标准
- 追踪 agent 从“会回答”转向“能执行”的关键工程层
- 记录 `runtime`、`sandbox`、`state`、`skills`、`handoff` 的公开最佳实践
- 帮助我们判断哪些基础设施已经进入产品主线，哪些还只是概念包装

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

