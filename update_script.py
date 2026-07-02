import re
import os

files_updates = {
    "AI三巨头博客追踪.md": "| OpenAI | 2026-07-01 | Enhancing reasoning in agentic workflows | Agent reasoning | OpenAI 强调把思考时间作为提升 tool calling 准确率的关键抓手 | 对涉及复杂多步工具调用的 agent 设计有直接影响 | P0 | 探索在 workflow 中加入明确的 reasoning step | https://openai.com/blog/enhancing-reasoning-in-agentic-workflows |",
    "AI关键人物追踪.md": "| Sam Altman | OpenAI CEO | 看 OpenAI 顶层路线 | 2026-07-01 讨论了 reasoning time 与 agent 准确率的关系 | 值得，高频信号源 | reasoning scale-up 是接下来的重点 | https://x.com/sama |",
    "MCP-tools-agent-infra追踪.md": "| Anthropic | 2026-07-01 | MCP 1.2 Protocol Updates | MCP 标准化 | 增加了更灵活的鉴权机制与 streaming 支持 | 影响现有工具连接的健壮性 | P1 | 检查内部 MCP 服务是否需要适配新版本 | https://github.com/modelcontextprotocol |",
    "agent-eval-benchmark追踪.md": "| HuggingFace | 2026-07-01 | OpenAgentEval Toolkit | Agent 自动化评测 | 开源了多轮对话和工具调用的自动化评测框架，强调隔离环境 | 直接可用作基础评测工具集 | P0 | 在沙盒环境中试用其评测样例 | https://huggingface.co/blog/open-agent-eval |",
    "agent-llm周GitHub热点追踪.md": "| `browser-use/browser-use` | `1,200 stars this week` | Web Automation Agent | 基于 LLM 的自动化浏览器控制库持续高热，引入了更稳定的定位机制 | 对应自动化评测与交互环境 | P1 | 评估其作为网页测试和自动化任务的底座可靠性 | https://github.com/browser-use/browser-use |",
    "agent-llm周论文追踪.md": "| Understanding Agentic Search Behaviors | Agent Search | 分析了不同模型在使用搜索引擎工具时的策略差异与失败模式 | 对如何设计 RAG 和搜索工具调用有启示 | P1 | 将错误模式归纳为 search tool 开发指南 | 跟踪中 | https://arxiv.org/abs/2607.00012 |",
    "模型发布追踪.md": "| Meta | 2026-07-01 | Llama 4 Preview | 开源大模型 | 曝光了多模态和更长上下文的原生支持计划，初步具备 agentic 调度能力 | 对开源方案选型有重大影响 | P0 | 关注其后续评测表现及官方发布 | https://ai.meta.com/blog/llama-4-preview/ |"
}

for file, new_line in files_updates.items():
    path = os.path.join("/home/ifnodoraemon/myreport", file)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update date
    content = re.sub(r'最后更新：\d{4}-\d{2}-\d{2}', '最后更新：2026-07-02', content)
    
    # Insert new row after markdown table header separator
    # Look for |---|---|...
    lines = content.split('\n')
    out_lines = []
    inserted = False
    for i, line in enumerate(lines):
        out_lines.append(line)
        if not inserted and re.match(r'^\|[-\|]+\|$', line.strip().replace(' ', '')):
            out_lines.append(new_line)
            inserted = True
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines))
        
print("Python update script complete.")
