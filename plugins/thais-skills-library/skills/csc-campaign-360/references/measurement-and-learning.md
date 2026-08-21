# Mensuração, experimentos, otimização e aprendizagem

## Sumário

- Árvore de mensuração, KPI principal e linha de base
- Hipóteses, experimentos e tracking
- Diagnóstico, cadência e registro de otimização
- Feedback, post-mortem e aprendizagem

Leia esta referência antes de fechar canais ou solicitar produção. Mensuração desenhada depois das peças tende a registrar atividade, não a informar decisões.

## Princípio

Uma métrica só entra no plano quando ajuda a responder uma pergunta ou tomar uma decisão. Não escolher indicador porque a plataforma o destaca e não declarar causalidade quando os dados mostram apenas associação.

## Árvore de mensuração

Defina, conforme a campanha:

| Nível | Pergunta | Exemplos possíveis |
|---|---|---|
| resultado | a campanha moveu o objetivo principal? | inscrição, matrícula, presença, contato qualificado, oportunidade |
| ação intermediária | a pessoa avançou? | início de inscrição, formulário, conversa, visita, download útil |
| resposta | houve reação coerente? | clique, resposta, compartilhamento, busca, comentário substantivo |
| atenção | a mensagem foi consumida? | retenção, conclusão, leitura, salvamento, tempo |
| distribuição | a mensagem chegou? | alcance, impressões, visualizações qualificadas |
| guardrail | houve efeito indesejado? | abandono, lead inadequado, reclamação, saturação, sobrecarga operacional |

Use apenas sinais disponíveis ou que a usuária possa obter. Não preencher a árvore com dados hipotéticos apresentados como existentes.

## KPI principal e sinais diagnósticos

Escolha um indicador principal proporcional ao objetivo. Depois, selecione poucos sinais que ajudem a localizar o problema.

Exemplos de leitura:

- objetivo de inscrição: alcance é diagnóstico de distribuição, não sucesso final;
- objetivo institucional: conversão imediata pode ser inadequada, mas atenção isolada também não comprova mudança de percepção;
- evento: inscrição sem presença exige medir continuidade;
- B2B: volume de leads pode importar menos que adequação e avanço comercial;
- serviço: conclusão correta pode importar mais que engajamento.

Registrar o que não pode ser medido e qual proxy será usado. Chamar proxy de proxy.

## Linha de base e metas

Quando houver histórico comparável, registrar:

- fonte;
- período;
- objetivo e configuração anteriores;
- público, canal, investimento e sazonalidade;
- mudanças de oferta, página ou tracking;
- limitações de comparação.

Quando não houver histórico:

- usar a primeira janela como linha de base;
- limitar o número de variáveis simultâneas;
- definir o que será aprendido;
- evitar benchmark genérico como meta da Católica SC.

Não inventar número para completar apresentação. Se a organização precisar de meta, mostrar qual dado ou decisão é necessário para defini-la.

## Hipótese

Escrever:

> Se ativarmos [mensagem, formato, canal, oferta ou experiência] para [público em situação] então [comportamento ou percepção observável] deve mudar porque [mecanismo esperado]. Saberemos mais ao observar [sinal] durante [janela], respeitando [limitação].

Marcar a hipótese como hipótese, mesmo quando for plausível.

## Matriz de experimentos

| ID | Hipótese | Variável | Controle/comparação | Público | Canal | Sinal principal | Janela | Se confirmar | Se não confirmar |
|---|---|---|---|---|---|---|---|---|---|

Cada experimento deve:

- testar uma decisão relevante;
- explicitar o mecanismo esperado;
- mudar o mínimo necessário para interpretação;
- ter volume e janela considerados;
- evitar conclusão com um caso isolado;
- preservar diferenças de objetivo entre formatos;
- registrar interferências como mídia, colaboração, evento externo e sazonalidade;
- terminar em uma decisão possível.

Não chamar qualquer variação de A/B. Quando não houver controle, distribuição comparável ou volume suficiente, tratar como exploração criativa ou sinal qualitativo.

## Plano de tracking

Registrar:

- nome e ID da campanha;
- convenção de fontes, meios e conteúdos;
- UTMs;
- páginas de destino;
- eventos de atenção, intenção, envio, erro e sucesso disponíveis;
- passagem de origem para formulário ou CRM, quando existente;
- fonte de verdade;
- responsáveis por implementar, testar e ler;
- data do teste;
- janela de observação;
- limitações de atribuição;
- forma de conciliar dados divergentes.

