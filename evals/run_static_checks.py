#!/usr/bin/env python3
"""Run dependency-free structural checks for the personal Skill library."""

from __future__ import annotations

import json
import hashlib
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
CASES_PATH = ROOT / "evals" / "cases.json"
PLUGINS_ROOT = ROOT / "plugins"
MARKETPLACE_PATH = ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN_ROOT = ROOT / "plugins" / "thais-skills-library"
SEO_PLUGIN_ROOT = ROOT / "plugins" / "seo-auditor-phd"
RESOURCE_PATTERN = re.compile(r"`((?:references|scripts|assets)/[^`]+)`")
PLUGIN_NAME_PATTERN = re.compile(r"[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*")
SEMVER_PATTERN = re.compile(
    r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"
)


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


def check_marketplace_plugins() -> tuple[list[str], int]:
    """Validate every marketplace entry and detect orphan plugin packages."""
    errors: list[str] = []
    try:
        marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"marketplace: arquivo inválido: {exc}"], 0

    if marketplace.get("name") != "thais-skills":
        errors.append("marketplace: name deve ser thais-skills")
    display_name = marketplace.get("interface", {}).get("displayName")
    if not isinstance(display_name, str) or not display_name.strip():
        errors.append("marketplace: interface.displayName ausente")
    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not entries:
        return errors + ["marketplace: plugins deve ser uma lista não vazia"], 0

    marketplace_names: list[str] = []
    for index, entry in enumerate(entries, start=1):
        label = f"marketplace: entrada {index}"
        if not isinstance(entry, dict):
            errors.append(f"{label} deve ser um objeto")
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not PLUGIN_NAME_PATTERN.fullmatch(name):
            errors.append(f"{label} possui name inválido")
            continue
        marketplace_names.append(name)
        source = entry.get("source")
        expected_path = f"./plugins/{name}"
        if not isinstance(source, dict) or source.get("source") != "local":
            errors.append(f"{name}: marketplace deve usar source local")
        elif source.get("path") != expected_path:
            errors.append(f"{name}: marketplace deve apontar para {expected_path}")
        policy = entry.get("policy")
        if not isinstance(policy, dict):
            errors.append(f"{name}: policy ausente no marketplace")
        else:
            if policy.get("installation") not in {
                "NOT_AVAILABLE",
                "AVAILABLE",
                "INSTALLED_BY_DEFAULT",
            }:
                errors.append(f"{name}: policy.installation inválida")
            if policy.get("authentication") not in {"ON_INSTALL", "ON_USE"}:
                errors.append(f"{name}: policy.authentication inválida")
        if not isinstance(entry.get("category"), str) or not entry["category"].strip():
            errors.append(f"{name}: category ausente no marketplace")

        plugin_root = PLUGINS_ROOT / name
        manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{name}: manifesto inválido: {exc}")
            continue
        if manifest.get("name") != name:
            errors.append(f"{name}: name do manifesto não coincide com a pasta")
        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER_PATTERN.fullmatch(version):
            errors.append(f"{name}: version não segue SemVer")
        description = manifest.get("description")
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{name}: description ausente no manifesto")
        skills_path = manifest.get("skills")
        if skills_path is not None:
            if skills_path != "./skills/":
                errors.append(f"{name}: skills deve usar o caminho ./skills/")
            else:
                bundled_skills = plugin_root / "skills"
                skill_dirs = sorted(
                    path for path in bundled_skills.iterdir()
                    if path.is_dir() and (path / "SKILL.md").is_file()
                ) if bundled_skills.is_dir() else []
                if not skill_dirs:
                    errors.append(f"{name}: manifesto declara Skills, mas nenhuma foi encontrada")
                for skill_dir in skill_dirs:
                    try:
                        frontmatter, _ = parse_frontmatter(skill_dir / "SKILL.md")
                    except ValueError as exc:
                        errors.append(f"{name}/{skill_dir.name}: {exc}")
                    else:
                        if frontmatter.get("name") != skill_dir.name:
                            errors.append(
                                f"{name}/{skill_dir.name}: name da Skill não coincide com a pasta"
                            )
                    agents_path = skill_dir / "agents" / "openai.yaml"
                    if agents_path.is_file():
                        agents_text = agents_path.read_text(encoding="utf-8")
                        prompt = quoted_yaml_value(agents_text, "default_prompt")
                        if prompt is None or not prompt.strip():
                            errors.append(
                                f"{name}/{skill_dir.name}: default_prompt precisa ser preenchido"
                            )
                        elif f"${skill_dir.name}" in prompt or f"@{skill_dir.name}" in prompt:
                            errors.append(
                                f"{name}/{skill_dir.name}: default_prompt deve ser neutro, "
                                "sem sintaxe de invocação"
                            )

    duplicates = sorted(
        name for name, count in Counter(marketplace_names).items() if count > 1
    )
    if duplicates:
        errors.append(f"marketplace: plugins duplicados: {', '.join(duplicates)}")
    disk_names = {
        path.name
        for path in PLUGINS_ROOT.iterdir()
        if path.is_dir() and (path / ".codex-plugin" / "plugin.json").is_file()
    }
    marketplace_name_set = set(marketplace_names)
    missing_entries = sorted(disk_names - marketplace_name_set)
    missing_packages = sorted(marketplace_name_set - disk_names)
    if missing_entries:
        errors.append(
            "marketplace: plugins no disco sem entrada: " + ", ".join(missing_entries)
        )
    if missing_packages:
        errors.append(
            "marketplace: entradas sem pacote no disco: " + ", ".join(missing_packages)
        )
    return errors, len(disk_names)


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
        if prompt is None or not prompt.strip():
            errors.append(f"{prefix}: default_prompt precisa ser preenchido")
        elif f"${prefix}" in prompt or f"@{prefix}" in prompt:
            errors.append(f"{prefix}: default_prompt deve ser neutro, sem sintaxe de invocação")
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
    result = subprocess.run(
        [sys.executable, "-X", "utf8", str(script)],
        input=sample,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    expected_fragments = (
        "OK\tTítulo\t[10/10]",
        "ACIMA\tTítulo",
        "DUPLICADO linhas",
        "OK\tTítulo\t[1/1]",
    )
    if result.returncode != 1 or any(fragment not in result.stdout for fragment in expected_fragments):
        details = (result.stdout + result.stderr).strip().replace("\n", " | ")
        return [
            "csc-paid-media-copy: audit_assets.py falhou no autoteste "
            f"(código {result.returncode}; saída: {details[-500:]})"
        ]
    return []


def tree_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def check_plugin_bundle(skill_names: set[str]) -> list[str]:
    errors: list[str] = []
    manifest_path = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"plugin: manifesto inválido: {exc}"]
    if manifest.get("name") != "thais-skills-library" or manifest.get("skills") != "./skills/":
        errors.append("plugin: identidade ou caminho de Skills inválido")
    bundled = PLUGIN_ROOT / "skills"
    bundled_names = {path.name for path in bundled.iterdir() if (path / "SKILL.md").is_file()}
    if bundled_names != skill_names:
        errors.append("plugin: conjunto de Skills diverge da biblioteca canônica")
    for name in sorted(skill_names & bundled_names):
        if tree_hashes(SKILLS_ROOT / name) != tree_hashes(bundled / name):
            errors.append(f"plugin: cópia de {name} diverge de skills/{name}")
    return errors


