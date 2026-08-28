# Auditoria-modelo — LP de Curso de Enfermagem

## Veredito

A LP é topicamente compatível com uma intenção comercial/transacional por formação em Enfermagem, mas não confirma tema e oferta nas zonas mais decisivas: o title, o H1 e o primeiro parágrafo são genéricos. Ao mesmo tempo, a expressão exata “curso de enfermagem” aparece cinco vezes em um único trecho, acima da faixa editorial inicial de 1–3 menções para as 256 palavras medidas. O problema, portanto, não é simplesmente falta ou excesso: é **distribuição artificial com baixa precisão informativa**.

A maior oportunidade é reconstruir a promessa e a cobertura para responder às decisões reais do candidato — duração, modalidade/local, turnos, matriz, práticas/estágios, formas de ingresso e investimento — sem inventar nenhum dado. O maior risco técnico observável é a ausência de meta viewport; indexação real, performance, mobile renderizado, SERP e canibalização não foram verificados.

## Escopo e evidências

| Campo | Conteúdo |
|---|---|
| Entrada | HTML estático de uma LP fictícia: `tests/fixtures/example-lp.html` |
| Data e contexto | 28/08/2026; pt-BR; URL-base fictícia `.example` |
| Keyword principal | “curso de enfermagem”, fornecida no teste; adequação à SERP não validada |
| Secundárias | “graduação em enfermagem” e “faculdade de enfermagem”, fornecidas no teste; a segunda exige validação de intenção |
| Intenção/funil | Inferido: investigação comercial com saída transacional — conhecer a formação e solicitar informações/inscrição |
| Evidências disponíveis | HTML estático e medições do analisador local |
| Não verificado | SERP, concorrentes, volume, dificuldade, ranking, GSC/GA4, headers HTTP, DOM pós-JS, indexação real, robots.txt, sitemap, hreflang recíproco, mobile renderizado, Core Web Vitals, backlinks, site inteiro e canibalização |

As contagens de keyword usam o conteúdo visível do elemento `<main>` — headings incluídos, title e meta excluídos. “Densidade” abaixo significa ocorrências exatas por 100 palavras do corpo; a pegada de tokens indica quantos tokens do corpo pertencem à expressão exata. Nenhuma das duas é tratada como meta de ranking.

## Backlog priorizado

Não há P0 confirmado: o HTML não mostra um bloqueio inequívoco de indexação, e o acesso necessário para confirmar rastreamento/indexação não faz parte do teste.

