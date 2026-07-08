# Markdown Note Contract

Maintain one note per paper. Use a fixed top-level structure for comparison across papers while preserving each paper's original subsection names inside Method and Experiments.

## Default structure

```markdown
# Title Reading

# Abstract and Task Positioning
## Claims to Verify in Method
## Claims to Verify in Experiments
## Not Reported in the Abstract

# Introduction
## Paragraph 1: <role or claim>
## Paragraph 2: <role or claim>

# Method
## <original subsection name>
## <original subsection name>

# Experiments
## Experimental Setup
## <original subsection name>

# Conclusion
## One-sentence memory point
## What is genuinely new
## Key assumptions and limitations
```

Each top-level stage may end with this optional subsection:

```markdown
## Questions and Clarifications

- **Question:** <the reader's original question>
  **Answer:** <the concise, confirmed answer>
```

Translate the subsection title and labels into the user's language. Omit it when no question materially affected understanding.

Translate headings into the user's language. If an existing Markdown note uses equivalent headings, update them instead of adding duplicates.

## Writing rules

- Write the confirmed understanding, not a transcript of the conversation.
- Keep Title Reading literal; do not retrospectively enrich it with information from the abstract or later sections.
- Prefer cohesive paragraphs for argument and concise bullets for mappings, configurations, or comparisons.
- Keep the number of headings proportional to the paper. Do not create a heading for every small observation.
- Preserve original subsection names under Method and Experiments so readers can return to the source.
- Preserve the user's existing comments, questions, images, PDF links, and wording unless they explicitly approve a rewrite.
- Preserve the reader's original wording for selected questions, allowing only minimal cleanup needed to understand the question outside the chat.
- Distill the final confirmed answer; this subsection is not a transcript of the conversation.
- Merge overlapping questions and exclude navigation, formatting, and housekeeping exchanges.
- If later discussion changes an answer, update the stage summary and its clarification together.
- Do not force YAML frontmatter. Preserve it when already present.
- Cite a page, section, equation, figure, or table when it materially helps verification.
- When resuming a note with a combined title-and-task section, split it only if the current session revisits that material, and preserve the user's wording.

## Obsidian math formulas

When the target note is located in an Obsidian vault:

- Inline math must use `$...$`. This includes variables inside tables, such as `$Q_h$` and `$D_t$`.
- Block math must use `$$...$$`, with the opening and closing `$$` delimiters each on their own line.
- Do not use `\(...\)` or `\[...\]`; these delimiters can render differently in Obsidian and are vulnerable to string-escaping errors.
- When LaTeX passes through a JavaScript string or tool wrapper, use a raw string such as `String.raw` or correctly double-escape backslashes. Verify that commands such as `\times`, `\theta`, and `\mid` reach the Markdown file with their backslashes intact.

Use this inline form:

```markdown
The high-resolution branch `$Q_h$` produces context token `$Z_1$`.
```

Use this block form:

```markdown
$$
P(D_{1:N};Z_1)=\prod_{t=2}^{N}P_\theta(D_t\mid D_{<t},Z_1).
$$
```

For example, a JavaScript wrapper may construct LaTeX with:

```javascript
const formula = String.raw`P_\theta(D_t\mid D_{<t},Z_1)`;
```

## Epistemic labels

Use labels only where authorship or certainty could otherwise be confused:

- **Paper statement:** what the authors explicitly claim or report.
- **Inference:** a conclusion derived from the method, equation, or evidence but not stated directly.
- **Critique:** the reader's or assistant's evaluation, concern, or alternative interpretation.

Render these labels in the user's language. Do not label obvious factual exposition sentence by sentence.

## Incremental write contract

Before every write:

1. Identify the single confirmed top-level section.
2. Select only candidate questions that materially affected understanding.
3. Re-read the existing note around that section.
4. Merge clarification into the section instead of appending contradictory fragments.
5. Write or revise the optional Questions and Clarifications subsection using original questions and confirmed answers.
6. Modify only that section; never write unconfirmed content.
7. If the stage contains formulas and the note is in an Obsidian vault, re-read the affected paragraphs and verify all of the following:
   - no `\(`, `\)`, `\[`, or `\]` delimiters remain;
   - variables that should be formulas are not left as plain parenthesized text such as `(Q_h)` or `(D_t)`;
   - every `$` and `$$` delimiter is paired, and each block delimiter occupies its own line;
   - every LaTeX command retains its complete backslash.
8. Before reporting the write complete, fix every formula-formatting problem found by the verification in step 7. Never report completion before this check passes.
9. Report the updated file path and stop at the next stage boundary.
