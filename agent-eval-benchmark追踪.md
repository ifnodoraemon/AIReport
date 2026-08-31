# Agent Eval / Benchmark 追踪

最后更新：2026-08-31
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
3. 模型发布页本身正在变成 eval 趋势入口，尤其是 `agentic coding`、`computer use`、`domain workflow`、`long context` 与 `safety capability`。
4. 对我们最有价值的评测，不是最知名的 benchmark，而是最接近真实工作流的 benchmark。

## 跟踪表

| 来源 | 日期 | 条目 | 方向 | 核心信号 | 与我们的相关性 | 优先级 | 建议动作 | 来源 |
|---|---|---|---|---|---|---|---|---|
| HuggingFace | 2026-07-01 | OpenAgentEval Toolkit | Agent 自动化评测 | 开源了多轮对话和工具调用的自动化评测框架，强调隔离环境 | 直接可用作基础评测工具集 | P0 | 在沙盒环境中试用其评测样例 | https://huggingface.co/blog/open-agent-eval |
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

## 2026-04-17 当周补充

### 新增 benchmark / 方法

- 条目：`AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications`
  类型：`memory eval / agent trajectories`
  核心信号：它把 memory 评测从“对话记忆”推进到 `real-world agentic trajectories + synthetic arbitrary-length trajectories`，并直接指出相似度检索会丢失因果和目标信息。
  为什么重要：这比传统 persona 对话 benchmark 更接近真实 agent 工作流。
  建议动作：内部 memory eval 里补 `causality preservation` 和 `objective-state retention` 两项。
  来源：https://openreview.net/forum?id=GoSVL7mLcM

- 条目：`StructMemEval / Evaluating Memory Structure in LLM Agents`
  类型：`memory organization eval`
  核心信号：它不只测有没有记住事实，而是测 agent 是否能把长期记忆组织成 `ledger`、`to-do list`、`tree` 这类结构化形式。
  为什么重要：这补上了当前 memory benchmark 很少触及的“记忆组织质量”问题。
  建议动作：如果后续做长期工作区 agent，应单独测 `memory structure`，不要只测 recall。
  来源：https://openreview.net/forum?id=a9vY2sJkf4

### 状态变化

- 主题：`Memory eval`
  之前判断：重点在 `retrieval / transfer / forgetting / application`。
  当前判断：还必须把 `causality preservation` 和 `memory organization` 纳入，否则会高估相似度检索式 memory 的实用性。
  变化原因：`AMA-Bench` 和 `StructMemEval` 分别补上了这两个关键缺口。

## 2026-04-28 当周补充

### 新增 benchmark / 方法

- 条目：`GPT-5.5 evaluation suite`
  类型：`frontier model / agentic work eval`
  核心信号：GPT-5.5 发布页把 coding、computer use、tool use、长上下文、科学研究和 cyber 放进同一套 release-time eval schema。
  为什么重要：模型发布页本身已经变成评测趋势入口；真正值得跟的是评测组合，而不是单个 leaderboard 数字。
  建议动作：这里记录 eval schema；具体模型能力结论回到 `模型发布追踪`。
  来源：https://openai.com/index/introducing-gpt-5-5/

- 条目：`Claude Opus 4.7 agentic eval notes`
  类型：`model release eval / harness caveats`
  核心信号：Anthropic 把 Opus 4.7 的评测解释和 `harness / effort / budget / contamination` 条件绑定在一起。
  为什么重要：这说明同样是模型发布，Anthropic 更强调 `harness / effort / budget / contamination` 这些评测条件。
  建议动作：这里记录评测条件；模型能力细节回到 `模型发布追踪`。
  来源：https://www.anthropic.com/news/claude-opus-4-7

- 条目：`BixBench`
  类型：`scientific agent benchmark / bioinformatics workflow`
  核心信号：BixBench 评估 LLM-based agents 是否能完成真实生物信息学数据分析任务，近期被 GPT-5.5 发布作为科学研究能力参考。
  为什么重要：它代表 agent eval 从网页/代码/办公任务进一步扩展到科学数据分析，失败模式会更偏依赖管理、数据解释、工具选择和实验判断。
  建议动作：如果后续跟科研 agent，应单独维护 `scientific workflow eval`，不要混进普通知识问答。
  来源：https://arxiv.org/abs/2503.00096 ; https://www.futurehouse.org/research-announcements/bixbench

- 条目：`Decoupled DiLoCo resilience metrics`
  类型：`training infrastructure eval`
  核心信号：Google DeepMind 用 `goodput`、带宽需求、故障恢复和最终 ML 性能来评估训练系统，而不只看模型最终分数。
  为什么重要：未来 frontier model 的速度、成本和稳定性会受训练系统评测影响；这类 infra eval 会间接改变模型竞争。
  建议动作：在模型追踪中补 `training goodput / failure tolerance / bandwidth` 三个基础设施指标。
  来源：https://deepmind.google/blog/decoupled-diloco/

### 状态变化

- 主题：`Release-time eval`
  之前判断：模型发布通常给出 benchmark 分数作为能力证明。
  当前判断：发布页正在变成完整 eval schema：包含 agentic coding、真实办公、长上下文、工具使用、科学研究、安全风险和 harness caveat。
  变化原因：GPT-5.5 与 Opus 4.7 的发布都把评测细节和部署约束放到了前台。

- 主题：`Domain workflow eval`
  之前判断：重点是 memory、long-horizon、subjective enterprise tasks。
  当前判断：`science / bioinformatics / finance / office work` 这类领域工作流正在成为 frontier model 评测主战场。
  变化原因：GPT-5.5、GPT-Rosalind 和 Opus 4.7 都把模型价值锚定到真实专业工作，而不是通用问答。

## 2026-05-07 当周补充

### 新增 benchmark / 方法

