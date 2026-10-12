#!/usr/bin/env python3
"""Checagens locais de candidatura. Somente leitura; Python 3.10+, stdlib."""

import argparse
import json
import re
import sys
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path, PureWindowsPath


class EntradaInvalida(ValueError):
    pass


def objeto(value, path, allowed, required=()):
    if not isinstance(value, dict):
        raise EntradaInvalida(f"{path}: deve ser objeto JSON")
    extra = set(value) - set(allowed)
    missing = set(required) - set(value)
    if extra:
        raise EntradaInvalida(f"{path}: chaves desconhecidas: {', '.join(sorted(extra))}")
    if missing:
        raise EntradaInvalida(f"{path}: chaves ausentes: {', '.join(sorted(missing))}")
    return value


def lista(value, path):
    if not isinstance(value, list):
        raise EntradaInvalida(f"{path}: deve ser lista")
    return value


def texto(value, path, nonempty=False):
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise EntradaInvalida(f"{path}: deve ser texto{' não vazio' if nonempty else ''}")
    return value


def booleano(value, path):
    if not isinstance(value, bool):
        raise EntradaInvalida(f"{path}: deve ser booleano")
    return value


def inteiro(value, path):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise EntradaInvalida(f"{path}: deve ser inteiro não negativo")
    return value


