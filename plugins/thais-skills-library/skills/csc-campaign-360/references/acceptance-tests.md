# Testes de aceitação da Campanha 360 CSC

## Sumário

- Pedidos mínimos, informações disponíveis e respostas incompletas
- Enquadramento da demanda, seleção de canais e conflitos factuais
- Conversão, mensuração, produção multiprofissional e campanhas críticas
- Encerramento e critério geral de aprovação

Use estes cenários ao criar ou alterar a Skill. Avalie o comportamento e as decisões, não a reprodução literal de seções.

## 1. Pedido mínimo

### Entrada

> Quero uma campanha 360 para divulgar um novo curso.

### Comportamento esperado

- reconhece que faltam decisões materiais;
- explica resumidamente o que entendeu;
- busca primeiro o que puder ser identificado em materiais e fontes disponíveis;
- pergunta proativamente por resultado, curso/oferta, público, janela e destino;
- não produz dezenas de peças como se a campanha estivesse definida;
- não exige que a usuária domine terminologia de marketing;
- oferece caminhos quando ela não souber uma resposta.

### Falha

- responde apenas `envie um briefing completo`;
- apresenta um formulário extenso sem priorização;
- inventa curso, público, meta, canais ou oferta;
- começa por calendário e formatos.

## 2. Informação já disponível

### Entrada

A usuária fornece documento atual com objetivo, público, oferta, datas, CTA, responsáveis e ativos.

### Comportamento esperado

- extrai os dados antes de perguntar;
- consulta a página oficial aplicável;
- pergunta somente por lacunas que alteram estratégia, risco ou execução;
- não pede novamente objetivo, data ou CTA já claros;
- registra diferenças entre documento e site.

### Falha

- repete um briefing genérico;
- presume que o documento elimina a checagem pública;
- oculta conflito.

## 3. Resposta `não sei`

### Entrada

> Não sei qual deve ser o público prioritário.

### Comportamento esperado

- não trava nem culpa a usuária;
- identifica públicos plausíveis apenas a partir de evidência disponível;
- mostra como a escolha altera mensagem, CTA ou canal;
- oferece cenários ou recomenda método de validação;
- pede decisão somente quando necessário;
- mantém como hipótese o que não foi confirmado.

### Falha

- inventa uma persona definitiva;
- faz a mesma pergunta com outras palavras;
- tenta falar com todos sem prioridade.

## 4. Demanda que não precisa de campanha

### Entrada

> Preciso corrigir a data em um card já aprovado.

### Comportamento esperado

- classifica como ajuste de peça;
- valida a data material;
- encaminha à execução apropriada;
- não impõe jornada, plano de canais ou post-mortem.

### Falha

- transforma a correção em projeto 360;
- altera estratégia ou outras peças sem autorização.

## 5. Pressão para estar em todos os canais

### Entrada

> Quero Instagram, TikTok, blog, Google, e-mail, WhatsApp e YouTube porque a campanha precisa ser 360.

### Comportamento esperado

- explica que 360 significa integração;
- avalia papel, público, capacidade, prova, destino e mensuração de cada frente;
- entrega `fazer`, `testar` e `não fazer agora`;
- preserva a escolha da usuária quando houver justificativa e capacidade;
- registra risco de duplicação ou sobrecarga.

### Falha

- aceita todos automaticamente;
- rejeita canais por preferência pessoal;
- recomenda frequência por costume.

## 6. Conflito factual temporal

### Entrada

Documento de campanha e página oficial mostram condições diferentes.

### Comportamento esperado

- identifica fontes, valores e datas;
- suspende a alegação conflitante;
- avança com partes seguras;
- pede reconciliação ao responsável;
- não escolhe silenciosamente a condição mais recente ou atraente.

### Falha

- mistura condições;
- usa a mais promocional;
- declara a campanha pronta.

## 7. Campanha de conversão sem destino pronto

### Entrada

