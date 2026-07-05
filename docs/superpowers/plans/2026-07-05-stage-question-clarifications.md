# Stage Question Clarifications Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an optional, curated Questions and Clarifications subsection to every confirmed paper-reading stage.

**Architecture:** Extend the existing stage loop rather than adding a separate note pipeline. The workflow collects candidate questions during conversation, and the Markdown contract writes only high-value questions with distilled confirmed answers when the stage itself is confirmed.

**Tech Stack:** Markdown skill instructions, Python `unittest`, Git

## Global Constraints

- Preserve the reader's original question wording except for minimal cleanup needed outside the chat.
- Store only questions that materially affect understanding; never log the full conversation.
- Write the Q&A subsection only after explicit stage confirmation.
- Keep answers concise, self-contained, and aligned with the confirmed stage summary.
- Update stale Q&A whenever later discussion changes the corresponding interpretation.
- Do not change the five reading stages, conclusion anchors, source handling, or autonomous-driving profile.

---

### Task 1: Add a failing contract for curated stage questions

**Files:**
- Modify: `tests/test_skill_contract.py`

**Interfaces:**
- Consumes: `SKILL_ROOT`, `read_required()`, and the existing `unittest` suite
- Produces: `test_stage_questions_are_curated_and_confirmation_gated`

- [ ] **Step 1: Add the contract test**

Add this method to `LazyPaperReaderContractTests`:

```python
def test_stage_questions_are_curated_and_confirmation_gated(self):
    skill = self.read_required("SKILL.md").lower()
    workflow = self.read_required("references/reading-workflow.md").lower()
    markdown = self.read_required("references/markdown-structure.md").lower()

    self.assertIn("questions and clarifications", markdown)
    self.assertIn("original wording", markdown)
    self.assertIn("confirmed answer", markdown)
    self.assertIn("omit", markdown)
    self.assertIn("candidate clarification", workflow)
    self.assertIn("navigation", workflow)
    self.assertIn("explicit confirmation", skill)
    self.assertIn("selected questions", skill)
    self.assertIn("not a transcript", markdown)
```

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```bash
python3 -m unittest tests.test_skill_contract.LazyPaperReaderContractTests.test_stage_questions_are_curated_and_confirmation_gated -v
```

Expected: FAIL because the current Markdown contract has no Questions and Clarifications subsection.

### Task 2: Implement question curation and confirmed note writing

**Files:**
- Modify: `skills/lazy-paper-reader/SKILL.md`
- Modify: `skills/lazy-paper-reader/references/reading-workflow.md`
- Modify: `skills/lazy-paper-reader/references/markdown-structure.md`

**Interfaces:**
- Consumes: the existing stage loop and confirmation-before-write contract
- Produces: candidate-question curation during conversation and an optional per-stage Q&A subsection at write time

- [ ] **Step 1: Extend the core stage loop**

In `SKILL.md`, replace the current six-step stage loop with:

```markdown
1. Read only the source material needed for that stage.
2. Explain it conversationally, using the paper's logic rather than line-by-line translation.
3. Pause for questions and correction. Retain only questions that materially change or sharpen the reader's understanding as candidate clarifications.
4. Obtain explicit confirmation before writing that stage to the Markdown note.
5. Append or revise only the confirmed section. At its end, write the selected questions with the reader's original wording and concise, confirmed answers; omit the subsection when no question qualifies.
6. Preserve unrelated note content.
7. Move to the next stage only after the write is complete.
```

Add this common mistake:

```markdown
- Logging every exchange as Q&A instead of curating questions that preserve a useful conceptual distinction.
```

- [ ] **Step 2: Add candidate-question selection to the reading workflow**

After the opening paragraph of `references/reading-workflow.md`, add a `Curate stage questions` section that requires the assistant to:

```markdown
## Curate stage questions

While discussing a stage, retain a question as a candidate clarification only when it exposes a mistaken assumption, separates easily confused concepts, clarifies the method or evidence path, changes the interpretation of a claim, or captures a reusable insight.

Do not retain navigation requests, formatting preferences, conversational housekeeping, or repeated questions that add no new distinction. Merge overlapping candidates while preserving the clearest original wording from the reader.

At explicit confirmation, pass the selected candidates to the Markdown note contract together with the confirmed stage summary. If later discussion changes an answer, revise both the summary and the clarification.
```

- [ ] **Step 3: Extend the Markdown note contract**

After the default-structure code block in `references/markdown-structure.md`, add:

````markdown
Each top-level stage may end with this optional subsection:

```markdown
## Questions and Clarifications

- **Question:** <the reader's original question>
  **Answer:** <the concise, confirmed answer>
```

Translate the subsection title and labels into the user's language. Omit it when no question materially affected understanding.
````

Add these writing rules:

```markdown
- Preserve the reader's original wording for selected questions, allowing only minimal cleanup needed to understand the question outside the chat.
- Distill the final confirmed answer; this subsection is not a transcript of the conversation.
- Merge overlapping questions and exclude navigation, formatting, and housekeeping exchanges.
- If later discussion changes an answer, update the stage summary and its clarification together.
```

In the incremental write contract, add selection and Q&A writing after the confirmed section is identified, while retaining the rule that no unconfirmed content is written.

- [ ] **Step 4: Run focused and full tests**

Run:

```bash
python3 -m unittest tests.test_skill_contract.LazyPaperReaderContractTests.test_stage_questions_are_curated_and_confirmation_gated -v
python3 -m unittest discover -s tests -v
```

Expected: the focused test passes and the full suite reports 10 passing tests.

- [ ] **Step 5: Run official validation and commit**

Run:

```bash
PYTHONPATH=/tmp/lazy-paper-reader-validator-deps python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/lazy-paper-reader
git diff --check
git add skills/lazy-paper-reader tests/test_skill_contract.py
git commit -m "feat: preserve key reader questions by stage"
```

Expected: validator prints `Skill is valid!`, diff check exits 0, and the commit succeeds.

### Task 3: Publish and refresh the installed skill

**Files:**
- Update installed copy: `$HOME/.codex/skills/lazy-paper-reader`

**Interfaces:**
- Consumes: the committed repository skill directory
- Produces: matching local installation and public `main` branch

- [ ] **Step 1: Synchronize the installed skill**

Run:

```bash
rsync -a --delete skills/lazy-paper-reader/ "$HOME/.codex/skills/lazy-paper-reader/"
diff -qr skills/lazy-paper-reader "$HOME/.codex/skills/lazy-paper-reader"
```

Expected: `diff` prints nothing and exits 0.

- [ ] **Step 2: Validate the installed copy**

Run:

```bash
PYTHONPATH=/tmp/lazy-paper-reader-validator-deps python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "$HOME/.codex/skills/lazy-paper-reader"
```

Expected: `Skill is valid!`.

- [ ] **Step 3: Push and verify remote state**

Run:

```bash
git push origin main
test "$(git rev-parse HEAD)" = "$(git ls-remote origin refs/heads/main | cut -f1)"
test -z "$(git status --porcelain)"
```

Expected: the local and remote commits match and the worktree is clean.
