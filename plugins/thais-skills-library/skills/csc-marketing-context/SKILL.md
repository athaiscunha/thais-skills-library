---
name: csc-marketing-context
description: Organiza, consulta e audita o contexto institucional e de marketing da Católica SC a partir de documentos fornecidos e do site oficial catolicasc.org.br, com rastreabilidade, classificação temporal e tratamento de conflitos. Use antes de criar ou revisar materiais da Católica SC, ao consolidar briefings e documentos, ao responder dúvidas sobre marca, públicos, produtos, diferenciais ou terminologia e ao atualizar a base de contexto compartilhada. Não use como substituto da página atual do produto, para inventar fatos ausentes, para conectar ferramentas externas ou para alterar documentos sem solicitação explícita.
---

# Contexto de Marketing | Católica SC

## Objetivo

Construir uma base factual rastreável para trabalhos da Católica SC. Combinar documentos fornecidos com consulta obrigatória ao site oficial, distinguir o que é durável do que muda e impedir que informação antiga vire verdade permanente.

Não conectar APIs, plataformas de marketing, crawlers, bancos de dados ou serviços externos. Trabalhar com os documentos colocados no escopo, com a conversa atual e com páginas públicas de `catolicasc.org.br` acessadas durante a tarefa.

## Carregar referências

Ler sempre:

- `references/source-policy.md` para regras de fonte, temporalidade e conflito;
- `references/voice-terminology.md` para nome, voz e nomenclatura.

Ler conforme a tarefa:

- contexto institucional: `references/institutional.md`;
- produtos e rotas oficiais: `references/products.md`;
- públicos, evidências de público ou personas: `references/audiences.md`;
- diferenciais, números, depoimentos ou outras provas: `references/proof-points.md`;
- entrada ou saída para outra Skill: `references/handoff.md`;
- revisão da Skill ou teste do método: `references/acceptance-tests.md`.

Usar essas referências como orientação durável e mapa de verificação. Nunca usá-las para dispensar a consulta atual ao site.

## Fluxo obrigatório

### 1. Definir o recorte

Identificar:

- tarefa e material que será produzido;
- produto, campanha, praça, modalidade e público envolvidos;
- documentos e links fornecidos;
- fatos materiais necessários;
- data de referência do pedido.

Tratar como fatos materiais, entre outros, nome de produto, modalidade, carga horária, campus ou unidade, calendário, professores, valor, desconto, regra, vigência, CTA, credenciamento, número institucional e prova quantitativa.

### 2. Ler os documentos

Extrair de cada documento:

- título ou nome do arquivo;
- data, versão e responsável, quando disponíveis;
- finalidade e campanha;
- fatos, decisões, linguagem e pendências;
- sinais de que o material é histórico, preliminar ou substituído.

Não presumir que o arquivo mais recente é o vigente sem evidência. Não pedir novamente informação que já esteja clara em documento atual.

### 3. Consultar o site oficial em toda tarefa

Antes da entrega final, consultar a página oficial mais específica e relevante em `catolicasc.org.br`, mesmo quando os documentos parecerem completos.

- Começar pela página do produto, curso, campanha ou assunto.
- Consultar página institucional, FAQ, edital ou ato quando a alegação exigir.
- Registrar internamente URL e data da consulta.
- Comparar os fatos materiais do documento com o conteúdo público atual.
- Não considerar snippet de busca, cache, blog antigo ou página agregadora como substituto da página atual.
- Não rastrear o site inteiro quando páginas específicas bastarem.

Quando a página relevante estiver fora de `catolicasc.org.br` por encaminhamento do próprio site, tratá-la como fonte complementar e registrar o domínio. Manter `catolicasc.org.br` como ponto obrigatório de partida.

Se o site não puder ser consultado, continuar somente quando houver caminho seguro, marcar o resultado como rascunho sem validação de atualidade e não afirmar que os dados estão atualizados.

### 4. Classificar cada fato

Usar uma destas classes:

- `durável`: identidade, princípio de voz ou nomenclatura com baixa chance de mudança;
- `operacional`: regra interna ou orientação de campanha válida no contexto informado;
- `temporal`: curso, modalidade, professor, turma, data, preço, desconto, edital, número ou CTA sujeito a mudança;
- `histórico`: fato sobre período encerrado ou material anterior;
- `incerto`: informação sem fonte suficiente, com conflito ou sem vigência confirmada.

Mesmo fatos duráveis podem ser revistos. Não registrar fato temporal como regra permanente da Skill.

### 5. Resolver divergências

Aplicar `references/source-policy.md`. Não decidir conflito silenciosamente.

- Separar o dado conflitante do restante do trabalho.
- Informar quais fontes divergem, o que cada uma afirma e quando foram consultadas.
- Priorizar a fonte mais específica, vigente e autorizada para aquele tipo de fato.
- Em informação pública material, exigir reconciliação quando documento vigente e site oficial divergem.
- Avançar com os fatos não conflitantes quando isso não criar risco.

Não preencher lacuna com memória, concorrente, inferência apresentada como fato ou material histórico.

### 6. Entregar contexto utilizável

Na ausência de formato pedido, entregar apenas o necessário em quatro blocos:

1. `Contexto confirmado`: síntese orientada à tarefa.
2. `Fontes consultadas`: documento ou página, versão ou data, URL quando houver.
3. `Fatos temporais`: itens que precisam de nova checagem antes de reutilização.
4. `Conflitos ou lacunas`: somente decisões que exigem atenção.

Quando a tarefa pedir uma matriz, usar:

| Fato | Valor | Fonte | Consulta/versão | Classe | Status |
|---|---|---|---|---|---|
| exemplo | valor confirmado | documento ou URL | data | temporal | confirmado, conflitante ou ausente |

Não sobrecarregar uma entrega criativa com o registro completo de fontes. Preservar o registro internamente e expor somente conflitos, limitações ou fontes quando forem úteis ou solicitados.

## Atualizar a base compartilhada

Alterar arquivos de contexto somente quando a usuária pedir atualização. Antes de gravar:

1. comparar com documentos e site atual;
2. remover ou isolar fatos temporais;
3. preservar a fonte e a data;
4. registrar conflitos sem apagá-los por conveniência;
5. manter linguagem factual e curta.

Uma tarefa de consulta não autoriza edição de documentos, repositório ou páginas.