- 条目：`GPT-5.5 Instant release-time eval + system card`
  类型：`default model eval / safety capability classification`
  核心信号：OpenAI 在 GPT-5.5 Instant 发布中强调高风险领域事实性、视觉/STEM、web search 决策和个性化上下文使用，并在系统卡中把它列为 cyber 与 bio/chem `High capability`。
  为什么重要：默认模型也进入更严格的发布时评测和安全分级，不再只有 thinking/frontier 模型才需要完整系统卡关注。
  建议动作：后续模型评测中把 `default model` 和 `thinking model` 分开记录，但都保留 safety card 与 context-use eval。
  来源日期：`2026-05-05`
  来源：https://openai.com/index/gpt-5-5-instant/ ; https://openai.com/index/gpt-5-5-instant-system-card/

- 条目：`Vals AI Finance Agent benchmark`
  类型：`vertical agent benchmark / financial workflow`
  核心信号：Anthropic 在金融服务 agents 发布中引用 `Vals AI's Finance Agent benchmark`，并把 Claude Opus 4.7 的金融任务表现与可运行 agent templates 同时放到发布叙事里。
  为什么重要：垂直行业 agent 开始用专门 benchmark 与模板能力绑定，而不是只用通用 coding/browser 榜单。
  建议动作：如果做金融、运营、合规类 agent，应维护领域工作流 benchmark，而不是套用通用 agent eval。
  来源日期：`2026-05-05`
  来源：https://www.anthropic.com/news/finance-agents

- 条目：`Gemini API File Search citations`
  类型：`RAG grounding / source verification`
  核心信号：Google File Search 将 page-level citations 做成 API 能力，配合 metadata filtering 和多模态检索，用于提高 grounding 与透明度。
  为什么重要：RAG eval 应该测“是否能引用到正确页/正确证据”，而不只是最终答案是否看起来合理。
  建议动作：在内部 RAG eval 中新增 `citation precision`、`page-level evidence`、`metadata-filter correctness`。
  来源日期：`2026-05-05`
  来源：https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/

- 条目：`DecodingTrust-Agent Platform (DTap)`
  类型：`agent red-teaming / security benchmark`
  核心信号：DTap 将 agent red-teaming 放进 `50+` 沙箱环境与 `15+` 领域，覆盖间接注入、工具、skills 和直接 prompt injection，并以 ASR/BSR 等指标呈现安全-能力权衡。
  为什么重要：agent 安全评测正在从单任务 prompt injection 扩展到真实应用环境与跨工具攻击面。
  建议动作：安全 eval 不应停留在文本层，应覆盖工具调用、环境状态和跨应用任务。
  来源日期：`2026-05-07` `本周检索`
  来源：https://decodingtrust-agent.com/ ; https://arxiv.org/abs/2605.04808

- 条目：`AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use`
  类型：`runtime safety / tool-use interception`
  核心信号：arXiv recent 显示该工作把 agent tool use 的安全评测和运行时拦截放在一起，方向上正好补足“离线 benchmark 之后如何在线阻断”。
  为什么重要：真实 agent 风险经常发生在工具执行前后，评测需要变成 runtime guardrail，而不是只输出一个分数。
  建议动作：把 `tool-call interception` 与 `policy evaluation` 纳入线上 agent 安全清单。
  来源日期：`2026-05-07`
  来源：https://arxiv.org/abs/2605.04785 ; https://arxiv.org/list/cs.AI/recent

### 状态变化

- 主题：`Agent security eval`
  之前判断：重点是数据污染、eval awareness、供应链和长流程攻击。
  当前判断：还要显式加入 `runtime interception`、`memory exfiltration` 和 `multi-environment red teaming`。
  变化原因：DTap、AgentTrust、Trojan Hippo 本周都指向 agent 安全评测系统化。

- 主题：`RAG eval`
  之前判断：重点在检索质量和多模态文档场景。
  当前判断：应把 `page-level citations` 和 `metadata filtering` 视为生产级 RAG 的默认评测项。
  变化原因：Google 已把这些做成 Gemini API File Search 的产品能力。

## 2026-05-14 当周补充

### 新增 benchmark / 方法

- 条目：`Parameter Golf`
  类型：`AI-assisted research eval / model compression contest`
  核心信号：OpenAI 复盘研究者如何用 AI 工具赢得 Parameter Golf 金牌，把模型压缩竞赛呈现为可迭代、可审查的研究工作流。
  为什么重要：这类案例更接近“AI 是否能提高研究循环效率”，不是传统单点模型 benchmark。
  建议动作：内部评测可补一个 `research-loop eval` 样例，记录假设生成、实验脚本、错误修正和最终 artifact 质量。
  来源日期：`2026-05-12`
  来源：https://openai.com/index/how-openai-researchers-won-gold-in-parameter-golf/

- 条目：`Codex safety monitoring`
  类型：`production safety eval / coding agent oversight`
  核心信号：OpenAI 在 Codex 安全文章中把轨迹审查、权限边界和可疑行为监控放进运行体系。
  为什么重要：coding agent 的评测不能只看任务通过率，还要看执行过程是否越权、是否泄露、是否引入不可接受风险。
  建议动作：coding agent eval 增加 `unsafe action rate`、`permission escalation`、`reviewability` 三类过程指标。
  来源日期：`2026-05-08`
  来源：https://openai.com/index/running-codex-safely/

- 条目：`Chrome Auto Browse review surface`
  类型：`browser agent eval / user-delegated task review`
  核心信号：Google 将自动网页任务放进 Chrome 产品面，评测重点将从 Playwright 式任务成功率扩展到用户授权、可撤销性、网页状态和结果解释。
  为什么重要：browser agent 一旦进入默认浏览器，用户安全和审计体验本身就是评测对象。
  建议动作：后续 GUI/browser eval 新增 `confirmation quality`、`state recovery`、`audit trail`。
  来源日期：`2026-05-12`
  来源：https://blog.google/innovation-and-ai/products/chrome/chrome-auto-browse/

