# Revisão crítica do teste

## Caso usado

LP fictícia de 256 palavras para “curso de enfermagem”, com title/H1/introdução genéricos, cinco repetições exatas concentradas, salto H2→H4, imagem sem alt, âncora “Saiba mais”, canonical presente e meta viewport ausente. O teste foi propositalmente limitado a HTML estático para verificar se a skill respeita lacunas de evidência.

## O que a primeira execução fez bem

- mediu cinco ocorrências exatas e distinguiu corpo, title, meta, H1, headings, primeiro parágrafo, primeiras 150 palavras e quartis;
- identificou concentração das cinco ocorrências no segundo quartil e pegada de 5,859% dos tokens;
- encontrou salto de heading, alt ausente e âncora genérica;
- preservou canonical/lang como sinais observados;
- declarou explicitamente que não mediu SERP, volume, dificuldade, indexação, CWV, canibalização ou autoria de IA.

## Falhas encontradas e correções

### 1. Viewport presente nos dados, ausente do backlog mecânico

**Falha:** `has_viewport_meta=false` aparecia no JSON, mas não gerava flag. Um auditor poderia ignorar o sinal ao ler apenas o resumo.

**Correção aplicada:** o analisador agora cria uma flag “mobile” quando a meta viewport não é observada, com linguagem condicional: é preciso confirmar a renderização antes de afirmar impacto real.

### 2. A janela de 150 palavras ocultava uma introdução genérica

**Falha:** todas as ocorrências estavam nas primeiras 150 palavras, mas nenhuma no primeiro parágrafo. Usar apenas a janela faria a abertura parecer adequada.

**Correção aplicada:** o analisador agora sinaliza separadamente a ausência no primeiro parágrafo e exige verificar se uma variação semântica inequívoca já cumpre a função antes de inserir o termo.

### 3. Risco de transformar a faixa de ocorrências em meta

**Falha potencial:** para 256 palavras, o analisador retorna 1–3 como faixa inicial. Uma saída superficial poderia recomendar “chegar a três” sem observar que o problema era concentração e baixa informação.

**Correção aplicada na auditoria:** a recomendação associa quantidade, zonas e reescrita. Ela pede 2–3 ocorrências no corpo **depois** da reconstrução — H1, introdução e no máximo um bloco central — e remove repetições em vez de apenas substituí-las. A metodologia e o JSON rotulam a faixa como `starting_band_not_target`.

### 4. Possibilidade de inventar dados acadêmicos para deixar a LP “completa”

**Falha potencial:** sugerir duração, estágio, reconhecimento ou investimento sem fonte melhoraria o texto apenas na aparência.

**Correção aplicada:** o relatório cria uma tabela de informações a coletar, responsáveis e destinos; reescritas usam `[validar]`. Nenhuma promessa foi preenchida com dados fictícios.

### 5. Score poderia sugerir auditoria técnica/sitewide completa

**Falha potencial:** uma nota global sem cobertura ocultaria a ausência de crawl, GSC, mobile e performance.

**Correção aplicada:** arquitetura/canibalização recebeu `N/A`; o total mostra cobertura de 90%, confiança por dimensão e ressalva explícita. Técnica e UX têm notas parciais com confiança baixa, baseadas somente em sinais observáveis.

### 6. Ausência de JSON-LD e meta robots poderia virar falso erro

**Falha potencial:** checklists binários frequentemente tratam qualquer tag ausente como falha.

**Correção aplicada:** ausência de JSON-LD virou oportunidade condicionada à aplicabilidade; ausência de meta robots não foi considerada bloqueio; canonical presente foi preservada. O relatório exige dados reais para indexação.

### 7. “Texto de IA” poderia virar acusação

**Falha potencial:** repetição e genericidade são compatíveis com muitas causas editoriais.

**Correção aplicada:** a auditoria cita padrões concretos e propõe condensação, prova e fonte, mas declara que não pode determinar autoria.

## Resultado após revisão

- 3 testes automatizados passaram: HTML, Markdown e aviso de limites.
- A medição final contém 8 flags de revisão, incluindo as duas adicionadas após a primeira execução.
- O relatório-modelo fecha todos os itens do contrato: escopo, evidência, backlog impacto/esforço, mapa de keywords, reescritas, score/cobertura, checklist e autocrítica.
- Nenhuma recomendação depende de volume, dificuldade, GSC/GA4, CWV ou SERP inventados.
- A skill passou no `quick_validate.py` oficial e o pacote passou no `validate_plugin.py` oficial do `plugin-creator`.
