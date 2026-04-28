# AIReport

`AIReport` 是一个持续维护的 AI 趋势追踪仓库，当前重点覆盖：

- `Agent / LLM` 论文追踪
- `Agent / LLM` GitHub 热点追踪
- `OpenAI / Anthropic / Google` 官方博客追踪
- `AI 关键人物` 追踪
- `模型发布` 追踪
- `MCP / tools / agent infra` 追踪
- `Agent eval / benchmark` 追踪
- `Wiki` 形式的长期知识沉淀

目标不是做资讯堆积，而是保留高信号内容，并把每周变化整理成可持续维护的判断文档。

## 当前内容

### 1. 论文追踪

文件：[agent-llm周论文追踪.md](./agent-llm周论文追踪.md)

关注主题：

- `agentic RL`
- `memory`
- `RAG 安全`
- `长流程评测`

### 2. GitHub 热点追踪

文件：[agent-llm周GitHub热点追踪.md](./agent-llm周GitHub热点追踪.md)

关注主题：

- `agent harness`
- `memory / context database`
- `plugin / MCP / skills`
- `GUI agent`

### 3. AI 三巨头博客追踪

文件：[AI三巨头博客追踪.md](./AI三巨头博客追踪.md)

关注范围：

- `OpenAI`
- `Anthropic`
- `Google / Google DeepMind`

重点跟踪：

- `model`
- `agent`
- `runtime`
- `eval`
- `context`
- `multimodal`

### 4. 模型发布追踪

文件：[模型发布追踪.md](./模型发布追踪.md)

关注主题：

- `frontier model`
- `低成本小模型`
- `tool use / agent-friendly`
- `上下文 / multimodal / 价格分层`

### 5. AI 关键人物追踪

文件：[AI关键人物追踪.md](./AI关键人物追踪.md)

关注主题：

- `Sam Altman / Dario Amodei / Demis Hassabis`
- `Andrew Ng / Fei-Fei Li`
- `Karpathy / Ilya` 等低频高信号人物

### 6. MCP / Tools / Agent Infra 追踪

文件：[MCP-tools-agent-infra追踪.md](./MCP-tools-agent-infra追踪.md)

关注主题：

- `MCP`
- `runtime / shell / container`
- `code execution`
- `skills / sandbox / state`

### 7. Agent Eval / Benchmark 追踪

文件：[agent-eval-benchmark追踪.md](./agent-eval-benchmark追踪.md)

关注主题：

- `memory eval`
- `long-horizon benchmark`
- `tool use eval`
- `主观质量 rubric`

### 8. Wiki MVP

目录：[wiki](./wiki)

当前种子页：

- [wiki/people/karpathy.md](./wiki/people/karpathy.md)
- [wiki/people/andrew-ng.md](./wiki/people/andrew-ng.md)
- [wiki/people/sam-altman.md](./wiki/people/sam-altman.md)
- [wiki/people/dario-amodei.md](./wiki/people/dario-amodei.md)
- [wiki/people/demis-hassabis.md](./wiki/people/demis-hassabis.md)
- [wiki/people/fei-fei-li.md](./wiki/people/fei-fei-li.md)
- [wiki/models/gpt-5-4.md](./wiki/models/gpt-5-4.md)
- [wiki/models/gemma-4.md](./wiki/models/gemma-4.md)
- [wiki/concepts/memory.md](./wiki/concepts/memory.md)
- [wiki/concepts/context-engineering.md](./wiki/concepts/context-engineering.md)
- [wiki/concepts/llm-wiki.md](./wiki/concepts/llm-wiki.md)
- [wiki/companies/openai-agent-stack.md](./wiki/companies/openai-agent-stack.md)
- [wiki/companies/anthropic-agent-stack.md](./wiki/companies/anthropic-agent-stack.md)
- [wiki/companies/google-agent-stack.md](./wiki/companies/google-agent-stack.md)
- [wiki/comparisons/openai-vs-anthropic-agent-stack.md](./wiki/comparisons/openai-vs-anthropic-agent-stack.md)
- [wiki/comparisons/gpt-5-4-vs-gemma-4.md](./wiki/comparisons/gpt-5-4-vs-gemma-4.md)
- [wiki/comparisons/memory-vs-context-engineering.md](./wiki/comparisons/memory-vs-context-engineering.md)

## 仓库结构