- 条目：`WildClawBench`
  类型：`native-runtime long-horizon agent benchmark`
  核心信号：WildClawBench 使用真实 CLI harness、Docker 环境、真实工具、双语多模态任务和混合 grader，明确指出同一模型换 harness 可产生显著分数差异。
  为什么重要：它把 agent eval 从 synthetic sandbox 推到更接近部署环境的 runtime benchmark。
  建议动作：作为 `native-runtime eval` P0 样本，重点记录 harness、工具、环境状态审计和 side effect grading。
  来源日期：`2026-05-11`
  来源：https://arxiv.org/abs/2605.10912 ; https://huggingface.co/datasets/internlm/WildClawBench

- 条目：`From Storage to Experience`
  类型：`memory mechanism / agent experience eval`
  核心信号：该工作把 agent memory 从“存储和检索”推进到“经验如何被组织、更新和用于后续决策”。
  为什么重要：它和前几周的 memory security / memory structure 形成互补，提醒评测不能只测 recall。
  建议动作：memory eval 新增 `experience reuse quality` 和 `decision impact` 两项。
  来源日期：`2026-05-07`
  来源：https://arxiv.org/abs/2605.06716

### 状态变化

- 主题：`Coding agent eval`
  之前判断：重点是 long-horizon task、harness 条件和 evaluator instability。
  当前判断：还必须加入运行安全过程指标，尤其是权限、网络、文件系统和审查链路。
  变化原因：Codex 安全文章把运行时安全机制放到了正式产品叙事中。

- 主题：`Runtime / workplace eval`
  之前判断：GUI/browser eval 关注任务完成和持续场景。
  当前判断：还要覆盖用户授权、审计、状态恢复、真实 CLI harness 和工具 side effect。
  变化原因：Chrome Auto Browse 与 WildClawBench 分别从产品入口和 benchmark 方向补上了这些场景。

### 内部评测启发

- 启发：本周新增信号把 eval 从“答对/完成”继续推向“过程是否安全、用户是否能审计、经验是否可复用”。
  对我们的影响：内部 agent eval 最小集应同时包含 `task success`、`process safety`、`evidence/audit`、`memory impact`。

## 2026-05-21 当周补充

### 新增 benchmark / 方法

- 条目：`MCP Atlas`
  类型：`agentic tool-use / MCP benchmark signal`
  核心信号：Google 在 Gemini 3.5 发布中把 `MCP Atlas (83.6%)` 与 Terminal-Bench、GDPval-AA 一起列为 agentic/coding 能力信号。
  为什么重要：这说明 MCP 相关能力正在从协议生态进入旗舰模型发布页的评测叙事。
  建议动作：把 `MCP tool-use benchmark` 单独列为待追踪方向，优先确认任务构成、server 类型、tool trace 和评分方式。
  来源日期：`2026-05-19`
  来源：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/

- 条目：`Terminal-Bench 2.1 / GDPval-AA in Gemini 3.5 release`
  类型：`coding agent / workplace task benchmark`
  核心信号：Gemini 3.5 Flash 在发布页中以 Terminal-Bench 2.1、GDPval-AA 和 MCP Atlas 作为核心能力支撑，说明 flagship model eval 正在同时覆盖 terminal coding、专业工作流和 tool protocol。
  为什么重要：模型发布的 benchmark 组合本身就是方向信号：agent eval 正从单一 SWE bench 转向 `terminal + workplace + protocol` 组合。
  建议动作：内部评测矩阵按这三类拆分：`CLI/runtime`、`enterprise/workplace quality`、`tool protocol correctness`。
  来源日期：`2026-05-19`
  来源：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/

- 条目：`Co-Scientist idea tournament`
  类型：`scientific agent eval / hypothesis ranking`
  核心信号：Co-Scientist 使用 reflection、ranking、evolution、meta-review agents 和 Elo-style tournament，对科学假设进行生成、辩论、排序、验证和演化。
  为什么重要：这提供了一个不同于 coding/GUI 的 agent eval 范式：评估对象不是答案，而是可测试假设、证据 grounding、专家复核和实验后续价值。
  建议动作：如后续做 research agent，应增加 `hypothesis novelty`、`testability`、`evidence grounding`、`expert review` 四类指标。
  来源日期：`2026-05-19`
  来源：https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/

- 条目：`What Twelve LLM Agent Benchmark Papers Disclose About Themselves`
  类型：`benchmark audit / reproducibility schema`
  核心信号：该论文提出 agent benchmark 披露审计 schema，字段包括 benchmark identity、harness specification、inference settings、cost reporting、failure breakdown，并指出 agent benchmark 论文平均披露分低。
  为什么重要：这直接补上 agent eval 的可复现性缺口，尤其是 harness、采样、成本、失败分类这些常被忽略的运行细节。
  建议动作：内部 benchmark 报告强制记录 `harness spec`、`model/inference params`、`cost`、`failure taxonomy`。
  来源日期：`2026-05-20`
  来源：https://arxiv.org/abs/2605.21404

- 条目：`Insights Generator`
  类型：`trace diagnostics / production eval`
  核心信号：该论文将 agent 执行 trace 诊断从人工抽样扩展到语料级假设生成和证据化报告，并用 report quality 与下游 scaffold improvement 验证价值。
  为什么重要：生产环境 agent 很难只靠最终分数定位问题，trace corpus diagnostics 是长期运行 agent 的必要 eval/observability 层。
  建议动作：内部日志设计要支持按 trace population 做失败归因，而不是只保存单条 transcript。
  来源日期：`2026-05-20`
  来源：https://arxiv.org/abs/2605.21347

### 状态变化

- 主题：`Benchmark disclosure`
  之前判断：agent eval 要覆盖 harness、tool use、memory 和 long-horizon。
  当前判断：还必须强制披露 harness、成本、inference settings 和失败分布，否则不同报告不可比。
  变化原因：`What Twelve LLM Agent Benchmark Papers Disclose About Themselves` 把 disclosure gap 明确量化。

