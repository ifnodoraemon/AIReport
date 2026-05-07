# Agent / LLM 每周跟踪

最后更新：2026-05-07

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
2. `Memory / context density` 正在成为 agent 的一等能力，而不只是外挂向量库或更长上下文窗口。
3. `RAG / agent 安全` 需要覆盖语料投毒和 reranking 层风险，不能只盯 prompt injection。
4. `评测` 正在从二元成功率转向长流程、主观质量、真实企业任务和科学研究工作流。

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

## 2026-04-11 当周补充

### 新增论文

- 论文：`Beyond Binary Correctness: Scaling Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks`
  为什么重要：它把长流程 agent 评测从 `pass/fail` 推向 `expert-grounded rubric + artifact checkpoints + human preference`，更接近真实企业工作。
  建议动作：如果我们继续做内容、设计、运营类 agent，应补一套 `subjective enterprise tasks` 评测框架。
  状态：`跟踪中`
  来源：https://arxiv.org/abs/2603.22744

- 论文：`Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models`
  为什么重要：这条线不靠慢速视觉模拟，而是用蒸馏出的语言-动作世界模型做主动 steering，说明 `world model -> control` 可能开始进入更实用的工程阶段。
  建议动作：如果后续要做 agent control / action drift / proactive recovery，可把它当作 world-model steering 的前沿样本。
  状态：`待读`
  来源：https://arxiv.org/abs/2603.23149

### 状态变化

- 主题：`Long-horizon agent eval`
  之前判断：需要从 `binary correctness` 转向更真实的长流程任务。
  当前判断：这条线已经开始进入 `enterprise subjective work`，并且强依赖专家 rubric 与中间工件。
  变化原因：`LH-Bench` 明显不再满足于传统 benchmark 范式。

- 主题：`Agent control / steering`
  之前判断：更像一个值得观察的研究方向。
  当前判断：随着 `Describe-Then-Act` 这类工作出现，主动 steering 已经值得进入中优先级观察列表。
  变化原因：该类方法开始把“先预判后执行”做成可落地、可加速的结构，而不是纯概念。

## 2026-04-17 当周补充

### 新增论文

- 论文：`AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications`
  为什么重要：它把 memory benchmark 从对话中心转向 `agent-environment trajectories`，并明确指出许多 memory 系统输在 `causality` 和 `objective information retention`。
  建议动作：后续内部长期记忆评测里，增加 `因果链保持` 和 `任务目标状态保持` 两项。
  状态：`可执行`
  来源：https://openreview.net/forum?id=GoSVL7mLcM

- 论文：`Evaluating Memory Structure in LLM Agents`
  为什么重要：它开始测 agent 是否会把记忆组织成合适结构，而不只是“能检索到事实”；这更接近真实长期工作区。
  建议动作：如果做 persistent workspace agent，补一组 `memory structure` 样例，如任务清单、分层目录、账本和树形知识。
  状态：`跟踪中`
  来源：https://openreview.net/forum?id=a9vY2sJkf4

- 论文：`Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks`
  为什么重要：这条线把 `experience-driven self-evolution`、长期任务、持续改进绑在一起，比纯 prompt orchestration 更接近“会积累经验的 agent”。
  建议动作：把它和 `system memory` 主题一起跟，重点看经验反思到底沉淀成什么可复用结构。
  状态：`待读`
  来源：https://openreview.net/forum?id=qTpFp3ixnv

### 状态变化

- 主题：`Memory`
  之前判断：memory 正在细分到 personalization、forgetting、diagnosis、memory-to-action。
  当前判断：还应显式加入 `causality preservation` 与 `memory structure`，因为真实 agent 失败经常不是“没记住”，而是“记忆被错误组织或失去因果链”。
  变化原因：`AMA-Bench` 与 `StructMemEval` 都在补这个缺口。

## 2026-04-28 当周补充

### 新增论文

- 论文：`GenericAgent: A Token-Efficient Self-Evolving LLM Agent via Contextual Information Density Maximization`
  为什么重要：这篇把长时 agent 的瓶颈重新表述为 `context information density`，并用 `hierarchical on-demand memory`、`SOP / executable code reuse`、`context truncation / compression` 解释为什么更长上下文不等于更强 agent。
  建议动作：把它和 `context-mode`、`Claude Context`、`memsearch` 这类 GitHub 热点一起看，优先研究“少放但放对”的上下文架构。
  状态：`跟踪中`
  来源：https://arxiv.org/abs/2604.17091 ; https://github.com/lsdefine/GenericAgent