| Prioridade | Achado e evidência | Por que pode afetar performance | Alteração concreta | Responsável | Impacto | Esforço | Confiança |
|---|---|---|---|---|---|---|---|
| P1 | **Observado:** title “Seu futuro começa aqui”, H1 “Transforme sua vocação…” e primeiro parágrafo não nomeiam o curso. | A pessoa e o mecanismo de busca demoram a confirmar tema, oferta e correspondência com a consulta; a promessa também não diferencia a página. | Substituir title, H1 e primeiro parágrafo pelas versões prontas deste relatório. | Conteúdo + SEO | Alto | Baixo | Alta para clareza; média para impacto orgânico sem SERP/GSC |
| P1 | **Medido:** 5 ocorrências exatas de “curso de enfermagem” nas 256 palavras; todas no 2º quartil, quatro no mesmo parágrafo; pegada de 5,859% dos tokens. | A repetição reduz fluidez e não amplia cobertura. Pode transmitir otimização artificial, enquanto as zonas de abertura permanecem genéricas. | Reduzir o bloco repetitivo; manter 2–3 ocorrências exatas no corpo total após a revisão: H1, introdução e, se natural, um heading/bloco central. Variar com “graduação em Enfermagem”, “formação” e “o curso” conforme o referente. | Conteúdo + SEO | Alto | Baixo | Alta |
| P1 | **Observado/inferido:** a LP promete uma “formação completa”, mas não informa duração, modalidade/local, turnos, matriz detalhada, práticas/estágios, formas de ingresso, investimento ou reconhecimento. | Falta informação de decisão e prova para a intenção comercial; o lead precisa converter antes de entender a oferta. Conteúdo raso também limita cobertura temática e citabilidade. | Criar um bloco factual com os campos listados em “Informações a coletar”. Publicar somente após validação institucional. | Produto acadêmico + Conteúdo | Alto | Médio | Alta para utilidade; efeito orgânico depende da demanda real |
| P1 | **Observado:** meta viewport ausente no HTML. | Pode fazer o layout usar uma largura de viewport inadequada em mobile. Não é possível confirmar o efeito visual sem renderização. | Adicionar `<meta name="viewport" content="width=device-width, initial-scale=1">` no `<head>` e validar em viewports móveis reais. | Desenvolvimento | Alto | Baixo | Alta sobre a ausência; média sobre o efeito sem renderização |
| P2 | **Observado:** salto de H2 para H4 em “O que você aprende”. | A hierarquia sugere uma dependência inexistente e pode prejudicar escaneabilidade e navegação assistiva. | Alterar o H4 para H2 ou H3 conforme o agrupamento final; a arquitetura proposta usa H2. | Conteúdo + Desenvolvimento | Médio | Baixo | Alta |
| P2 | **Observado:** imagem do laboratório sem atributo `alt`, `width` ou `height`. | O conteúdo/função não é comunicado a leitores de tela; dimensões ausentes podem contribuir para deslocamento de layout, embora CLS não tenha sido medido. | Se informativa, usar alt contextual após confirmar a cena; exemplo: `alt="Estudantes em atividade prática no laboratório de Enfermagem"`. Informar dimensões intrínsecas. Se decorativa, usar `alt=""`. | Conteúdo + Desenvolvimento | Médio | Baixo | Alta para o atributo; média para o texto sem ver a imagem |
| P2 | **Observado:** âncora “Saiba mais” aponta para `/infraestrutura`. | A âncora não antecipa o destino; o contexto ajuda, mas há alternativa mais clara para navegação e compreensão. | Trocar por “Conheça os laboratórios e espaços de prática”, preservando o destino após confirmar que a página cobre isso. | Conteúdo | Médio | Baixo | Alta |
| P2 | **Observado/inferido:** title e meta são genéricos; a meta tem 88 caracteres e não apresenta oferta, diferencial ou próximo passo. | Perde-se uma oportunidade editorial de aumentar a correspondência percebida e o clique; a meta pode ser reescrita pelo buscador. | Aplicar title/meta propostos e testar CTR somente com GSC e período suficiente. | SEO + Conteúdo | Médio | Baixo | Alta para clareza; baixa/média para ganho de CTR sem dado real |
| P2 | **Observado:** não há perguntas respondidas, bloco comparável, autoria/revisão acadêmica ou fontes. | A página oferece poucos trechos autocontidos para featured snippets, AEO/GEO e poucas provas observáveis de experiência/confiabilidade. | Adicionar respostas factuais curtas, matriz/estrutura consultável, responsável pelo conteúdo e fontes institucionais. FAQ apenas com dúvidas reais e respostas publicáveis. | Conteúdo + Produto acadêmico | Médio | Médio | Média |
| P3 | **Observado:** não há JSON-LD. | A ausência não é erro por si só; pode existir oportunidade de descrever entidade e navegação de forma consistente. | Depois de fechar conteúdo/template, avaliar `Organization`, `BreadcrumbList` e `Course` quando os dados visíveis sustentarem o markup; validar e não prometer rich result. | SEO técnico + Desenvolvimento | Baixo/médio | Médio | Média/baixa sem contexto do site |

## Mapa de keywords e distribuição

| Termo/variação | Papel e intenção | Ocorrências medidas | Zonas atuais | Faixa aproximada sugerida | Ação e local exato |
|---|---|---:|---|---|---|
| curso de enfermagem | Principal, hipótese comercial/transacional | 5 no corpo; 1,953 ocorrência/100 palavras; pegada de tokens 5,859% | title 0; meta 0; H1 0; H2–H6 1; primeiro parágrafo 0; primeiras 150 palavras 5; quartis `[0,5,0,0]`; slug exato 0 | 1–3 no corpo de 256 palavras como ponto de partida, não quota | Após reescrever, usar no H1, uma vez na introdução e opcionalmente em um heading/bloco central. Remover três repetições do parágrafo atual. Usar uma vez no title e uma vez na meta fora da contagem do corpo. |
| graduação em enfermagem | Secundária, variação natural e possivelmente mais precisa sobre o tipo de formação | 0 | ausente em todas as zonas medidas | 1–2, se a oferta for de graduação e a SERP/terminologia institucional confirmarem | Usar em “Como funciona a graduação em Enfermagem” e uma vez no corpo; não duplicar no mesmo parágrafo. |
| faculdade de enfermagem | Secundária proposta, mas semanticamente ambígua: pode significar escola/unidade, não o curso | 0 | ausente | 0 até validação | Não inserir por enquanto. Validar intenção na SERP e nomenclatura institucional; se a instituição não tiver uma “Faculdade de Enfermagem” como entidade, descartar. |
| Enfermagem / formação em Enfermagem / o curso | Variações e referentes naturais | não calculadas como termo exato | “Enfermagem” aparece; demais exigem leitura contextual | Sem quota | Alternar apenas quando o referente permanecer claro; priorizar expansão informativa, não troca mecânica de palavras. |

