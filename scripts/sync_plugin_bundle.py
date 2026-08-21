#!/usr/bin/env python3
"""Regenerate the installable plugin bundle from the canonical Skills."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / "plugins" / "thais-skills-library" / "skills"


def skill_directories(root: Path) -> list[Path]:
    return sorted(path for path in root.iterdir() if (path / "SKILL.md").is_file())


def main() -> int:
    source_skills = skill_directories(SOURCE)
    if not source_skills:
        raise SystemExit("Nenhuma Skill canônica encontrada em skills/.")

    expected_parent = ROOT / "plugins" / "thais-skills-library"
    if TARGET.parent != expected_parent:
        raise SystemExit("Destino do bundle fora do plugin esperado.")

    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True)

    for source_skill in source_skills:
        shutil.copytree(source_skill, TARGET / source_skill.name)
    catalog = SOURCE / "README.md"
    if catalog.is_file():
        shutil.copy2(catalog, TARGET / catalog.name)

    names = ", ".join(path.name for path in source_skills)
    print(f"Bundle sincronizado: {len(source_skills)} Skills ({names})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