def check_seo_plugin() -> list[str]:
    errors: list[str] = []
    skill_root = SEO_PLUGIN_ROOT / "skills" / "seo-auditor-phd"

    required_files = (
        skill_root / "SKILL.md",
        skill_root / "agents" / "openai.yaml",
        skill_root / "references" / "audit-methodology.md",
        skill_root / "references" / "data-acquisition.md",
        skill_root / "references" / "report-contract.md",
        skill_root / "scripts" / "analyze_onpage.py",
        SEO_PLUGIN_ROOT / "tests" / "test_analyze_onpage.py",
        SEO_PLUGIN_ROOT / "tests" / "fixtures" / "example-lp.html",
        SEO_PLUGIN_ROOT / "evals" / "example-audit.md",
        SEO_PLUGIN_ROOT / "evals" / "example-measurements.json",
        SEO_PLUGIN_ROOT / "evals" / "critical-review.md",
    )
    for path in required_files:
        if not path.is_file():
            errors.append(f"seo-auditor-phd: arquivo obrigatório ausente: {path.relative_to(ROOT)}")

    if (skill_root / "SKILL.md").is_file():
        try:
            frontmatter, _ = parse_frontmatter(skill_root / "SKILL.md")
        except ValueError as exc:
            errors.append(f"seo-auditor-phd: {exc}")
        else:
            if frontmatter.get("name") != "seo-auditor-phd":
                errors.append("seo-auditor-phd: name da Skill não coincide com a pasta")

    measurements_path = SEO_PLUGIN_ROOT / "evals" / "example-measurements.json"
    if measurements_path.is_file():
        try:
            json.loads(measurements_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"seo-auditor-phd: example-measurements.json inválido: {exc}")

    if (SEO_PLUGIN_ROOT / "tests").is_dir():
        result = subprocess.run(
            [
                sys.executable,
                "-X",
                "utf8",
                "-m",
                "unittest",
                "discover",
                "-s",
                str(SEO_PLUGIN_ROOT / "tests"),
                "-v",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        if result.returncode != 0:
            details = (result.stdout + result.stderr).strip().replace("\n", " | ")
            errors.append(f"seo-auditor-phd: testes falharam: {details[-500:]}")
    return errors


def main() -> int:
    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").is_file())
    skill_names = {path.name for path in skill_dirs}
    errors: list[str] = []
    warnings: list[str] = []
    marketplace_errors, plugin_count = check_marketplace_plugins()
    errors.extend(marketplace_errors)
    for skill_dir in skill_dirs:
        skill_errors, skill_warnings = check_skill(skill_dir)
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)
    errors.extend(check_cases(skill_names))
    errors.extend(check_paid_asset_auditor())
    errors.extend(check_plugin_bundle(skill_names))
    errors.extend(check_seo_plugin())

    for warning in warnings:
        print(f"AVISO {warning}")
    for error in errors:
        print(f"ERRO {error}")
    if errors:
        print(f"FALHOU: {len(errors)} erro(s), {len(warnings)} aviso(s)")
        return 1
    print(
        f"OK: {len(skill_dirs)} Skills canônicas, {plugin_count} plugin(s), "
        f"{len(warnings)} aviso(s), nenhum erro"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
