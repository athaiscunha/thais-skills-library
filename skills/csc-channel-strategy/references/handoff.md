# Contrato de passagem

Usar este pacote para transformar contexto em decisões de canal e encaminhar briefs executáveis sem escrever as peças finais.

## Entrada mínima

- `problema`: objetivo institucional ou de marketing, objetivo de comunicação e período;
- `públicos`: recortes e tarefas ou tensões sustentadas pelas fontes;
- `context_packet`: fatos, fontes, datas, classes temporais, status e conflitos;
- `estado_atual`: canais, editorias, campanhas e decisões já aprovadas;
- `capacidade`: pessoas, acervo, captação, design, aprovação, verba e prazos disponíveis;
- `evidências`: sinais de desempenho com período e limites de comparabilidade;
- `restrições`: legais, reputacionais, operacionais e decisões de não fazer;
- `hipóteses_e_pendências`: suposições de planejamento e escolhas ainda abertas.

## Saída mínima — `channel_strategy_packet`

- `snapshot_em`: data do contexto e das regras de plataforma consultadas;
- `decisão_estratégica`: problema, objetivo, público e princípio orientador;
- `papéis_dos_canais`: função, conteúdo nativo, ação, dependências e critério de decisão;
- `sistema_editorial`: pilares e editorias com promessa, ponto de vista, matéria-prima e limites;
- `operação`: cadência ou faixa de teste, fluxo, capacidade pressuposta e governança;
- `hipóteses_de_medição`: sinal primário, sinais de apoio e decisão futura, sem meta inventada;
- `base_factual`: referências usadas, datas, classes e fatos temporais a revalidar;
- `conflitos_e_pendências`: impacto e decisão necessária.

## Passagem para `csc-social-content` — `social_content_brief`

Ao encaminhar uma peça social, emitir as mesmas chaves exigidas pela Skill receptora:

- `brief`: objetivo, público, canal, ação esperada, janela e decisão já aprovada;
- `sistema_editorial`: pilar, editoria, promessa, ponto de vista e invariantes; marcar `não aplicável` ou `pendente` quando a peça não pertencer a uma editoria definida;
- `matéria_prima`: documentos, páginas, pessoas, acervo, acontecimento ou oportunidade validada que sustentam a execução;
- `context_packet`: pacote factual integral, com fatos, fontes, datas, classes temporais, status e conflitos; não substituir por um resumo de `base_factual`;
- `cta_e_destino`: ação, URL, vigência, data de verificação e responsável pela confirmação final;
- `produção`: pessoas, locais, captação, acervo, design, edição, prazo e aprovações disponíveis ou pendentes;
- `restrições`: formato, acessibilidade, direitos, compliance, voz, alegações suspensas e conteúdos recentes a não repetir;
- `hipóteses_e_pendências`: pressupostos reversíveis separados dos insumos e decisões ainda ausentes.

Não omitir campo obrigatório para fazer o brief parecer completo: registrar `pendente`, seu impacto e quem deve decidir ou confirmar. Não preencher copy, roteiro ou legenda para completar o pacote.

## Regras de continuidade

- Manter hipótese estratégica separada de fato e de resultado observado.
- Não transferir editoria sem sua definição vigente nem inventar invariantes ausentes.
- Exigir nova checagem de fatos temporais antes da execução pública.
- Manter o `context_packet` rastreável até a peça final e indicar explicitamente o responsável pela última confirmação do CTA.