### Diagnóstico de stuffing

Não há diagnóstico por densidade isolada. Há, porém, um **sinal editorial forte de repetição artificial**: as cinco ocorrências exatas estão no mesmo quartil e quatro compõem uma sequência de frases com estrutura quase idêntica. A correção indicada é condensar e redistribuir, não trocar cada repetição por um sinônimo.

## Auditoria por dimensão

### 1. Intenção, funil e estratégia de keywords — atenção

**Inferido:** a página pretende captar pessoas que avaliam uma graduação e querem informações para ingresso. O formulário confirma fundo/meio de funil comercial. A keyword principal é plausível, mas não foi validada contra a SERP brasileira atual; “faculdade de enfermagem” pode representar outra entidade/intenção.

**Correção:** confirmar a consulta principal e suas variações na SERP e, se houver integração, em GSC/SEO suite. Manter a LP orientada à escolha/ingresso; dúvidas amplamente informacionais podem virar conteúdo de apoio com links internos.

### 2. Title, meta, URL, headings, introdução e corpo — crítico

**Observado:** o title e o H1 cabem em faixas usuais de tamanho, mas são semanticamente genéricos. A meta description tem 88 caracteres e poderia descrever qualquer curso. O slug `/cursos/enfermagem` é curto, estável e contém a entidade central; não precisa repetir a frase completa “curso de enfermagem”. A hierarquia tem H1 → H2 → H4.

**Correção:** aplicar as versões prontas; manter o slug; reorganizar H2s; explicar a oferta imediatamente.

### 3. Cobertura, profundidade, E-E-A-T e conteúdo raso — crítico

**Observado:** termos como “completa”, “essenciais”, “importantes”, “transformadora”, “única”, “moderno”, “inovador” e “diferenciada” não vêm acompanhados de critério, dado ou exemplo. O texto nomeia áreas de estudo, mas não fornece a informação necessária para comparar ou decidir.

**Correção:** substituir adjetivos por detalhes verificáveis: duração, carga/estrutura, modalidades, locais, práticas, estágios, laboratórios, corpo docente, reconhecimento, processo seletivo, bolsas/investimento e canais de atendimento. Para E-E-A-T, identificar responsável/revisor acadêmico, data de atualização e fontes oficiais; não inventar credenciais nem selos.

### 4. Arquitetura, links e canibalização — parcialmente observável

**Observado:** há links para cursos, inscrição, infraestrutura e privacidade; uma âncora é genérica. **Requer dados:** profundidade, páginas órfãs, links de entrada, conflitos entre páginas de curso e possíveis artigos sobre Enfermagem.

**Correção:** trocar a âncora; em um crawl/site map, verificar links de páginas institucionais e conteúdos informacionais para esta LP. Para canibalização, comparar consultas e URLs no GSC antes de consolidar ou redirecionar qualquer página.

### 5. Imagens e acessibilidade — atenção

**Observado:** a imagem não tem `alt`, largura ou altura. O formulário de exemplo associa `label` e `input` por `for/id`, um sinal positivo. Contraste, teclado, foco, mensagens de erro e imagem real não foram testados.

**Correção:** definir função/alt após inspecionar a imagem, incluir dimensões, testar formulário e CTA por teclado e leitor de tela. Não alegar que todas essas falhas são fatores diretos de ranking; o impacto mais claro é experiência e compreensão.

### 6. Técnica, indexabilidade, mobile e performance — evidência limitada

**Observado:** `lang="pt-BR"` e canonical absoluta coerente com a URL-base; não há meta viewport. Não há meta robots, o que por si só não bloqueia indexação. **Requer dados:** status, X-Robots-Tag, robots.txt, sitemap, canonical escolhida pelo buscador, renderização JS, hreflang, indexação, LCP/INP/CLS, recursos e comportamento mobile.

**Correção:** adicionar viewport e validar. Coletar inspeção de URL/GSC ou crawler para indexabilidade; PageSpeed/Lighthouse e dados de campo para performance. Não estimar CWV a partir do HTML.

### 7. Snippet, CTR, featured snippets, GEO e AEO — crítico

