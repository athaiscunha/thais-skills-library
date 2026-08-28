# Contrato do relatório

O relatório deve permitir que redator, designer, desenvolvedor e gestor executem as mudanças sem reinterpretar recomendações vagas. Reduza se o pedido for estreito, mas preserve evidência, limite e ação concreta.

## Abertura

Comece pelo veredito em 3–6 linhas:

- adequação ou inadequação à intenção;
- maior oportunidade;
- maior risco;
- limitação decisiva da análise.

Em seguida, registre:

| Campo | Conteúdo |
|---|---|
| Entrada | URL, arquivo, HTML, texto ou conjunto de páginas |
| Data e contexto | Data, idioma, país/dispositivo quando aplicável |
| Keyword principal | Informada, validada ou hipótese |
| Secundárias | Informadas, validadas ou hipóteses |
| Intenção/funil | Classificação e justificativa curta |
| Evidências disponíveis | HTML, DOM, SERP, GSC, GA4, crawler, ferramenta SEO etc. |
| Não verificado | Itens fora de alcance |

## Backlog priorizado

Ordene primeiro por impacto provável, depois por confiança e esforço. Use:

- **P0 — bloqueio:** impede rastreamento/indexação ou torna a página essencialmente inadequada à intenção;
- **P1 — alto impacto:** forte desalinhamento, ausência estrutural ou oportunidade diretamente ligada à resposta/conversão;
- **P2 — melhoria relevante:** aumenta clareza, cobertura, links, snippet ou experiência;
- **P3 — refinamento/teste:** hipótese de CTR, ajuste editorial ou experimento sem evidência suficiente para prioridade maior.

Para cada item, preencha:

| Prioridade | Achado e evidência | Por que pode afetar performance | Alteração concreta | Responsável | Impacto | Esforço | Confiança |
|---|---|---|---|---|---|---|---|

`Responsável` pode ser conteúdo, SEO, design, desenvolvimento, analytics ou produto. Impacto/esforço: alto, médio ou baixo. Confiança: alta, média ou baixa, com motivo quando não for alta.

Regras:

- Cite o elemento ou trecho. Para URL, informe a página.
- Diferencie fator direto, efeito indireto e hipótese de teste.
- Diga **onde** alterar: title, meta, H1, parágrafo 1, seção X, template, link da URL A para B etc.
- Inclua texto substituto pronto quando a mudança for editorial.
- Para mudança técnica, forneça estado atual, estado desejado e critério de aceite verificável.

## Mapa de keywords e distribuição

Use uma tabela:

| Termo/variação | Papel e intenção | Ocorrências medidas | Zonas atuais | Faixa aproximada sugerida | Ação e local exato |
|---|---|---:|---|---|---|

Explique o denominador da densidade e se a contagem inclui title, meta, headings ou somente corpo. Nunca peça repetições só para atingir a faixa. Quando a página já estiver natural, a ação pode ser “manter”.

## Auditoria por dimensão

Para cada dimensão pertinente, entregue:

1. **Estado:** adequado, atenção, crítico ou não verificável.
2. **Evidência:** observado/medido/inferido/requer dados.
3. **Leitura crítica:** implicação real, sem generalidades.
4. **Correção:** específica e proporcional.

Cubra, conforme escopo:

- intenção, keyword principal/secundárias, entidades e semântica;
- title, meta description, URL, H1–H6, início e corpo;
- cobertura, profundidade, redundância, FAQ, provas e E-E-A-T;
- links internos, âncoras, arquitetura e canibalização;
- imagens, alt text e acessibilidade pertinente;
- indexabilidade, canonical, robots, sitemap, hreflang, dados estruturados;
- mobile, performance, Core Web Vitals e renderização;
- snippet/CTR, featured snippets, GEO/AEO;
- riscos editoriais de conteúdo possivelmente automatizado.

## Bloco de reescritas

Quando houver mudanças editoriais, entregue versões prontas:

- title proposto + contagem de caracteres;
- meta description proposta + contagem de caracteres;
- H1 e hierarquia H2/H3;
- primeiro parágrafo;
- trechos problemáticos em formato `atual → proposto`;
- FAQ ou bloco de featured snippet apenas quando houver demanda real;
- âncoras e contexto de links internos.

Preserve fatos e voz da marca. Marque `[validar informação]` quando uma prova, número ou credencial for necessária e não estiver disponível.

## Scores e cobertura

Apresente nota 0–10 por dimensão, peso, confiança e justificativa curta. Use `N/A` sem penalizar o total quando não houver evidência. Mostre:

- score heurístico ponderado sobre dimensões avaliadas;
- cobertura percentual do score;
- aviso: “O score organiza o diagnóstico; não prevê ranking, tráfego ou conversão”.

## Checklist final de conformidade

Use `✅ conforme`, `⚠️ parcial`, `❌ não conforme` ou `— não verificado` para:

- intenção e funil;
- keyword principal e secundárias;
- distribuição e ausência de stuffing;
- title, meta, headings, URL, introdução e corpo;
- entidades e cobertura temática;
- conteúdo útil, não raso/redundante;
- E-E-A-T e verificabilidade;
- links internos, âncoras, arquitetura e canibalização;
- imagens e alt text;
- dados estruturados;
- indexabilidade, canonical, robots, sitemap, hreflang;
- mobile, performance e Core Web Vitals;
- acessibilidade relevante;
- snippet/CTR;
- GEO/AEO e featured snippets;
- riscos editoriais de conteúdo possivelmente automatizado.

## Autorrevisão obrigatória

Antes de finalizar, responda internamente:

- Todas as afirmações factuais vêm da entrada ou de fonte identificada?
- Algum item marcado como erro depende de dados ausentes?
- Contagens e denominadores conferem?
- A recomendação de keywords diz termo, quantidade aproximada, zona e variação?
- As reescritas preservam intenção, fatos e conversão?
- Há recomendações contraditórias entre SEO, UX, acessibilidade e marca?
- O backlog separa bloqueios de refinamentos?
- `N/A` foi usado em vez de zero para dimensões sem dados?
- O score está explicitamente descrito como heurístico e mostra cobertura?
- Um profissional consegue executar cada item sem pedir “o que exatamente devo mudar?”

Se qualquer resposta for “não”, revise antes de entregar.
