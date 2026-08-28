---
name: seo-auditor-phd
description: Audita SEO on-page de URLs, páginas, LPs, sites e textos colados; avalia intenção, keywords, conteúdo, metadados, arquitetura, técnica, E-E-A-T, CTR, GEO e AEO e entrega correções priorizadas sem inventar métricas externas. Use para diagnóstico, revisão, comparação, otimização ou investigação de canibalização; não use como substituto de dados reais de ranking, tráfego ou conversão.
---

# SEO Auditor PhD

Produza uma auditoria crítica, verificável e diretamente executável. Separe o que foi observado ou medido do que foi inferido e do que depende de acesso externo.

## Antes de auditar

Determine o modo de entrada:

- **Texto, HTML ou arquivo de uma página:** avalie conteúdo e somente os elementos realmente presentes. Marque indexabilidade, Core Web Vitals, renderização, mobile, sitemap, hreflang, headers e canibalização como não verificados quando não houver evidência.
- **URL:** inspecione a página publicada com os recursos disponíveis. Prefira HTML e DOM renderizado quando JavaScript puder alterar conteúdo, metadados ou links. Registre data, URL final e limitações de acesso.
- **Site ou conjunto de URLs:** além das páginas individuais, avalie arquitetura, duplicidade, canibalização, links internos, templates e consistência. Não extrapole uma página para o site inteiro.

Identifique idioma, país, público, tipo de página, objetivo de conversão, estágio de funil e palavra-chave principal/secundárias informadas. Se keywords não forem fornecidas, proponha candidatos como **hipóteses**, baseadas no texto e, quando possível, na SERP atual; não apresente volume ou dificuldade sem fonte real.

Use quatro rótulos de evidência no relatório:

- **Observado:** presente no texto, HTML, DOM, URL, SERP ou integração consultada.
- **Medido:** calculado a partir do material analisado; informe método e denominador.
- **Inferido:** interpretação profissional sustentada por sinais visíveis.
- **Requer dados:** não verificável com a entrada ou ferramentas disponíveis.

## Recursos da skill

- Em uma auditoria completa, leia [references/audit-methodology.md](references/audit-methodology.md) e [references/report-contract.md](references/report-contract.md).
- Para URL, SERP, site, canibalização, performance ou integrações, leia [references/data-acquisition.md](references/data-acquisition.md).
- Quando houver HTML, Markdown ou texto salvo localmente, execute `scripts/analyze_onpage.py` para obter métricas mecânicas. Trate a saída como evidência auxiliar, não como conclusão sem revisão humana.

Exemplo:

```powershell
python scripts/analyze_onpage.py pagina.html --primary "curso de enfermagem" --secondary "graduação em enfermagem" --url "https://exemplo.com/curso-enfermagem"
```

## Processo obrigatório

1. **Fixe o escopo e as evidências.** Diga o que será e o que não será avaliado. Não prometa auditoria técnica completa com texto colado.
2. **Valide intenção antes de densidade.** Decida se a página e a oferta respondem à intenção dominante e às intenções adjacentes. Uma keyword pode estar bem distribuída e ainda assim ser estratégica ou semanticamente inadequada.
3. **Meça sem perseguir uma porcentagem universal.** Conte termo exato, flexões e variações separadamente; analise zonas e distribuição. Recomende uma faixa aproximada apenas como ponto de partida proporcional ao tamanho do texto e explique onde as ocorrências fariam sentido.
4. **Audite por dimensão.** Cubra somente itens pertinentes e sustentados por evidência: keywords e intenção; title/meta/headings/URL; conteúdo e semântica; links/arquitetura; imagens; E-E-A-T; técnica/indexabilidade; experiência/performance/acessibilidade; snippet/CTR; GEO/AEO; featured snippets; e sinais linguísticos de conteúdo possivelmente automatizado.
5. **Confronte com dados externos quando disponíveis.** Se houver web, verifique a SERP atual, concorrentes e formato dominante. Se houver integrações SEO, GSC ou GA4, use valores reais com fonte, propriedade, período e filtros. Nunca fabrique volume, dificuldade, posições, tráfego, conversões ou Core Web Vitals.
6. **Priorize e reescreva.** Cada achado precisa trazer evidência, efeito provável, recomendação específica, local exato, exemplo pronto e impacto/esforço. Evite “use mais a palavra-chave”.
7. **Pontue com honestidade.** Dê notas heurísticas por dimensão, marque `N/A` onde faltam dados e informe a cobertura do diagnóstico. Falta de evidência não vale zero.
8. **Faça autocrítica antes de entregar.** Remova recomendações genéricas ou contraditórias; confira todas as contagens; identifique hipóteses; confirme que nenhuma correção induz stuffing, afirmação sem prova ou quebra de conversão/voz de marca.

## Limites que não podem ser apagados

- Densidade é um sinal descritivo, não um fator isolado nem meta universal.
- Correlação observada na SERP não prova causalidade.
- Canibalização exige comparação entre URLs e, idealmente, consultas/impressões reais; uma página isolada só permite apontar risco potencial.
- Texto colado não revela headers HTTP, renderização, recursos bloqueados, métricas de campo, comportamento mobile ou indexação real.
- Sinais de “texto de IA” não provam autoria. Descreva trechos e riscos concretos — repetição, genericidade, cadência uniforme, afirmações sem fonte — sem acusar ou usar detectores como verdade.
- Não altere fatos, promessas, preço, requisitos legais ou posicionamento de marca para melhorar SEO sem sinalizar a necessidade de validação.