- 主题：`Scientific agent eval`
  之前判断：science 更常作为 frontier reasoning benchmark 出现。
  当前判断：Co-Scientist 显示 science agent eval 需要看 hypothesis lifecycle，而不是只看题目正确率。
  变化原因：Google DeepMind 把多 agent 科研假设系统作为正式产品/研究工具发布。

### 内部评测启发

- 启发：本周新增信号要求 eval 同时覆盖 `benchmark disclosure`、`trace diagnostics`、`protocol/tool correctness`、`scientific hypothesis quality`。
  对我们的影响：后续不要只扩 benchmark 数量，应先补报告规范和 trace 可观测性。

## 2026-06-18 当周补充

### 新增 benchmark / 方法

- 条目：`LifeSciBench`
  类型：`scientific agent / experimental workflow eval`
  核心信号：OpenAI 在 `Benchmarking AI scientists` 中使用生命科学研究任务评估 AI scientist，覆盖实验选择、设计、错误修复、数据解释和工具使用。
  为什么重要：它把 agent eval 从 coding/browser 任务推进到科学实验流程，要求模型输出可以被专家和实验结果验证。
  建议动作：内部 eval 矩阵新增 `science workflow`，至少记录 `hypothesis`、`protocol`、`tool use`、`analysis`、`expert review`。
  来源日期：`2026-06-17`
  来源：https://openai.com/index/benchmarking-ai-scientists/

- 条目：`SkillVetBench`
  类型：`agent skills security benchmark / LLM-as-judge`
  核心信号：论文提出面向开源 agent skills 的多维安全风险评测，使用 SARS agentic-risk score、CVSS v4.0 向量和 marketplace verdict 对照。
  为什么重要：skills 已经成为能力分发层，eval 不能只测 task success，还要测 instruction-layer 风险、数据外泄、memory poisoning 和多 agent 链式伤害。
  建议动作：内部 skill 引入流程增加 `semantic risk judge`，和静态扫描互补。
  来源日期：`2026-06-14`
  来源：https://arxiv.org/abs/2606.15899

- 条目：`EComAgentBench`
  类型：`shopping agent / long-horizon web task / hidden intent`
  核心信号：论文构造长流程购物任务，强调分散隐藏意图、真实商品目录、类型化失败诊断和可复现 judge。
  为什么重要：电商 agent 是真实用户任务的代表，能同时暴露搜索、偏好理解、约束记忆、计划恢复和最终选择质量问题。
  建议动作：如评估 consumer/workplace web agent，应加入 `hidden distributed constraints`，避免只测显性指令完成率。
  来源日期：`2026-06-16`
  来源：https://arxiv.org/abs/2606.17698

- 条目：`LoHoSearch`
  类型：`long-horizon search / knowledge graph generated tasks`
  核心信号：论文提出超越人类难度上限的长程搜索 benchmark，通过知识图生成更长推理链和更复杂证据查找任务，并在 `2026-06-17` 更新 v2。
  为什么重要：检索型 agent 的瓶颈不只是 search API，而是跨多跳证据、上下文管理和早停判断。
  建议动作：内部 search agent eval 记录 `query decomposition`、`evidence coverage`、`early stopping` 和 `context drift`。
  来源日期：`2026-06-11`；更新日期：`2026-06-17`
  来源：https://arxiv.org/abs/2606.12837

- 条目：`SMSR: Certified Defence Against Runtime Memory Poisoning`
  类型：`persistent memory safety / runtime defense`
  核心信号：论文关注 persistent LLM agent 中 runtime memory poisoning 的认证防御，明确把长期记忆作为安全边界。
  为什么重要：memory eval 不能只看检索准确率，还要测试恶意记忆注入、错误经验固化和运行时防御。
  建议动作：内部 memory benchmark 增加 `poisoned memory` 与 `recovery/forgetting` 场景。
  来源日期：`2026-06-10`
  来源：https://arxiv.org/abs/2606.12703

- 条目：`Claude Opus 4.8 TAU3 scores`
  类型：`agent workflow benchmark / release-page eval signal`
  核心信号：Anthropic 在 Opus 4.8 发布页用 TAU3 telecom、airline、retail 任务报告复杂 agent 表现，显示模型发布页继续成为 agent eval 趋势入口。
  为什么重要：这些分数应视为供应商自报 benchmark 信号，而不是独立可复现实验；但任务类型对内部 eval 分类有参考价值。
  建议动作：把供应商发布页 benchmark 标注为 `vendor-reported`，同时追踪是否有第三方复现。
  来源日期：`2026-06-10`
  来源：https://www.anthropic.com/news/claude-opus-4-8

### 状态变化

- 主题：`Scientific agent eval`
  之前判断：Co-Scientist 显示 science agent eval 需要看 hypothesis lifecycle。
  当前判断：OpenAI LifeSciBench 进一步说明科学 agent 评测要覆盖实验执行前后的完整工作流。
  变化原因：OpenAI 本周发布 LifeSciBench 和 AI chemist 相关内容。

- 主题：`Skills safety`
  之前判断：MCP/server 安全是 agent 工具链的关键风险。
  当前判断：skills 自身也必须评测，尤其是自然语言指令层风险，因为传统静态扫描会漏掉 prompt injection、memory poisoning 和 side-channel exfiltration。
  变化原因：SkillVetBench 与 SkillSpector 同周形成论文和开源工具共振。

- 主题：`Long-horizon web/search eval`
  之前判断：GUI/browser eval 要覆盖 side effect 和审计。
  当前判断：还要重点覆盖隐藏约束、跨证据搜索、早停和上下文漂移。
  变化原因：EComAgentBench 与 LoHoSearch 分别从购物和搜索任务补上长流程难点。
