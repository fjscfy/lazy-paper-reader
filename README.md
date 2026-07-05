# lazy-paper-reader

Interactive paper reading, not one-shot summarization.

`lazy-paper-reader` is a Codex Agent Skill that helps you reconstruct a paper's argument and evidence stage by stage. It explains one section at a time, resolves questions in conversation, and updates a single Markdown note only after you confirm the interpretation.

## Why use it?

- Reads in stages instead of overwhelming you with a full-paper summary.
- Connects each method design to its motivation and author justification.
- Separates paper statements, reasonable inference, and critique.
- Treats experiments as evidence: what each result supports and what it does not.
- Resumes from an existing Markdown note without overwriting your wording.
- Adds a dedicated review profile for autonomous-driving world models.

## Reading workflow

1. Title and task positioning
2. Introduction and its argument chain
3. Method, motivation, data flow, and distinctive design choices
4. Experimental setup, qualitative evidence, and quantitative evidence
5. Conclusion with three retrieval anchors:
   - One-sentence memory point
   - What is genuinely new
   - Key assumptions and limitations

Related Work is skipped on the first pass and revisited only when a novelty claim needs verification.

## Supported inputs

- A local PDF
- An official paper URL
- A paper title to resolve to a primary source
- An existing Markdown note to resume

## Install

Codex discovers user-level Agent Skills from `$HOME/.agents/skills`.

```bash
git clone https://github.com/fjscfy/lazy-paper-reader.git
mkdir -p "$HOME/.agents/skills"
cp -R lazy-paper-reader/skills/lazy-paper-reader "$HOME/.agents/skills/lazy-paper-reader"
```

Codex detects skill changes automatically. If the skill does not appear, restart Codex.

Invoke it explicitly:

```text
Use $lazy-paper-reader to guide me through this paper stage by stage and maintain one Markdown note.
```

Codex may also invoke it implicitly when your request matches the skill description.

## Repository structure

```text
skills/lazy-paper-reader/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── reading-workflow.md
    ├── markdown-structure.md
    └── autonomous-driving-world-model.md
```

## License

[MIT](LICENSE)

## 中文说明

`lazy-paper-reader` 是一个交互式 Codex 论文阅读 Skill。它不会一次性生成整篇摘要，而是按“标题与任务定位 → 引言 → 方法 → 实验 → 结论”逐阶段讲解；只有在你确认当前理解后，才会更新同一份 Markdown 笔记。

它支持本地 PDF、论文链接、论文标题和已有笔记，并为自动驾驶 World Model 论文提供额外的分析视角。用户级安装目录为 `$HOME/.agents/skills/lazy-paper-reader`。
