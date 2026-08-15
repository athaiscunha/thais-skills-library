#!/usr/bin/env python3
"""Run dependency-free structural checks for the personal Skill library."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
CASES_PATH = ROOT / "evals" / "cases.json"
RESOURCE_PATTERN = re.compile(r"`((?:references|scripts|assets)/[^`]+)`")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("frontmatter ausente ou mal delimitado")
    raw, body = text[4:].split("\n---\n", 1)
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"([a-z_]+):\s*(.+)", line)
        if not match:
            raise ValueError(f"linha de frontmatter não suportada: {line!r}")
        key, value = match.groups()
        values[key] = value.strip().strip('"')
    return values, body


def quoted_yaml_value(text: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}:\s*\"([^\"]*)\"\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def check_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_path = skill_dir / "SKILL.md"
    prefix = skill_dir.name

    if not skill_path.is_file():
        return [f"{prefix}: SKILL.md ausente"], warnings

    try:
        frontmatter, body = parse_frontmatter(skill_path)
    except ValueError as exc:
        return [f"{prefix}: {exc}"], warnings

    if set(frontmatter) != {"name", "description"}:
        errors.append(f"{prefix}: frontmatter deve conter somente name e description")
    if frontmatter.get("name") != prefix:
        errors.append(f"{prefix}: name não coincide com o nome da pasta")
    description = frontmatter.get("description", "")
    if "Use " not in description or "Não use " not in description:
        errors.append(f"{prefix}: description precisa declarar quando usar e quando não usar")
    if len(body.splitlines()) > 500:
        errors.append(f"{prefix}: corpo do SKILL.md excede 500 linhas")
    if (skill_dir / "README.md").exists():
        errors.append(f"{prefix}: README.md não deve ficar dentro da Skill")
    if not (skill_dir / "references" / "acceptance-tests.md").is_file():
        errors.append(f"{prefix}: references/acceptance-tests.md ausente")

    text_files = list(skill_dir.rglob("*.md")) + list(skill_dir.rglob("*.yaml"))
    combined = "\n".join(path.read_text(encoding="utf-8") for path in text_files)
    for relative in sorted(set(RESOURCE_PATTERN.findall(combined))):
        if not (skill_dir / relative).exists():
            errors.append(f"{prefix}: recurso referenciado não existe: {relative}")

    skill_text = skill_path.read_text(encoding="utf-8")
    references_dir = skill_dir / "references"
    if references_dir.is_dir():
        for reference in sorted(references_dir.glob("*.md")):
            relative = f"references/{reference.name}"
            if f"`{relative}`" not in skill_text:
                errors.append(f"{prefix}: {relative} não está roteado diretamente pelo SKILL.md")
            lines = reference.read_text(encoding="utf-8").splitlines()
            if len(lines) > 100 and "## Sumário" not in lines[:25]:
                warnings.append(f"{prefix}: {relative} tem mais de 100 linhas e não possui sumário inicial")

    agents_path = skill_dir / "agents" / "openai.yaml"
    if not agents_path.is_file():
        errors.append(f"{prefix}: agents/openai.yaml ausente")
    else:
        agents_text = agents_path.read_text(encoding="utf-8")
        prompt = quoted_yaml_value(agents_text, "default_prompt")
        short_description = quoted_yaml_value(agents_text, "short_description")
        if prompt is None or f"${prefix}" not in prompt:
            errors.append(f"{prefix}: default_prompt precisa mencionar ${prefix}")
        if short_description is None or not 25 <= len(short_description) <= 64:
            errors.append(f"{prefix}: short_description deve ter entre 25 e 64 caracteres")

    return errors, warnings


def check_cases(skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    if not CASES_PATH.is_file():
        return ["evals/cases.json ausente"]
    try:
        payload = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"evals/cases.json inválido: {exc}"]

    if not isinstance(payload, dict) or not isinstance(payload.get("cases"), list):
        return ["evals/cases.json deve conter um objeto com a lista cases"]

    required = {
        "id",
        "skill",
        "prompt",
        "preconditions",
        "expected",
        "reject_if",
        "requires_live_web",
    }
    ids: set[str] = set()
    coverage: Counter[str] = Counter()
    type_coverage: Counter[str] = Counter()
    for index, case in enumerate(payload["cases"], start=1):
        label = f"caso {index}"
        if not isinstance(case, dict):
            errors.append(f"{label}: deve ser um objeto")
            continue
        missing = required - set(case)
        if missing:
            errors.append(f"{label}: campos ausentes: {', '.join(sorted(missing))}")
            continue
        extra = set(case) - required
        if extra:
            errors.append(f"{label}: campos extras: {', '.join(sorted(extra))}")
        case_id = case["id"]
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{label}: id inválido")
        elif case_id in ids:
            errors.append(f"{label}: id duplicado: {case_id}")
        ids.add(case_id)
        skill = case["skill"]
        if skill not in skill_names:
            errors.append(f"{case_id}: Skill desconhecida: {skill}")
        else:
            coverage[skill] += 1
        if not isinstance(case["prompt"], str) or not case["prompt"].strip():
            errors.append(f"{case_id}: prompt vazio")
        for field in ("preconditions", "expected", "reject_if"):
            if not isinstance(case[field], list) or not case[field]:
                errors.append(f"{case_id}: {field} deve ser uma lista não vazia")
        if isinstance(case["expected"], list) and case["expected"]:
            match = re.match(
                r"^Tipo (activation|non_activation_or_failure|adversarial) —",
                str(case["expected"][0]),
            )
            if not match:
                errors.append(f"{case_id}: expected[0] não declara um tipo válido")
            else:
                type_coverage[match.group(1)] += 1
        if not isinstance(case["requires_live_web"], bool):
            errors.append(f"{case_id}: requires_live_web deve ser booleano")

    for skill in sorted(skill_names):
        if coverage[skill] != 3:
            errors.append(f"{skill}: cobertura deve ser exatamente 3 ({coverage[skill]}/3)")
    for case_type in ("activation", "non_activation_or_failure", "adversarial"):
        if type_coverage[case_type] != len(skill_names):
            errors.append(
                f"tipo {case_type}: cobertura deve ser {len(skill_names)} "
                f"({type_coverage[case_type]}/{len(skill_names)})"
            )
    return errors


def check_paid_asset_auditor() -> list[str]:
    script = SKILLS_ROOT / "csc-paid-media-copy" / "scripts" / "audit_assets.py"
    if not script.is_file():
        return ["csc-paid-media-copy: scripts/audit_assets.py ausente"]
    sample = (
        "campo\tlimite\ttexto\n"
        "Título\t10\tNo limite!\n"
        "Título\t5\tAcima do limite\n"
        "Descrição\t20\tTexto repetido\n"
        "Descrição\t20\t  texto   repetido  \n"
        "Título\t1\te\u0301\n"
    )
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".tsv") as handle:
        handle.write(sample)
        handle.flush()
        result = subprocess.run(
            [sys.executable, str(script), handle.name],
            capture_output=True,
            text=True,
            check=False,
        )
    expected_fragments = (
        "OK\tTítulo\t[10/10]",
        "ACIMA\tTítulo",
        "DUPLICADO linhas",
        "OK\tTítulo\t[1/1]",
    )
    if result.returncode != 1 or any(fragment not in result.stdout for fragment in expected_fragments):
        return ["csc-paid-media-copy: audit_assets.py falhou no autoteste"]
    return []


def main() -> int:
    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").is_file())
    skill_names = {path.name for path in skill_dirs}
    errors: list[str] = []
    warnings: list[str] = []
    for skill_dir in skill_dirs:
        skill_errors, skill_warnings = check_skill(skill_dir)
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)
    errors.extend(check_cases(skill_names))
    errors.extend(check_paid_asset_auditor())

    for warning in warnings:
        print(f"AVISO {warning}")
    for error in errors:
        print(f"ERRO {error}")
    if errors:
        print(f"FALHOU: {len(errors)} erro(s), {len(warnings)} aviso(s)")
        return 1
    print(f"OK: {len(skill_dirs)} Skills, {len(warnings)} aviso(s), nenhum erro")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