- 论文：`Decoupled DiLoCo for Resilient Distributed Pre-training`
  为什么重要：它把 frontier model 训练的关键问题从“更多 GPU/TPU”推进到 `低通信、异步、跨数据中心、故障隔离`，并用 Gemma 4 训练实验说明训练 goodput 可以显著改善。
  建议动作：虽然它不是 agent 论文，但应纳入 LLM 基础设施跟踪，因为未来模型发布速度和成本会受这类训练架构影响。
  状态：`跟踪中`
  来源：https://arxiv.org/abs/2604.21428 ; https://deepmind.google/blog/decoupled-diloco/

- 论文：`BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology` `补录`
  为什么重要：BixBench 面向真实 bioinformatics 多步分析任务，近期又被 `GPT-5.5` 发布页作为科学研究能力评测信号引用，说明科研 agent 评测正在从知识问答转向真实数据分析工作流。
  建议动作：把 `scientific agent eval` 从通用 long-horizon eval 中拆出来，单独关注数据、工具、实验解释和失败归因。
  状态：`可执行`
  来源：https://arxiv.org/abs/2503.00096 ; https://www.futurehouse.org/research-announcements/bixbench

- 论文：`The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break`
  为什么重要：这篇提出 `HORIZON`，收集 `3100+` 条跨四类 agentic domain 的轨迹，并用 trajectory-grounded LLM-as-a-Judge 做失败归因。它比单纯成功率更适合解释“为什么长任务一长就崩”。
  建议动作：把它作为长流程 agent 评测的 P0 漏项，和 `LH-Bench`、`AMA-Bench` 一起放进内部 eval 设计。
  状态：`可执行`
  来源：https://arxiv.org/abs/2604.11978

- 论文：`AgenticQwen: Training Small Agentic Language Models with Dual Data Flywheels for Industrial-Scale Tool Use`
  为什么重要：它把小模型、agentic RL、synthetic data flywheel 和工业级 tool use 绑定起来，说明 `agentic small model` 已经不是成本优化小分支，而可能成为高频执行层。
  建议动作：把它放进 `small executor model / agentic RL` 主题，后续和 `GPT-5.4 mini/nano`、`Gemini Flash-Lite` 做系统层对比。
  状态：`跟踪中`
  来源：https://arxiv.org/abs/2604.21590

- 论文：`SkillGraph: Graph Foundation Priors for LLM Agent Tool Sequence Recommendation`
  为什么重要：它把工具选择拆成 `retrieval` 和 `ordering` 两个问题，用近 `49,831` 条成功轨迹构建工具执行图，直指真实 agent 中“工具选到了但顺序错了”的失败模式。
  建议动作：把 `tool sequence prior` 加入 tool-use eval，不要只评估工具召回率。
  状态：`跟踪中`
  来源：https://arxiv.org/abs/2604.19793

- 论文：`Your Agent Is Mine: Measuring Malicious Intermediary Attacks on the LLM Supply Chain`
  为什么重要：这篇把第三方 LLM API router 定义成 agent 供应链攻击面，实测发现恶意注入、secret exfiltration 和 YOLO-mode 风险；它比传统 prompt injection 更贴近生产 agent 的真实边界。
  建议动作：把 `router integrity / tool-call signing / transparency logging` 加入 RAG/agent 安全主题，不再只盯语料投毒。
  状态：`可执行`
  来源：https://arxiv.org/abs/2604.08407

- 论文：`The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?`
  为什么重要：它指出工具增强模型会系统性过度调用工具，并把原因拆成 `knowledge epistemic illusion` 和 reward design；这直接影响 agent 成本、延迟和错误传播。
  建议动作：内部 tool-use eval 应加入 `unnecessary tool call rate`，否则 agent 看似更可靠，实际可能只是更贵、更慢。
  状态：`跟踪中`
  来源：https://arxiv.org/abs/2604.19749

- 论文：`AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement Learning`
  为什么重要：它把 graph learning 重新表述为 agentic navigation + inference，并用 graph-native tools 与 curriculum RL 提升图任务效果，和 `Graph RAG / code graph context` 主线同向。
  建议动作：作为 P1 观察项，重点看图结构能否用于 codebase / enterprise knowledge context，而不是只看图学习 benchmark。
  状态：`跟踪中`
  来源：https://arxiv.org/abs/2604.05846

### 状态变化

- 主题：`Context / memory`
  之前判断：memory 重点在检索、组织、因果和任务目标保持。
  当前判断：还应加入 `context density`、`tool sequence prior` 与 `tool overuse control`，即有限上下文里保留什么、工具如何排序、何时不该调用工具。
  变化原因：GenericAgent、SkillGraph、Tool-Overuse、context-mode、Claude Context、memsearch 共同指向“上下文质量和工具调用质量”。

