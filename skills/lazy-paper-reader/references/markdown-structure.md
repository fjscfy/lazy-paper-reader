# Markdown Note Contract

Maintain one note per paper. Use a fixed top-level structure for comparison across papers while preserving each paper's original subsection names inside Method and Experiments.

## Default structure

```markdown
# Title and Task Positioning

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

Translate headings into the user's language. If an existing Markdown note uses equivalent headings, update them instead of adding duplicates.

## Writing rules

- Write the confirmed understanding, not a transcript of the conversation.
- Prefer cohesive paragraphs for argument and concise bullets for mappings, configurations, or comparisons.
- Keep the number of headings proportional to the paper. Do not create a heading for every small observation.
- Preserve original subsection names under Method and Experiments so readers can return to the source.
- Preserve the user's existing comments, questions, images, PDF links, and wording unless they explicitly approve a rewrite.
- Do not force YAML frontmatter. Preserve it when already present.
- Cite a page, section, equation, figure, or table when it materially helps verification.

## Epistemic labels

Use labels only where authorship or certainty could otherwise be confused:

- **Paper statement:** what the authors explicitly claim or report.
- **Inference:** a conclusion derived from the method, equation, or evidence but not stated directly.
- **Critique:** the reader's or assistant's evaluation, concern, or alternative interpretation.

Render these labels in the user's language. Do not label obvious factual exposition sentence by sentence.

## Incremental write contract

Before every write:

1. Identify the single confirmed top-level section.
2. Re-read the existing note around that section.
3. Merge clarification into the section instead of appending contradictory fragments.
4. Modify only that section.
5. Report the updated file path and stop at the next stage boundary.
