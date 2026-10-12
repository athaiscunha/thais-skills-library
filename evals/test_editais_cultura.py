import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "editais-cultura" / "scripts" / "validar_candidatura.py"
EXAMPLE = ROOT / "skills" / "editais-cultura" / "assets" / "candidatura-exemplo.json"


class CandidaturaTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory(prefix="editais-cultura-test-")
        self.addCleanup(self.temp_dir.cleanup)
        self.base = Path(self.temp_dir.name)
        self.data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        self.data["pendencias"] = []
        (self.base / "anexos").mkdir(exist_ok=True)
        # Somente fixture. O validador deve inspecionar metadados, nunca alegar validar PDF.
        (self.base / "anexos" / "portfolio.pdf").write_bytes(b"%PDF-1.7\nfixture para metadados\n")

    def run_case(self, expected_exit, expected_code=None, raw=None):
        path = self.base / "candidatura.json"
        path.write_text(raw if raw is not None else json.dumps(self.data, ensure_ascii=False), encoding="utf-8")
        files = [p for p in self.base.rglob("*") if p.is_file()]
        before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
        proc = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, check=False)
        self.assertEqual(proc.stderr, b"", proc.stderr.decode(errors="replace"))
        self.assertEqual(proc.returncode, expected_exit, proc.stdout.decode("utf-8"))
        result = json.loads(proc.stdout.decode("utf-8"))
        self.assertEqual(set(result), {"erros", "avisos", "verificacoes", "total"})
        after = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
        self.assertEqual(before, after, "Validação não pode alterar candidatura/anexos")
        if expected_code:
            self.assertIn(expected_code, [e["codigo"] for e in result["erros"]])
        return result

    def test_valid_multisource(self):
        result = self.run_case(0)
        self.assertEqual(result["total"]["orcamento"], "2250.00")
        self.assertEqual(result["total"]["elegivel_solicitacao"], "2000.00")
        self.assertEqual(result["total"]["por_categoria"]["materiais"], "500.00")
        self.assertEqual(result["total"]["por_fonte"]["recursos_proprios"], "250.00")

    def test_decimal_fraction_exact(self):
        self.data["orcamento"] = {
            "valor_solicitado": "0.3", "total_declarado": "0.3", "itens": [
                {"id": "F1", "descricao": "Fracionário", "quantidade": 3,
                 "valor_unitario": 0.1, "total_declarado": "0.30",
                 "categoria": "servicos", "fonte": "edital", "elegivel": True}]}
        result = self.run_case(0)
        self.assertEqual(result["total"]["orcamento"], "0.3")

    def test_duplicate_id(self):
        self.data["orcamento"]["itens"][1]["id"] = "I01"
        self.run_case(1, "ID_ITEM_DUPLICADO")

    def test_negative_and_nonfinite(self):
        for value in ("-1", "NaN", "Infinity", "-Infinity", True, "R$ 3,00"):
            with self.subTest(value=value):
                self.data["orcamento"]["itens"][0]["valor_unitario"] = value
                result = self.run_case(1, "NUMERO_INVALIDO")
                self.assertIsNone(result["total"]["orcamento"])

    def test_request_over_limit_and_mismatch(self):
        self.data["orcamento"]["valor_solicitado"] = "3000"
        result = self.run_case(1, "TETO_SOLICITACAO_EXCEDIDO")
        self.assertIn("SOLICITACAO_DIVERGENTE", [e["codigo"] for e in result["erros"]])

    def test_declared_item_and_total_mismatch(self):
        self.data["orcamento"]["itens"][0]["total_declarado"] = "1"
        self.data["orcamento"]["total_declarado"] = "1"
        result = self.run_case(1, "TOTAL_ITEM_DIVERGENTE")
        self.assertIn("TOTAL_ORCAMENTO_DIVERGENTE", [e["codigo"] for e in result["erros"]])

    def test_absolute_total_and_category_limits(self):
        self.data["regras"]["orcamento"]["teto_total"] = "2000"
        self.data["regras"]["orcamento"]["limites_categoria"]["materiais"] = "499.99"
        result = self.run_case(1, "TETO_TOTAL_EXCEDIDO")
        self.assertIn("TETO_CATEGORIA_EXCEDIDO", [e["codigo"] for e in result["erros"]])

    def test_eligibility_pending(self):
        self.data["orcamento"]["itens"][0]["elegivel"] = None
        result = self.run_case(1, "ELEGIBILIDADE_PENDENTE")
        self.assertIsNone(result["total"]["elegivel_solicitacao"])

    def test_ineligible_requested_item(self):
        self.data["orcamento"]["itens"][0]["elegivel"] = False
        self.run_case(1, "ITEM_INELEGIVEL_SOLICITADO")

    def test_disallowed_source_and_category(self):
        self.data["orcamento"]["itens"][0]["fonte"] = "outra"
        self.data["orcamento"]["itens"][0]["categoria"] = "outra"
        result = self.run_case(1, "VALOR_NAO_PERMITIDO")
        self.assertEqual(len([e for e in result["erros"] if e["codigo"] == "VALOR_NAO_PERMITIDO"]), 2)

    def test_missing_required_text_and_unicode_limit(self):
        self.data["campos"]["titulo"] = "  "
        self.run_case(1, "CAMPO_OBRIGATORIO")
        self.data["campos"]["titulo"] = "a\u0301😀"
        self.data["regras"]["campos"]["titulo"]["max_caracteres"] = 2
        result = self.run_case(1, "CAMPO_LONGO")
        count = [v for v in result["verificacoes"] if v["codigo"] == "CARACTERES_UNICODE" and v["caminho"] == "$.campos.titulo"]
        self.assertEqual(count[0]["quantidade"], 3)

    def test_missing_file_and_missing_required_attachment(self):
        self.data["anexos"][0]["caminho"] = "anexos/inexistente.pdf"
        self.run_case(1, "ANEXO_AUSENTE")
        self.data["anexos"] = []
        self.run_case(1, "ANEXO_OBRIGATORIO")

    def test_attachment_empty_large_extension_and_duplicate(self):
        file = self.base / "anexos" / "portfolio.pdf"
        file.write_bytes(b"")
        self.run_case(1, "ANEXO_VAZIO")
        file.write_bytes(b"12345")
        self.data["regras"]["anexos"][0]["max_bytes"] = 4
        self.run_case(1, "ANEXO_GRANDE")
        self.data["regras"]["anexos"][0]["max_bytes"] = 100
        self.data["regras"]["anexos"][0]["extensoes"] = [".jpg"]
        self.run_case(1, "EXTENSAO_NAO_PERMITIDA")
        self.data["regras"]["anexos"][0]["extensoes"] = [".pdf"]
        self.data["anexos"].append(copy.deepcopy(self.data["anexos"][0]))
        self.run_case(1, "ID_ANEXO_DUPLICADO")

    def test_disallowed_path(self):
        for value in ("../outside.pdf", "C:\\outside.pdf", "/tmp/outside.pdf", "C:relative.pdf", "\\rooted.pdf"):
            with self.subTest(path=value):
                self.data["anexos"][0]["caminho"] = value
                self.run_case(1, "CAMINHO_NAO_RELATIVO")

    def test_explicit_pending(self):
        self.data["pendencias"] = ["Falta comprovação territorial"]
        self.run_case(1, "PENDENCIA_EXPLICITA")

    def test_invalid_json_and_duplicate_key(self):
        for raw in ("{", '{"x": 1, "x": 2}', '{"x": NaN}', '{"x": Infinity}'):
            with self.subTest(raw=raw):
                self.run_case(2, "ENTRADA_INVALIDA", raw)

    def test_unknown_rule_and_invalid_type(self):
        self.data["regras"]["orcamento"]["tetoo_total"] = "1000"
        self.run_case(2, "ENTRADA_INVALIDA")
        del self.data["regras"]["orcamento"]["tetoo_total"]
        self.data["campos"]["titulo"] = 123
        self.run_case(2, "ENTRADA_INVALIDA")

    def test_invalid_rule_limits(self):
        self.data["regras"]["campos"]["titulo"]["min_caracteres"] = 1000
        self.run_case(2, "ENTRADA_INVALIDA")

    def test_schema_version_boolean_is_invalid(self):
        self.data["versao"] = True
        self.run_case(2, "ENTRADA_INVALIDA")


if __name__ == "__main__":
    unittest.main(verbosity=2)
