# Conversational Uncertainty Check Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a two-question uncertainty check to the conversation immediately before each stage confirmation.

**Architecture:** Insert the check into the existing stage loop between question discussion and explicit confirmation. Keep detailed prompt wording and persistence boundaries in the reading workflow, while leaving the Markdown contract unchanged.

**Tech Stack:** Markdown skill instructions, Python `unittest`, Git

## Global Constraints

- The check proactively answers exactly two prompts: least-certain judgment and likely blind spot.
- Run it after stage discussion stabilizes and before requesting explicit confirmation.
- Keep it conversational only; do not write it to Markdown or candidate Q&A tracking by default.
- Avoid generic cautions; if no material issue exists, state that briefly and explain why.
- If the check changes the interpretation, revise the stage and run the check again before confirmation.
- Preserve all six reading stages, note structure, Obsidian formula rules, and domain profiles.

---

### Task 1: Add a failing conversational-check contract

**Files:**
- Modify: `tests/test_skill_contract.py`

**Interfaces:**
- Consumes: `read_required()`
- Produces: `test_uncertainty_check_is_conversational_and_precedes_confirmation`

- [ ] **Step 1: Add the test**

Add this method to `LazyPaperReaderContractTests`:

```python
def test_uncertainty_check_is_conversational_and_precedes_confirmation(self):
    skill = self.read_required("SKILL.md").lower()
    workflow = self.read_required("references/reading-workflow.md").lower()
    markdown = self.read_required("references/markdown-structure.md").lower()

    stage_loop = skill.split("for every stage:", 1)[1].split(
        "never read and summarize", 1
    )[0]
    self.assertIn("uncertainty check", stage_loop)
    self.assertLess(
        stage_loop.index("uncertainty check"),
        stage_loop.index("explicit confirmation"),
    )

    for phrase in (
        "least certain judgment",
        "most likely overlooking",
        "conversation only",
        "do not write it to the markdown note",
        "do not add it to candidate clarification tracking",
        "run the two-item check again",
    ):
        self.assertIn(phrase, workflow)

    self.assertNotIn("uncertainty check", markdown)
```

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```bash
python3 -m unittest tests.test_skill_contract.LazyPaperReaderContractTests.test_uncertainty_check_is_conversational_and_precedes_confirmation -v
```

Expected: FAIL because the stage loop and workflow do not contain the uncertainty check.

### Task 2: Implement the conversational check

**Files:**
- Modify: `skills/lazy-paper-reader/SKILL.md`
- Modify: `skills/lazy-paper-reader/references/reading-workflow.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: the current per-stage explanation, Q&A, and confirmation loop
- Produces: a repeatable two-item epistemic pause before confirmation

- [ ] **Step 1: Insert the check into the core stage loop**

In `SKILL.md`, replace the current steps 4 through 7 with:

```markdown
4. Run the two-item conversational uncertainty check defined in `references/reading-workflow.md`. If it changes the interpretation, continue discussion, revise the stage understanding, and run the check again.
5. Obtain explicit confirmation before writing that stage to the Markdown note.
6. Append or revise only the confirmed section. At its end, write the selected questions with the reader's original wording and concise, confirmed answers; omit the subsection when no question qualifies.
7. Preserve unrelated note content.
8. Move to the next stage only after the write is complete.
```

- [ ] **Step 2: Add the detailed workflow rule**

In `references/reading-workflow.md`, add this section after `Curate stage questions`:

```markdown
## Run a conversational uncertainty check

After the stage explanation and question discussion have stabilized, but before requesting explicit confirmation, proactively answer exactly two prompts in the user's language:

1. **Least certain judgment:** What judgment am I least certain about right now? Does the uncertainty come from information the paper does not state, insufficient evidence, or a relevant section that has not been read yet?
2. **Possible blind spot:** What are we most likely overlooking or taking for granted right now? Are there unchecked assumptions, alternative explanations, counterexamples, or evaluation dimensions?

Keep the answers concrete and tied to the current paper stage. Do not invent generic cautions merely to fill the structure. If no material issue is found, state that briefly and explain why the available evidence is sufficient at this stage.

This check is conversation only by default. Do not write it to the Markdown note, do not treat it as a reader question, and do not add it to candidate clarification tracking unless the user explicitly asks to preserve that specific content.

If the check triggers further discussion or changes the interpretation, revise the stage understanding and run the two-item check again before requesting confirmation.
```

- [ ] **Step 3: Add one README feature bullet**

Under `Why use it?`, add:

```markdown
- Surfaces the least-certain judgment and likely blind spot before each stage is confirmed.
```

- [ ] **Step 4: Run focused and full tests**

Run:

```bash
python3 -m unittest tests.test_skill_contract.LazyPaperReaderContractTests.test_uncertainty_check_is_conversational_and_precedes_confirmation -v
python3 -m unittest discover -s tests -v
```

Expected: the focused test passes and the full suite reports 13 passing tests.

- [ ] **Step 5: Validate and commit**

Run:

```bash
PYTHONPATH=/tmp/lazy-paper-reader-validator-deps python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/lazy-paper-reader
git diff --check
git add README.md skills/lazy-paper-reader tests/test_skill_contract.py
git commit -m "feat: add conversational uncertainty checks"
```

Expected: the validator prints `Skill is valid!`, diff check exits 0, and the commit succeeds.

### Task 3: Synchronize installation and GitHub

**Files:**
- Update installed copy: `$HOME/.codex/skills/lazy-paper-reader`

**Interfaces:**
- Consumes: the committed repository skill
- Produces: a matching installed skill and public GitHub `main`

- [ ] **Step 1: Synchronize and validate the installed copy**

Run:

```bash
rsync -a --delete skills/lazy-paper-reader/ "$HOME/.codex/skills/lazy-paper-reader/"
diff -qr skills/lazy-paper-reader "$HOME/.codex/skills/lazy-paper-reader"
PYTHONPATH=/tmp/lazy-paper-reader-validator-deps python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "$HOME/.codex/skills/lazy-paper-reader"
```

Expected: `diff` prints nothing and validation succeeds.

- [ ] **Step 2: Push and verify**

Run:

```bash
git push origin main
test "$(git rev-parse HEAD)" = "$(git ls-remote origin refs/heads/main | cut -f1)"
test -z "$(git status --porcelain)"
```

Expected: GitHub `main` matches local `HEAD` and the worktree is clean.
