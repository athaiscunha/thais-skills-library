# Produção, governança e contratos de passagem

## Sumário

- Pacote-mãe, matriz de ativos e brief universal
- Handoffs para conteúdo, mídia paga e SEO
- Briefs para design, vídeo e landing page
- Atendimento, governança, go-live e critério de pronto

Leia esta referência quando a estratégia estiver suficientemente definida para planejar ativos ou encaminhar trabalho a uma especialidade. Não use a produção para esconder uma decisão estratégica aberta.

## Pacote-mãe da campanha

Mantenha um `campaign_packet` com:

- `snapshot_em`: data do contexto e da última validação;
- `identificação`: nome interno, tipo, nível e janela;
- `status`: etapa e gate atual;
- `responsáveis`: solicitante, owner, aprovadores e executores;
- `decisão_estratégica`: problema, objetivos, público, proposta e mecanismo;
- `context_packet`: fatos, fontes, datas, classes, conflitos e restrições;
- `jornada`: momentos, barreiras, provas e ações;
- `mensagens`: hierarquia, provas, objeções e proibições;
- `canais`: papéis, limites, dependências e sinais;
- `conversão`: destinos, eventos, atendimento e continuidade;
- `mensuração`: indicador principal, sinais, tracking, hipóteses e decisões;
- `operação`: capacidade, cronograma, matriz de ativos, direitos e aprovações;
- `riscos_e_pendências`: impacto, responsável e prazo de decisão;
- `histórico`: versão, alteração, responsável, data e motivo.

Não reduzir o `context_packet` a alegações soltas. Preserve fonte, data, classe temporal e status até a execução.

## Matriz-mãe de ativos

Use somente os campos que orientam execução e gestão:

| ID | Canal | Público | Momento | Trabalho | Ângulo | Formato | Mensagem/prova | CTA/destino | Variação | Dependência | Responsável | Prazo | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Convenção recomendada:

```text
[CAMPANHA]-[PÚBLICO]-[ETAPA]-[CANAL]-[FORMATO]-[ÂNGULO]-[VARIAÇÃO]
```

Exemplo interno:

```text
POSIA-PROF-CONS-META-VIDEO-PROVA-V02
```

Adapte a convenção existente quando a equipe já tiver uma. Não impor um novo padrão que rompa rastreamento ou versionamento em uso.

## Brief universal de ativo

Cada ativo deve registrar:

- ID e versão;
- objetivo da peça dentro da campanha;
- público e situação;
- momento da jornada;
- trabalho principal;
- mensagem e ângulo;
- fato ou prova;
- CTA e destino;
- formato, dimensões ou duração;
- estrutura narrativa;
- matéria-prima;
- pessoas, ambientes ou acervo;
- texto visível, locução ou elementos obrigatórios;
- direção visual ou audiovisual;
- acessibilidade;
- direitos e autorizações;
- adaptações e variações;
- restrições factuais, verbais, visuais, jurídicas e técnicas;
- data de validade dos fatos temporais;
- responsável pela última conferência;
- dependências;
- aprovadores;
- prazo;
- critério de pronto;
- parâmetros de rastreamento, quando aplicáveis.

Marcar `pendente`, impacto e responsável. Não deixar campo crítico em branco para o brief parecer completo.

## Handoff para `csc-social-content`

Entregar:

- `brief`: objetivo, público, canal, ação, janela e decisão aprovada;
- `sistema_editorial`: pilar, editoria, promessa, ponto de vista e invariantes, ou `não aplicável`/`pendente`;
- `matéria_prima`: documentos, páginas, pessoas, ambientes, acervo e acontecimento;
- `context_packet` integral;
- `mensagem_e_ângulo`: papel da peça, barreira, prova e hipótese;
- `cta_e_destino`: ação, URL, vigência, consulta e responsável pela confirmação;
- `produção`: captação, design, edição, prazos e aprovações;
- `restrições`: acessibilidade, direitos, compliance, voz, alegações suspensas e conteúdos recentes a não repetir;
- `mensuração`: sinal da peça e relação com o resultado da campanha;
- `pendências`: decisão, impacto e responsável.

