# LLM Wiki

最后更新：2026-04-06

关联总览：

- [wiki/people/karpathy.md](../people/karpathy.md)
- [wiki/concepts/memory.md](./memory.md)
- [wiki/concepts/context-engineering.md](./context-engineering.md)
- [README.md](/home/ifnodoraemon/myreport/README.md)

## 这是什么

`LLM Wiki` 是 Karpathy 在 `2026-04-04` 发布的一个高信号概念：让 agent 把知识持续整理成结构化 wiki，而不是每次问答都临时做一次 `RAG`。

来源：

- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## 为什么重要

它真正改变的是知识系统的组织方式：

- `RAG` 更像按需检索
- `LLM Wiki` 更像持续编译知识

这会直接影响：

- memory
- context quality
- cross-session continuity
- handoff stability

## 当前判断

### 1. 它不是“再做一个笔记工具”

更准确地说，它是在把：

- 原始资料
- 结构化知识
- agent 更新规则

拼成一个可持续演进的知识系统。

### 2. 它特别适合当前这个仓库

因为这个仓库本来就在做：

- 周更追踪
- 高信号筛选
- 长期判断

差的正是一层能被长期复用的 page system，而不是更多单篇周报。

### 3. 它和普通 RAG 的区别很关键

- `RAG`：每次临时检索、临时拼接
- `LLM Wiki`：持续更新页面、沉淀结构、可被反复复用

## 最小实现应该包含什么

- `raw timeline`
- `wiki pages`
- `update rules`
- `change log`

在当前仓库里，已经分别对应到：

- 根目录总览文档
- `wiki/` 页面
- `wiki/README.md`
- `wiki/log.md`

## 当前仓库里的作用

这个仓库正在朝 `LLM Wiki` 方向渐进迁移：

- 根目录保留 `timeline + judgment`
- `wiki/` 负责 `stable knowledge`

这意味着以后新增内容可以同时落到两层：

- 周更新
- 长期沉淀

## 还要继续观察什么

- `LLM Wiki` 是否会从个人方法演变成更标准的平台模式
- 它会如何和 `context database`、`memory library`、`graph knowledge` 分工
- 这个仓库是否需要进一步补 `people / models / concepts / companies` 之外的页面类型