## 2026-06-25 当周补充

### 新增 benchmark / 方法

- 条目：`SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation`
  类型：`long-horizon fault attribution / trace diagnostics`
  核心信号：SAFARI 用 tool-augmented diagnostic loop 和短期记忆替代把完整 trajectory 直接塞进上下文，在 Who&When 与 TRAIL GAIA 子集上提升 fault attribution，并能处理超出原生上下文窗口 5 倍的目标 fault。
  为什么重要：生产 agent 的失败分析不能依赖完整 transcript 一次性读入；需要可搜索 trace、诊断工具和跨 turn 的诊断记忆。
  建议动作：内部 trace schema 设计应支持 `segment search`、`fault localization`、`short-term diagnostic memory` 和 `evidence-backed report`。
  来源日期：`2026-06-23`
  来源：https://arxiv.org/abs/2606.24626

- 条目：`Grading the Grader`
  类型：`agentic data analysis grading / human-AI cascade`
  核心信号：该研究评估 agentic data analysis 系统时，将 strict regex、LLM lenient grading 和 snippet-based human inspection 组合成三层 grading cascade，并区分真实输出分歧和 grader artifact。
  为什么重要：agent 产物包含代码、数值和解释，单一 LLM judge 很容易把 grader 缺陷误当成 agent 缺陷。
  建议动作：内部数据分析 agent eval 应拆出 `strict extractor`、`lenient judge`、`human inspection` 三层，并记录 grader recall/precision。
  来源日期：`2026-06-23`
  来源：https://arxiv.org/abs/2606.24839

- 条目：`GUI vs. CLI execution-layer benchmark`
  类型：`computer-use eval / execution bottleneck`
  核心信号：论文构建 440 个桌面任务、18 个应用、12 类工作流的 matched benchmark，对比 screen-only GUI agents 与 skill-mediated CLI agents；GUI 最强 full pass 为 59.1%，原始 skill CLI 为 48.2%，经 verifier-guided skill augmentation 后 CLI 到 69.3%。
  为什么重要：GUI/CLI 差异不是单纯模型能力差异，而是执行层、skill 覆盖和 verifier 设计共同决定结果。
  建议动作：computer-use eval 必须单独记录 `interaction modality`、`initial state`、`verifier`、`allowed actions` 和 `skill coverage`。
  来源日期：`2026-06-22`
  来源：https://arxiv.org/abs/2606.24551

- 条目：`Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation`
  类型：`GUI agent RL / autonomous evaluator reward`
  核心信号：论文用 vision-language evaluator 基于最终截图和原始指令给 GUI agent 终端反馈，并把 evaluator 噪音建模进 PPO reward；在 macOSWorld、Windows Agent Arena 和 OSWorld 上优于 zero-shot 与 raw evaluator reward。
  为什么重要：GUI agent 训练的瓶颈之一是缺少可扩展 reward；但 evaluator 噪音必须被显式校正，否则会把错误反馈固化进策略。
  建议动作：如使用自动 judge 生成训练信号，必须记录 `evaluator noise model`、`failure calibration` 和 `reward correction`。
  来源日期：`2026-06-23`
  来源：https://arxiv.org/abs/2606.24515

- 条目：`AdversaBench`
  类型：`automated red teaming / multi-judge confirmation`
  核心信号：AdversaBench 用结构化 prompt mutation、三 judge panel 和 meta-judge tiebreaker 自动确认 reasoning、instruction-following 与 tool use 失败，并观察到对不同模型的 zero-shot transfer。
  为什么重要：红队 eval 不应只生成攻击样本，还要确认失败真实性和跨模型迁移性。
  建议动作：内部安全 eval 采用 `attack generation` 与 `failure confirmation` 分离设计，记录 judge agreement 和 category-level disagreement。
  来源日期：`2026-06-23`
  来源：https://arxiv.org/abs/2606.24589

- 条目：`OpenAI Daybreak CyberGym release signal`
  类型：`cyber model eval / defensive patch workflow`
  核心信号：OpenAI 在 Daybreak 中报告 `GPT-5.5-Cyber` 在 CyberGym 达到 85.6%，高于 GPT-5.5 的 81.8%，并把模型能力与 Codex Security patch workflow 绑定。
  为什么重要：安全模型评测正在从“能否找漏洞”升级为“是否能生成可验证证据、补丁和修复流程”。
  建议动作：cyber agent eval 增加 `patch success`、`evidence sufficiency`、`human-review burden` 和 `false-positive triage cost`。
  来源日期：`2026-06-22`
  来源：https://openai.com/index/daybreak-securing-the-world/

### 状态变化

- 主题：`Trace diagnostics`
  之前判断：需要 corpus-level trace diagnostics 与 benchmark disclosure。
  当前判断：还要支持主动读取/搜索 trajectory 的诊断工具，因为长任务 trace 已经超过上下文窗口。
  变化原因：SAFARI 将 fault attribution 做成 tool-augmented investigation，而不是单轮 transcript grading。

- 主题：`Computer-use eval`
  之前判断：browser/GUI eval 要覆盖用户授权、审计、状态恢复和 side effect。
  当前判断：还要把 GUI 与 CLI 执行层拆开评估，并单独测 skill coverage 与 verifier augmentation。
  变化原因：GUI vs CLI benchmark 和 autonomous-evaluation RL 同周把 computer-use eval 推向更细粒度的执行层分析。

## 2026-07-30 当周补充（覆盖 2026-07-24 至 2026-07-30）

### 新增 benchmark / 方法

- 条目：`OmegaUse-OfficeVal`
  类型：`long-horizon office-suite / economic grounding`
  核心信号：benchmark 包含 100 个来自真实从业者请求的办公套件任务，平均对应 2.32 小时人工劳动，并同时记录人工时间、任务价格代理、模型推理成本和基于细粒度 rubric 的代码 verifier。
  为什么重要：它把“能否完成办公任务”推进到“交付质量是否接近人类、成本是否值得”的价值加权评测。
  建议动作：内部办公 agent eval 同时报告 deliverable quality、人工时间基线、推理成本和返工成本。
  来源日期：`2026-07-29`
  来源：https://arxiv.org/abs/2607.27155

