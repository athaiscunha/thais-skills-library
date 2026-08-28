# Aquisição de evidências e limites

Leia esta referência quando a entrada incluir URL/site, quando houver investigação de SERP, concorrência, canibalização, técnica ou performance, ou quando integrações externas estiverem disponíveis.

## Matriz de capacidade

| Entrada/evidência | Pode concluir | Não pode concluir sem mais dados |
|---|---|---|
| Texto colado | intenção aparente, keywords, estrutura textual visível, cobertura, legibilidade, E-E-A-T textual, GEO/AEO editorial | HTML real, metadados ausentes, status, indexação, canonical, robots, links de template, mobile, CWV, canibalização confirmada |
| HTML estático | itens acima + tags, links, imagens, structured data presente, directives no documento | DOM pós-JS, headers, indexação real, métricas de campo, SERP, site inteiro |
| URL acessível | HTML/DOM observado, URL final, elementos públicos, experiência visual disponível | ranking, volume, conversão, CWV de campo ou canibalização sem ferramentas/dados adequados |
| Conjunto/crawl de URLs | arquitetura, padrões, duplicidade, profundidade, sobreposição potencial | consultas e desempenho reais sem GSC/ferramenta SEO |
| SERP atual | formato dominante, concorrentes visíveis, features e intenção provável naquele contexto | volume/dificuldade exatos, causalidade de ranking |
| GSC/GA4/SEO suite | métricas presentes na integração e no período consultado | métricas não expostas ou propriedades/períodos não consultados |

## URL e página publicada

Quando houver web ou navegador:

1. Abra a URL informada e registre URL final, data e qualquer bloqueio.
2. Inspecione HTML-fonte e DOM renderizado quando possível. Se divergirem, indique qual versão sustenta cada achado.
3. Verifique title, meta description, canonical, robots, headings, texto, links, imagens, hreflang e JSON-LD.
4. Observe status/redirects e headers somente se a ferramenta os expuser.
5. Avalie mobile/responsividade com viewport ou captura apropriada; não presuma pelo desktop.
6. Para técnica/performance, use ferramenta real disponível e preserve o contexto do teste.

Se acesso falhar, não simule o conteúdo. Informe a falha e solicite HTML, exportação do crawler, captura, relatório Lighthouse/PageSpeed ou dados pertinentes.

## SERP e concorrentes

Se houver acesso à web e o pedido justificar:

- pesquise a keyword principal e 1–3 variações decisivas;
- defina país/idioma e, quando relevante, localidade/dispositivo;
- registre a data da verificação;
- compare tipo de página, proposta, títulos, subtópicos, entidades, formatos de resposta e features visíveis;
- use concorrentes realmente encontrados, com URL/fonte;
- explique quando a personalização/localização pode alterar resultados.

Não copie concorrentes nem transforme frequência média em regra. Use o conjunto para testar intenção, lacunas e formatos. Não invente volume, dificuldade, CPC, share of voice ou posição histórica.

## Integrações SEO, GSC e GA4

Quando disponíveis, consulte somente propriedades e dados autorizados. Registre:

- nome da fonte/ferramenta;
- propriedade/domínio;
- período e comparação;
- país, dispositivo, tipo de busca e demais filtros;
- data da extração;
- limitações de amostragem, arredondamento ou cobertura.

Use GSC para consultas, páginas, cliques, impressões, CTR, posição e indexação quando expostos. Use GA4 para comportamento/conversão somente se configuração de eventos e escopo forem conhecidos. Use ferramentas SEO para volume, dificuldade, backlinks, crawl e rankings apenas com valores retornados pela integração. Se a integração não responder, marque `requer dados`.

## Canibalização e arquitetura

O mínimo útil é uma lista de URLs e seus títulos/H1/conteúdo; o diagnóstico ganha confiança com consultas por página no GSC ou rankings por URL. Construa uma matriz:

| Consulta/tema | URL | Intenção | Impressões/ranking (se real) | Sobreposição | Ação candidata |
|---|---|---|---|---|---|

Não recomende redirecionar ou remover apenas por semelhança lexical. Confirme finalidade, tráfego, backlinks, conversões, canonical, campanhas e papel no funil.

## Core Web Vitals e performance

Distinga:

- **campo:** dados de usuários reais, normalmente agregados e no percentil 75;
- **laboratório:** execução sintética sujeita a hardware, rede e variabilidade;
- **origem x URL:** dado agregado do domínio não é o mesmo que dado da página.

Registre LCP, INP e CLS com fonte/data/contexto quando disponíveis. Para oportunidades técnicas, relacione o recurso ou etapa causal observada: imagem LCP, JS de terceiros, fonte, CSS bloqueante, long task, layout sem dimensões etc. Não converta uma captura visual em métricas inventadas.

## Evidência e citação

Mantenha um pequeno log de fontes. Para a página, cite URL e elemento. Para web, inclua links diretos. Para integrações, inclua nome e período. Diferencie claramente:

- achado comprovado;
- inferência razoável;
- hipótese para teste;
- lacuna que exige coleta.
