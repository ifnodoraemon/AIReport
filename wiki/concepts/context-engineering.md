# Context Engineering

最后更新：2026-04-06

关联总览：

- [MCP-tools-agent-infra追踪](/home/ifnodoraemon/myreport/MCP-tools-agent-infra追踪.md)
- [agent-llm周GitHub热点追踪](/home/ifnodoraemon/myreport/agent-llm周GitHub热点追踪.md)
- [AI关键人物追踪](/home/ifnodoraemon/myreport/AI关键人物追踪.md)
- [wiki/concepts/memory.md](./memory.md)

## 这是什么

`context engineering` 指的不是“把 prompt 写得更漂亮”，而是系统性设计 agent 在任务中能看到什么、保留什么、压缩什么、传递什么。

## 为什么重要

当前公开信号已经很一致：

- `OpenAI` 在讲 `compaction`、`container context`、`skills`
- `Anthropic` 在讲 `progress notes`、`handoff artifacts`、`context compaction`
- GitHub 热点在做 `context database`
- `Karpathy` 开始把知识组织问题写成 `LLM Wiki`
- `Andrew Ng` 侧的 `Context Hub` 说明这已经进入开发者工具层

这意味着 `context` 不再只是模型输入，而是独立工程层。

## 当前判断

### 1. context engineering 是 agent 能否长时稳定运行的核心

它决定：

- agent 看到的事实是否干净
- 多轮任务是否会漂移
- handoff 是否可持续
- 成本是否可控

### 2. 它至少包含四件事

- context selection
- context compaction
- context handoff
- context grounding

### 3. 它和 memory 高度重叠，但不等于 memory

- `memory` 更强调长期保留和更新
- `context engineering` 更强调当前任务里如何组织与交付上下文

## 当前最值得跟的实现方向

### `compaction / notes / handoff artifacts`

- 更偏长时任务稳定性

### `context database / shared doc hub`

- 更偏开发者和组织级知识交付

### `LLM Wiki`

- 更偏知识编译和持续积累

## 还要继续观察什么

- `context engineering` 是否会成为平台默认能力，而不是 agent 应用层自己补
- 它会如何与 `memory`、`MCP`、`monitoring` 收敛成统一系统
