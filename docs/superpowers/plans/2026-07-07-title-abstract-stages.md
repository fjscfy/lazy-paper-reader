# Separate Title and Abstract Stages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make title reading literal and move task positioning into a new, fully explained abstract stage.

**Architecture:** Expand the existing five-stage workflow to six stages without changing the confirmation or note-writing mechanism. Update the core skill order, detailed workflow, Markdown contract, README summary, and contract tests as one coherent behavior change.

**Tech Stack:** Markdown skill instructions, Python `unittest`, Git

## Global Constraints

- Title Reading uses only words present in the title and does not consult the abstract or introduction.
- Abstract and Task Positioning reconstructs the task, gap, high-level method, reported result, and claimed contribution.
- The abstract stage ends with a Method/Experiments verification ledger and marks unreported information.
- Title and abstract are separate confirmation, note-writing, and Q&A boundaries.
- Preserve source handling, confirmation-before-write, curated Q&A, method and experiment analysis, conclusion anchors, and the autonomous-driving profile.
- Synchronize the installed skill and push GitHub `main` after validation.

---

### Task 1: Add failing six-stage workflow contracts

**Files:**
- Modify: `tests/test_skill_contract.py`

**Interfaces:**
- Consumes: `read_required()` and `REPO_ROOT`
- Produces: contract coverage for stage order, literal title reading, abstract reconstruction, and public README structure

- [ ] **Step 1: Update the existing workflow-stage expectation**

In `test_reading_workflow_covers_required_stages`, replace `Title and Task Positioning` with `Title Reading`, add `Abstract and Task Positioning` immediately after it, and retain the remaining four stages.

- [ ] **Step 2: Add a focused behavior test**

Add this method to `LazyPaperReaderContractTests`:

```python
def test_title_is_literal_and_abstract_handles_task_positioning(self):
    skill = self.read_required("SKILL.md")
    workflow = self.read_required("references/reading-workflow.md")
    markdown = self.read_required("references/markdown-structure.md")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    for text in (skill, workflow, markdown, readme):
        self.assertLess(text.index("Title Reading"), text.index("Abstract and Task Positioning"))

    title_block = workflow.split("## 1. Title Reading", 1)[1].split(
        "## 2. Abstract and Task Positioning", 1
    )[0].lower()
    abstract_block = workflow.split(
        "## 2. Abstract and Task Positioning", 1
    )[1].split("## 3. Introduction", 1)[0].lower()

    self.assertIn("directly supported", title_block)
    self.assertIn("do not use the abstract or introduction", title_block)
    self.assertIn("verification ledger", abstract_block)
    self.assertIn("method", abstract_block)
    self.assertIn("experiments", abstract_block)
    self.assertIn("not report", abstract_block)
```

- [ ] **Step 3: Run the focused tests and verify RED**

Run:

```bash
python3 -m unittest \
  tests.test_skill_contract.LazyPaperReaderContractTests.test_reading_workflow_covers_required_stages \
  tests.test_skill_contract.LazyPaperReaderContractTests.test_title_is_literal_and_abstract_handles_task_positioning \
  -v
```

Expected: FAIL because the current workflow combines title and task positioning and the new abstract stage is absent.

### Task 2: Implement the six-stage reading and note workflow

**Files:**
- Modify: `skills/lazy-paper-reader/SKILL.md`
- Modify: `skills/lazy-paper-reader/references/reading-workflow.md`
- Modify: `skills/lazy-paper-reader/references/markdown-structure.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: the existing stage loop, Q&A curation, and incremental Markdown contract
- Produces: `Title Reading -> Abstract and Task Positioning -> Introduction -> Method -> Experiments -> Conclusion`

- [ ] **Step 1: Change the core stage order**

In `SKILL.md`, replace the order sentence with:

```markdown
Use this order: title reading, abstract and task positioning, introduction, method, experiments, conclusion.
```

- [ ] **Step 2: Replace the combined workflow stage**

In `references/reading-workflow.md`, replace `## 1. Title and Task Positioning` with two sections.

The title section must state that it explains only information directly supported by the title, may identify explicitly named research objects, tasks, method families, representations, system roles, emphasized characteristics, and ambiguous paper-specific terms, and must not use the abstract or introduction to infer inputs, outputs, motivation, architecture, novelty, or results.

The abstract section must reconstruct the task and setting, stated importance, existing limitation, high-level idea, reported inputs and outputs, main result or capability claim, and claimed contribution. It must end with a verification ledger containing claims to verify in Method, claims to verify in Experiments, and information the abstract does not report. Renumber Introduction through Conclusion as stages 3 through 6.

- [ ] **Step 3: Split the Markdown top-level headings**

In the default structure of `references/markdown-structure.md`, replace:

```markdown
# Title and Task Positioning
```

with:

```markdown
# Title Reading

# Abstract and Task Positioning
## Claims to Verify in Method
## Claims to Verify in Experiments
## Not Reported in the Abstract
```

Add a writing rule that title content must not be retrospectively enriched from later sections. Add a resume rule that an existing combined section is split only when revisited and without discarding user wording.

- [ ] **Step 4: Update the README workflow**

Replace the current first workflow item with two items:

```markdown
1. Literal title reading
2. Abstract and task positioning
```

Renumber Introduction through Conclusion to items 3 through 6. In the Chinese summary, replace the five-stage sequence with `标题字面阅读 → 摘要与任务定位 → 引言 → 方法 → 实验 → 结论`.

- [ ] **Step 5: Run focused and full tests**

Run:

```bash
python3 -m unittest \
  tests.test_skill_contract.LazyPaperReaderContractTests.test_reading_workflow_covers_required_stages \
  tests.test_skill_contract.LazyPaperReaderContractTests.test_title_is_literal_and_abstract_handles_task_positioning \
  -v
python3 -m unittest discover -s tests -v
```

Expected: both focused tests pass and the full suite reports 11 passing tests.

- [ ] **Step 6: Validate and commit**

Run:

```bash
PYTHONPATH=/tmp/lazy-paper-reader-validator-deps python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/lazy-paper-reader
git diff --check
git add README.md skills/lazy-paper-reader tests/test_skill_contract.py
git commit -m "feat: add a dedicated abstract reading stage"
```

Expected: the validator prints `Skill is valid!`, diff check exits 0, and the commit succeeds.

### Task 3: Synchronize installation and GitHub

**Files:**
- Update installed copy: `$HOME/.codex/skills/lazy-paper-reader`

**Interfaces:**
- Consumes: the committed repository skill
- Produces: an identical valid local installation and public GitHub `main`

- [ ] **Step 1: Synchronize and validate the installed copy**

Run:

```bash
rsync -a --delete skills/lazy-paper-reader/ "$HOME/.codex/skills/lazy-paper-reader/"
diff -qr skills/lazy-paper-reader "$HOME/.codex/skills/lazy-paper-reader"
PYTHONPATH=/tmp/lazy-paper-reader-validator-deps python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "$HOME/.codex/skills/lazy-paper-reader"
```

Expected: `diff` prints nothing and the validator prints `Skill is valid!`.

- [ ] **Step 2: Push and verify**

Run:

```bash
git push origin main
test "$(git rev-parse HEAD)" = "$(git ls-remote origin refs/heads/main | cut -f1)"
test -z "$(git status --porcelain)"
```

Expected: GitHub `main` matches local `HEAD` and the worktree is clean.
