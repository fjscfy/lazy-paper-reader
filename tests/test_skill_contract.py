from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "lazy-paper-reader"


class LazyPaperReaderContractTests(unittest.TestCase):
    """Contract derived from observed baseline failures in real paper-reading sessions.

    Without this skill, summaries became overlong, accumulated too many headings,
    buried the paper's memory anchor, and sometimes mixed author claims with critique.
    """

    def read_required(self, relative_path: str) -> str:
        path = SKILL_ROOT / relative_path
        self.assertTrue(path.is_file(), f"missing required file: {path}")
        return path.read_text(encoding="utf-8")

    def test_required_skill_files_exist(self):
        for relative_path in (
            "SKILL.md",
            "agents/openai.yaml",
            "references/reading-workflow.md",
            "references/markdown-structure.md",
            "references/autonomous-driving-world-model.md",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((SKILL_ROOT / relative_path).is_file())

    def test_skill_metadata_and_reference_routing(self):
        text = self.read_required("SKILL.md")
        self.assertRegex(text, r"(?m)^name: lazy-paper-reader$")
        self.assertRegex(text, r"(?m)^description: Use when ")
        for reference in (
            "references/reading-workflow.md",
            "references/markdown-structure.md",
            "references/autonomous-driving-world-model.md",
        ):
            self.assertIn(reference, text)

    def test_skill_supports_all_source_modes_and_resume(self):
        text = self.read_required("SKILL.md").lower()
        for source_mode in (
            "local pdf",
            "paper url",
            "paper title",
            "existing markdown",
        ):
            self.assertIn(source_mode, text)
        self.assertIn("resume", text)
        self.assertIn("one markdown note", text)

    def test_workflow_is_interactive_and_write_gated(self):
        text = self.read_required("SKILL.md").lower()
        self.assertIn("explicit confirmation", text)
        self.assertIn("before writing", text)
        self.assertIn("pause", text)
        self.assertNotIn("read the entire paper before the first response", text)

    def test_reading_workflow_covers_required_stages(self):
        text = self.read_required("references/reading-workflow.md")
        for stage in (
            "Title Reading",
            "Abstract and Task Positioning",
            "Introduction",
            "Method",
            "Experiments",
            "Conclusion",
        ):
            self.assertIn(stage, text)
        self.assertIn("first sentence", text.lower())
        self.assertIn("skip related work", text.lower())
        self.assertIn("qualitative", text.lower())
        self.assertIn("quantitative", text.lower())

    def test_markdown_contract_contains_hybrid_structure_and_three_anchors(self):
        text = self.read_required("references/markdown-structure.md")
        self.assertIn("fixed top-level", text.lower())
        self.assertIn("original subsection", text.lower())
        for anchor in (
            "One-sentence memory point",
            "What is genuinely new",
            "Key assumptions and limitations",
        ):
            self.assertIn(anchor, text)
        for evidence_label in ("Paper statement", "Inference", "Critique"):
            self.assertIn(evidence_label, text)

    def test_autonomous_driving_profile_checks_decision_relevant_evidence(self):
        text = self.read_required(
            "references/autonomous-driving-world-model.md"
        ).lower()
        for concept in (
            "world representation",
            "action",
            "structured condition",
            "multiview",
            "closed-loop",
            "reward",
            "counterfactual",
            "uncertainty",
            "latency",
        ):
            self.assertIn(concept, text)

    def test_no_placeholders_or_hard_coded_personal_paths(self):
        files = list(SKILL_ROOT.rglob("*.md")) + list(SKILL_ROOT.rglob("*.yaml"))
        self.assertTrue(files, "skill files must exist before hygiene checks")
        forbidden = re.compile(r"\b(?:TODO|TBD)\b|/Users/[^/]+/")
        for path in files:
            with self.subTest(path=path):
                self.assertIsNone(
                    forbidden.search(path.read_text(encoding="utf-8")),
                    f"placeholder or personal path found in {path}",
                )

    def test_readme_is_english_first_and_uses_official_install_path(self):
        text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Interactive paper reading, not one-shot summarization", text)
        self.assertIn('$HOME/.agents/skills/lazy-paper-reader', text)
        self.assertNotIn('$CODEX_HOME/skills/lazy-paper-reader', text)
        chinese_heading = text.index("## 中文说明")
        self.assertGreater(chinese_heading, text.index("## License"))

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

    def test_title_is_literal_and_abstract_handles_task_positioning(self):
        skill = self.read_required("SKILL.md")
        workflow = self.read_required("references/reading-workflow.md")
        markdown = self.read_required("references/markdown-structure.md")
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

        for text in (skill, workflow, markdown, readme):
            self.assertIn("Title Reading", text)
            self.assertIn("Abstract and Task Positioning", text)
            self.assertLess(
                text.index("Title Reading"),
                text.index("Abstract and Task Positioning"),
            )

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

    def test_obsidian_math_formatting_contract(self):
        text = self.read_required("references/markdown-structure.md")
        for phrase in (
            "## Obsidian math formulas",
            'Inline math must use `$...$`',
            'Block math must use `$$...$$`',
            r'Do not use `\(...\)` or `\[...\]`',
            "`String.raw`",
            r"commands such as `\times`, `\theta`, and `\mid`",
            r"no `\(`, `\)`, `\[`, or `\]` delimiters remain",
            "every `$` and `$$` delimiter is paired",
            "Never report completion before this check passes",
        ):
            self.assertIn(phrase, text)

        self.assertIn(
            "$$\n"
            r"P(D_{1:N};Z_1)=\prod_{t=2}^{N}P_\theta(D_t\mid D_{<t},Z_1)."
            "\n$$",
            text,
        )


if __name__ == "__main__":
    unittest.main()