Há objetivo de inscrição, mas a landing page e o formulário ainda não foram testados.

### Comportamento esperado

- marca prontidão de conversão como pendente ou vermelha;
- pode avançar com estratégia, criação e plano de QA;
- não recomenda investimento ou go-live como se o caminho estivesse funcional;
- atribui owner e teste necessários;
- verifica correspondência entre peça, página e atendimento.

### Falha

- considera o CTA suficiente;
- mede apenas cliques;
- ignora confirmação e atendimento.

## 8. Campanha sem histórico

### Entrada

> Não temos benchmark nem resultados anteriores comparáveis.

### Comportamento esperado

- não inventa meta;
- cria linha de base e janela de aprendizagem;
- limita variáveis;
- formula hipóteses e decisões futuras;
- distingue exploração de teste controlado.

### Falha

- usa média genérica de mercado como meta da Católica SC;
- promete causalidade;
- trata um ativo como evidência definitiva.

## 9. Produção para vários profissionais

### Entrada

A campanha aprovada exige carrossel, vídeo, anúncios, página e material para atendimento.

### Comportamento esperado

- cria `campaign_packet` e matriz-mãe;
- emite briefs específicos para social, design, vídeo, mídia, página e atendimento;
- preserva a mesma base factual;
- adapta função, profundidade e CTA;
- define dependências, versões, direitos, responsáveis e critérios de pronto;
- o próximo profissional consegue executar sem reconstruir a estratégia.

### Falha

- entrega somente textos;
- repete a mesma mensagem em todos os formatos;
- omite captação, especificações, tracking, aprovação ou direitos.

## 10. Pedido de copy isolada dentro de campanha definida

### Entrada

A usuária fornece um brief de campanha aprovado e pede apenas assets de Meta Ads.

### Comportamento esperado

- não reinicia a estratégia sem motivo;
- verifica somente fatos temporais e lacunas essenciais;
- encaminha a `csc-paid-media-copy` com brief completo;
- não inventa segmentação ou orçamento;
- mantém convenção de campanha e hipótese dos assets.

### Falha

- obriga a refazer todo o processo 360;
- entrega estratégia de mídia sem dados ou autorização;
- ignora limites e diversidade de copy.

## 11. Campanha crítica

### Entrada

Campanha de alta visibilidade com condição comercial, várias unidades, nova página e investimento informado.

### Comportamento esperado

- classifica como modo Crítico;
- exige gates humanos, owners e contingência;
- valida fatos por recorte;
- testa página, formulário e tracking;
- não mistura modalidades, câmpus ou condições;
- só atribui verde após resolver bloqueios vermelhos.

### Falha

- trata como campanha padrão;
- aceita aprovação implícita;
- publica um resumo que oculta pendências.

## 12. Encerramento

### Entrada

A usuária fornece resultados de campanha e pede análise.

### Comportamento esperado

- preserva fonte, período e configuração;
- separa observação, interpretação, hipótese e decisão;
- diagnostica a jornada antes de culpar a criação;
- incorpora página, atendimento e sazonalidade quando houver dados;
- registra aprendizado e limite de reuso;
- não transforma fato temporal em regra permanente.

### Falha

- declara sucesso ou fracasso por uma métrica isolada;
- confunde correlação com causalidade;
- propõe mudança sem explicar qual evidência a sustenta.

## Critério geral de aprovação

A Skill passa quando, nos cenários aplicáveis:

- conduz o briefing sem exigir que a usuária antecipe o formulário;
- reutiliza informações disponíveis;
- faz apenas perguntas materialmente úteis;
- diferencia fato, hipótese, decisão e resultado;
- seleciona canais por função;
- integra conversão e atendimento;
- prepara mensuração antes da produção;
- entrega handoffs executáveis;
- preserva autorização e não realiza ações externas não solicitadas;
- bloqueia publicação somente pelo risco relevante, sem impedir progresso seguro.
