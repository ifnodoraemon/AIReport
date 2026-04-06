# AIReport Wiki

最后更新：2026-04-06

这不是对现有追踪文档的替代，而是它们的下层知识库。

目标：

- 保留根目录现有文档的 `周更 / 总览 / 判断`
- 把高复用信息沉淀成可持续维护的页面
- 让后续新增内容不只停留在“某周新增一条”，而能进入长期知识结构

## 结构

- `index.md`：wiki 总索引
- `log.md`：wiki 级别变更日志
- `people/`：关键人物页
- `models/`：模型页
- `concepts/`：主题页
- `companies/`：公司路线页
- `comparisons/`：横向比较页
- `templates/`：新页面模板

## 维护规则

- `raw timeline` 留在根目录追踪文档
- `stable knowledge` 写入 wiki 页面
- 页面尽量回答四个问题：
  - 这是什么
  - 为什么重要
  - 当前判断是什么
  - 还要继续观察什么
- 新增信息时，优先更新已有页面，只有明显新实体 / 新主题时才新建页面
- 页面里的结论尽量链接回根目录对应总览文档，避免脱离上下文

## 什么时候进 Wiki

默认规则：

- 如果一条信息只在当周有意义，保留在根目录专题追踪文档
- 如果一条信息预计会被重复引用 `2` 次以上，就进入 `wiki/`
- 如果它代表的是稳定实体或稳定主题，优先进入 `wiki/`

常见应该进 `wiki/` 的内容：

- 人物：`Sam Altman`、`Karpathy` 这类会被长期反复提到的人
- 模型：`GPT-5.4`、`Gemma 4` 这类需要持续对照的模型
- 概念：`memory`、`context engineering`、`LLM Wiki`
- 公司路线：`OpenAI agent stack`、`Anthropic agent stack`
- 对比：会被反复引用的稳定比较，例如 `OpenAI vs Anthropic`

常见不必马上进 `wiki/` 的内容：

- 单周热榜项目但未形成长期判断
- 一次性会议新闻
- 只出现一次且没有延续性的访谈观点

## 页面命名规则

- 人物页：`people/<slug>.md`
- 模型页：`models/<slug>.md`
- 概念页：`concepts/<slug>.md`
- 公司路线页：`companies/<slug>.md`
- 比较页：`comparisons/<slug>.md`
- 模板页：`templates/<type>.md`

`slug` 统一使用小写英文字母和连字符，例如：

- `sam-altman.md`
- `gpt-5-4.md`
- `context-engineering.md`

## 推荐更新流程

1. 先更新根目录专题追踪文档
2. 判断本次新增是否会长期复用
3. 若会复用，则同步更新对应 wiki 页
4. 在 `log.md` 追加一条记录
5. 如果没有合适页面，优先从 `templates/` 复制模板新建

## 当前种子页

- [people/karpathy.md](./people/karpathy.md)
- [people/andrew-ng.md](./people/andrew-ng.md)
- [people/sam-altman.md](./people/sam-altman.md)
- [people/dario-amodei.md](./people/dario-amodei.md)
- [models/gpt-5-4.md](./models/gpt-5-4.md)
- [models/gemma-4.md](./models/gemma-4.md)
- [concepts/memory.md](./concepts/memory.md)
- [concepts/context-engineering.md](./concepts/context-engineering.md)
- [concepts/llm-wiki.md](./concepts/llm-wiki.md)
- [companies/openai-agent-stack.md](./companies/openai-agent-stack.md)
- [companies/anthropic-agent-stack.md](./companies/anthropic-agent-stack.md)
- [companies/google-agent-stack.md](./companies/google-agent-stack.md)
- [comparisons/openai-vs-anthropic-agent-stack.md](./comparisons/openai-vs-anthropic-agent-stack.md)
- [comparisons/gpt-5-4-vs-gemma-4.md](./comparisons/gpt-5-4-vs-gemma-4.md)
- [comparisons/memory-vs-context-engineering.md](./comparisons/memory-vs-context-engineering.md)
