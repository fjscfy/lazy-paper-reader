# README Discoverability Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Present the repository in English by default, retain a concise Chinese section, document the official Agent Skills installation location, and improve GitHub-native discovery metadata.

**Architecture:** Keep the skill implementation unchanged. Add a README contract test, rewrite only the root `README.md`, then update repository metadata through GitHub CLI and verify local and remote state.

**Tech Stack:** Markdown, Python `unittest`, GitHub CLI, Git

## Global Constraints

- English is the primary README language; `中文说明` is the final substantive section.
- The documented user-level install target is `$HOME/.agents/skills/lazy-paper-reader`.
- Do not change skill behavior, source layout, releases, social preview, or external listings.
- Repository metadata must match the approved description and eight approved topics exactly.

---

### Task 1: English-first README contract and content

**Files:**
- Modify: `tests/test_skill_contract.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: the existing repository layout under `skills/lazy-paper-reader`
- Produces: an English-first README with an official user-level installation command and a final Chinese section

- [ ] **Step 1: Add a failing README contract test**

Add this method to `LazyPaperReaderContractTests`:

```python
def test_readme_is_english_first_and_uses_official_install_path(self):
    text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    self.assertIn("Interactive paper reading, not one-shot summarization", text)
    self.assertIn('$HOME/.agents/skills/lazy-paper-reader', text)
    self.assertNotIn('$CODEX_HOME/skills/lazy-paper-reader', text)
    chinese_heading = text.index("## 中文说明")
    self.assertGreater(chinese_heading, text.index("## License"))
```

- [ ] **Step 2: Run the new test and verify RED**

Run:

```bash
python3 -m unittest tests.test_skill_contract.LazyPaperReaderContractTests.test_readme_is_english_first_and_uses_official_install_path -v
```

Expected: FAIL because the current README lacks the English value proposition and official installation path.

- [ ] **Step 3: Rewrite the README**

Replace `README.md` with sections in this order:

```markdown
# lazy-paper-reader

Interactive paper reading, not one-shot summarization.

`lazy-paper-reader` is a Codex Agent Skill that helps you reconstruct a paper's argument and evidence stage by stage. It explains one section at a time, resolves questions in conversation, and updates a single Markdown note only after you confirm the interpretation.

## Why use it?

- Reads in stages instead of overwhelming you with a full-paper summary.
- Connects each method design to its motivation and author justification.
- Separates paper statements, reasonable inference, and critique.
- Treats experiments as evidence: what each result supports and what it does not.
- Resumes from an existing Markdown note without overwriting your wording.
- Adds a dedicated review profile for autonomous-driving world models.

## Reading workflow

1. Title and task positioning
2. Introduction and its argument chain
3. Method, motivation, data flow, and distinctive design choices
4. Experimental setup, qualitative evidence, and quantitative evidence
5. Conclusion with three retrieval anchors:
   - One-sentence memory point
   - What is genuinely new
   - Key assumptions and limitations

Related Work is skipped on the first pass and revisited only when a novelty claim needs verification.

## Supported inputs

- A local PDF
- An official paper URL
- A paper title to resolve to a primary source
- An existing Markdown note to resume

## Install

Codex discovers user-level Agent Skills from `$HOME/.agents/skills`.

```bash
git clone https://github.com/fjscfy/lazy-paper-reader.git
mkdir -p "$HOME/.agents/skills"
cp -R lazy-paper-reader/skills/lazy-paper-reader "$HOME/.agents/skills/lazy-paper-reader"
```

Codex detects skill changes automatically. If the skill does not appear, restart Codex.

Invoke it explicitly:

```text
Use $lazy-paper-reader to guide me through this paper stage by stage and maintain one Markdown note.
```

Codex may also invoke it implicitly when your request matches the skill description.

## Repository structure

```text
skills/lazy-paper-reader/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── reading-workflow.md
    ├── markdown-structure.md
    └── autonomous-driving-world-model.md
```

## License

[MIT](LICENSE)

## 中文说明

`lazy-paper-reader` 是一个交互式 Codex 论文阅读 Skill。它不会一次性生成整篇摘要，而是按“标题与任务定位 → 引言 → 方法 → 实验 → 结论”逐阶段讲解；只有在你确认当前理解后，才会更新同一份 Markdown 笔记。

它支持本地 PDF、论文链接、论文标题和已有笔记，并为自动驾驶 World Model 论文提供额外的分析视角。用户级安装目录为 `$HOME/.agents/skills/lazy-paper-reader`。
```

- [ ] **Step 4: Run the README test and full contract suite**

Run:

```bash
python3 -m unittest tests.test_skill_contract.LazyPaperReaderContractTests.test_readme_is_english_first_and_uses_official_install_path -v
python3 -m unittest discover -s tests -v
```

Expected: the focused test passes and the full suite reports 9 passing tests.

- [ ] **Step 5: Commit the README change**

```bash
git add README.md tests/test_skill_contract.py
git commit -m "docs: make README English-first"
```

### Task 2: GitHub description, topics, and publication verification

**Files:**
- No repository files modified

**Interfaces:**
- Consumes: authenticated GitHub CLI access to `fjscfy/lazy-paper-reader`
- Produces: approved public repository description and topic metadata

- [ ] **Step 1: Update repository metadata**

Run:

```bash
gh repo edit fjscfy/lazy-paper-reader \
  --description "An interactive Codex skill for reading research papers stage by stage and maintaining evidence-aware Markdown notes." \
  --add-topic codex \
  --add-topic agent-skills \
  --add-topic research-papers \
  --add-topic paper-reading \
  --add-topic academic-research \
  --add-topic markdown \
  --add-topic computer-vision \
  --add-topic world-model
```

Expected: exit code 0.

- [ ] **Step 2: Run final local validation**

Run:

```bash
python3 -m unittest discover -s tests -v
PYTHONPATH=/tmp/lazy-paper-reader-validator-deps python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" skills/lazy-paper-reader
git diff --check
```

Expected: 9 tests pass, the validator prints `Skill is valid!`, and `git diff --check` exits 0.

- [ ] **Step 3: Push and verify remote state**

Run:

```bash
git push origin main
gh repo view fjscfy/lazy-paper-reader --json description,repositoryTopics,url,visibility
test "$(git rev-parse HEAD)" = "$(git ls-remote origin refs/heads/main | cut -f1)"
test -z "$(git status --porcelain)"
```

Expected: the API output contains the approved description and eight topics, local and remote commits match, and the worktree is clean.