def decimal_exato(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
        raise ValueError("usar número JSON ou texto decimal, sem símbolo monetário")
    if isinstance(value, str) and not re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", value):
        raise ValueError("usar decimal com ponto, sem separador de milhar; NaN/infinito não são aceitos")
    try:
        number = Decimal(value)
    except InvalidOperation as exc:
        raise ValueError("decimal inválido") from exc
    if not number.is_finite():
        raise ValueError("NaN/infinito não são aceitos")
    if number < 0:
        raise ValueError("valor negativo não é aceito")
    # Limites técnicos de representação, não regras do edital. Sem arredondamento.
    if len(number.as_tuple().digits) > 100 or abs(number.as_tuple().exponent) > 100:
        raise ValueError("decimal excede a representação técnica: 100 algarismos ou expoente ±100")
    return number


def decimal_regra(value, path):
    try:
        return decimal_exato(value)
    except ValueError as exc:
        raise EntradaInvalida(f"{path}: {exc}") from exc


def strings_unicas(value, path):
    values = lista(value, path)
    for i, item in enumerate(values):
        texto(item, f"{path}[{i}]", True)
    if len(values) != len(set(values)):
        raise EntradaInvalida(f"{path}: valores duplicados")
    return values


def validar_estrutura(data):
    objeto(data, "$", {"versao", "regras", "campos", "orcamento", "anexos", "pendencias"},
           {"versao", "regras", "campos", "orcamento", "anexos", "pendencias"})
    if type(data["versao"]) is not int or data["versao"] != 1:
        raise EntradaInvalida("$.versao: somente o inteiro 1 é aceito")
    rules = objeto(data["regras"], "$.regras", {"fonte", "campos", "orcamento", "anexos"},
                   {"fonte", "campos", "orcamento", "anexos"})
    texto(rules["fonte"], "$.regras.fonte", True)
    if not isinstance(rules["campos"], dict):
        raise EntradaInvalida("$.regras.campos: deve ser objeto")
    for name, rule in rules["campos"].items():
        path = f"$.regras.campos.{name}"
        texto(name, path, True)
        objeto(rule, path, {"obrigatorio", "min_caracteres", "max_caracteres"}, {"obrigatorio"})
        booleano(rule["obrigatorio"], path + ".obrigatorio")
        for key in ("min_caracteres", "max_caracteres"):
            if key in rule:
                inteiro(rule[key], path + "." + key)
        if "min_caracteres" in rule and "max_caracteres" in rule and rule["min_caracteres"] > rule["max_caracteres"]:
            raise EntradaInvalida(path + ": mínimo de caracteres excede máximo")
    budget = objeto(rules["orcamento"], "$.regras.orcamento",
                    {"fonte_solicitacao", "teto_solicitacao", "teto_total", "categorias_permitidas",
                     "fontes_permitidas", "limites_categoria"}, {"fonte_solicitacao"})
    texto(budget["fonte_solicitacao"], "$.regras.orcamento.fonte_solicitacao", True)
    for key in ("teto_solicitacao", "teto_total"):
        if key in budget:
            decimal_regra(budget[key], "$.regras.orcamento." + key)
    for key in ("categorias_permitidas", "fontes_permitidas"):
        if key in budget:
            strings_unicas(budget[key], "$.regras.orcamento." + key)
    if "fontes_permitidas" in budget and budget["fonte_solicitacao"] not in budget["fontes_permitidas"]:
        raise EntradaInvalida("$.regras.orcamento: fonte_solicitacao não está em fontes_permitidas")
    if "limites_categoria" in budget:
        if not isinstance(budget["limites_categoria"], dict):
            raise EntradaInvalida("$.regras.orcamento.limites_categoria: deve ser objeto")
        for name, amount in budget["limites_categoria"].items():
            texto(name, "$.regras.orcamento.limites_categoria", True)
            decimal_regra(amount, "$.regras.orcamento.limites_categoria." + name)
            if "categorias_permitidas" in budget and name not in budget["categorias_permitidas"]:
                raise EntradaInvalida(f"$.regras.orcamento.limites_categoria: categoria não permitida: {name}")
    seen = set()
    for i, rule in enumerate(lista(rules["anexos"], "$.regras.anexos")):
        path = f"$.regras.anexos[{i}]"
        objeto(rule, path, {"id", "obrigatorio", "extensoes", "max_bytes"}, {"id", "obrigatorio"})
        aid = texto(rule["id"], path + ".id", True)
        if aid in seen:
            raise EntradaInvalida(path + ": id de regra de anexo duplicado")
        seen.add(aid)
        booleano(rule["obrigatorio"], path + ".obrigatorio")
        if "max_bytes" in rule:
            inteiro(rule["max_bytes"], path + ".max_bytes")
        if "extensoes" in rule:
            for ext in strings_unicas(rule["extensoes"], path + ".extensoes"):
                if not re.fullmatch(r"\.[a-z0-9]+", ext):
                    raise EntradaInvalida(path + ": extensões devem usar formato minúsculo '.pdf', '.jpg' etc.")
    if not isinstance(data["campos"], dict):
        raise EntradaInvalida("$.campos: deve ser objeto")
    for name, value in data["campos"].items():
        texto(name, "$.campos", True)
        texto(value, "$.campos." + name)
    budget = objeto(data["orcamento"], "$.orcamento", {"valor_solicitado", "total_declarado", "itens"},
                    {"valor_solicitado", "itens"})
    for i, item in enumerate(lista(budget["itens"], "$.orcamento.itens")):
        path = f"$.orcamento.itens[{i}]"
        objeto(item, path, {"id", "descricao", "quantidade", "valor_unitario", "total_declarado",
                            "categoria", "fonte", "elegivel"},
               {"id", "descricao", "quantidade", "valor_unitario", "categoria", "fonte", "elegivel"})
        for key in ("id", "descricao", "categoria", "fonte"):
            texto(item[key], path + "." + key, True)
        if item["elegivel"] is not None:
            booleano(item["elegivel"], path + ".elegivel")
    for i, item in enumerate(lista(data["anexos"], "$.anexos")):
        path = f"$.anexos[{i}]"
        objeto(item, path, {"id", "caminho"}, {"id", "caminho"})
        texto(item["id"], path + ".id", True)
        texto(item["caminho"], path + ".caminho", True)
    for i, pending in enumerate(lista(data["pendencias"], "$.pendencias")):
        texto(pending, f"$.pendencias[{i}]", True)


def serializar_decimal(value):
    return format(value, "f")


def relatorio_vazio():
    return {"erros": [], "avisos": [], "verificacoes": [], "total": None}


def validar(data, base):
    validar_estrutura(data)
    report = relatorio_vazio()
    report["total"] = {"orcamento": None, "elegivel_solicitacao": None, "solicitado": None,
                       "por_categoria": None, "por_fonte": None, "anexos_bytes": 0}

    def issue(kind, code, path, message):
        report[kind].append({"codigo": code, "caminho": path, "mensagem": message})

    def check(ok, code, path, message, **details):
        report["verificacoes"].append({"codigo": code, "caminho": path,
                                      "resultado": "ok" if ok else "erro", **details})
        if not ok:
            issue("erros", code, path, message)

    def amount(value, path):
        try:
            return decimal_exato(value)
        except ValueError as exc:
            issue("erros", "NUMERO_INVALIDO", path, str(exc))
            return None

    rules = data["regras"]
    for name, rule in rules["campos"].items():
        value = data["campos"].get(name, "")
        path = "$.campos." + name
        present = bool(value.strip())
        if rule["obrigatorio"]:
            check(present, "CAMPO_OBRIGATORIO", path, "Campo obrigatório ausente ou vazio.")
        if name in data["campos"]:
            size = len(value)
            report["verificacoes"].append({"codigo": "CARACTERES_UNICODE", "caminho": path,
                                          "resultado": "ok", "quantidade": size})
            if "min_caracteres" in rule and (present or rule["obrigatorio"]):
                check(size >= rule["min_caracteres"], "CAMPO_CURTO", path,
                      f"Campo tem {size} pontos de código Unicode; mínimo configurado: {rule['min_caracteres']}.")
            if "max_caracteres" in rule:
                check(size <= rule["max_caracteres"], "CAMPO_LONGO", path,
                      f"Campo tem {size} pontos de código Unicode; máximo configurado: {rule['max_caracteres']}.")
    for name in data["campos"].keys() - rules["campos"].keys():
        issue("avisos", "CAMPO_SEM_REGRA", "$.campos." + name,
              "Campo sem regra configurada; obrigatoriedade e limites não foram verificados.")
    issue("avisos", "CONTAGEM_DO_PORTAL", "$.campos",
          "A contagem usa pontos de código Unicode, inclui espaços/quebras e não normaliza texto. Conferir o contador do portal.")

    budget = data["orcamento"]
    brules = rules["orcamento"]
    requested = amount(budget["valor_solicitado"], "$.orcamento.valor_solicitado")
    if requested is not None:
        report["total"]["solicitado"] = serializar_decimal(requested)
    declared = amount(budget["total_declarado"], "$.orcamento.total_declarado") if "total_declarado" in budget else None
    complete = True
    eligibility_complete = True
    total = Decimal(0)
    eligible = Decimal(0)
    categories = {}
    sources = {}
    seen = set()
    for i, item in enumerate(budget["itens"]):
        path = f"$.orcamento.itens[{i}]"
        iid = item["id"]
        check(iid not in seen, "ID_ITEM_DUPLICADO", path + ".id", f"ID de item duplicado: {iid}.")
        seen.add(iid)
        for key, permitted in (("categoria", "categorias_permitidas"), ("fonte", "fontes_permitidas")):
            if permitted in brules:
                check(item[key] in brules[permitted], "VALOR_NAO_PERMITIDO", path + "." + key,
                      f"Valor '{item[key]}' não consta em {permitted}.")
        if item["elegivel"] is None:
            eligibility_complete = False
            issue("erros", "ELEGIBILIDADE_PENDENTE", path + ".elegivel",
                  "Elegibilidade do item não foi confirmada na candidatura.")
        elif item["fonte"] == brules["fonte_solicitacao"]:
            check(item["elegivel"], "ITEM_INELEGIVEL_SOLICITADO", path + ".elegivel",
                  "Item declarado inelegível foi alocado à fonte da solicitação.")
        quantity = amount(item["quantidade"], path + ".quantidade")
        unit = amount(item["valor_unitario"], path + ".valor_unitario")
        item_declared = amount(item["total_declarado"], path + ".total_declarado") if "total_declarado" in item else None
        if quantity is None or unit is None:
            complete = False
            continue
        computed = quantity * unit
        total += computed
        categories[item["categoria"]] = categories.get(item["categoria"], Decimal(0)) + computed
        sources[item["fonte"]] = sources.get(item["fonte"], Decimal(0)) + computed
        if item["fonte"] == brules["fonte_solicitacao"] and item["elegivel"] is True:
            eligible += computed
        report["verificacoes"].append({"codigo": "TOTAL_ITEM_CALCULADO", "caminho": path,
                                      "resultado": "ok", "total": serializar_decimal(computed)})
        if item_declared is not None:
            check(computed == item_declared, "TOTAL_ITEM_DIVERGENTE", path + ".total_declarado",
                  f"Total declarado difere de quantidade × valor unitário ({serializar_decimal(computed)}).")
        if quantity == 0 or unit == 0:
            issue("avisos", "ITEM_ZERADO", path, "Item possui quantidade ou valor unitário zero; conferir intenção.")
    if complete:
        report["total"]["orcamento"] = serializar_decimal(total)
        report["total"]["por_categoria"] = {k: serializar_decimal(v) for k, v in sorted(categories.items())}
        report["total"]["por_fonte"] = {k: serializar_decimal(v) for k, v in sorted(sources.items())}
        if eligibility_complete:
            report["total"]["elegivel_solicitacao"] = serializar_decimal(eligible)
            if requested is not None:
                check(requested == eligible, "SOLICITACAO_DIVERGENTE", "$.orcamento.valor_solicitado",
                      "Valor solicitado difere da soma dos itens declarados elegíveis alocados à fonte da solicitação.")
        if declared is not None:
            check(total == declared, "TOTAL_ORCAMENTO_DIVERGENTE", "$.orcamento.total_declarado",
                  f"Total declarado difere da soma calculada ({serializar_decimal(total)}).")
        if "teto_total" in brules:
            check(total <= decimal_regra(brules["teto_total"], "$.regras.orcamento.teto_total"),
                  "TETO_TOTAL_EXCEDIDO", "$.orcamento", "Soma do orçamento excede teto total configurado.")
        for category, limit in brules.get("limites_categoria", {}).items():
            check(categories.get(category, Decimal(0)) <= decimal_regra(limit, "$.regras.orcamento.limites_categoria"),
                  "TETO_CATEGORIA_EXCEDIDO", "$.orcamento.itens",
                  f"Soma da categoria '{category}' excede o teto absoluto configurado, consideradas todas as fontes.")
    else:
        issue("avisos", "SOMAS_NAO_VERIFICADAS", "$.orcamento",
              "Ao menos um item não pôde ser calculado; totais e comparações dependentes não foram produzidos.")
    if requested is not None and "teto_solicitacao" in brules:
        check(requested <= decimal_regra(brules["teto_solicitacao"], "$.regras.orcamento.teto_solicitacao"),
              "TETO_SOLICITACAO_EXCEDIDO", "$.orcamento.valor_solicitado", "Valor solicitado excede teto configurado.")
    if "teto_solicitacao" not in brules:
        issue("avisos", "TETO_NAO_CONFIGURADO", "$.regras.orcamento",
              "Não foi configurado teto da solicitação; confirmar a regra do edital.")

    arules = {rule["id"]: rule for rule in rules["anexos"]}
    seen = set()
    resolved_seen = set()
    for i, item in enumerate(data["anexos"]):
        path = f"$.anexos[{i}]"
        aid = item["id"]
        check(aid not in seen, "ID_ANEXO_DUPLICADO", path + ".id", f"ID de anexo duplicado: {aid}.")
        seen.add(aid)
        rule = arules.get(aid, {})
        if not rule:
            issue("avisos", "ANEXO_SEM_REGRA", path, "Anexo não possui limites específicos configurados.")
        rel = Path(item["caminho"])
        win = PureWindowsPath(item["caminho"])
        if rel.is_absolute() or win.is_absolute() or win.drive or win.root or ".." in rel.parts or ".." in win.parts:
            issue("erros", "CAMINHO_NAO_RELATIVO", path + ".caminho",
                  "Usar caminho relativo dentro da pasta da candidatura, sem '..', unidade ou raiz absoluta.")
            continue
        try:
            full = (base / rel).resolve()
            if not full.is_relative_to(base):
                issue("erros", "ANEXO_FORA_DA_BASE", path + ".caminho", "Arquivo resolvido está fora da pasta da candidatura.")
                continue
            if not full.is_file():
                issue("erros", "ANEXO_AUSENTE", path + ".caminho", "Arquivo ausente ou caminho não é arquivo regular.")
                continue
            size = full.stat().st_size
        except (OSError, ValueError, RuntimeError) as exc:
            issue("erros", "ANEXO_INACESSIVEL", path + ".caminho", f"Não foi possível inspecionar anexo ({type(exc).__name__}).")
            continue
        if full in resolved_seen:
            issue("avisos", "ARQUIVO_REUTILIZADO", path + ".caminho", "Mesmo arquivo foi usado em mais de um anexo.")
        else:
            report["total"]["anexos_bytes"] += size
        resolved_seen.add(full)
        check(size > 0, "ANEXO_VAZIO", path + ".caminho", "Arquivo tem zero bytes.", bytes=size)
        if "max_bytes" in rule:
            check(size <= rule["max_bytes"], "ANEXO_GRANDE", path + ".caminho",
                  f"Arquivo tem {size} bytes; limite configurado: {rule['max_bytes']}.")
        if "extensoes" in rule:
            check(full.suffix.lower() in rule["extensoes"], "EXTENSAO_NAO_PERMITIDA", path + ".caminho",
                  "Extensão do nome de arquivo não consta nas extensões configuradas.")
    for aid, rule in arules.items():
        if rule["obrigatorio"]:
            check(aid in seen, "ANEXO_OBRIGATORIO", "$.anexos", f"Anexo obrigatório não listado: {aid}.")
    for i, pending in enumerate(data["pendencias"]):
        issue("erros", "PENDENCIA_EXPLICITA", f"$.pendencias[{i}]", pending)
    issue("avisos", "ALCANCE_LIMITADO", "$",
          "Checagem local da configuração fornecida. Não valida conteúdo/assinatura de anexos, regras oficiais, elegibilidade jurídica, mérito, nota, chance ou envio ao portal.")
    return report


def objeto_sem_duplicatas(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise EntradaInvalida(f"JSON contém chave duplicada: {key}")
        result[key] = value
    return result


def constante_invalida(value):
    raise EntradaInvalida(f"Constante inválida em JSON: {value}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidatura", help="JSON UTF-8; anexos relativos à pasta deste arquivo")
    args = parser.parse_args()
    try:
        path = Path(args.candidatura).resolve()
        data = json.loads(path.read_text(encoding="utf-8-sig"), parse_float=Decimal,
                          parse_constant=constante_invalida, object_pairs_hook=objeto_sem_duplicatas)
        with localcontext() as context:
            context.prec = 1000
            report = validar(data, path.parent)
        code = 1 if report["erros"] else 0
    except (ValueError, InvalidOperation, OSError, UnicodeError, RecursionError) as exc:
        report = relatorio_vazio()
        report["erros"].append({"codigo": "ENTRADA_INVALIDA", "caminho": "$", "mensagem": str(exc)})
        code = 2
    output = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    # UTF-8 consistente mesmo em consoles Windows com outra página de código.
    if hasattr(sys.stdout, "buffer"):
        sys.stdout.buffer.write(output.encode("utf-8"))
    else:
        sys.stdout.write(output)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
