---
name: lazy-paper-reader
description: Use when a user wants guided, stage-by-stage understanding or critique of a research paper, or wants to create or resume cumulative Markdown paper notes from a local PDF, paper URL, paper title, or existing note.
---

# Lazy Paper Reader

## Core principle

Reconstruct the paper's argument and evidence with the user instead of producing a one-shot summary. Read one stage at a time, resolve questions in conversation, and write only the understanding the user has confirmed.

## Load the protocol

Before reading a paper:

1. Resolve the source and working mode using the next section.
2. Read `references/reading-workflow.md` completely.
3. Only in Note mode, read `references/markdown-structure.md` completely. Do not load the writing contract in Conversation mode.
4. If the paper concerns autonomous-driving world models, also read `references/autonomous-driving-world-model.md` completely. Do not load this domain profile for unrelated papers.

## Resolve the source and working mode

Support all four source modes: local PDF, paper URL, paper title, and existing Markdown note.

1. If an existing Markdown note is supplied, read it first and resume from the first incomplete stage. Preserve the user's wording and edits.
2. Otherwise, prefer an official HTML or TeX source, then an official PDF. Resolve a paper title to a primary source before analysis.
3. Use Conversation mode by default when the user has not asked to create, save, or update notes. In Conversation mode, do not ask for an output path and do not write a note.
4. Use Note mode when the user supplies an existing Markdown note or explicitly asks to create, save, maintain, or update one. If no note path is known, ask for it before the first write. Maintain one Markdown note per paper; never create a duplicate silently.
5. Let the user switch modes at any time. When switching into Note mode, ask where to write and obtain confirmation before backfilling any earlier discussion.
6. Match the user's language unless they request another language.

## Run the stage loop

Use this default order: Title Reading, Abstract and Task Positioning, Introduction, Method, Experiments, Conclusion. It is a navigation guide, not a prerequisite chain. Follow the user's requested stage; let them jump ahead, skip a stage, revisit an earlier stage, or resume wherever useful.

For every requested stage:

1. Read only the source material needed for that stage.
2. Explain it conversationally, using the paper's logic rather than line-by-line translation.
3. Pause for questions and correction. Retain only questions that materially change or sharpen the reader's understanding as candidate clarifications.
4. Run the two-item conversational uncertainty check defined in `references/reading-workflow.md`. If it changes the interpretation, continue discussion, revise the stage understanding, and run the check again.
5. In Conversation mode, continue according to the user's direction without requesting write confirmation.
6. In Note mode, obtain explicit confirmation before writing that stage to the Markdown note.
7. Append or revise only the confirmed section and any permitted linked ledger update. At the section's end, write the selected questions with the reader's original wording and concise, confirmed answers; omit the subsection when no question qualifies.
8. Preserve unrelated note content.
9. After the conversation or write is complete, follow the user's requested stage or offer the next stage in the default order.

In guided mode, never read and summarize the entire paper before the first response. If the user explicitly requests a one-shot overview, honor that scope without pretending every stage has been completed. Never write an unconfirmed interpretation. In Note mode, if the user changes an interpretation, update the affected note section before continuing.

## Maintain evidence discipline

- Separate paper statements, reasonable inference, and critique using the conventions in `references/markdown-structure.md`.
- Mark missing details as not reported; do not infer datasets, resources, supervision, or causal claims from convention.
- Treat a metric as evidence only for the property it measures. Visual quality does not establish dynamics, causality, planning value, or closed-loop safety.
- Skip Related Work on the first pass. Return to specific related-work passages only when checking a novelty claim or comparison.

## Complete the reading

At the conclusion, present exactly these three retrieval anchors; in Note mode, end the note with them:

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
- Logging every exchange as Q&A instead of curating questions that preserve a useful conceptual distinction.
