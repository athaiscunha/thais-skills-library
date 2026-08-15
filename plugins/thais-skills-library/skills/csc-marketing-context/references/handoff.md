# Contrato de passagem

Usar este pacote ao receber contexto de outra Skill ou entregar base factual para a próxima etapa. Manter datas em `AAAA-MM-DD` e referências por identificador estável.

## Entrada mínima

- `destino`: tarefa e Skill que usarão o contexto;
- `recorte`: produto, campanha, praça, modalidade, público e data de referência aplicáveis;
- `fontes`: documento ou URL, tipo, versão/data e data de consulta;
- `fatos necessários`: alegações materiais que a tarefa seguinte precisa sustentar;
- `decisões e hipóteses`: separadas entre si, com origem e responsável quando houver;
- `restrições`: linguagem, compliance, escopo, prazo e usos proibidos;
- `conflitos e pendências`: divergências conhecidas e confirmações ainda necessárias.

## Saída mínima — `context_packet`

- `snapshot_em`: data da última verificação;
- `escopo`: onde o pacote pode ser usado;
- `fatos`: para cada item, valor, classe (`durável`, `operacional`, `temporal`, `histórico` ou `incerto`), status, referências e data de verificação;
- `voz_e_terminologia`: somente decisões aplicáveis ao recorte;
- `conflitos`: fontes divergentes, alegação de cada uma e decisão suspensa;
- `hipóteses`: inferências permitidas, sempre rotuladas e sem promoção a fato;
- `restrições_de_uso`: alegações ou aplicações que o pacote não sustenta;
- `pendências`: dado faltante, responsável ou fonte esperada e impacto na próxima etapa.

## Regras de continuidade

- Preservar fonte, data, classe e status de cada fato; não entregar alegação solta.
- Não apagar conflito porque a próxima Skill consegue avançar sem ele.
- Revalidar fato temporal no site oficial antes de publicação; o pacote registra a checagem anterior, mas não substitui a consulta atual.
- A Skill seguinte pode restringir um status, mas só pode elevá-lo após nova verificação registrada.
