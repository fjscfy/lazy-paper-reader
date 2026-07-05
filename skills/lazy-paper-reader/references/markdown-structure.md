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
7. Report the updated file path and stop at the next stage boundary.
