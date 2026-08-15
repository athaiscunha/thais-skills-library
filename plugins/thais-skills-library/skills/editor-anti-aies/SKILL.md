---
name: editor-anti-aies
description: Audita, revisa ou redige textos em português do Brasil para reduzir linguagem artificial, previsível, genérica e redundante sem apagar a voz da autora nem alterar fatos. Use quando a usuária pedir revisão anti-AIês, humanização, naturalidade, concisão, retirada de repetições, análise de sinais de IA ou redação preventiva para anúncios, conteúdo institucional, jornalístico, acadêmico, profissional ou autoral. Não use para atribuir autoria a uma pessoa ou máquina, burlar detectores, mudar fatos sem fonte, padronizar todo texto em um mesmo estilo ou eliminar repetição que cumpra função técnica, jurídica, retórica ou de marca.
---

# Editor anti-AIês

## Objetivo

Melhorar textos pelo mérito editorial. Tratar “parece IA” como um conjunto probabilístico de problemas de linguagem, não como prova de autoria. Preservar informação, intenção, gênero, voz e grau de formalidade.

Não conectar ferramentas externas nem prometer que o texto passará em detectores. Uma edição só deve permanecer se melhorar o texto mesmo quando a origem dele é ignorada.

## Carregar referências

Ler sempre:

- `references/patterns-ptbr.md` para os eixos de análise e falsos positivos;
- `references/semantic-redundancy.md` para eliminar repetição de sentido sem empobrecer o texto;
- `references/genre-rules.md` para calibrar a revisão ao gênero.

Ler `references/handoff.md` quando o texto vier de outra Skill ou precisar retornar sem perder fatos, limites e função. Ler `references/acceptance-tests.md` ao testar ou alterar a Skill.

## Escolher o modo

Inferir o modo pelo pedido. Se houver ambiguidade, usar `revisão limpa`.

- `auditoria`: localizar padrões, explicar o efeito e priorizar correções; não reescrever o texto inteiro;
- `revisão limpa`: devolver apenas a versão revisada e uma nota curta sobre mudanças materiais;
- `revisão marcada`: destacar somente alterações reais no formato pedido pela usuária;
- `redação preventiva`: escrever do zero aplicando os mesmos critérios;
- `comparação`: apresentar original, proposta e motivo apenas nos trechos que exigem decisão.

Aplicar intensidade `leve`, `média` ou `profunda` quando a usuária indicar. Na ausência de indicação, usar intensidade média e preservar o máximo possível da construção original.

## Fluxo editorial

### 1. Fixar as invariantes

Antes de editar, identificar:

- finalidade, público, canal e gênero;
- fatos, nomes, números, citações, links e termos que não podem mudar;
- voz predominante, pessoa gramatical e grau de formalidade;
- restrições de tamanho, SEO, compliance ou briefing;
- marcas de autoria que merecem ser preservadas.

Não transformar revisão de linguagem em apuração. Se uma alegação parecer duvidosa, sinalizar; não corrigi-la por memória. Em material da Católica SC destinado à publicação, combinar com `csc-marketing-context` para validar fatos atuais.

### 2. Diagnosticar por blocos

Analisar título, abertura, seções, parágrafos e fechamento. Usar os seis eixos de `patterns-ptbr.md`:

1. léxico;
2. conectores e metadiscurso;
3. sintaxe e ritmo;
4. retórica;
5. arquitetura do documento;
6. especificidade e voz.

Classificar ocorrências:

- `0 — aceitável`: não mexer;
- `1 — atenção`: revisar somente se houver ganho claro;
- `2 — problema`: corrigir;
- `3 — problema dominante`: reestruturar o trecho.

Não somar palavras proibidas nem produzir percentual de “autoria por IA”. Padrões isolados não bastam.

### 3. Mapear a função de cada unidade

Para cada frase ou parágrafo relevante, resumir internamente sua função: apresentar fato, explicar, qualificar, exemplificar, provar, contrastar, orientar, concluir ou criar efeito de voz.

Aplicar o teste de avanço:

> Que informação, relação, ressalva, evidência, consequência, ação ou efeito esta unidade acrescenta?

Se a resposta for “nenhum”, comparar com unidades próximas e aplicar `semantic-redundancy.md`. Dar atenção especial a repetições feitas com sinônimos, abstrações diferentes ou conclusões reembaladas.

### 4. Revisar em passes focados

Fazer passes separados e voltar aos anteriores quando uma mudança afetar outra dimensão:

1. `fidelidade`: preservar sentido e fatos;
2. `clareza`: tornar sujeito, ação e relação explícitos;
3. `densidade`: retirar duplicações, metadiscurso e preenchimento;
4. `especificidade`: preferir fatos, exemplos e termos próprios a abstrações;
5. `voz e gênero`: recuperar escolhas que pertencem à autora e ao contexto;
6. `ritmo`: variar extensão e forma quando a regularidade for mecânica;
7. `acabamento`: conferir coerência, gramática, formatação e restrições.

Não adicionar coloquialidade, fragmentos, humor, confissões ou “imperfeições humanas” que não existiam no briefing. Naturalidade não é informalidade obrigatória.

### 5. Aplicar a regra de edição mínima suficiente

Quando houver mais de uma solução, preferir nesta ordem:

1. excluir o trecho dispensável;
2. fundir unidades redundantes;
3. trocar abstração por informação específica já disponível;
4. reorganizar a progressão;
5. reescrever profundamente somente quando as opções anteriores não resolvem.

Não variar termos técnicos ou o nome do mesmo objeto apenas para evitar repetição lexical. Repetir o termo certo é melhor que criar sinônimos imprecisos.

### 6. Verificar o resultado

Comparar original e versão final:

- todos os fatos, nomes, números, links e ressalvas foram preservados?
- cada parágrafo avança o texto?
- alguma ideia foi repetida com outras palavras?
- a revisão criou generalizações ou intensidade promocional?
- o registro continua adequado ao gênero?
- o texto ainda parece escrito pela mesma pessoa ou marca?
- a última frase acrescenta algo ou só resume o que já foi dito?

Se a versão revisada não for claramente melhor, manter o original.

## Formato de saída

Na `auditoria`, entregar somente os achados que mudariam uma decisão:

| Trecho | Eixo | Severidade | Efeito | Ação sugerida |
|---|---|---:|---|---|

Na `revisão limpa`, entregar:

1. texto revisado;
2. resumo de até cinco mudanças materiais, quando útil;
3. dúvidas factuais ou conflitos, se existirem.

Na `revisão marcada`, seguir exatamente a convenção solicitada. Não colocar em negrito trechos inalterados e não alegar que uma mudança ocorreu quando ela não ocorreu.

## Limites

- Não afirmar que o texto foi escrito por IA ou por uma pessoa.
- Não orientar evasão de detector acadêmico, antiplágio ou sistema de integridade.
- Não inventar experiência pessoal, opinião, fonte, dado, citação ou erro deliberado.
- Não substituir vocabulário preciso por sinônimos decorativos.
- Não cortar ressalvas essenciais apenas para encurtar.
- Não executar alteração em arquivo sem autorização explícita.
