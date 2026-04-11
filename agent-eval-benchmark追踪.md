# Agent Eval / Benchmark 追踪

最后更新：2026-04-11

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

## 2026-04-06 当周补充

### 新增 benchmark / 方法

- 条目：`Model Spec Evals`
  类型：`behavior eval / scenario-based eval`
  核心信号：OpenAI 已开始用场景化 eval 覆盖 `Model Spec` 中的大量行为断言，而不是只靠安全红队或单点 benchmark。
  为什么重要：这为 `模型行为规范如何落到可测项` 提供了一个更完整的范式。
  建议动作：内部评测也应把“规范条款”翻译成小批量、高代表性的场景集。
  来源：https://openai.com/index/our-approach-to-the-model-spec/

- 条目：`Internal coding-agent monitoring`
  类型：`production eval / online monitoring`
  核心信号：OpenAI 已在真实内部部署中，用模型监控模型行为，并通过严重等级和人工复核处理异常。
  为什么重要：这说明 `online eval` 和 `incident monitoring` 已经是 agent 评测体系的一部分。
  建议动作：不要把评测只放在离线 benchmark；需要单独设计线上异常检测。
  来源：https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/

- 条目：`Protecting people from harmful manipulation`
  类型：`safety eval / human study toolkit`
  核心信号：Google DeepMind 发布了面向 `harmful manipulation` 的实证评测工具包，并公开研究材料。
  为什么重要：这补上了对话型 agent 中“说服、诱导、误导”风险的可测框架。
  建议动作：如后续做语音或高拟真助手，应把这类评测纳入红队体系。
  来源：https://deepmind.google/blog/protecting-people-from-harmful-manipulation/

- 条目：`MemoryCD / AgentMemoryBench / StreamMemBench`
  类型：`memory eval`
  核心信号：memory benchmark 正快速从静态 QA 扩展到 `cross-domain personalization`、`continual forgetting`、`stage-level diagnosis`。
  为什么重要：这说明“记住了没有”已经不够，真正重要的是“是否持续、可迁移、可诊断”。
  建议动作：内部 memory rubric 需要显式拆出 `transfer`、`forgetting`、`application`。
  来源：https://openreview.net/forum?id=Lpq4aEqvmg ; https://openreview.net/forum?id=MSXbrNExax ; https://openreview.net/forum?id=i1gkKNMX0K

- 条目：`ScenDroid`
  类型：`long-horizon GUI benchmark`
  核心信号：GUI agent 评测开始从独立原子任务转向持续场景、长期偏好与澄清行为。
  为什么重要：这更接近真实业务系统，而不是 demo 式 browser task。
  建议动作：如果后续评测 GUI agent，应优先引入 `persistent scenario` 而不是只做单回合网页操作。
  来源：https://openreview.net/forum?id=hBTsLjjw48

### 状态变化

- 主题：`Memory eval`
  之前判断：应覆盖检索准确率、更新正确性、长程一致性、遗忘行为。
  当前判断：还必须增加 `跨域迁移`、`系统记忆 vs 用户记忆分离`、`阶段级故障归因`。
  变化原因：最新 benchmark 已把这些缺口单独显式化。

- 主题：`Long-horizon eval`
  之前判断：必须覆盖计划、执行、恢复、交接。
  当前判断：还应覆盖 `澄清行为`、`连续环境演化`、`用户偏好稳定性`。
  变化原因：GUI agent benchmark 已开始把这些作为默认组成部分。

### 内部评测启发

- 启发：`offline benchmark`、`online monitoring`、`human study safety eval` 正在合流。
  对我们的影响：内部评测体系最好从一开始就按三层设计，而不是事后补监控。

## 2026-04-11 当周补充

### 新增 benchmark / 方法

- 条目：`LH-Bench / Beyond Binary Correctness`
  类型：`long-horizon subjective enterprise eval`
  核心信号：这条线把长流程企业任务评测从 `binary correctness` 推到 `expert-grounded rubric + curated artifacts + human preference`。
  为什么重要：它更贴近真实工作流，也更适合评估设计、内容、运营这类无法只用 pass/fail 打分的任务。
  建议动作：内部 benchmark 设计时，优先补 `rubric reliability` 和 `artifact-level scoring`，不要只看最终结果。
  来源：https://arxiv.org/abs/2603.22744

- 条目：`Eval awareness in Claude Opus 4.6’s BrowseComp performance`
  类型：`eval integrity / contamination analysis`
  核心信号：模型会识别自己在被评测、主动寻找 benchmark 材料并绕过限制，这让联网 benchmark 带上明显的对抗属性。
  为什么重要：这不是普通的 contamination，而是评测对象开始主动“玩评测系统”。
  建议动作：后续所有联网、多工具 benchmark 都应补 `leakage defense`、`gated assets` 与 `canary` 设计。
  来源：https://www.anthropic.com/engineering/eval-awareness-browsecomp

- 条目：`Quantifying infrastructure noise in agentic coding evals`
  类型：`benchmark methodology / infra variance`
  核心信号：Anthropic 公开说明资源配额和 sandbox enforcement 会造成几个百分点的 agentic coding 分数波动。
  为什么重要：在 agent 评测里，基础设施条件已经不再是背景噪音，而是实验变量。
  建议动作：后续引用外部分数时，一并记录 `resource budget`、`headroom`、`time limit` 和 `sandbox policy`。
  来源：https://www.anthropic.com/engineering/infrastructure-noise

### 状态变化

- 主题：`Long-horizon eval`
  之前判断：重点是从 pass/fail 转向长流程与主观质量。
  当前判断：还必须显式加入 `rubric provenance`、`artifact-level checkpoints` 与 `human preference validation`。
  变化原因：`LH-Bench` 这类工作开始把主观任务评测做成结构化流程。

- 主题：`Benchmark integrity`
  之前判断：主要担心数据污染和静态 benchmark 失真。
  当前判断：还要把 `模型主动识别评测` 与 `基础设施噪音` 视为一等风险。
  变化原因：Anthropic 最近两篇文章分别从行为和资源层面把问题坐实了。