**Observado:** title/meta não especificam o curso; headings não estruturam perguntas/decisões; não há respostas diretas, tabela factual, fontes ou data. **Inferido:** isso reduz a capacidade de extração e citação, mas não prova baixa visibilidade em IA.

**Correção:** criar blocos autocontidos com informações validadas, headings de decisão e uma síntese factual. Pesquisar a SERP antes de escolher formato de featured snippet. Não adicionar FAQ ou JSON-LD em massa apenas “para IA”.

### 8. Risco editorial associado a conteúdo automatizado — atenção, sem atribuição

**Observado:** abertura ampla (“O mercado muda todos os dias”), sequência repetitiva (“O curso de enfermagem…”) e adjetivos sem prova produzem genericidade e cadência mecânica. Isso não prova autoria por IA.

**Correção:** cortar a abertura, consolidar o bloco repetitivo, trocar adjetivos por fatos, exemplos e fonte/responsável. Não usar detector de IA como veredito.

## Reescritas prontas

### Title

`Curso de Enfermagem | Faculdade Horizonte` — 41 caracteres.

### Meta description

`Conheça o curso de Enfermagem da Faculdade Horizonte, veja formação, práticas e estrutura e receba informações sobre ingresso e investimento.` — 141 caracteres.

### H1

`Curso de Enfermagem: formação para cuidar com competência` — 57 caracteres.

### Primeiro parágrafo

`O curso de Enfermagem da Faculdade Horizonte reúne fundamentos biológicos, práticas de cuidado, ética e trabalho em equipe. Conheça a formação, veja como funcionam as atividades práticas e solicite informações sobre duração, horários, investimento e processo seletivo.`

Essa versão confirma tema e próximo passo, mas só deve permanecer se todos os itens citados forem efetivamente apresentados na página ou no atendimento.

### Parágrafo repetitivo

**Atual:** “O curso de enfermagem oferece uma formação completa […] No curso de enfermagem […] Nosso curso de enfermagem […] O curso de enfermagem prepara você […]”.

**Proposto:** `Na graduação em Enfermagem, você estuda fundamentos biológicos, saúde coletiva, ética, gestão e práticas de cuidado. Ao longo da formação, atividades teóricas e práticas desenvolvem tomada de decisão, comunicação e trabalho em equipe. Consulte abaixo a matriz curricular, os espaços de aprendizagem e as informações de ingresso.`

### Hierarquia sugerida

- H1 — Curso de Enfermagem: formação para cuidar com competência
- H2 — Como funciona a graduação em Enfermagem
- H2 — O que você aprende
- H2 — Onde acontecem as atividades práticas
- H2 — Duração, horários e investimento
- H2 — Como ingressar no curso
- H2 — Dúvidas frequentes sobre o curso

### Âncora interna

Substituir `Saiba mais` por `Conheça os laboratórios e espaços de prática`, se a página de destino realmente cobrir esses elementos.

### Bloco curto para AEO/GEO

`O curso de Enfermagem é uma graduação voltada à formação de profissionais para o cuidado em saúde. Na Faculdade Horizonte, a formação inclui [validar componentes], tem duração de [validar] e é oferecida em [validar modalidade, local e turnos].`

O bloco só deve ser publicado depois de preencher e validar os campos; não pode virar uma resposta genérica ou uma alegação sem fonte.

### FAQs candidatas

Publicar somente após obter respostas oficiais e confirmar demanda:

- Quanto tempo dura o curso de Enfermagem?
- Em quais turnos e locais o curso é oferecido?
- Como funcionam as atividades práticas e os estágios?
- Quais são as formas de ingresso?
- Onde consultar investimento, bolsas e financiamento?

## Informações a coletar antes da publicação

| Informação | Fonte/validação necessária | Destino na página |
|---|---|---|
| Duração, carga e periodicidade | Coordenação/registro acadêmico | bloco-resumo e FAQ |
| Modalidade, campus e turnos | Oferta vigente | hero/bloco-resumo |
| Matriz curricular | Documento oficial atualizado | seção “O que você aprende” |
| Práticas, laboratórios e estágios | Coordenação + equipe responsável | seções específicas e alt/captions de imagens |
| Reconhecimento/autorização | Fonte institucional/oficial | bloco de confiança, sem extrapolar |
| Corpo docente e responsáveis | RH/coordenação e consentimentos | E-E-A-T/autoria/revisão |
| Processo seletivo | Edital/página vigente | “Como ingressar” + CTA |
| Investimento, bolsas e financiamento | Comercial/financeiro + regras vigentes | bloco de decisão e FAQ |
| Data de atualização e responsável editorial | Governança de conteúdo | rodapé editorial |

