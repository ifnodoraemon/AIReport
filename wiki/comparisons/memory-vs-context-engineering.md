# Memory vs Context Engineering

最后更新：2026-04-06

关联页面：

- [Memory](../concepts/memory.md)
- [Context Engineering](../concepts/context-engineering.md)
- [LLM Wiki](../concepts/llm-wiki.md)

## 比较目的

这页用来避免把 `memory` 和 `context engineering` 混成同一个词。

## 当前结论

### 1. `memory` 更强调长期保留与更新

主要问题是：

- 记住了什么
- 更新得对不对
- 会不会忘错
- 能不能跨 session 保持一致

### 2. `context engineering` 更强调当前任务中的组织与交付

主要问题是：

- 当前该给 agent 看什么
- 怎么压缩
- 怎么交接
- 怎么减少噪音和漂移

## 关系

- `memory` 是长期层
- `context engineering` 是任务交付层
- 二者高度重叠，但不等价

一个粗略理解是：

- `memory` 负责“知识和状态是否被保留”
- `context engineering` 负责“保留的内容如何进入当前任务”

## 为什么这个区分重要

如果不区分：

- 很容易把所有问题都归结成“上下文太短”
- 或者把所有问题都归结成“没记住”

但真实系统里常见的是：

- memory 有了，但 context 交付差
- 或 context 很干净，但长期记忆根本没建立

## 对我们的影响

后续做系统设计时，最好分开提需求：

- `memory requirements`
- `context requirements`

后续做评测时，也最好分开打分：

- `memory eval`
- `context quality eval`

## 当前建议

- 继续把 `memory-first` 作为主线
- 但不要把 `context engineering` 降格成 prompt 细节
- `LLM Wiki` 正好是把两者连接起来的一种实践
