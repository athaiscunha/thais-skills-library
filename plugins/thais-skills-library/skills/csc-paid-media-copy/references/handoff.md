# Contrato de passagem

Usar este pacote para receber base de campanha e encaminhar assets para validação, acabamento ou operação. Manter fatos do produto separados de hipóteses e resultados de mídia.

## Entrada mínima

- `entrega`: plataforma, campanha, objetivo, campos, quantidades e limites pedidos;
- `recorte`: produto, público, estágio, praça, modalidade e período;
- `context_packet`: fatos com fonte, data, classe temporal, status e conflitos;
- `destino_e_cta`: URL ou ação confirmada e vigência, quando aplicável;
- `criativo`: texto, fala, imagem, cartela e elementos fixos já previstos;
- `hipóteses_de_copy`: territórios a testar, sem tratá-los como fatos;
- `dados_de_performance`: período, métrica, exposição e comparabilidade, quando fornecidos;
- `restrições_e_pendências`: compliance, oferta, aprovação, formato e dados ausentes.

## Saída mínima — `paid_copy_packet`

- `snapshot_em`: data das fontes e especificações verificadas;
- `base_factual_usada`: alegações com referência, classe e status;
- `assets`: plataforma, campo, texto, contagem/limite quando material, função e hipótese dominante;
- `relações_do_criativo`: o que já aparece na arte, fala ou cartela e o que cada asset acrescenta;
- `validação`: limites, duplicações, combinabilidade e riscos verificados;
- `hipóteses_para_teste`: variável pretendida e sinal que permitiria compará-la;
- `conflitos_e_bloqueios`: alegações suspensas e assets afetados;
- `pendências`: dado, aprovação ou destino necessário antes de veiculação.

## Regras de continuidade

- Não repassar dado de performance como prova do produto ou promessa ao público.
- Preservar texto, campo e limite como unidade; o acabamento não pode quebrar combinabilidade nem contagem.
- Marcar como rascunho qualquer saída sem validação atual do site ou de condição temporal material.
- Uma Skill posterior pode melhorar linguagem, mas não resolver conflito factual nem alterar hipótese sem registrar a decisão.
