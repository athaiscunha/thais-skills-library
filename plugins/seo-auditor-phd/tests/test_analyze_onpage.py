import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PLUGIN_ROOT / "skills" / "seo-auditor-phd" / "scripts" / "analyze_onpage.py"
FIXTURE_PATH = PLUGIN_ROOT / "tests" / "fixtures" / "example-lp.html"

SPEC = importlib.util.spec_from_file_location("analyze_onpage", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AnalyzeOnPageTests(unittest.TestCase):
    def test_html_fixture_measures_observed_signals(self):
        source = FIXTURE_PATH.read_text(encoding="utf-8")
        report = MODULE.build_report(
            FIXTURE_PATH,
            source,
            "curso de enfermagem",
            ["graduação em enfermagem", "faculdade de enfermagem"],
            "https://www.faculdadehorizonte.example/cursos/enfermagem",
        )

        self.assertEqual(report["measurement_scope"]["input_mode"], "html")
        self.assertEqual(
            report["document"]["title"],
            "Seu futuro começa aqui | Faculdade Horizonte",
        )
        self.assertFalse(report["document"]["has_viewport_meta"])
        self.assertEqual(
            report["document"]["canonical"],
            ["https://www.faculdadehorizonte.example/cursos/enfermagem"],
        )
        self.assertGreater(report["content"]["word_count"], 200)
        self.assertEqual(report["headings"]["counts_by_level"]["h1"], 1)
        self.assertEqual(len(report["headings"]["level_jumps"]), 1)

        primary = report["keywords"][0]
        self.assertEqual(primary["exact_occurrences_in_body"], 5)
        self.assertEqual(primary["zones"]["title"], 0)
        self.assertEqual(primary["zones"]["h1"], 0)
        self.assertEqual(primary["zones"]["first_paragraph"], 0)
        self.assertEqual(primary["zones"]["h2_h6"], 1)

        self.assertEqual(len(report["images"]["missing_alt_attribute"]), 1)
        self.assertEqual(len(report["links"]["generic_anchors"]), 1)
        self.assertEqual(report["structured_data"]["jsonld_document_count"], 0)
        flag_areas = [item["area"] for item in report["mechanical_review_flags"]]
        self.assertIn("mobile", flag_areas)
        self.assertIn("introdução", flag_areas)
        self.assertIn(
            "search volume and keyword difficulty",
            report["measurement_scope"]["not_measured"],
        )

    def test_markdown_parser_keeps_headings_links_and_images(self):
        sample = """# Guia de bolsas\n\nVeja o [edital de bolsas](/edital).\n\n![Estudante no laboratório](lab.jpg)\n"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.md"
            path.write_text(sample, encoding="utf-8")
            report = MODULE.build_report(path, sample, "bolsas", [], "https://example.com/bolsas")

        self.assertEqual(report["measurement_scope"]["input_mode"], "markdown_or_text")
        self.assertEqual(report["headings"]["counts_by_level"]["h1"], 1)
        self.assertEqual(report["links"]["counts_by_kind"]["internal"], 1)
        self.assertEqual(report["images"]["items"][0]["alt"], "Estudante no laboratório")

    def test_markdown_render_states_limits(self):
        source = FIXTURE_PATH.read_text(encoding="utf-8")
        report = MODULE.build_report(FIXTURE_PATH, source, "curso de enfermagem", [], None)
        rendered = MODULE.render_markdown(report)
        self.assertIn("não avaliam intenção, ranking, volume", rendered)
        self.assertIn("Faixa inicial", rendered)


if __name__ == "__main__":
    unittest.main()