Não preencher redes sociais com peças promocionais apenas para dar volume à campanha. Respeitar o papel editorial do perfil e diferenciar conteúdo nativo de adaptação.

## Handoff para `csc-paid-media-copy`

Entregar:

- objetivo da campanha e resultado principal;
- plataforma e formato solicitados;
- objetivo de mídia aprovado, se fornecido;
- público estratégico e estágio;
- oferta e condições;
- proposta central;
- mensagens, provas e objeções;
- CTA e página de destino;
- datas, vigências e revalidação;
- ângulos criativos que precisam ser cobertos;
- variedade esperada entre assets;
- limites de caracteres e especificações atuais verificadas;
- alegações proibidas;
- contexto visual disponível;
- convenção de nome e tracking;
- hipótese de cada variação;
- aprovações e responsável final.

Não pedir à copy que resolva silenciosamente:

- orçamento;
- segmentação;
- bidding;
- flighting;
- arquitetura de campanha;
- remarketing;
- escala ou pausa.

Quando essas decisões forem necessárias, emitir `paid_media_strategy_requirements` para a pessoa de mídia:

- resultado e evento de otimização desejados;
- jornada e públicos prioritários;
- regiões, modalidades e restrições confirmadas;
- orçamento e período fornecidos;
- inventário criativo;
- páginas e eventos disponíveis;
- exclusões, dependências e riscos;
- hipóteses a testar;
- critérios de leitura e decisão ainda pendentes.

## Handoff para `csc-seo-blog`

Entregar:

- intenção e tarefa de busca;
- papel do conteúdo na campanha;
- público e momento;
- pergunta central;
- tema, palavra-chave ou cluster, quando fornecido ou pesquisado;
- fontes oficiais e fatos temporais;
- relação com páginas de produto;
- profundidade e utilidade esperadas;
- CTA e caminho de continuidade;
- linkagem interna relevante;
- riscos de canibalização ou duplicação conhecidos;
- validade e necessidade de atualização;
- métrica ou sinal do conteúdo;
- restrições e aprovações.

Não tratar artigo como simples expansão da legenda. O conteúdo deve atender intenção de busca e funcionar fora da campanha.

## Brief para design

Entregar ao designer:

- objetivo e papel do ativo;
- público, situação e momento;
- mensagem prioritária e hierarquia;
- prova e informação obrigatória;
- CTA e destino;
- formato, dimensões, proporções e áreas seguras;
- quantidade e relação entre peças;
- direção de arte: intenção, atmosfera, hierarquia e função dos elementos;
- pessoas, ambientes, imagens ou ilustrações necessárias;
- acervo disponível e direitos;
- texto exato em arte;
- elementos de marca e restrições;
- acessibilidade, contraste, tamanho e legibilidade;
- adaptações por canal;
- variações criativas e o que deve permanecer constante;
- referências funcionais, explicando o que aproveitar e o que evitar;
- nomenclatura e organização de arquivos;
- entregáveis editáveis e exportados, quando definidos;
- responsáveis, prazo e aprovadores;
- critério de aprovação.

Não usar frases vagas como `deixar moderno`, `usar identidade jovem` ou `fazer algo impactante` sem traduzir em função visual observável.

## Brief para vídeo

Entregar à equipe de vídeo:

- objetivo e papel;
- público e momento;
- mensagem, tensão e prova;
- abertura e promessa dos primeiros segundos;
- progressão narrativa;
- roteiro de fala ou locução;
- texto em tela;
- duração e proporções;
- lista de cenas e planos;
- pessoas e responsabilidades;
- locações, autorizações e logística;
- perguntas de entrevista, quando aplicáveis;
- B-roll obrigatório e desejável;
- captação de áudio;
- direção de apresentação sem forçar espontaneidade;
- ritmo e lógica de edição;
- legendas, contraste e acessibilidade;
- trilha e direitos;
- CTA e encerramento;
- variações de gancho, corpo ou CTA;
- versões, cortes e thumbnails;
- prazo de captação, primeiro corte, revisão e entrega;
- aprovadores e limites de alteração;
- critério de pronto.

