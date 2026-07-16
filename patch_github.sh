sed -i 's/最后更新：[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/最后更新：2026-07-16/' agent-llm周GitHub热点追踪.md

awk '
/^## 本周新增热点项目/ {
  print $0
  print "\n### 1. [vibe-investing](https://github.com/gameworkerkim/vibe-investing)"
  print "- **标签**：`agent / finance`"
  print "- **趋势**：`2026-07-16` 新晋趋势项目"
  print "- **简介**：围绕投资分析与决策辅助的 AI 代理工具流。"
  print "- **为什么值得关注**：展示了 Agent 框架在垂直金融领域的应用扩展。"
  print "\n### 2. [codegen_orchestrator](https://github.com/vladmesh/codegen_orchestrator)"
  print "- **标签**：`agent / codegen / orchestrator`"
  print "- **趋势**：`2026-07-16` 活跃度上升"
  print "- **简介**：用于管理多个代码生成 Agent 协作编排的框架。"
  print "- **为什么值得关注**：符合当前多智能体（Multi-agent）编排趋势，尤其在代码编写和维护场景中。"
  print "\n### 3. [ledgerlens](https://github.com/zzlawlzz/ledgerlens)"
  print "- **标签**：`agent / infra`"
  print "- **趋势**：`2026-07-16` 更新"
  print "- **简介**：专注于账本及日志洞察的轻量级 Agent 工具链。"
  print "- **为什么值得关注**：数据分析与审计的专属工具代理化。"
  next
}
{ print }
' agent-llm周GitHub热点追踪.md > tmp.md && mv tmp.md agent-llm周GitHub热点追踪.md
