# Conversational Uncertainty Check Design

## Goal

Make the skill expose uncertainty and likely blind spots before the user confirms each reading stage, without adding routine meta-commentary to the Markdown note.

## Interaction Point

For every reading stage, run the uncertainty check after the stage explanation and question discussion have stabilized, but before asking for explicit confirmation to write the stage.

The assistant proactively answers exactly two prompts:

1. What judgment am I least certain about right now? Does the uncertainty come from information the paper does not state, insufficient evidence, or a relevant section that has not been read yet?
2. What are we most likely overlooking or taking for granted right now? Are there unchecked assumptions, alternative explanations, counterexamples, or evaluation dimensions?

Translate the prompts and answers into the user's language.

## Output Behavior

Present the answers under one compact conversational label such as `Uncertainty Check`. Keep each answer concrete and tied to the current paper stage.

Do not produce generic cautions merely to fill the structure. If no material uncertainty or blind spot is found, say so briefly and state why the current evidence is sufficient at this stage.

If the check triggers further user questions or changes the interpretation, continue the discussion, revise the stage understanding, and run the two-item check again before requesting confirmation.

## Persistence Boundary

The uncertainty check is conversational only by default:

- do not write it into the Markdown note;
- do not treat it as a reader question for `Questions and Clarifications`;
- do not add it to candidate clarification tracking;
- write it only if the user explicitly requests that specific content be preserved.

The check does not replace the abstract verification ledger, evidence labels, critique, or stage Q&A. It is a final epistemic pause before the existing confirmation gate.

## Scope

Update the core stage loop and detailed reading workflow. Add contract coverage and a concise README feature bullet. Preserve the six stages, Markdown structure, source resolution, Obsidian formula rules, and all domain-specific profiles.

## Verification

- Contract tests require both prompts and their placement before explicit confirmation.
- Contract tests require conversation-only behavior and exclusion from Markdown and Q&A tracking.
- Existing tests and official skill validation must continue to pass.
- The installed skill and GitHub `main` must match the repository source after publication.