```text
.
├── AGENTS.md
├── AI关键人物追踪.md
├── README.md
├── AI三巨头博客追踪.md
├── agent-eval-benchmark追踪.md
├── MCP-tools-agent-infra追踪.md
├── agent-llm周GitHub热点追踪.md
├── agent-llm周论文追踪.md
├── wiki
│   ├── README.md
│   ├── companies
│   ├── comparisons
│   ├── concepts
│   ├── index.md
│   ├── log.md
│   ├── models
│   ├── people
│   └── templates
└── 模型发布追踪.md
```

## 使用方式

建议从下面顺序阅读：

1. 先看 `AI三巨头博客追踪`，快速理解大厂当前公开主线
2. 再看 `AI关键人物追踪`，理解哪些人最值得长期盯
3. 然后看 `模型发布追踪`，建立模型层的横向比较基线
4. 再看 `MCP / tools / agent infra追踪`，理解工程基础设施主线
5. 然后看 `agent-eval-benchmark追踪`，收口评测和 benchmark 方法学
6. 再看 `agent-llm周论文追踪`，补研究侧趋势和长期主题
7. 最后看 `agent-llm周GitHub热点追踪`，判断哪些方向已经开始工程化
8. 如果要沉淀长期知识，再进入 `wiki/`

## 更新原则

- 优先保留高信号条目，不追求面面俱到
- 每周新增条目控制在少量核心内容，避免文档失焦
- 新增内容尽量回答三个问题：
  - 发生了什么
  - 为什么重要
  - 对我们的实际影响是什么
- 根目录文档负责 `周更和判断`，`wiki/` 负责 `长期沉淀和复用`

## 追踪分工与去重规则

为避免同一事件在多份文档里重复展开，后续按下面规则记录：

- `AI三巨头博客追踪`：只记录三家公司官方发布的路线信号和横向判断，不重复写完整模型参数、论文细节或 GitHub 项目拆解。
- `模型发布追踪`：只维护模型层基线，包括模型名、定位、能力变化、适用场景和来源；同一模型相关的 runtime、eval、人物动态只保留短链接。
- `agent-llm周论文追踪`：作为论文主入口，负责新论文筛选、主题判断和建议动作；评测文档只引用论文结论，不重复全文展开。
- `agent-eval-benchmark追踪`：只维护评测方法、benchmark schema、grader/rubric/observability 设计，不重复记录普通模型发布。
- `MCP-tools-agent-infra追踪`：只维护 runtime、MCP、tool use、sandbox、memory、privacy、observability 等工程基础设施。
- `agent-llm周GitHub热点追踪`：只记录开源项目热度和工程信号，不把官方博客或论文内容复制进来。
- `AI关键人物追踪`：只记录人物路线变化和来源入口，不重复公司发布内容；公司正式发布回链到对应专题文档。

默认做法：一条高信号事件只在一个主文档展开，其他文档只写一句“影响判断 + 交叉链接”。历史周更可以保留，但新周更按这个规则收敛。

## 后续可扩展方向

- 新增 `eval / benchmark` 专题
- 新增 `安全 / governance` 专题
- 新增按周汇总的 `weekly digest`

## 最近一次补充

- `2026-04-28`：更新至最新一周高信号，补入 `OpenAI GPT-5.5 / Privacy Filter / GPT-Rosalind`、`Anthropic Claude Opus 4.7 / Claude Design / Amazon 5GW compute`、`Google Gemini Enterprise Agent Platform / Decoupled DiLoCo`，补充 `HORIZON / AgenticQwen / SkillGraph / Tool-Overuse` 等论文漏项，并新增追踪分工与去重规则。
- `2026-04-17`：已继续更新根目录追踪文档，新增 `OpenAI Agents SDK` 与 `Codex for (almost) everything`、`Google Gemini Robotics-ER 1.6 / Flash TTS`、`AMA-Bench / StructMemEval / self-evolving agent` 等论文补录，并刷新 GitHub 热点与关键人物判断。
- `2026-04-11`：已全面更新根目录追踪文档，补入 `OpenAI GPT-5.4 mini/nano` 与 `enterprise AI operating layer`、`Anthropic Mythos preview / Project Glasswing / compute partnership` 与最新 `managed agents / auto mode / harness / eval` 信号、`Google Gemini 3.1 Pro / Flash Live / Gemma 4 / Antigravity`，并刷新论文、评测、GitHub 热点和人物判断。
- `2026-04-06`：已为 `AI三巨头博客追踪`、`AI关键人物追踪`、`模型发布追踪`、`MCP-tools-agent-infra追踪`、`agent-eval-benchmark追踪`、`agent-llm周论文追踪`、`agent-llm周GitHub热点追踪` 追加最新条目与补录，并新增 `wiki/` 最小结构，不删除旧内容。
