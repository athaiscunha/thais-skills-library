#!/usr/bin/env python3
"""Deterministic on-page measurements for SEO Auditor PhD.

This script measures what is present in a local HTML, Markdown, or text file.
It deliberately does not infer search intent, ranking potential, search volume,
keyword difficulty, Core Web Vitals, indexation, or authorship.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urljoin, urlparse


WORD_RE = re.compile(r"[^\W_]+(?:['’\-][^\W_]+)*", re.UNICODE)
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
SPACE_RE = re.compile(r"\s+")
MARKDOWN_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")

EXCLUDED_TAGS = {"script", "style", "noscript", "template", "svg"}
GENERIC_ANCHORS = {
    "aqui",
    "clique aqui",
    "saiba mais",
    "leia mais",
    "ver mais",
    "acesse",
    "link",
    "more",
    "learn more",
    "read more",
    "click here",
}
VOWELS = set("aeiouáéíóúâêôãõàü")


def clean_space(value: str) -> str:
    return SPACE_RE.sub(" ", html.unescape(value or "")).strip()


def words(value: str) -> list[str]:
    return WORD_RE.findall(value or "")


def normalized_tokens(value: str) -> list[str]:
    return [token.casefold() for token in words(value)]


def phrase_positions(text: str, phrase: str) -> list[int]:
    haystack = normalized_tokens(text)
    needle = normalized_tokens(phrase)
    if not needle or len(needle) > len(haystack):
        return []
    width = len(needle)
    return [
        index
        for index in range(len(haystack) - width + 1)
        if haystack[index : index + width] == needle
    ]


def count_phrase(text: str, phrase: str) -> int:
    return len(phrase_positions(text, phrase))


def contains_phrase(text: str, phrase: str) -> bool:
    return bool(phrase_positions(text, phrase))


def keyword_band(word_count: int) -> str:
    if word_count <= 300:
        return "1–3"
    if word_count <= 600:
        return "2–5"
    if word_count <= 1200:
        return "3–8"
    if word_count <= 2000:
        return "4–12"
    return "5–15"


def approximate_syllables(token: str) -> int:
    token = token.casefold()
    groups = 0
    previous_vowel = False
    for char in token:
        current_vowel = char in VOWELS
        if current_vowel and not previous_vowel:
            groups += 1
        previous_vowel = current_vowel
    return max(1, groups)


def reading_metrics(text: str, paragraphs: list[str]) -> dict[str, Any]:
    token_list = words(text)
    sentences = [item for item in SENTENCE_RE.split(clean_space(text)) if words(item)]
    sentence_count = max(1, len(sentences)) if token_list else 0
    syllable_count = sum(approximate_syllables(token) for token in token_list)
    if not token_list:
        flesch = None
        avg_sentence = None
    else:
        avg_sentence = round(len(token_list) / sentence_count, 1)
        flesch = round(
            248.835
            - 1.015 * (len(token_list) / sentence_count)
            - 84.6 * (syllable_count / len(token_list)),
            1,
        )
    paragraph_word_counts = [len(words(item)) for item in paragraphs if words(item)]
    return {
        "word_count": len(token_list),
        "sentence_count": sentence_count,
        "paragraph_count": len(paragraph_word_counts),
        "average_words_per_sentence": avg_sentence,
        "long_sentences_over_30_words": sum(
            1 for sentence in sentences if len(words(sentence)) > 30
        ),
        "long_paragraphs_over_120_words": sum(
            1 for count in paragraph_word_counts if count > 120
        ),
        "flesch_portuguese_approximation": flesch,
        "flesch_caveat": (
            "Triagem aproximada por grupos vocálicos; revise exemplos no texto e não use como veredito."
        ),
    }


@dataclass
class LinkItem:
    href: str
    anchor: str


@dataclass
class ImageItem:
    src: str
    alt: str | None
    width: str | None
    height: str | None
    loading: str | None


class OnPageHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_chunks: list[str] = []
        self.in_title = False
        self.visible_chunks: list[str] = []
        self.main_chunks: list[str] = []
        self.in_body = False
        self.main_depth = 0
        self.excluded_depth = 0
        self.jsonld_depth = 0
        self.jsonld_chunks: list[str] = []
        self.headings: list[dict[str, Any]] = []
        self.main_headings: list[dict[str, Any]] = []
        self.heading_level: int | None = None
        self.heading_chunks: list[str] = []
        self.heading_started_in_main = False
        self.paragraphs: list[str] = []
        self.main_paragraphs: list[str] = []
        self.in_paragraph = False
        self.paragraph_chunks: list[str] = []
        self.paragraph_started_in_main = False
        self.links: list[LinkItem] = []
        self.in_anchor = False
        self.anchor_href = ""
        self.anchor_chunks: list[str] = []
        self.images: list[ImageItem] = []
        self.meta: dict[str, list[str]] = {}
        self.canonicals: list[str] = []
        self.hreflang: list[dict[str, str]] = []
        self.html_lang: str | None = None
        self.has_viewport = False

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key.casefold(): value or "" for key, value in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.casefold()
        attr = self._attrs(attrs)

        if tag == "html":
            self.html_lang = attr.get("lang") or None
        if tag == "body":
            self.in_body = True
        if tag == "main":
            self.main_depth += 1
        if tag == "title":
            self.in_title = True

        if tag == "script" and attr.get("type", "").casefold() == "application/ld+json":
            self.jsonld_depth += 1
        elif tag in EXCLUDED_TAGS:
            self.excluded_depth += 1

        if tag == "meta":
            name = (attr.get("name") or attr.get("property") or attr.get("http-equiv") or "").casefold()
            content = clean_space(attr.get("content", ""))
            if name:
                self.meta.setdefault(name, []).append(content)
            if name == "viewport":
                self.has_viewport = True

        if tag == "link":
            rel_tokens = {part.casefold() for part in attr.get("rel", "").split()}
            href = clean_space(attr.get("href", ""))
            if "canonical" in rel_tokens and href:
                self.canonicals.append(href)
            if "alternate" in rel_tokens and attr.get("hreflang") and href:
                self.hreflang.append({"lang": attr["hreflang"], "href": href})

        if tag in {f"h{level}" for level in range(1, 7)}:
            self.heading_level = int(tag[1])
            self.heading_chunks = []
            self.heading_started_in_main = self.main_depth > 0
        if tag == "p":
            self.in_paragraph = True
            self.paragraph_chunks = []
            self.paragraph_started_in_main = self.main_depth > 0
        if tag == "a":
            self.in_anchor = True
            self.anchor_href = clean_space(attr.get("href", ""))
            self.anchor_chunks = []
        if tag == "img":
            self.images.append(
                ImageItem(
                    src=clean_space(attr.get("src", "")),
                    alt=clean_space(attr["alt"]) if "alt" in attr else None,
                    width=attr.get("width") or None,
                    height=attr.get("height") or None,
                    loading=attr.get("loading") or None,
                )
            )

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.casefold()

        if tag == "title":
            self.in_title = False
        if tag == "body":
            self.in_body = False
        if tag == "main" and self.main_depth:
            self.main_depth -= 1

        if tag == "script" and self.jsonld_depth:
            self.jsonld_depth -= 1
        elif tag in EXCLUDED_TAGS and self.excluded_depth:
            self.excluded_depth -= 1

        if self.heading_level and tag == f"h{self.heading_level}":
            text = clean_space(" ".join(self.heading_chunks))
            item = {"level": self.heading_level, "text": text}
            self.headings.append(item)
            if self.heading_started_in_main:
                self.main_headings.append(item)
            self.heading_level = None
            self.heading_chunks = []
            self.heading_started_in_main = False
        if tag == "p" and self.in_paragraph:
            text = clean_space(" ".join(self.paragraph_chunks))
            if text:
                self.paragraphs.append(text)
                if self.paragraph_started_in_main:
                    self.main_paragraphs.append(text)
            self.in_paragraph = False
            self.paragraph_chunks = []
            self.paragraph_started_in_main = False
        if tag == "a" and self.in_anchor:
            self.links.append(
                LinkItem(href=self.anchor_href, anchor=clean_space(" ".join(self.anchor_chunks)))
            )
            self.in_anchor = False
            self.anchor_href = ""
            self.anchor_chunks = []

    def handle_data(self, data: str) -> None:
        if self.jsonld_depth:
            self.jsonld_chunks.append(data)
            return
        if self.in_title:
            self.title_chunks.append(data)
        if self.excluded_depth:
            return
        value = clean_space(data)
        if not value:
            return
        if self.in_body:
            self.visible_chunks.append(value)
            if self.main_depth:
                self.main_chunks.append(value)
        if self.heading_level:
            self.heading_chunks.append(value)
        if self.in_paragraph:
            self.paragraph_chunks.append(value)
        if self.in_anchor:
            self.anchor_chunks.append(value)


def extract_jsonld_types(raw_chunks: list[str]) -> tuple[int, list[str], list[str]]:
    raw = "\n".join(raw_chunks).strip()
    if not raw:
        return 0, [], []
    decoder = json.JSONDecoder()
    cursor = 0
    documents: list[Any] = []
    errors: list[str] = []
    while cursor < len(raw):
        while cursor < len(raw) and raw[cursor].isspace():
            cursor += 1
        if cursor >= len(raw):
            break
        try:
            document, end = decoder.raw_decode(raw, cursor)
            documents.append(document)
            cursor = end
        except json.JSONDecodeError as exc:
            errors.append(f"JSON-LD inválido próximo ao caractere {exc.pos}: {exc.msg}")
            break

    types: list[str] = []

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            node_type = value.get("@type")
            if isinstance(node_type, str):
                types.append(node_type)
            elif isinstance(node_type, list):
                types.extend(str(item) for item in node_type)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    for document in documents:
        visit(document)
    return len(documents), sorted(set(types)), errors


def parse_markdown_or_text(source: str) -> dict[str, Any]:
    headings: list[dict[str, Any]] = []
    for line in source.splitlines():
        match = MARKDOWN_HEADING_RE.match(line.strip())
        if match:
            headings.append({"level": len(match.group(1)), "text": clean_space(match.group(2))})
    images = [
        ImageItem(src=match.group(2), alt=clean_space(match.group(1)), width=None, height=None, loading=None)
        for match in MARKDOWN_IMAGE_RE.finditer(source)
    ]
    links = [
        LinkItem(href=match.group(2), anchor=clean_space(match.group(1)))
        for match in MARKDOWN_LINK_RE.finditer(source)
    ]
    visible = MARKDOWN_IMAGE_RE.sub(lambda match: match.group(1), source)
    visible = MARKDOWN_LINK_RE.sub(lambda match: match.group(1), visible)
    visible = re.sub(r"^#{1,6}\s+", "", visible, flags=re.MULTILINE)
    visible = re.sub(r"[`*_~>]", "", visible)
    paragraphs = [clean_space(part) for part in re.split(r"\n\s*\n", visible) if clean_space(part)]
    return {
        "title": "",
        "meta": {},
        "canonicals": [],
        "hreflang": [],
        "html_lang": None,
        "has_viewport": False,
        "headings": headings,
        "paragraphs": paragraphs,
        "links": links,
        "images": images,
        "visible_text": clean_space(visible),
        "jsonld_documents": 0,
        "jsonld_types": [],
        "jsonld_errors": [],
    }


def parse_source(source: str, suffix: str) -> tuple[str, dict[str, Any]]:
    is_html = suffix.casefold() in {".html", ".htm"} or bool(
        re.search(r"<!doctype\s+html|<html\b|<head\b|<body\b", source, re.IGNORECASE)
    )
    if not is_html:
        return "markdown_or_text", parse_markdown_or_text(source)

    parser = OnPageHTMLParser()
    parser.feed(source)
    parser.close()
    jsonld_documents, jsonld_types, jsonld_errors = extract_jsonld_types(parser.jsonld_chunks)
    has_main_content = bool(parser.main_chunks)
    visible_chunks = parser.main_chunks or parser.visible_chunks
    return "html", {
        "title": clean_space(" ".join(parser.title_chunks)),
        "meta": parser.meta,
        "canonicals": parser.canonicals,
        "hreflang": parser.hreflang,
        "html_lang": parser.html_lang,
        "has_viewport": parser.has_viewport,
        "headings": parser.main_headings if has_main_content else parser.headings,
        "paragraphs": parser.main_paragraphs if has_main_content else parser.paragraphs,
        "links": parser.links,
        "images": parser.images,
        "visible_text": clean_space(" ".join(visible_chunks)),
        "jsonld_documents": jsonld_documents,
        "jsonld_types": jsonld_types,
        "jsonld_errors": jsonld_errors,
    }


def heading_analysis(headings: list[dict[str, Any]]) -> dict[str, Any]:
    levels = [item["level"] for item in headings]
    jumps: list[dict[str, Any]] = []
    for previous, current in zip(headings, headings[1:]):
        if current["level"] > previous["level"] + 1:
            jumps.append(
                {
                    "from": f"H{previous['level']}",
                    "from_text": previous["text"],
                    "to": f"H{current['level']}",
                    "to_text": current["text"],
                }
            )
    normalized = [clean_space(item["text"]).casefold() for item in headings if item["text"]]
    duplicates = sorted(text for text, count in Counter(normalized).items() if count > 1)
    return {
        "total": len(headings),
        "counts_by_level": {f"h{level}": levels.count(level) for level in range(1, 7)},
        "items": headings,
        "level_jumps": jumps,
        "duplicate_texts_casefolded": duplicates,
    }


def classify_links(links: list[LinkItem], base_url: str | None) -> dict[str, Any]:
    base_host = urlparse(base_url).netloc.casefold() if base_url else ""
    counts = Counter()
    generic: list[dict[str, str]] = []
    empty: list[str] = []
    items: list[dict[str, str]] = []

    for item in links:
        href = clean_space(item.href)
        anchor = clean_space(item.anchor)
        resolved = urljoin(base_url, href) if base_url else href
        parsed = urlparse(resolved)
        if not href or href.startswith("#"):
            kind = "fragment_or_empty"
        elif parsed.scheme in {"mailto", "tel", "javascript"}:
            kind = "special"
        elif base_host and parsed.netloc.casefold() == base_host:
            kind = "internal"
        elif href.startswith(("/", "./", "../")):
            kind = "internal_relative"
        elif parsed.scheme in {"http", "https"}:
            kind = "external"
        else:
            kind = "other"
        counts[kind] += 1
        if anchor.casefold() in GENERIC_ANCHORS:
            generic.append({"anchor": anchor, "href": href})
        if not anchor:
            empty.append(href)
        items.append({"href": href, "resolved": resolved, "anchor": anchor, "kind": kind})

    return {
        "total": len(links),
        "counts_by_kind": dict(counts),
        "generic_anchors": generic,
        "empty_anchor_hrefs": empty,
        "items": items,
    }


def image_analysis(images: list[ImageItem]) -> dict[str, Any]:
    missing = [asdict(item) for item in images if item.alt is None]
    empty = [asdict(item) for item in images if item.alt == ""]
    without_dimensions = [
        asdict(item) for item in images if item.width is None or item.height is None
    ]
    lazy = [asdict(item) for item in images if (item.loading or "").casefold() == "lazy"]
    return {
        "total": len(images),
        "missing_alt_attribute": missing,
        "empty_alt_review_if_decorative": empty,
        "without_explicit_width_or_height": without_dimensions,
        "lazy_loaded": lazy,
        "items": [asdict(item) for item in images],
    }


def quartile_distribution(body_text: str, phrase: str) -> list[int]:
    token_count = len(normalized_tokens(body_text))
    counts = [0, 0, 0, 0]
    if not token_count:
        return counts
    for position in phrase_positions(body_text, phrase):
        quartile = min(3, int(position * 4 / token_count))
        counts[quartile] += 1
    return counts


def keyword_analysis(
    phrase: str,
    body_text: str,
    title: str,
    meta_description: str,
    headings: list[dict[str, Any]],
    first_paragraph: str,
    slug: str,
) -> dict[str, Any]:
    body_word_count = len(words(body_text))
    phrase_width = len(words(phrase))
    occurrences = count_phrase(body_text, phrase)
    h1_text = " ".join(item["text"] for item in headings if item["level"] == 1)
    other_heading_text = " ".join(item["text"] for item in headings if item["level"] > 1)
    first_150 = " ".join(words(body_text)[:150])
    return {
        "phrase": phrase,
        "phrase_token_count": phrase_width,
        "exact_occurrences_in_body": occurrences,
        "occurrences_per_100_body_words": (
            round(occurrences * 100 / body_word_count, 3) if body_word_count else None
        ),
        "keyword_token_footprint_percent": (
            round(occurrences * phrase_width * 100 / body_word_count, 3)
            if body_word_count
            else None
        ),
        "starting_band_not_target": keyword_band(body_word_count),
        "zones": {
            "title": count_phrase(title, phrase),
            "meta_description": count_phrase(meta_description, phrase),
            "h1": count_phrase(h1_text, phrase),
            "h2_h6": count_phrase(other_heading_text, phrase),
            "first_paragraph": count_phrase(first_paragraph, phrase),
            "first_150_words": count_phrase(first_150, phrase),
            "url_slug": count_phrase(slug.replace("-", " "), phrase),
        },
        "body_quartiles_q1_to_q4": quartile_distribution(body_text, phrase),
        "distribution_caveat": (
            "Contagem exata, sem flexões ou sinônimos. A faixa é ponto de partida editorial, não meta de densidade."
        ),
    }


def build_review_flags(
    title: str,
    meta_description: str,
    headings: dict[str, Any],
    keyword_results: list[dict[str, Any]],
    images: dict[str, Any],
    links: dict[str, Any],
    canonical: list[str],
    robots: list[str],
    has_viewport: bool,
    mode: str,
) -> list[dict[str, str]]:
    flags: list[dict[str, str]] = []

    def add(area: str, observation: str, why_review: str) -> None:
        flags.append({"area": area, "observation": observation, "why_review": why_review})

    if mode == "html":
        if not title:
            add("title", "Title ausente no HTML.", "A página perde um sinal descritivo central e uma peça do snippet.")
        elif len(title) < 30 or len(title) > 65:
            add(
                "title",
                f"Title com {len(title)} caracteres.",
                "Faixas de comprimento são triagem; revise clareza, diferenciação e truncamento provável.",
            )
        if not meta_description:
            add("meta description", "Meta description ausente.", "O buscador poderá formar o snippet sem uma proposta editorial.")
        elif len(meta_description) < 70 or len(meta_description) > 170:
            add(
                "meta description",
                f"Meta description com {len(meta_description)} caracteres.",
                "Revise utilidade para CTR; comprimento isolado não é erro de ranking.",
            )
        if not canonical:
            add("canonical", "Canonical não encontrada no HTML.", "Confirme estratégia de duplicidade antes de classificar como erro.")
        if not has_viewport:
            add(
                "mobile",
                "Meta viewport não observada no HTML.",
                "Confirme a renderização em dispositivos móveis; a ausência pode comprometer o layout responsivo.",
            )
        if robots and any("noindex" in value.casefold() for value in robots):
            add("indexabilidade", "Diretiva noindex observada.", "Confirme se a exclusão é intencional; nãoindex não é erro por definição.")

    h1_count = headings["counts_by_level"]["h1"]
    if h1_count == 0:
        add("headings", "Nenhum H1 observado.", "Um rótulo principal claro costuma melhorar compreensão e estrutura.")
    elif h1_count > 1:
        add("headings", f"{h1_count} H1 observados.", "Revise o contexto sem assumir que múltiplos H1 são automaticamente inválidos.")
    if headings["level_jumps"]:
        add("headings", "Saltos de nível observados.", "Confirme se a hierarquia comunica dependência lógica ou se níveis foram usados apenas para estilo.")

    if keyword_results:
        primary = keyword_results[0]
        zones = primary["zones"]
        missing_zones = [zone for zone in ("title", "h1", "first_150_words") if zones[zone] == 0]
        if missing_zones:
            add(
                "keyword principal",
                "Termo exato ausente de: " + ", ".join(missing_zones) + ".",
                "Revise intenção e naturalidade antes de inserir; zonas importam mais que uma taxa global.",
            )
        if zones["first_paragraph"] == 0:
            add(
                "introdução",
                "Termo exato ausente do primeiro parágrafo.",
                "Confirme se a introdução identifica tema e oferta por variação inequívoca; não insira o termo se isso piorar a fluência.",
            )
        footprint = primary["keyword_token_footprint_percent"] or 0
        if footprint > 3:
            add(
                "keyword principal",
                f"Pegada do termo exato de {footprint}% dos tokens do corpo.",
                "É apenas sinal mecânico para revisar repetições em contexto, não diagnóstico automático de stuffing.",
            )
        quartiles = primary["body_quartiles_q1_to_q4"]
        if sum(quartiles) >= 3 and max(quartiles) == sum(quartiles):
            add(
                "keyword principal",
                f"Todas as {sum(quartiles)} ocorrências estão no mesmo quartil do corpo.",
                "Concentração pode indicar distribuição artificial; leia os trechos antes de alterar.",
            )

    if images["missing_alt_attribute"]:
        add(
            "imagens",
            f"{len(images['missing_alt_attribute'])} imagem(ns) sem atributo alt.",
            "Defina alt contextual ou marque como decorativa conforme a função; não preencha com keyword por padrão.",
        )
    if links["generic_anchors"]:
        add(
            "links",
            f"{len(links['generic_anchors'])} âncora(s) genérica(s) observada(s).",
            "O contexto pode compensar, mas âncoras descritivas geralmente ajudam navegação e compreensão do destino.",
        )
    return flags


def build_report(path: Path, source: str, primary: str | None, secondary: list[str], url: str | None) -> dict[str, Any]:
    mode, parsed = parse_source(source, path.suffix)
    body_text = parsed["visible_text"]
    title = parsed["title"]
    meta_description = (parsed["meta"].get("description") or [""])[0]
    robots = parsed["meta"].get("robots", [])
    headings = heading_analysis(parsed["headings"])
    first_paragraph = parsed["paragraphs"][0] if parsed["paragraphs"] else ""
    slug = urlparse(url).path.rstrip("/").split("/")[-1] if url else path.stem
    phrases = [item for item in [primary, *secondary] if item]
    keyword_results = [
        keyword_analysis(
            item,
            body_text,
            title,
            meta_description,
            parsed["headings"],
            first_paragraph,
            slug,
        )
        for item in phrases
    ]
    links = classify_links(parsed["links"], url)
    images = image_analysis(parsed["images"])
    reading = reading_metrics(body_text, parsed["paragraphs"])
    faq_heading_candidates = [
        item["text"]
        for item in parsed["headings"]
        if "?" in item["text"] or item["text"].casefold().startswith(("como ", "o que ", "por que ", "qual ", "quando "))
    ]
    flags = build_review_flags(
        title,
        meta_description,
        headings,
        keyword_results,
        images,
        links,
        parsed["canonicals"],
        robots,
        parsed["has_viewport"],
        mode,
    )
    return {
        "measurement_scope": {
            "input_path": str(path),
            "input_mode": mode,
            "provided_url": url,
            "measured_from": "main element when present; otherwise visible body/text",
            "not_measured": [
                "search intent and funnel fit",
                "search volume and keyword difficulty",
                "rankings, traffic, CTR and conversions",
                "SERP and competitors",
                "actual indexation and crawl behavior",
                "HTTP headers and redirect chain",
                "rendered DOM when input is static HTML",
                "Core Web Vitals and mobile behavior",
                "sitewide cannibalization",
                "content authorship or AI generation",
            ],
        },
        "document": {
            "title": title,
            "title_characters": len(title),
            "meta_description": meta_description,
            "meta_description_characters": len(meta_description),
            "html_lang": parsed["html_lang"],
            "has_viewport_meta": parsed["has_viewport"],
            "canonical": parsed["canonicals"],
            "robots_meta": robots,
            "hreflang": parsed["hreflang"],
            "url_slug": slug,
        },
        "content": {
            **reading,
            "first_paragraph": first_paragraph,
        },
        "headings": headings,
        "keywords": keyword_results,
        "links": links,
        "images": images,
        "structured_data": {
            "jsonld_document_count": parsed["jsonld_documents"],
            "types": parsed["jsonld_types"],
            "parse_errors": parsed["jsonld_errors"],
        },
        "answer_formats": {
            "question_heading_candidates": faq_heading_candidates,
            "faqpage_schema_observed": "FAQPage" in parsed["jsonld_types"],
        },
        "mechanical_review_flags": flags,
        "interpretation_warning": (
            "As flags são triagem mecânica. Valide intenção, contexto, função do elemento e evidência externa antes de classificar impacto."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    document = report["document"]
    content = report["content"]
    lines = [
        "# Medições on-page",
        "",
        f"- Modo: `{report['measurement_scope']['input_mode']}`",
        f"- Palavras medidas: {content['word_count']}",
        f"- Title: {document['title'] or '— ausente/não disponível'} ({document['title_characters']} caracteres)",
        f"- Meta description: {document['meta_description'] or '— ausente/não disponível'} ({document['meta_description_characters']} caracteres)",
        "",
        "## Keywords",
        "",
        "| Termo | Corpo | /100 palavras | Title | H1 | Primeiras 150 | Quartis | Faixa inicial |",
        "|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in report["keywords"]:
        zones = item["zones"]
        lines.append(
            f"| {item['phrase']} | {item['exact_occurrences_in_body']} | "
            f"{item['occurrences_per_100_body_words']} | {zones['title']} | {zones['h1']} | "
            f"{zones['first_150_words']} | {item['body_quartiles_q1_to_q4']} | "
            f"{item['starting_band_not_target']} |"
        )
    lines.extend(["", "## Flags para revisão", ""])
    for flag in report["mechanical_review_flags"]:
        lines.append(f"- **{flag['area']}:** {flag['observation']} {flag['why_review']}")
    lines.extend(
        [
            "",
            "> Estas medições não avaliam intenção, ranking, volume, indexação real, CWV ou autoria.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mede sinais on-page em HTML, Markdown ou texto sem inventar dados externos."
    )
    parser.add_argument("input", type=Path, help="Arquivo HTML, Markdown ou texto.")
    parser.add_argument("--primary", help="Keyword principal para contagem exata.")
    parser.add_argument(
        "--secondary",
        action="append",
        default=[],
        help="Keyword secundária; repita o argumento para mais de uma.",
    )
    parser.add_argument("--url", help="URL-base para slug e classificação de links.")
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="Formato da saída padrão.",
    )
    parser.add_argument("--output", type=Path, help="Grava a saída neste arquivo.")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    if not args.input.is_file():
        print(f"Arquivo não encontrado: {args.input}", file=sys.stderr)
        return 2
    source = args.input.read_text(encoding="utf-8-sig")
    report = build_report(args.input, source, args.primary, args.secondary, args.url)
    output = (
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.format == "json"
        else render_markdown(report)
    )
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
