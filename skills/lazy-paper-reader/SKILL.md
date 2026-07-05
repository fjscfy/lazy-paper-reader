---
name: lazy-paper-reader
description: Use when a user wants to read, understand, critique, or resume notes on a research paper from a local PDF, paper URL, paper title, or existing Markdown note.
---

# Lazy Paper Reader

## Core principle

Reconstruct the paper's argument and evidence with the user instead of producing a one-shot summary. Read one stage at a time, resolve questions in conversation, and write only the understanding the user has confirmed.

## Load the protocol

Before reading a paper:

1. Read `references/reading-workflow.md` completely.
2. Read `references/markdown-structure.md` completely.
3. If the paper concerns autonomous-driving world models, also read `references/autonomous-driving-world-model.md` completely. Do not load this domain profile for unrelated papers.

## Resolve the source and note

Support all four source modes: local PDF, paper URL, paper title, and existing Markdown note.

1. If an existing Markdown note is supplied, read it first and resume from the first incomplete stage. Preserve the user's wording and edits.
2. Otherwise, prefer an official HTML or TeX source, then an official PDF. Resolve a paper title to a primary source before analysis.
3. Ask for the output path before creating a new note. Maintain one Markdown note per paper; never create a duplicate silently.
4. Match the user's language unless they request another language.

## Run the stage loop

Use this order: title and task positioning, introduction, method, experiments, conclusion.

For every stage:

1. Read only the source material needed for that stage.
2. Explain it conversationally, using the paper's logic rather than line-by-line translation.
3. Pause for questions and correction.
4. Obtain explicit confirmation before writing that stage to the Markdown note.
5. Append or revise only the confirmed section, preserving unrelated note content.
6. Move to the next stage only after the write is complete.

Never read and summarize the entire paper before the first response. Never write an unconfirmed interpretation. If the user changes an interpretation, update the note before continuing.

## Maintain evidence discipline

- Separate paper statements, reasonable inference, and critique using the conventions in `references/markdown-structure.md`.
- Mark missing details as not reported; do not infer datasets, resources, supervision, or causal claims from convention.
- Treat a metric as evidence only for the property it measures. Visual quality does not establish dynamics, causality, planning value, or closed-loop safety.
- Skip Related Work on the first pass. Return to specific related-work passages only when checking a novelty claim or comparison.

## Complete the reading

End the note with exactly these three conclusion anchors:

1. One-sentence memory point.
2. What is genuinely new compared with prior work.
3. Key assumptions and limitations.

Do not replace the detailed note with these anchors; they are the retrieval handle for the completed reading.

## Common mistakes

- Listing every input condition instead of identifying the paper's distinctive idea.
- Restating the abstract without recovering the introduction's argument chain.
- Describing modules without mapping each design back to its motivation.
- Copying result tables without stating what each experiment proves.
- Treating author framing as established fact.
- Producing many shallow headings that make the note harder to remember.