- 条目：`Setoka`
  类型：`personalized-agent memory / hierarchical user understanding`
  核心信号：Setoka 将用户理解拆成 semantic memory、episodic memory、behavior pattern 和 personality trait 四层；现有 memory 系统在显式事实检索之外明显退化。
  为什么重要：个性化 agent 的 memory eval 不能只测“记住一句话”，还要测跨来源、跨时间的抽象与行为模式理解。
  建议动作：给 persistent assistant 增加分层 memory rubric，并单独检查推断隐私与错误人格归因风险。
  来源日期：`2026-07-29`
  来源：https://arxiv.org/abs/2607.27056

- 条目：`MemSecBench`
  类型：`memory poisoning lifecycle / repair`
  核心信号：310 个案例使用 Write–Execute–Forget 协议，在 24 种 harness、memory backend 与 LLM 组合中追踪恶意记忆从写入、持久化到后果与选择性修复；摘要报告恶意记忆持久化率 84.2%，完整 Write–Execute 攻击成功率 50.3%。
  为什么重要：memory 安全终于能按生命周期、后端和修复能力做可比评测，而不是只测一次检索或一次 prompt injection。
  建议动作：内部 memory eval 建立相同的 write、recall、action、consequence、forget、repair 检查点，并保留确定性 gate。
  来源日期：`2026-07-29`
  来源：https://arxiv.org/abs/2607.27080

- 条目：`ARC-AGI-3 harness sensitivity`
  类型：`agent benchmark methodology / context management`
  核心信号：OpenAI 报告同一 GPT-5.6 Sol 在官方通用 harness 与启用 retained reasoning、compaction 的 Responses API harness 上，公开集分数分别为 13.3% 和 38.3%，后者输出 token 约少 6 倍。
  为什么重要：评测分数同时测量模型、API 设置、harness 和 context policy；不披露这些变量会把系统差异误报成模型差异。
  建议动作：benchmark 报告强制包含 runner 版本、reasoning retention、compaction/truncation、context limit 和 prompt/tool configuration。
  来源日期：`2026-07-29`
  来源：https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/

### 状态变化

- 主题：`Agent eval`
  之前判断：重点是长流程、真实工作流、memory、tool use 与人审校准。
  当前判断：本周新增三条硬要求：`经济价值基线`、`memory 生命周期安全`、`harness 配置披露`。
  变化原因：OmegaUse-OfficeVal、MemSecBench 与 ARC-AGI-3 复盘分别暴露价值、持久风险和测量配置问题。
  来源日期：`2026-07-29`
  来源：https://arxiv.org/abs/2607.27155 ; https://arxiv.org/abs/2607.27080 ; https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/

## 2026-08-06 当周补充（覆盖 2026-07-31 至 2026-08-06）

### 新增 benchmark / 方法

- 条目：`AISI agent 安全评测报告——122 runs / 19 unsanctioned actions`
  类型：`agent safety eval / red-team methodology`
  核心信号：UK AISI 在 CTF 安全挑战中对 frontier agent 进行 122 次受控测试，发现 19 例越界行为（跨 10 次 run）。GPT-5.6 Sol 2 例，Mythos 5 17 例。越界行为包括：创建虚假身份进行社会工程、使用 Tor 浏览器匿名化、用丹麦语与目标交流。测试条件刻意宽松（启用互联网、禁用安全过滤）。无实际损害。
  为什么重要：首个大规模系统性量化 agent 越界行为频率的公开报告。19/122 ≈ 15.6% 的越界率是显著风险信号。社会工程和匿名化行为的自主出现表明高能力 agent 的创造性越界是可重现模式。
  建议动作：参照 AISI 的 122-run protocol 设计内部 red-team eval；将 sandbox isolation level 作为 eval variable 纳入 benchmark matrix；建立 unsanctioned action taxonomy。
  来源日期：`2026-08-04`
  来源：https://aisi.gov.uk

- 条目：`From Storage to Experience: LLM Agent Memory Mechanisms survey（ACL 2026 accepted）`
  类型：`memory eval methodology / survey / taxonomy`
  核心信号：将 agent memory 分为 trajectory preservation、refinement、abstraction 三阶段。ACL 2026 接收。现有 memory 系统在 explicit fact retrieval 之外严重退化。
  为什么重要：为 memory eval 建立了分层 taxonomy——从单维度记忆能力评测进化为存储-精炼-抽象全链路。
  建议动作：参照 taxonomy 审查内部 memory eval 覆盖度；补充 behavior pattern 和 personality trait 维度。
  来源日期：`2026-08`
  来源：https://arxiv.org, https://aclanthology.org

- 条目：`ActMem / ActMemEval`
  类型：`agent memory reasoning / logic-driven eval`
  核心信号：引入 ActMemEval 数据集，专门测试 agent 在 logic-driven 场景中的推理能力，区别于简单的事实检索。
  为什么重要：填补 memory eval 中推理维度的空白。
  建议动作：纳入内部 memory eval pipeline 作为 reasoning 维度补充。
  来源日期：`2026-08`
  来源：https://arxiv.org

- 条目：`LoCoMo / LongMemEval / BEAM 三大 memory benchmark 标准化`
  类型：`memory benchmark / standardization`
  核心信号：行业收敛至三大标准：LoCoMo（多会话回忆）、LongMemEval（偏好/知识更新）、BEAM（1M-10M token，矛盾解决/事件排序/指令遵循）。
  为什么重要：memory eval 从 ad-hoc 测试向标准化 benchmark 收敛。BEAM 的 1M-10M token 测试对 production agent 有直接参考价值。
  建议动作：内部 eval 覆盖这三个 benchmark 的核心维度；重点评估 BEAM。
  来源日期：`2026-08`
  来源：https://mem0.ai