- 主题：`Agent eval`
  之前判断：长流程、主观质量、memory-to-action 是关键。
  当前判断：还要加入 `long-horizon failure attribution`、`scientific workflow` 与 `agent supply-chain security`。
  变化原因：HORIZON、BixBench、Your Agent Is Mine 分别补上长任务诊断、科学工作流和 router 供应链风险。

## 2026-05-07 当周补充

### 新增论文

- 论文：`LongSeeker: Elastic Context Orchestration for Long-Horizon Search Agents`
  为什么重要：arXiv recent 显示该工作把长流程搜索 agent 的核心问题表述为 `elastic context orchestration`，与近期 GitHub `context-mode`、Google File Search 多模态检索、GenericAgent 的 `context density` 主线一致。
  建议动作：将其加入 `context orchestration / long-horizon search` 主题，优先看它如何决定哪些历史证据保留、压缩、检索和恢复。
  状态：`待读`
  来源日期：`2026-05-07`
  来源：https://arxiv.org/abs/2605.05191 ; https://arxiv.org/list/cs.AI/recent

- 论文：`DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents`
  为什么重要：DTap 把 agent red-teaming 扩展到多应用、多工具、多环境的交互式平台，并公开强调间接注入、tools、skills 和直接 prompt injection。
  建议动作：把它放进 `agent security eval` P0 观察项，用于补足当前安全评测中过度依赖文本 prompt 的缺口。
  状态：`可执行`
  来源日期：`2026-05-07`
  来源：https://arxiv.org/abs/2605.04808 ; https://decodingtrust-agent.com/

- 论文：`AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use`
  为什么重要：从标题与 arXiv recent 信息看，它把 agent tool use 的安全评测与运行时拦截放在一起，说明安全不再只是在离线 benchmark 打分，而要进入 agent loop。
  建议动作：跟进其 runtime policy / interception 设计，判断是否能映射到内部 tool-call guardrail。
  状态：`待读`
  来源日期：`2026-05-07`
  来源：https://arxiv.org/abs/2605.04785 ; https://arxiv.org/list/cs.AI/recent

- 论文：`Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration`
  为什么重要：它把持久记忆本身定义成数据外泄攻击面，攻击可通过一次不可信工具调用植入休眠 payload，并在后续敏感话题中激活；报告中还给出跨 memory backend 的防御/效用权衡。
  建议动作：内部 memory 设计必须加入 `untrusted write path`、`sensitive-topic activation`、`memory quarantine` 和 `write-time provenance`。
  状态：`可执行`
  来源日期：`2026-05-03`
  来源：https://arxiv.org/abs/2605.01970

- 论文：`AuditRepairBench: A Paired-Execution Trace Corpus for Evaluator-Channel Ranking Instability in Agent Repair`
  为什么重要：该题目直接指向 agent repair 评测中的 evaluator-channel ranking instability，说明修复类 agent 不仅要看是否修好，还要看评估器和执行轨迹是否稳定。
  建议动作：在 coding agent eval 中增加 `paired trace` 和 `evaluator instability` 维度，避免只看单次 pass/fail。
  状态：`待读`
  来源日期：`2026-05-07`
  来源：https://arxiv.org/abs/2605.04624 ; https://arxiv.org/list/cs.AI/recent

- 论文：`LCM: Lossless Context Management`
  为什么重要：该题目与本周 `context-mode`、LongSeeker 和 Gemini File Search 共同指向“上下文不应只靠截断/摘要”的方向。
  建议动作：作为 `lossless / recoverable context` 主题观察项，重点确认它是否提供可执行的上下文恢复机制。
  状态：`待读`
  来源日期：`2026-05-07`
  来源：https://arxiv.org/abs/2605.04050 ; https://arxiv.org/list/cs.AI/recent

### 状态变化

- 主题：`Memory security`
  之前判断：memory 是能力与评测主线。
  当前判断：memory 也已经成为高优先级安全主线，尤其是跨 session 持久 payload、敏感话题触发和数据外泄。
  变化原因：`Trojan Hippo` 直接把长期记忆攻击从概念演示推进到系统化评估。

- 主题：`Context engineering`
  之前判断：重点是 context density、tool sequence prior、tool overuse control。
  当前判断：还要加入 `elastic / lossless / recoverable context orchestration`。
  变化原因：LongSeeker 与 LCM 同周出现在 arXiv recent，和 GitHub / Google API 信号一致。

- 主题：`Agent安全评测`
  之前判断：供应链、router integrity、长流程攻击是新增重点。
  当前判断：还必须覆盖 `runtime interception` 与 `multi-environment red teaming`。
  变化原因：AgentTrust 与 DTap 都把安全评测推向运行时和多环境平台。
