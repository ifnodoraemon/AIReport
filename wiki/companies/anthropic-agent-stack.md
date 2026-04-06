# Anthropic Agent Stack

最后更新：2026-04-06

关联总览：

- [AI三巨头博客追踪](/home/ifnodoraemon/myreport/AI三巨头博客追踪.md)
- [MCP-tools-agent-infra追踪](/home/ifnodoraemon/myreport/MCP-tools-agent-infra追踪.md)
- [AI关键人物追踪](/home/ifnodoraemon/myreport/AI关键人物追踪.md)

## 这是什么

这里说的 `Anthropic agent stack`，指的是 Anthropic 最近公开表达里逐渐成型的一整套 `coding / agents / MCP / eval / safety` 组合。

## 主要组成

- `Claude Opus 4.6`
- `Claude Sonnet 4.6`
- `Claude Code`
- `MCP`
- `code execution`
- `context compaction`
- `long-running harness`
- `agent eval`
- `Anthropic Institute`

## 为什么重要

Anthropic 现在最值得关注的，不是单篇模型发布，而是它把：

- `powerful coding agents`
- `MCP ecosystem`
- `eval discipline`
- `policy / safety interface`

放到了一起。

## 当前判断

### 1. Anthropic 更像 `coding agent + MCP + eval discipline`

- 相比 OpenAI，更强调 `coding`
- 相比 Google，更强调 `agent workflow discipline`

### 2. `MCP + long-running harness` 是它的明显特征

- `progress notes`
- `handoff artifacts`
- `code execution`
- `context compaction`

这些都说明 Anthropic 对长流程 agent 的理解更偏工程现实。

### 3. 安全与治理不是外围叙事

- `Anthropic Institute`
- 政府合作
- eval 方法学

这些都说明它在试图把能力和治理一起产品化、组织化。

## 还要继续观察什么

- `MCP` 是否会继续成为 Anthropic 的生态主轴
- `Claude Code` 和模型层的边界会如何收敛
- `eval / safety / policy` 是否会继续成为产品叙事的默认部分

## 主要来源

- https://www.anthropic.com/news/claude-opus-4-6
- https://www.anthropic.com/news/claude-sonnet-4-6
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- https://www.anthropic.com/engineering/code-execution-with-mcp
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- https://www.anthropic.com/news/the-anthropic-institute?s=09
