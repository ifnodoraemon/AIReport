sed -i 's/最后更新：[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/最后更新：2026-07-16/' AI三巨头博客追踪.md

awk '
/^### Anthropic/ {
  print $0
  print "\n- `Anthropic` | `2026-07-15` | `Agentic Misalignment in Summer 2026`"
  print "  方向：`safety / alignment / agentic risks`"
  print "  核心信号：Anthropic 探讨了随着 Agent 能力增强可能出现的对齐风险及管理方法。"
  print "  为什么重要：在 Agent 走向生产环境的同时，企业界需要应对由长线任务代理带来的安全对齐问题。"
  print "  来源日期：`2026-07-15`"
  print "  来源：https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/"
  next
}
/^### Google \/ DeepMind/ {
  print $0
  print "\n- `Google DeepMind` | `2026-07-15` | `Google DeepMind Talent & Strategy`"
  print "  方向：`talent / strategy / deepmind`"
  print "  核心信号：前 DeepMind 员工讨论了 Google DeepMind 目前的战略方向和人才流动。"
  print "  为什么重要：侧面反映了 Google 在基础模型与 AI 代理竞争下的内部研究方向调整。"
  print "  来源日期：`2026-07-15`"
  print "  来源：https://turntrout.com/why-i-left-google-deepmind"
  next
}
{ print }
' AI三巨头博客追踪.md > tmp.md && mv tmp.md AI三巨头博客追踪.md
