# Agent / LLM 每周跟踪

最后更新：2026-04-06

跟踪范围：近期与 `agent`、`LLM`、`memory`、`RAG 安全`、`评测` 相关的论文与趋势

## 目的

这份文件作为长期维护的每周跟踪记录，用于：

- 跟踪值得关注的 agent / LLM 新论文
- 记录这些论文对我们工作的实际影响
- 记录建议实验与后续动作
- 按周更新状态变化与新增风险信号

## 当前判断

当前最值得关注的高信号主题：

1. `Agentic RL` 正在从 prompt orchestration 转向训练与基础设施问题。
2. `Memory` 正在成为 agent 的一等能力，而不只是外挂向量库。
3. `RAG / agent 安全` 需要覆盖语料投毒和 reranking 层风险，不能只盯 prompt injection。
4. `评测` 正在从二元成功率转向长流程、主观质量和真实企业任务。

## 跟踪表

| 论文 | 主题 | 核心结论 | 与我们的相关性 | 优先级 | 建议动作 | 状态 | 来源 |
|---|---|---|---|---|---|---|---|
| ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning | Agentic RL | Agent 训练不稳定是核心瓶颈之一，论文给出更稳定的训练 recipe 和统一分析框架 | 如果我们想做可训练 agent，而不是只做 orchestration，这篇很重要 | P1 | 复用其分析维度，指导我们的 agent 训练与日志设计 | 跟踪中 | https://arxiv.org/abs/2602.21534 |
| AgentRL: Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task Framework | Agentic RL | 将 agent 训练推进到多轮、多任务、异步 pipeline 和统一 function-call 接口 | 对长期 agent 平台设计有参考价值 | P2 | 在投入 RL 之前，先研究其 pipeline 和数据 / 日志结构 | 跟踪中 | https://openreview.net/forum?id=zq3vAmuUk9 |
| Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions | Memory | Memory 应同时覆盖检索正确率、测试时学习、长程理解、选择性遗忘四个维度 | 如果我们构建 persistent agent，这篇直接相关 | P0 | 将其 memory 维度转成内部评测标准 | 可执行 | https://openreview.net/forum?id=DT7JyQC3MR |
| MobileMem: Evaluating Long-Horizon Memory for Language Agents in Real-World Mobile Environments | Memory | 真实个性化 memory 需要来自用户行为的长期记忆，而不只是对话历史 | 对个性化助手和真实用户建模高度相关 | P0 | 在内部 benchmark 中加入跨 session、跨 app 的 memory 场景 | 可执行 | https://openreview.net/forum?id=w5I11HrMgJ |
| CamoDocs: Poisoning Attack against Retrieval-Augmented Language Models | RAG 安全 | RAG 容易受到更隐蔽的语料投毒攻击，传统仅面向 prompt 的 threat model 不够 | 任何接外部知识的系统都直接受影响 | P0 | 做一次离线 corpus poisoning 红队测试 | 可执行 | https://openreview.net/forum?id=1azfkKV93x |
| Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation | RAG 安全 | 安全评估需要考虑竞争攻击者，而不是只假设单一 adversary | 对开放语料场景下的真实威胁建模很重要 | P1 | 扩展 threat model 和攻击模拟假设 | 跟踪中 | https://openreview.net/forum?id=nBta7psl5J |
| Knowledge Access Beats Model Size: Memory Augmented Routing for Persistent AI Agents | Memory / Routing | 从标题判断，persistent agent 的效果可能更受知识访问与路由设计影响，而不是单纯模型大小 | 如果我们在模型规模和系统架构之间做权衡，这篇可能重要 | P1 | 待摘要 / 全文可读后优先确认其 routing 方法是否可落地 | 待读 | https://arxiv.org/list/cs.CL/recent |
| PERMA: Benchmarking Personalized Memory Agents via Event-Driven Preference and Realistic Task Environments | 个性化 Memory | 从标题判断，这篇可能是面向事件与偏好的现实化个性记忆 benchmark | 如果个性化在 roadmap 上，值得持续跟踪 | P1 | 先读 benchmark 设计，再判断是否映射到内部任务 | 待读 | https://arxiv.org/list/cs.AI/recent |
| MemCollab: Cross-Agent Memory Collaboration via Contrastive Trajectory Distillation | 多 Agent Memory | 从标题判断，重点是 agent 间的记忆共享与蒸馏 | 只有在我们确定走多 agent 路线时才高度相关 | P2 | 重点检查它是否真的提升 memory 质量，而不只是协作包装 | 待读 | https://arxiv.org/list/cs.AI/recent |
| ProGRank: Probe-Gradient Reranking to Defend Dense-Retriever RAG from Corpus Poisoning | RAG 防御 | 从标题判断，reranking 层可能会成为实用的抗投毒控制点 | 对我们有潜在价值，因为 reranker 防御更容易渐进集成 | P1 | 先读摘要和实验结果，再判断是否值得做最小 PoC | 待读 | https://arxiv.org/list/cs.AI/recent |
| Beyond Binary Correctness: Scaling Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks | 评测 | 从标题判断，agent 评测正在从成功 / 失败转向企业任务中的主观质量评价 | 如果我们的任务无法完全自动判分，这篇很相关 | P1 | 将评测从 pass/fail 扩展到 quality rubric | 待读 | https://arxiv.org/list/cs.AI/recent |
| Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models | Agent 控制 | 从标题判断，world-model 风格的 steering 可能帮助 agent 提前校正动作与计划 | 如果我们遇到 action drift 或计划执行不稳定，这个方向值得关注 | P2 | 等我们开始做 steering / control 质量优化时再重点阅读 | 待读 | https://arxiv.org/list/cs.AI/recent |