## Scores heurísticos

| Dimensão | Peso | Nota | Confiança | Justificativa |
|---|---:|---:|---|---|
| Intenção e estratégia de keywords | 15 | 4/10 | Média | intenção plausível, mas não validada na SERP; mapa atual concentra a principal e não trabalha secundárias |
| Semântica on-page e metadados | 15 | 4/10 | Alta | title/H1/introdução genéricos; slug adequado; hierarquia tem salto |
| Qualidade, cobertura e E-E-A-T | 15 | 3/10 | Alta | conteúdo raso, provas e informações decisivas ausentes |
| Arquitetura, links e canibalização | 10 | N/A | — | uma LP isolada não sustenta score do site/canibalização; apenas a âncora foi auditada |
| Técnica e indexabilidade | 15 | 5/10 | Baixa | canonical/lang presentes e viewport ausente; indexação real, headers e crawl não verificados |
| UX, mobile, performance e acessibilidade | 10 | 4/10 | Baixa | sinais observáveis de viewport/alt; CWV, mobile visual, teclado e contraste não testados |
| Snippet, CTR, GEO/AEO e formatos de resposta | 10 | 3/10 | Média | snippet genérico e baixa extraibilidade; SERP/CTR reais ausentes |
| Clareza, legibilidade e conversão | 10 | 4/10 | Alta | CTA existe, mas a decisão é solicitada antes de a oferta ser explicada |

**Score heurístico ponderado:** 39/100 sobre as dimensões avaliadas. **Cobertura:** 90% dos pesos; três dimensões têm confiança baixa por falta de dados externos/visuais. O score organiza o diagnóstico; não prevê ranking, tráfego ou conversão.

## Checklist final de conformidade

| Item | Estado | Nota curta |
|---|---|---|
| Intenção e funil | ⚠️ parcial | coerência provável, sem SERP/dados reais |
| Keyword principal e secundárias | ❌ não conforme | principal mal distribuída; secundárias ausentes/uma ambígua |
| Distribuição e ausência de stuffing | ❌ não conforme | concentração e repetição textual; diagnóstico contextual, não por densidade isolada |
| Title, meta, headings, URL, introdução e corpo | ❌ não conforme | slug adequado; demais exigem revisão substancial |
| Entidades e cobertura temática | ❌ não conforme | informações de decisão ausentes |
| Conteúdo útil, não raso/redundante | ❌ não conforme | repetição e adjetivos sem prova |
| E-E-A-T e verificabilidade | ❌ não conforme | autoria/revisão/fontes/provas ausentes |
| Links internos e âncoras | ⚠️ parcial | links existem; uma âncora genérica |
| Arquitetura e canibalização | — não verificado | requer site/crawl/GSC |
| Imagens e alt text | ❌ não conforme | imagem sem alt e dimensões |
| Dados estruturados | — não verificado | ausência observada; aplicabilidade depende do template/conteúdo |
| Indexabilidade, canonical e robots | ⚠️ parcial | canonical presente; indexação/headers/robots.txt não verificados |
| Sitemap e hreflang | — não verificado | fora do HTML/escopo |
| Mobile | ❌ não conforme no sinal observado | viewport ausente; layout não renderizado |
| Performance e Core Web Vitals | — não verificado | requer ferramenta/dados reais |
| Acessibilidade relevante | ⚠️ parcial | label do formulário presente; alt ausente; testes completos não realizados |
| Snippet/CTR | ❌ não conforme editorialmente | title/meta genéricos; CTR real ausente |
| GEO/AEO e featured snippets | ❌ não conforme | faltam respostas diretas, fatos, fonte e estrutura |
| Riscos editoriais de conteúdo possivelmente automatizado | ⚠️ parcial | genericidade e cadência mecânica; sem atribuir autoria |

## Autorrevisão aplicada

- Contagens conferidas contra `example-measurements.json`.
- Nenhum dado de volume, dificuldade, ranking, tráfego, CTR, conversão ou CWV foi criado.
- Itens sem evidência foram marcados como não verificados ou receberam confiança baixa.
- A faixa de 1–3 ocorrências foi usada como ponto de partida editorial, não como quota.
- A recomendação de keyword informa quantidade aproximada, zonas e variações.
- Fatos do curso ausentes foram convertidos em campos `[validar]`, não em alegações.
- Ausência de JSON-LD, meta robots ou keyword completa no slug não foi tratada automaticamente como erro.
- O risco de conteúdo automatizado foi descrito por trechos e efeitos, sem alegar autoria.