Se depender de depoimento, separar perguntas de apuração de frases aprovadas. Não roteirizar experiência pessoal como se fosse fala espontânea real.

## Brief para landing page ou destino

Entregar:

- papel da página na jornada;
- origem provável do tráfego;
- público e contexto de chegada;
- proposta e hierarquia de informação;
- condições, provas e objeções;
- CTA principal e secundário;
- campos de formulário e justificativa;
- mensagem de sucesso e próximo passo;
- experiência móvel;
- acessibilidade;
- política e consentimento aplicáveis;
- integrações e responsável técnico;
- eventos de visualização, intenção, envio, erro e sucesso, conforme disponibilidade;
- UTMs e persistência de origem;
- mensagem compatível com anúncios e conteúdos;
- testes funcionais;
- responsável pelo conteúdo, desenvolvimento, dados e aprovação;
- plano de contingência.

Não declarar campanha pronta para conversão quando a página ainda não foi publicada, testada ou alinhada com a promessa.

## Handoff para atendimento, comercial ou matrículas

Entregar somente informações aprovadas:

- nome e objetivo da campanha;
- público e origem provável;
- oferta, condições e vigência;
- páginas oficiais;
- CTA e próximo passo;
- perguntas frequentes;
- objeções conhecidas;
- respostas sustentadas;
- alegações que não podem ser feitas;
- rota para dúvida não prevista;
- responsável e prazo de atendimento fornecidos;
- informação que precisa ser registrada;
- motivos de perda ou abandono que devem retornar ao marketing;
- regra de proteção de dados;
- data de atualização do material.

Não inventar processo, script comercial, SLA ou permissão de contato. Sinalizar dependências.

## Governança

### Papéis mínimos

Identifique, conforme o caso:

- owner da campanha;
- responsável por fatos e oferta;
- responsável por estratégia;
- responsável por criação;
- responsáveis por design e vídeo;
- responsável por mídia;
- responsável por página e dados;
- responsável por atendimento;
- aprovador final;
- responsável por registrar aprendizados.

Uma pessoa pode acumular papéis. O importante é não deixar uma decisão crítica sem dono.

### Registro de decisão

Para mudanças materiais, guardar:

| Data | Decisão | Motivo/evidência | Impacto | Responsável | Ativos afetados |
|---|---|---|---|---|---|

Mudança de oferta, público, CTA, condição, página, conceito, tracking ou objetivo exige revisão dos ativos dependentes.

### Aprovação

Definir para cada gate:

- o que está sendo aprovado;
- quem aprova;
- até quando;
- quais pendências permanecem;
- qual risco foi aceito;
- qual versão está aprovada.

Silêncio não equivale a aprovação. Não declarar autorização que não foi dada.

## Pacote de go-live

Antes da ativação, consolidar:

- inventário e versões finais;
- links e destinos;
- UTMs e identificadores;
- calendário e janela;
- responsáveis;
- aprovações;
- contatos de contingência;
- fatos temporais e validade;
- direitos de uso;
- eventos e testes;
- plano de monitoramento;
- decisão em caso de erro;
- assets de substituição, se necessários;
- status `verde`, `amarelo` ou `vermelho` e justificativa.

## Critério de pronto do pacote de produção

O pacote está pronto quando o próximo profissional consegue:

1. entender a função da entrega;
2. localizar fatos e fontes;
3. executar sem reconstruir a estratégia;
4. saber o que pode variar e o que deve permanecer;
5. identificar dependências e responsáveis;
6. produzir no formato correto;
7. submeter à pessoa certa;
8. saber como a peça será avaliada;
9. evitar alegações e usos proibidos;
10. registrar a versão efetivamente utilizada.
