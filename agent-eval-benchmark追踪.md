# Agent Eval / Benchmark 追踪

最后更新：2026-03-25

参考文档：`/home/ifnodoraemon/myreport/agent-llm周论文追踪.md`、`/home/ifnodoraemon/myreport/AI三巨头博客追踪.md`

跟踪范围：近期与 `agent eval`、`long-horizon benchmark`、`subjective quality`、`production eval`、`memory eval`、`tool use eval` 相关的高信号论文、博客和方法学

## 目的

这份文件作为长期维护的评测记录，用于：

- 统一收口 `benchmark`、`grader`、`rubric`、`online eval`、`human review`
- 区分哪些评测适合研究验证，哪些适合真实生产系统
- 跟踪 agent 评测从单轮正确率向长流程和真实任务迁移的趋势
- 为内部评测设计提供稳定参考

## 当前判断

当前最值得关注的高信号主题：

1. `agent eval` 已经不能停留在单轮问答正确率，必须覆盖 `multi-step`、`tool use`、`memory`、`handoff`。
2. 纯 benchmark 分数已经不够，`自动 grader + 人审校准 + 生产监控` 正在成为更现实的组合。
3. 对我们最有价值的评测，不是最知名的 benchmark，而是最接近真实工作流的 benchmark。

## 跟踪表

| 来源 | 日期 | 条目 | 方向 | 核心信号 | 与我们的相关性 | 优先级 | 建议动作 | 来源 |
|---|---|---|---|---|---|---|---|---|
| Anthropic | 2026-01-09 | Demystifying evals for AI agents | Agent eval 方法学 | 把 `task`、`trial`、`grader`、`transcript`、`human review` 讲成一套完整方法论 | 这是内部 agent eval 框架的直接参考 | P0 | 先按这套术语建立内部评测框架草案 | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents |
| Anthropic | 2026-01-21 | Designing AI-resistant technical evaluations | AI 时代评测失效 | 说明旧的技术评测很容易被模型穿透，必须重新设计更抗 AI 的任务 | 如果我们做招聘或内部能力测试，这篇很关键 | P0 | 重新审视现有 take-home test 和评测任务 | https://www.anthropic.com/engineering/AI-resistant-technical-evaluations |
| OpenReview | 2025-01-25 | Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | Memory eval | memory 评测至少要覆盖 `retrieval`、`test-time learning`、`long-range understanding`、`selective forgetting` | 对 persistent agent 设计非常直接 | P0 | 把四个维度转成最小 memory rubric | https://openreview.net/forum?id=DT7JyQC3MR |
| OpenReview | 2025-01-25 | MobileMem | Long-horizon memory benchmark | 真实移动场景下的长期记忆评测，比纯对话型 benchmark 更接近真实用户任务 | 如果做跨 session agent，这条线很重要 | P0 | 给内部评测补跨 session、跨 app 场景 | https://openreview.net/forum?id=w5I11HrMgJ |
| arXiv recent / 待读 | 2026-03-25 snapshot | Beyond Binary Correctness: Scaling Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks | 长流程 / 主观型评测 | 高信号方向是从 `pass/fail` 转向企业任务中的质量 rubric | 对真实业务任务尤其相关 | P1 | 继续跟进并抽取适合内部的主观评价维度 | https://arxiv.org/list/cs.AI/recent |
| OpenAI 博客信号 | 2026-03-17 | GPT-5.4 / GDPval / tool search | Frontier eval / tool-use eval | OpenAI 已把 `tool search` 和更复杂的能力评估绑定在模型发布叙事里 | 说明 tool-use eval 已成为旗舰模型必答题 | P1 | 把 `tool search` 单独列成模型评测项 | https://openai.com/index/introducing-gpt-5-4/ |

## 横向观察

### 1. `Memory eval` 是最容易被低估的部分

- 单轮 benchmark 很难揭示长期记忆问题
- `跨 session`、`更新正确性`、`遗忘行为` 更接近真实风险

### 2. `Long-horizon eval` 才能区分真 agent 和 prompt 包装

- 会回答不等于会完成任务
- 评测必须覆盖 `计划`、`执行`、`恢复`、`交接`

### 3. `主观质量评测` 会越来越重要

- 企业任务经常无法二元打分
- 后续需要更多 `rubric-based` 评测而不是单一 success rate

## 当前优先级

### P0

- 建立内部 `memory eval` 最小清单
- 建立内部 `tool use / long-horizon task` 评测项
- 定义 `自动 grader + 人审校准` 的组合方式

### P1

- 跟踪主观型和企业型 benchmark
- 跟踪生产环境下的在线评测与质量监控

## 近期建议动作

### 本周

- 定义最小 `memory rubric`：检索准确率、更新正确性、长程一致性、遗忘行为
- 定义最小 `agent rubric`：任务完成度、工具调用质量、恢复能力、输出可用性

### 未来两周

- 把内部任务按 `单轮`、`多轮`、`长流程`、`生产监控` 四层分类
- 补一组真实工作流样例，而不是只做 synthetic benchmark

## 每周更新模板

每周更新时复制下面这段：

```md
## YYYY-MM-DD 当周

### 新增 benchmark / 方法

- 条目：
  类型：
  核心信号：
  为什么重要：
  建议动作：

### 状态变化

- 主题：
  之前判断：
  当前判断：
  变化原因：

### 内部评测启发

- 启发：
  对我们的影响：

### 备注

- 
```

## 来源说明

- 优先使用论文主页、官方工程博客和模型发布页
- 对尚未完整阅读的条目，统一视为趋势信号，不直接当作最终结论

