# Stage Question Clarifications Design

## Goal

Make each paper-reading note preserve the reader's most important conceptual obstacles without turning the note into a conversation transcript.

## Note Structure

Each top-level reading stage may end with one optional subsection:

```markdown
## Questions and Clarifications

- **Question:** <the reader's original question>
  **Answer:** <the concise, confirmed answer>
```

Translate the subsection title and labels into the user's language. Omit the subsection when the stage produced no question that materially affected understanding.

## Selection Rules

Record a question only when it does at least one of the following:

- exposes a mistaken assumption;
- distinguishes two easily confused concepts;
- clarifies an input, output, representation, objective, training path, inference path, metric, or experimental claim;
- changes the interpretation of the paper's motivation, method, novelty, evidence, assumption, or limitation;
- captures a reusable insight the reader is likely to need later.

Do not record navigation requests, formatting preferences, repeated questions that add no new distinction, or conversational housekeeping. Merge overlapping questions while preserving the clearest original wording from the user.

## Writing Behavior

During a stage, answer questions conversationally and keep candidate clarifications in working context. Do not write them immediately.

When the user explicitly confirms the stage:

1. Write or revise the confirmed stage summary.
2. Add the selected questions at the end of that same stage.
3. Preserve each selected question in the user's original wording, except for minimal typo or reference cleanup needed to make it understandable outside the chat.
4. Write the answer as the final confirmed understanding, not as a transcript and not as the assistant's first attempt.
5. Keep answers self-contained and concise, while retaining equations or examples when they are essential to the distinction.

If later discussion changes an answer, update both the stage summary and the corresponding clarification. Never leave a stale answer that contradicts the main note.

## Existing Notes

When resuming an existing note, preserve the user's current questions and comments. Reuse an equivalent existing Q&A subsection instead of creating a duplicate. Apply the new structure only to stages discussed or revised in the current reading session.

## Scope

This change updates the reading workflow and Markdown note contract. It does not change the five reading stages, confirmation-before-write behavior, conclusion anchors, source resolution, or autonomous-driving world-model profile.

## Verification

- Contract tests require the optional per-stage subsection and its selection rules.
- Contract tests require preservation of the user's question wording and a distilled confirmed answer.
- Contract tests reject transcript-style logging and immediate unconfirmed writes.
- Existing skill validation and all prior contract tests must continue to pass.
