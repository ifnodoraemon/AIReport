# Andrej Karpathy

最后更新：2026-04-06

关联总览：

- [AI关键人物追踪](/home/ifnodoraemon/myreport/AI关键人物追踪.md)
- [MCP-tools-agent-infra追踪](/home/ifnodoraemon/myreport/MCP-tools-agent-infra追踪.md)

## 角色

- `Eureka Labs` 创始人
- 高信号技术解释者
- 在 `LLM / agent / harness / education` 上有持续影响力

## 为什么重要

Karpathy 的价值不主要在“公司路线图”，而在于：

- 提前说清楚工程范式变化
- 给出足够小、足够清晰的最小实现
- 把复杂系统问题压缩成可以动手实践的形式

## 最近高信号动作

### 1. `llm-wiki.md`

- 日期：`2026-04-04`
- 来源：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 核心：把知识系统从“临时 RAG”改成“持续维护的 wiki”

当前判断：

- 这不是普通笔记方法，而是 `memory-first + context engineering` 的一个很强工程化表达
- 对当前仓库尤其相关，因为本仓库天然适合从追踪文档过渡到 wiki

### 2. `microgpt.py`

- 最近可确认活跃更新时间：`2026-03-13`
- 来源：https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95
- 核心：继续维护最小可理解 LLM 实现

当前判断：

- Karpathy 仍然重视“最小实现 + 可教学 + 可实验”
- 这类输出适合当作内部学习和原型参考，不适合直接当生产方案

### 3. `testable / observable / legible`

- 来源：https://x.com/karpathy/status/2026738848420737474
- 核心：要把工作变成 `testable / observable / legible`，agent 才能进入更长循环

当前判断：

- 这和 `runtime + eval + monitoring` 主线高度一致
- Karpathy 这条线更像“工程范式早期信号源”

## 应该重点跟什么

- 新的 `gist`
- 关于 `agent research`、`observability`、`CLI / web / API` 的 `X` 发言
- 是否出现更完整的 `LLM Wiki` 或 `autoresearch` 实践

## 暂不该过度解读什么

- 单条概念性发言
- 未被后续 gist、代码或官网内容支撑的试探性想法
