#!/usr/bin/env python3
"""Audit character limits and normalized duplicates in a TSV asset bank.

Input columns: field<TAB>limit<TAB>text
The first row may be an English or Portuguese header. Read a file path or stdin.
"""

from __future__ import annotations

import csv
import io
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path


def load_text() -> str:
    if len(sys.argv) > 2:
        raise SystemExit("uso: audit_assets.py [arquivo.tsv]")
    if len(sys.argv) == 2:
        return Path(sys.argv[1]).read_text(encoding="utf-8-sig")
    return sys.stdin.read()


def normalize_asset(asset: str) -> str:
    """Normalize harmless Unicode and whitespace differences for duplicate checks."""
    normalized = unicodedata.normalize("NFKC", asset)
    return re.sub(r"\s+", " ", normalized).strip().casefold()


def main() -> int:
    rows = list(csv.reader(io.StringIO(load_text()), delimiter="\t"))
    header = [c.strip().casefold() for c in rows[0][:3]] if rows else []
    if header in (["field", "limit", "text"], ["campo", "limite", "texto"]):
        rows = rows[1:]
        first_line = 2
    else:
        first_line = 1

    seen: dict[str, list[int]] = defaultdict(list)
    failures = 0
    for number, row in enumerate(rows, start=first_line):
        if len(row) != 3:
            print(f"ERRO linha {number}: esperado field<TAB>limit<TAB>text")
            failures += 1
            continue
        field, raw_limit, asset = row
        field = field.strip()
        if not field:
            print(f"ERRO linha {number}: campo vazio")
            failures += 1
            continue
        try:
            limit = int(raw_limit)
        except ValueError:
            print(f"ERRO linha {number}: limite inválido {raw_limit!r}")
            failures += 1
            continue
        if limit < 1:
            print(f"ERRO linha {number}: limite deve ser positivo")
            failures += 1
            continue
        if not asset.strip():
            print(f"ERRO linha {number}: texto vazio")
            failures += 1
            continue
        counted_asset = unicodedata.normalize("NFC", asset)
        count = len(counted_asset)
        status = "OK" if count <= limit else "ACIMA"
        print(f"{status}\t{field}\t[{count}/{limit}]\t{asset}")
        if count > limit:
            failures += 1
        seen[normalize_asset(asset)].append(number)

    for asset, numbers in seen.items():
        if asset and len(numbers) > 1:
            print(f"DUPLICADO linhas {','.join(map(str, numbers))}: {asset}")
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
