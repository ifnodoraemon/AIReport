# Memory

最后更新：2026-04-06

关联总览：

- [agent-llm周论文追踪](/home/ifnodoraemon/myreport/agent-llm周论文追踪.md)
- [agent-eval-benchmark追踪](/home/ifnodoraemon/myreport/agent-eval-benchmark追踪.md)
- [agent-llm周GitHub热点追踪](/home/ifnodoraemon/myreport/agent-llm周GitHub热点追踪.md)
- [MCP-tools-agent-infra追踪](/home/ifnodoraemon/myreport/MCP-tools-agent-infra追踪.md)

## 这是什么

这里的 `memory` 不是“上下文窗口更长”，而是 agent 在多轮、多任务、跨 session 工作中持续保留、更新、调用知识和状态的能力。

## 为什么重要

当前几乎所有高信号来源都在强化同一个判断：

- 论文在补 `memory benchmark`
- GitHub 在做 `cross-session memory`、`context database`
- 产品在推 `context compaction`、`memory`、`handoff`
- Karpathy 这类人物开始直接把知识组织问题写成 `LLM Wiki`

这说明 `memory` 已经从研究话题变成工程主线。

## 当前判断

### 1. memory 是一等系统能力

它不再只是外挂向量库，而是影响：

- agent 连续性
- 工具调用质量
- handoff 稳定性
- 成本和上下文利用率

### 2. memory 至少有四层

- `short-term context`
- `cross-session memory`
- `structured knowledge`
- `memory-to-action`

### 3. 评测必须拆开做

不能只测“答没答对”，至少要分：

- retrieval
- update correctness
- forgetting
- cross-session continuity
- memory application

## 当前最值得跟的实现方向

### `LLM Wiki`

- 更偏知识编译层
- 适合长期研究、情报、项目知识库

### `context database / memory library`

- 更偏基础设施组件
- 适合嵌入现有 agent runtime

### `cross-session memory plugin`

- 更偏产品接入层
- 适合快速验证体验价值

## 还要继续观察什么

- `memory` 是否会从 agent 功能扩展成标准平台能力
- `retrieval-stage defense` 是否会和 memory 层合流
- `wiki / graph / database` 三种组织形态最终会如何分工
