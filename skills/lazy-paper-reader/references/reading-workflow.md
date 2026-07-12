# Interactive Paper-Reading Workflow

Use this protocol for whichever stage the user requests. The numbered order is the default route, not a prerequisite chain. Explain first and answer questions in both working modes; request explicit confirmation only before a Note-mode write.

## Curate stage questions

While discussing a stage, retain a question as a candidate clarification only when it exposes a mistaken assumption, separates easily confused concepts, clarifies the method or evidence path, changes the interpretation of a claim, or captures a reusable insight.

Do not retain navigation requests, formatting preferences, conversational housekeeping, or repeated questions that add no new distinction. Merge overlapping candidates while preserving the clearest original wording from the reader.

In Note mode, at explicit confirmation, pass the selected candidates to the Markdown note contract together with the confirmed stage summary. If later discussion changes an answer, revise both the summary and the clarification. In Conversation mode, keep the exchange conversational unless the user switches modes and explicitly approves backfilling it.

## Summarize stage uncertainty after completion

Run this summary once per completed stage, not after each assistant answer or user question. Run it after the stage discussion ends in Conversation mode, and after the confirmed write in Note mode.

Summarize only material findings under two categories in the user's language:

- **Least certain judgments:** identify any current judgment whose uncertainty comes from information the paper does not state, insufficient evidence, or a relevant section that has not been read yet.
- **Possible blind spots:** identify any unchecked assumption, alternative explanation, counterexample, or evaluation dimension that could change the current interpretation.

Do not force an item into either category. Each category may contain zero, one, or multiple material items. If both are empty, say briefly that no material uncertainty or blind spot was identified at this stage; do not invent generic cautions merely to fill the structure.

This summary is conversation only by default. Do not write it to the Markdown note, do not treat it as a reader question, and do not add it to candidate clarification tracking unless the user explicitly asks to preserve that specific content.

If the summary triggers further discussion or changes the interpretation, reopen the stage. In Note mode, obtain confirmation before correcting the note. Rerun the summary after the corrected stage in Conversation mode or after the corrected write in Note mode.

## 1. Title Reading

Explain only information directly supported by the words in the title:

- the named research object, domain, or task, when explicit;
- the named method family, representation, or system role, when explicit;
- the characteristic or claim emphasized by the wording;
- ambiguous terms or likely paper-specific names that must be resolved later.

Do not use the abstract or introduction to enrich this stage. Do not infer exact inputs, outputs, motivation, architecture, novelty, or experimental outcome unless the title states them. Mark unresolved points as unknown rather than completing the story from convention.

## 2. Abstract and Task Positioning

Read the abstract as the authors' compressed account of the paper. Reconstruct:

- the task and setting;
- why the task matters, when stated;
- the existing limitation or research gap;
- the proposed high-level idea;
- inputs and outputs only when reported or directly recoverable;
- the main experimental result or capability claim;
- the authors' claimed contribution.

End with a short verification ledger:

- claims to verify in Method;
- claims to verify in Experiments;
- information the abstract does not report.

Treat this task positioning as provisional. Later sections may narrow or overturn it; do not present the abstract's framing as a final judgment.

Keep the abstract verification ledger alive across later stages. In Conversation mode, retain it in the working context. In Note mode, record it in the Abstract section and close its entries through linked updates after the relevant Method or Experiments stage is confirmed.

## 3. Introduction

Read the introduction paragraph by paragraph in order.

For each paragraph:

1. Treat the first sentence as a hypothesis for the paragraph's summary.
2. Read the remaining sentences and note any qualification, evidence, transition, or change of scope.
3. State the paragraph's role: context, task value, existing approach, limitation, research gap, proposed solution, contribution, or evidence preview.
4. Explain what logical dependency connects it to the previous paragraph.

After all paragraphs, reconstruct one argument chain:

```text
task importance -> current approach -> unresolved problem -> proposed idea -> claimed contribution
```

Do not translate every sentence. Do not accept a broad motivation when the actual method solves a narrower problem.

## 4. Method

Skip Related Work on the first pass. Read preliminaries only when they define notation or machinery required by the proposed method.

Start with a method-level map:

- inputs and their provenance;
- outputs;
- trainable and fixed components;
- training-time data flow;
- inference-time data flow;
- objectives and supervision.

Then retain the paper's original subsection names. For each subsection, answer:

- Which motivation or limitation does this design address?
- What exactly enters and leaves the component?
- What is trained, frozen, optimized, sampled, or computed by a fixed algorithm?
- How is it implemented?
- Why did the authors choose this design?
- What assumption makes the design valid?
- What is unique, and what is standard infrastructure?
- How does the paper justify the choice: derivation, ablation, citation, or intuition?

For equations, explain the objective, symbols, tensor roles, and gradient path only to the depth needed to understand the method. Distinguish a new model architecture from a data pipeline, training strategy, loss, or inference heuristic.

Before completing this stage, revisit every Method-related item in the abstract verification ledger. Mark each as Confirmed, Refined, Unsupported, or Still unknown, and state the evidence. In Note mode, update those ledger entries together with the confirmed Method section.

## 5. Experiments

Read experiment infrastructure before results:

- datasets, scene selection, train/validation/test split;
- baselines and comparison fairness;
- metrics and what each metric actually measures;
- training schedule, resolution, hardware, parameter count, latency, and resource use;
- implementation details required to reproduce the main claim.

Write "not reported" for absent information.

Then read qualitative and quantitative evidence. For each experiment, record:

```text
claim being tested -> comparison or intervention -> observation -> justified conclusion
```

Check whether:

- qualitative examples may be cherry-picked;
- quantitative metrics match the claimed capability;
- ablations isolate the proposed component;
- downstream gains establish usefulness rather than correlation;
- open-loop results are being presented as closed-loop ability;
- compute and data advantages make the comparison unequal.

Summarize conclusions rather than copying whole tables. Keep exact numbers when they determine the claim's magnitude or ranking.

Before completing this stage, revisit every Experiments-related item in the abstract verification ledger. Mark each as Confirmed, Refined, Unsupported, or Still unknown, and state the supporting or missing evidence. In Note mode, update those ledger entries together with the confirmed Experiments section.

## 6. Conclusion

Synthesize the completed reading into exactly three anchors:

### One-sentence memory point

State the task, distinctive mechanism, and demonstrated outcome in one sentence.

### What is genuinely new

Identify the smallest defensible difference from prior work. Do not list routine components, extra conditions, or scale increases unless they change the capability or problem formulation.

### Key assumptions and limitations

State the assumptions that must hold, the missing evidence, and the boundary beyond which the paper's conclusions do not follow.