## 当前优先级

### P0

- 基于近期 benchmark 维度，建立内部 `memory` 评测清单
- 做一次离线 `RAG corpus poisoning` 红队测试

### P1

- 提升 `长流程 agent 评测`，尤其是主观型或企业型任务
- 持续跟进 `knowledge routing`、`个性化 memory`、`reranking 层防御`

### P2

- 跟踪 `agentic RL` 的训练基础设施和训练 recipe
- 仅在产品方向明确需要时，再投入 `多 agent memory / collaboration`

## 近期建议动作

### 本周

- 定义最小 memory 评测 rubric：检索准确率、更新正确性、遗忘行为、长程一致性
- 定义最小 RAG 安全测试集：投毒文档、良性邻居伪装、reranker 压力样例

### 未来两周

- 统一 agent 运行日志格式，支持 step-level 分析
- 在评测中加入长流程与主观质量指标

### 本月

- 决定近期平台策略更偏 `memory-first` 还是 `training-first`
- 当前默认建议：`memory-first`，除非我们已经具备较强的多轮训练 pipeline

## 每周更新模板

每周更新时复制下面这段：

```md
## YYYY-MM-DD 当周

### 新增论文

- 论文：
  为什么重要：
  建议动作：

### 状态变化

- 论文：
  之前状态：
  当前状态：
  变化原因：

### 新风险 / 新信号

- 信号：
  对我们的影响：

### 实验 / 跟进项

- 项目：
  负责人：
  截止日期：
  状态：

### 备注

- 
```

## 置信度说明

- 直接有 arXiv 或 OpenReview 论文页面支撑的条目，置信度更高。
- 来自 `2026-03-25` arXiv recent 列表、但尚未完整阅读的论文，统一标记为 `待读`，应视为趋势信号，而不是最终结论。

## 2026-04-06 当周补充

### 新增论文

- 论文：`MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization`
  为什么重要：把长期记忆 benchmark 从“合成 persona 对话”推进到“跨年、跨域、真实用户行为”，更接近真实个性化助手。
  建议动作：如果我们做 persistent agent，优先吸收它的 `cross-domain` 和 `life-long` 设计。
  状态：`可执行`
  来源：https://openreview.net/forum?id=Lpq4aEqvmg

- 论文：`Benchmarking Continual Agent Memory for Online Learning, Transfer, and Forgetting` `AgentMemoryBench`
  为什么重要：把 `system memory` 和 `personal memory` 放在同一框架下评估，并显式覆盖 `improvement / retention / forgetting / conflict resolution`。
  建议动作：把“系统经验记忆”和“用户偏好记忆”拆成两条内部指标，不再混着评。
  状态：`可执行`
  来源：https://openreview.net/forum?id=MSXbrNExax

- 论文：`Streaming Memory Benchmark: Stage-level Diagnosis with Evidence Dependency Control`
  为什么重要：它不只看最终答对没答对，而是把 memory pipeline 拆成 `formation / management / retrieval / application` 四段诊断。
  建议动作：内部 memory eval 里加入阶段级指标，否则很难知道失败是存储、检索还是应用问题。
  状态：`可执行`
  来源：https://openreview.net/forum?id=i1gkKNMX0K

- 论文：`ScenDroid: A Scenario-Level Benchmark for Long-Horizon, Time-Evolving GUI Agents`
  为什么重要：GUI agent benchmark 开始从 `atomic reset` 走向 `persistent scenario`，并显式纳入长期偏好和连续工作流。
  建议动作：把 GUI agent 评测从单步成功率升级到 `scenario continuity` 和 `clarification behavior`。
  状态：`跟踪中`
  来源：https://openreview.net/forum?id=hBTsLjjw48

- 论文：`Mem2ActBench: A Benchmark for Evaluating Long-Term Memory Utilization in Task-Oriented Autonomous Agents`
  为什么重要：把 memory 评测从“能不能答出旧信息”推进到“能不能用记忆补全工具调用参数并执行动作”。
  建议动作：后续内部 benchmark 应单独测 `memory -> tool parameter grounding`，不要只测 QA 回忆。
  状态：`跟踪中`
  来源：https://openreview.net/forum?id=hiRJ90xzJY

- 论文：`RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation` `补录`
  为什么重要：把 RAG 防御明确前移到 `retriever` 阶段，而且不需要改生成模型，更接近真实渐进式落地路径。
  建议动作：如果要做最小 PoC，优先从 `retrieval-stage defense` 入手，而不是直接改生成链路。
  状态：`跟踪中`
  来源：https://openreview.net/forum?id=66iLCQVIoP

### 状态变化

- 主题：`Memory`
  之前判断：memory 是一等能力，但评测维度还偏静态。
  当前判断：memory 评测已经快速细分到 `cross-domain personalization`、`continual forgetting`、`stage-level diagnosis`、`memory-to-action` 四条子线。
  变化原因：最近一个月的新 benchmark 基本都在补“长期、连续、可执行”这三个缺口。

- 主题：`Long-horizon agent eval`
  之前判断：需要从 pass/fail 转向长流程。
  当前判断：长流程 benchmark 已开始把 `persistent GUI environment`、`user clarification`、`time-evolving scenario` 做成默认要素。
  变化原因：`ScenDroid` 这类 benchmark 已经不再满足于短任务成功率。

### 新风险 / 新信号

- 信号：`memory retrieval` 和 `memory application` 正被明确区分。
  对我们的影响：如果只看最终回答准确率，我们可能会误判 memory 系统已经够好。

- 信号：RAG 防御开始从“检测异常回答”转向“在检索阶段削弱污染影响”。
  对我们的影响：这更适合作为现有 RAG 系统的渐进式安全加固路径。
