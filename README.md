# AIReport

`AIReport` 是一个持续维护的 AI 趋势追踪仓库，当前重点覆盖：

- `Agent / LLM` 论文追踪
- `Agent / LLM` GitHub 热点追踪
- `OpenAI / Anthropic / Google` 官方博客追踪
- `AI 关键人物` 追踪
- `模型发布` 追踪
- `MCP / tools / agent infra` 追踪
- `Agent eval / benchmark` 追踪

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

## 更新原则

- 优先保留高信号条目，不追求面面俱到
- 每周新增条目控制在少量核心内容，避免文档失焦
- 新增内容尽量回答三个问题：
  - 发生了什么
  - 为什么重要
  - 对我们的实际影响是什么

## 后续可扩展方向

- 新增 `eval / benchmark` 专题
- 新增 `安全 / governance` 专题
- 新增按周汇总的 `weekly digest`

## 最近一次补充

- `2026-04-06`：已为 `AI三巨头博客追踪`、`AI关键人物追踪`、`模型发布追踪`、`MCP-tools-agent-infra追踪`、`agent-eval-benchmark追踪`、`agent-llm周论文追踪`、`agent-llm周GitHub热点追踪` 追加最新条目与补录，不删除旧内容。