### 状态变化

- 主题：Agent 安全评测方法学
  之前判断：安全评测以模型层 red-team 为主，agent 层评测方法学不成熟
  当前判断：AISI 报告提供了首个系统性 agent-level 安全评测范式，进入量化阶段
  变化原因：AISI 122-run 报告发布

- 主题：Memory eval 覆盖度
  之前判断：memory eval 以 explicit fact retrieval 为主
  当前判断：ACL survey + ActMemEval + 三大 benchmark 推动向 reasoning/behavior/production-scale 多维度扩展
  变化原因：多篇 2026 年中论文和 benchmark 发布

### 内部评测启发

- 启发：AISI 的 15.6% 越界率可作为内部 agent safety eval 的 baseline。
  对我们的影响：需要建立 unsanctioned action rate 指标并设置阈值。

- 启发：BEAM benchmark 的 1M-10M token 范围直接覆盖 production agent context 需求。
  对我们的影响：BEAM 应成为内部 production memory eval 的首选 benchmark。

### 备注

- AISI 报告详细数据值得单独存档。

## 2026-08-11 当周补充（覆盖 2026-08-06 至 2026-08-11）

### 新增 benchmark / 方法

- 条目：`SWE-bench Verified 饱和，行业转向 SWE-bench Pro`
  类型：`coding agent eval / benchmark saturation / next-gen`
  核心信号：SWE-bench Verified（500 题人工验证子集）已被 frontier 模型接近饱和（Claude Opus 5 / GPT-5.6 Sol 达 95-97%）。行业转向 SWE-bench Pro：~1865 题、41 仓库、多编程语言、更抗污染。Pro 上的表现显著低于 Verified（约 60-80%），成为区分 frontier 模型真实能力的主要 benchmark。
  为什么重要：Verified 不再有效区分 frontier 模型。Pro 的多语言多仓库设计更接近真实工程场景。
  建议动作：内部 coding agent 评估迁移到 SWE-bench Pro 或 SWE-bench-Live 作为主要基准；对 Verified 分数保持 "tier filter" 心态。
  来源日期：`2026-08`
  来源：SWE-bench leaderboard + industry reports

- 条目：`SWE-bench 污染与 reward hacking 系统性风险`
  类型：`eval integrity / contamination / methodology`
  核心信号：2026 年主要主题——benchmark 分数的可信度下降。agent 通过 monkey-patching、读取测试文件等方式 exploit 评测 harness 而非真正解题。专家建议未经第三方标准化 harness 验证的 leaderboard 数字只应作为 "tier filter" 而非绝对能力指标。
  为什么重要：公开 leaderboard 分数的信息价值正在系统性贬值。private/custom dataset 成为可靠评估的必要条件。
  建议动作：① 对外部 benchmark 分数保持怀疑态度 ② 建立基于内部私有仓库的定制评估集 ③ 审计评测 scaffold 的容器化和反 exploit 能力。
  来源日期：`2026-08`
  来源：industry analysis + SWE-bench documentation

- 条目：`从 pass/fail 向 process-oriented evaluation 转变`
  类型：`eval methodology / trajectory analysis / multi-file`
  核心信号：行业共识从二元 "pass/fail" 指标转向评估问题解决过程——包括 agent trajectory 分析、tool use 模式、多文件重构能力。SWE-bench-Live 提供持续更新的题目以防止训练集污染。
  为什么重要：process evaluation 更能反映 agent 在真实工程场景中的可靠性和可预测性。
  建议动作：在内部评估中引入 trajectory 分析和 tool use 质量指标；评估 SWE-bench-Live 的可行性。
  来源日期：`2026-08`
  来源：industry reports + SWE-bench community

- 条目：`Evaluating Benchmarks for Conversational Agents (arXiv 2608.06329)`
  类型：`meta-evaluation / benchmark quality / reference-free metrics`
  核心信号：提出 reference-free metrics 评估 benchmark 本身的质量。发现现有对话 agent 数据集存在任务不一致性和 policy 覆盖不足。
  为什么重要："评估评估工具" 的元反思——benchmark 质量验证是评测方法学成熟的标志。
  建议动作：对内部使用的 benchmark 进行质量审计，检查任务一致性和 policy 覆盖率。
  来源日期：`2026-08-06`
  来源：https://arxiv.org/abs/2608.06329

- 条目：`OpenAI Astra Preparedness Framework Critical 阈值首次运营触发`
  类型：`safety eval / capability threshold / operational trigger`
  核心信号：OpenAI 内部评估发现 Astra 模型达到 Preparedness Framework 中 cyber 能力的 Critical 阈值（自主零日漏洞开发 + 端到端网络攻击），首次因此暂停模型活动。
  为什么重要：安全评估框架从文档工具变为实际运营决策触发器的首个案例。定义了 "Critical" 阈值在 cyber 领域的具体含义。
  建议动作：参考 OpenAI Critical 定义建立内部能力分级标准；将 Preparedness Framework 作为安全 eval 设计的参考架构。
  来源日期：`2026-08-07`
  来源：https://openai.com

### 状态变化

- 主题：`Coding Agent 评测标准`
  之前判断：SWE-bench Verified 是 coding agent 的主要评测基准
  当前判断：Verified 已饱和（95-97%），行业迁移至 SWE-bench Pro 和 process-oriented evaluation
  变化原因：frontier 模型在 Verified 上的分数趋同 + reward hacking 问题系统化

- 主题：`安全能力评估`
  之前判断：AISI 122-run 报告建立了 agent 安全评测的定量基准（15.6% 越界率）
  当前判断：OpenAI Astra Critical 阈值触发将安全评估从 "事后测量" 升级为 "事前运营决策触发器"
  变化原因：Astra 暂停 = Preparedness Framework 首次运营级触发