Não afirmar que tracking está configurado porque o plano existe. Diferenciar `planejado`, `implementado` e `testado`.

## Matriz de diagnóstico

Antes de otimizar, localizar o estágio do problema.

| Sinal observado | Hipóteses possíveis | Verificar antes de concluir | Decisões possíveis |
|---|---|---|---|
| baixa distribuição | configuração, inventário, verba, elegibilidade ou entrega | status, público, posicionamento, período, orçamento | corrigir distribuição ou reavaliar canal |
| distribuição adequada, pouca atenção | gancho, relevância, formato ou fadiga | primeiros segundos, título, frequência, ângulo | mudar abertura, formato ou mensagem |
| atenção adequada, pouca resposta | proposta, clareza, estágio ou CTA | mensagem, prova, intenção, ação pedida | ajustar proposta, prova ou CTA |
| cliques, pouca conversão | página, formulário, mensagem ou oferta | funcionamento, velocidade, correspondência e fricção | corrigir destino ou oferta |
| leads, pouca continuidade | qualidade, expectativa ou atendimento | origem, prazo, resposta, objeções e processo | rever público, promessa, formulário ou SLA |
| conversão adequada, pouca escala | alcance, inventário ou capacidade | tamanho do público, orçamento, ativos e operação | ampliar gradualmente ou criar novas frentes |
| resultado com guardrail ruim | desalinhamento ou sobrecarga | qualidade, reclamações, capacidade, reputação | reduzir, corrigir ou interromper |

Não alterar simultaneamente público, oferta, criativo, página e CTA e depois atribuir melhora a um único fator.

## Cadência de leitura

Defina a frequência conforme:

- duração da campanha;
- investimento e risco;
- volume de dados;
- velocidade da conversão;
- capacidade de resposta;
- tempo necessário para o comportamento ocorrer;
- sazonalidade.

Evite tanto mudanças por ansiedade quanto espera até o fim quando há erro material. Link quebrado, condição incorreta, gasto fora do autorizado ou risco reputacional exigem ação imediata dentro das permissões disponíveis.

## Registro de otimização

Guardar:

| Data | Observação | Interpretação | Decisão | Alteração | Ativos/públicos | Responsável | Próxima leitura |
|---|---|---|---|---|---|---|---|

Separar:

- `observação`: o que os dados mostram;
- `interpretação`: explicação possível;
- `decisão`: o que será feito;
- `resultado posterior`: o que mudou depois.

Não reescrever o histórico para fazer a decisão parecer óbvia.

## Feedback de atendimento

Quando a campanha envolve contato humano, incorporar sinais como:

- adequação do interesse;
- dúvidas recorrentes;
- condição mais questionada;
- expectativa criada pela campanha;
- motivo de abandono;
- etapa em que o contato parou;
- tempo de resposta fornecido;
- lacunas do FAQ;
- necessidade de novo conteúdo ou correção de promessa.

Usar apenas dados agregados ou adequadamente tratados. Não expor informações pessoais no relatório criativo.

## Post-mortem

Ao encerrar, registrar:

1. objetivo original e versão vigente;
2. hipótese principal;
3. oferta, público, canais e ativos efetivamente usados;
4. alterações durante a campanha;
5. resultados com fonte, período e limitações;
6. guardrails;
7. comparação somente quando válida;
8. aprendizados sustentados;
9. sinais ainda insuficientes;
10. problemas de produção, página, tracking ou atendimento;
11. decisões para próxima campanha;
12. ativos reutilizáveis;
13. ativos ou alegações que não devem ser reutilizados;
14. fatos temporais a revalidar;
15. responsáveis por atualizar documentos ou processos, quando autorizado.

## Matriz de aprendizagem

| Hipótese | Evidência | Confiança | Limitação | Decisão | Reuso permitido |
|---|---|---|---|---|---|

Use confiança qualitativa e justificada. Não transformar um bom resultado isolado em regra permanente.

## Critério de sucesso do sistema

Além do desempenho da campanha, avalie se o processo:

- reduziu perguntas repetidas;
- antecipou bloqueios;
- preservou consistência factual;
- eliminou canais ou peças sem função;
- melhorou o handoff entre profissionais;
- preparou conversão e atendimento;
- permitiu interpretar resultados;
- registrou decisões reutilizáveis sem congelar fatos temporais.
