"""Static invariants for Prompt Optimizer content and reviewer fixtures."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "prompt-optimizer"


class ContentContractTest(unittest.TestCase):
    def test_registry_schema_and_unique_sources(self):
        registry = json.loads((SKILL / "references" / "source-registry.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["schema_version"], "1.0")
        self.assertFalse(registry["policy"]["automatic_updates"])
        sources = registry["sources"]
        ids = [source["id"] for source in sources]
        self.assertEqual(len(ids), len(set(ids)))
        required = {
            "id",
            "url",
            "source_type",
            "authority_tier",
            "license",
            "license_scope",
            "permitted_use",
            "cautions",
        }
        for source in sources:
            self.assertEqual(set(source), required)
            self.assertTrue(source["url"].startswith("https://"))
            self.assertIn(source["authority_tier"], {1, 2, 3, 4})

    def test_required_discovery_anchors_are_registered(self):
        registry = json.loads((SKILL / "references" / "source-registry.json").read_text(encoding="utf-8"))
        ids = {source["id"] for source in registry["sources"]}
        expected = {
            "openai-prompt-engineering",
            "anthropic-prompting-best-practices",
            "google-gemini-prompting-strategies",
            "github-awesome-copilot",
            "prompts-chat",
            "langgpt",
            "promptsource",
            "dair-prompt-engineering-guide",
        }
        self.assertTrue(expected.issubset(ids))

    def test_security_invariants_are_explicit(self):
        security = (SKILL / "references" / "external-content-security.md").read_text(encoding="utf-8").lower()
        for invariant in (
            "untrusted data",
            "never execute downloaded scripts",
            "injection detection is heuristic",
            "leaked system prompts",
            "license",
        ):
            self.assertIn(invariant, security)

    def test_acceptance_suite_covers_merged_modes_and_new_risks(self):
        text = (ROOT / "tests" / "acceptance-cases.md").read_text(encoding="utf-8")
        ids = set(re.findall(r"^\| ([A-Z]+\d+) \|", text, flags=re.MULTILINE))
        required = {
            "G1", "W1", "R1", "C1", "P1", "A1", "K1", "E1", "N1",
            "M1", "M2", "M3", "M4", "S1", "S2", "L1", "L2", "L3", "L4", "L5", "V1",
        }
        self.assertTrue(required.issubset(ids))

    def test_payload_contains_no_source_pdf_or_copied_prompt_dataset(self):
        forbidden_suffixes = {".pdf", ".csv"}
        files = [path for path in SKILL.rglob("*") if path.is_file()]
        self.assertFalse(any(path.suffix.lower() in forbidden_suffixes for path in files))
        self.assertFalse(any("prompt engineering research framework" in path.name.lower() for path in files))

    def test_payload_has_no_machine_specific_paths(self):
        for path in SKILL.rglob("*"):
            if path.is_file():
                text = path.read_text(encoding="utf-8", errors="ignore")
                self.assertNotIn("/Users/sabribenradhia", text, path)


if __name__ == "__main__":
    unittest.main()