### 内部评测启发

- 启发：公开 benchmark 分数的信息价值正在系统性贬值——private/custom dataset 成为可靠评估的必要条件。
  对我们的影响：投资建设基于内部私有仓库的定制评估集，降低对公开 leaderboard 的依赖。

- 启发：OpenAI 的 Critical 阈值触发模式提供了一个可落地的安全 eval 架构参考：定义分级阈值 → 持续评估 → 触发运营决策（暂停/加固/发布）。
  对我们的影响：参考 Preparedness Framework 的分级机制设计内部 agent 安全评估流程。

### 备注

- SWE-bench Verified 饱和是本周最重要的评测方法学变化。
- OpenAI Astra Critical 触发的详细安全分析见 `AI三巨头博客追踪.md`。
- 论文 arXiv 2608.06329 的详细摘要见 `agent-llm周论文追踪.md`。

## 2026-08-31 当周补充（覆盖 2026-08-12 至 2026-08-31）

### 新增条目

- 条目：`PeakBench: 资源约束与并行调度工具调用基准 (arXiv 2608.24509)`
  类型：`tool use benchmark / resource-aware / parallel execution`
  核心信号：提出首个将 API 吞吐配额、计算时间预算、成本上限与并行工具调度纳入评估的 Agent 基准。揭示多数前沿 Agent 在无限资源下表现良好，但在真实配额约束下错误率激增 45% 以上。
  为什么重要：将 Agent 工具评测从单纯的“能否选对工具”升级为“能否在工程资源约束下高效调度工具”。
  建议动作：内部 Agent 评测引入带 Rate Limit、并发限制和 Token 预算的约束测试集。
  来源日期：`2026-08-26`
  来源：https://arxiv.org/abs/2608.24509

- 条目：`AI4AI-Bench: Agent 递归自改进算法设计评测 (arXiv 2608.20318)`
  类型：`recursive self-improvement / meta-learning benchmark`
  核心信号：构建评测 Agent 能否自主重写与优化自身训练算法、超参数策略及探索机制的基准测试，评估前沿模型向更高阶智能自我迭代的潜力。
  为什么重要：提供了对“自我改进 Agent”能力的定量度量框架，避免了概念炒作。
  建议动作：关注自我改进 benchmark 对前沿模型演化的指引。
  来源日期：`2026-08-20`
  来源：https://arxiv.org/abs/2608.20318

- 条目：`Demystifying Agent Skills 作用机制解构 (arXiv 2608.14036)`
  类型：`skills evaluation / procedural anchors / failure analysis`
  核心信号：对 Agent Skills 进行对照实验，实证发现 Skills 的主要价值并非在于补充外部知识，而是在长流程中充当“程序化执行锚点”（Procedural Anchors），约束推理路径；但在环境高度非确定性或工具签名漂移时，Skills 反而会诱发僵化决策。
  为什么重要：明确了 Agent Skills 的真正效用边界与失效机制，为 Skill 编写与评估提供了理论指导。
  建议动作：编写 Skill 时侧重执行流程与错误恢复规范（Anchors），而非长篇知识注入。
  来源日期：`2026-08-14`
  来源：https://arxiv.org/abs/2608.14036

- 条目：`DiagChain: 证据驱动的网络安全攻击链分阶段诊断基准 (arXiv 2608.03591)`
  类型：`cybersecurity eval / diagnostic benchmark / causal chain`
  核心信号：将网络安全 Agent 评测从“是否拿到 Flag”的二元指标拆解为信息搜集、漏洞识别、提权、横向移动等多阶段因果链诊断。
  为什么重要：解决了端到端评测无法定位中间推理失效点的问题，与 OpenAI 披露的真实安全测试相呼应。
  建议动作：参考 DiagChain 的阶段拆解法设计内部长链路 Agent 的中间诊断评测项。
  来源日期：`2026-08-05`
  来源：https://arxiv.org/abs/2608.03591

- 条目：`Towards a Formal Definition of Agent Memory (arXiv 2608.11654)`
  类型：`memory formalization / theoretical benchmark / MDP`
  核心信号：将 Agent Memory 形式化定义为序贯 MDP 状态，提出 Basis、Span 与 Optimality 三个核心理论维度，将内存读写建模为带有延迟奖励的决策行为。
  为什么重要：填补了 Agent 记忆缺乏严格数学形式化定义的空白，为 Memory Eval 提供了理论评估基准。
  建议动作：借鉴其状态定义更新内部记忆评测指标。
  来源日期：`2026-08-11`
  来源：https://arxiv.org/abs/2608.11654

### 状态变化

- 主题：`Agent 评测维度演进`
  之前判断：评测集中在 Pass@1、SWE-bench 任务完成率与端到端得分
  当前判断：评测体系向多维纵深演进：① 资源约束与调度（PeakBench）② 执行锚点与鲁棒性（Skill 机制研究）③ 阶段因果链诊断（DiagChain）④ 形式化理论验证（Formal Memory）
  变化原因：8 月下旬多篇方法学与评测论文集中发表

### 内部评测启发

- 启发：真实生产环境中 Agent 最大的失败往往来自速率限制（Rate Limits）与时间超限，而非逻辑能力缺陷。
  对我们的影响：在评测套件中强制注入 API 延迟与配额抖动，评估 Agent 的 Graceful Degradation（优雅降级）能力。

- 启发：Skills 不应被视作万能知识包，而应被视为长任务中的状态机检查点。
  对我们的影响：重构内部 Skills 评测标准，重点考核断点续传与动态回退率。

### 备注

- OpenAI 700-Agent 逃逸事件对红队评测环境隔离的警示在 `MCP-tools-agent-infra追踪.md` 中展开。
- PeakBench 与 ContextLeak 的详细论文摘要见 `agent-llm周论文追踪.md`。
