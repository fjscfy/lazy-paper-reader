# Separate Title and Abstract Stages Design

## Goal

Prevent the title stage from over-interpreting the paper while ensuring the abstract receives a complete, explicit reading before the introduction.

## Stage Order

The workflow becomes six confirmed stages:

1. Title Reading
2. Abstract and Task Positioning
3. Introduction
4. Method
5. Experiments
6. Conclusion

Title and abstract are separate interaction and note-writing boundaries. Each stage is explained, discussed, explicitly confirmed, and written before the next begins. Each may contain its own optional Questions and Clarifications subsection.

## Title Reading

The title stage explains only information directly supported by the words in the title:

- the named research object, domain, or task, when explicit;
- the named method family, representation, or system role, when explicit;
- the characteristic or claim emphasized by the wording;
- ambiguous terms or likely paper-specific names that must be resolved later.

Do not use the abstract or introduction to enrich this stage. Do not infer exact inputs, outputs, motivation, architecture, novelty, or experimental outcome unless the title states them. Mark unresolved points as unknown rather than completing the story from convention.

The note uses a top-level `Title Reading` heading translated into the user's language.

## Abstract and Task Positioning

After the title stage is confirmed, read the abstract as the author's compressed account of the paper. Reconstruct:

- the task and setting;
- why the task matters, when the abstract states it;
- the existing limitation or research gap;
- the proposed high-level idea;
- inputs and outputs only when reported or directly recoverable;
- the main experimental result or capability claim;
- the author's claimed contribution.

End with a short verification ledger that separates:

- claims to verify in the Method section;
- claims to verify in the Experiments section;
- information the abstract does not report.

The abstract stage establishes a provisional task position, not a final judgment. Later sections may narrow or overturn it. The note uses a top-level `Abstract and Task Positioning` heading translated into the user's language.

## Existing Notes

When resuming a note that combines title and task positioning, preserve the user's text. Split it only when the current session revisits that material and the separation can be performed without losing wording. Do not silently reorganize untouched sections.

## Scope

Update the core stage loop, detailed reading workflow, Markdown note structure, README workflow summary, and contract tests. Preserve source resolution, confirmation-before-write behavior, curated stage Q&A, method and experiment analysis, conclusion anchors, and the autonomous-driving world-model profile.

## Verification

- Contract tests require six stages in the correct order.
- Contract tests require literal-only title reading and prohibit abstract-based enrichment during that stage.
- Contract tests require explicit abstract reconstruction and a Method/Experiments verification ledger.
- README and Markdown structure must show separate title and abstract stages.
- Existing tests and official skill validation must continue to pass.
