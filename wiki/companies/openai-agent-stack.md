# OpenAI Agent Stack

最后更新：2026-04-06

关联总览：

- [AI三巨头博客追踪](/home/ifnodoraemon/myreport/AI三巨头博客追踪.md)
- [MCP-tools-agent-infra追踪](/home/ifnodoraemon/myreport/MCP-tools-agent-infra追踪.md)
- [模型发布追踪](/home/ifnodoraemon/myreport/模型发布追踪.md)
- [wiki/models/gpt-5-4.md](../models/gpt-5-4.md)

## 这是什么

这里说的 `OpenAI agent stack`，不是单个模型或单个 API，而是 OpenAI 最近公开叙事里逐渐拼起来的一整套 agent 平台能力。

## 主要组成

- `GPT-5.4`
- `Responses API`
- `computer environment`
- `shell / container`
- `Model Spec`
- `Model Spec Evals`
- `internal coding-agent monitoring`
- `Codex / harness engineering`

## 为什么重要

如果只看某一次模型发布，会低估 OpenAI 真正在做的事。

更准确的判断是：

- 模型是核心能力层
- runtime 是执行层
- spec / eval 是行为约束层
- monitoring 是上线后的治理层

这四层正在收敛成一套更完整的 agent 平台。

## 当前判断

### 1. OpenAI 不再只是在卖模型

更像是在卖：

- `agent-ready model`
- `execution environment`
- `governance layer`

### 2. `spec + runtime + monitoring` 是最值得注意的组合

这说明真正难的已经不是“会不会调用工具”，而是：

- 任务能不能跑得久
- 行为边界能不能定义
- 异常能不能被发现和处置

### 3. 这对我们意味着什么

如果我们只学：

- prompt
- function calling

而不学：

- context / runtime
- spec / eval
- monitoring / incident handling

那会明显跟不上这条主线。

## 还要继续观察什么

- OpenAI 是否会继续把 `tool search`、`skills`、`compaction` 深化成标准平台能力
- `Codex`、`Responses API`、`computer environment` 的边界会如何收敛
- 行为规范是否会继续从 `Model Spec` 扩展到更强的开发者接口

## 主要来源

- https://openai.com/index/introducing-gpt-5-4/
- https://openai.com/index/equip-responses-api-computer-environment/
- https://openai.com/index/harness-engineering/
- https://openai.com/index/our-approach-to-the-model-spec/
- https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/
