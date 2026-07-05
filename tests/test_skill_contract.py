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
            "Title and Task Positioning",
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


if __name__ == "__main__":
    unittest.main()
