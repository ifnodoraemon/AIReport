# Repository Guidelines

## Project Structure & Module Organization

This repository is a Markdown-first research and tracking repo. There is no application source code, test suite, or build output.

- `README.md`: entry point and reading order.
- `AI三巨头博客追踪.md`: official blog tracking for OpenAI, Anthropic, and Google/DeepMind.
- `agent-llm周论文追踪.md`: paper tracking for agent, LLM, memory, RAG security, and evals.
- `agent-llm周GitHub热点追踪.md`: weekly GitHub trend analysis.
- `AGENTS.md`: contributor instructions for future updates.

Keep new files at the repository root unless a clear subdirectory structure becomes necessary.

## Build, Test, and Development Commands

There is no build pipeline for this repository. Use lightweight validation before committing:

- `git status`: confirm intended file changes.
- `git diff --check`: catch trailing whitespace and conflict markers.
- `rg '^#|^##' *.md`: quickly review heading structure across documents.
- `sed -n '1,200p' README.md`: preview a document section from the terminal.

If a richer Markdown lint step is introduced later, document it here before relying on it.

## Coding Style & Naming Conventions

Write in concise, professional Markdown. Prefer short sections, flat bullet lists, and tables only when comparison is useful.

- Use UTF-8 Markdown files with clear `#`, `##`, `###` headings.
- Keep file names descriptive and stable; existing topic files use Chinese names plus domain keywords.
- Update `最后更新：YYYY-MM-DD` whenever content meaningfully changes.
- Prefer relative links inside the repo, for example `./AI三巨头博客追踪.md`.
- Cite primary sources directly; do not paste long quotations.

## Testing Guidelines

Testing here means editorial validation:

- Verify dates, company names, and source URLs.
- Check that new sections match the existing templates.
- Confirm tables remain readable in GitHub Markdown.
- Re-read for duplication and low-signal filler before committing.

## Commit & Pull Request Guidelines

Current history uses short, imperative commit messages such as `Initial commit` and `Add repository README and gitignore`. Continue that style.

- Good examples: `Add weekly model release tracker`, `Update AI三巨头博客追踪`
- Keep each commit focused on one document set or one maintenance task.

For pull requests, include:

- a short summary of what changed,
- the documents affected,
- any new source categories added,
- screenshots only if formatting changed substantially in GitHub preview.

## Agent-Specific Instructions

Preserve the repository’s purpose: high-signal tracking, not news dumping. When adding entries, explain what changed, why it matters, and what action it suggests.

