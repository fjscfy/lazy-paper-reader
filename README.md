# lazy-paper-reader

Interactive paper reading, not one-shot summarization.

`lazy-paper-reader` is a Codex Agent Skill that helps you reconstruct a paper's argument and evidence stage by stage. Use it for conversation-only reading or for maintaining a cumulative Markdown note.

## Why use it?

- Reads in stages instead of overwhelming you with a full-paper summary.
- Connects each method design to its motivation and author justification.
- Separates paper statements, reasonable inference, and critique.
- Treats experiments as evidence: what each result supports and what it does not.
- Resumes from an existing Markdown note without overwriting your wording.
- Adds a dedicated review profile for autonomous-driving world models.
- Surfaces the least-certain judgment and likely blind spot before each stage is confirmed.
- Lets you jump to, skip, or revisit any stage instead of forcing a linear reading order.
- Reopens the abstract's claims after Method and Experiments so provisional claims become evidence-backed conclusions.

## Working modes

- **Conversation mode:** the default when you only want explanation or critique. No output path and no note writes.
- **Note mode:** enabled when you provide a note or ask to create or update one. Every write requires confirmation.

You can switch modes during a reading session. Earlier discussion is never backfilled into a note without confirmation.

## Reading workflow

1. Title Reading
2. Abstract and Task Positioning
3. Introduction and its argument chain
4. Method, motivation, data flow, and distinctive design choices
5. Experimental setup, qualitative evidence, and quantitative evidence
6. Conclusion with three retrieval anchors:
   - One-sentence memory point
   - What is genuinely new
   - Key assumptions and limitations

This is the default route. You can start from Method, jump to Experiments, revisit the Abstract, or skip any stage. Related Work is skipped on the first pass and revisited only when a novelty claim needs verification.

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

`lazy-paper-reader` 是一个交互式 Codex 论文阅读 Skill，支持只对话、不写笔记的默认模式，也支持经确认后持续维护 Markdown 笔记。六阶段是推荐路线，不是强制顺序，可以直接跳到方法、实验或任意阶段。

它支持本地 PDF、论文链接、论文标题和已有笔记，并为自动驾驶 World Model 论文提供额外的分析视角。用户级安装目录为 `$HOME/.agents/skills/lazy-paper-reader`。
