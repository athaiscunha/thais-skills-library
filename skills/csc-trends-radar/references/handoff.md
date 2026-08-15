# Contrato de passagem

Usar este pacote para receber o recorte da rodada e encaminhar oportunidades confirmadas sem confundir sinal, trend, aplicação e fato institucional.

## Entrada mínima

- `rodada`: data, fuso, plataformas, mercado e janela observada;
- `foco`: públicos, editorias, produtos, calendário e objetivo relevante;
- `materiais`: links, capturas ou observações com perfil, plataforma e data;
- `context_packet`: fatos da Católica SC com fonte, data, classe temporal, status e conflitos;
- `capacidade`: pessoas, acervo, prazo, captação, edição e aprovação;
- `histórico`: itens usados, recusados ou em acompanhamento, com data e motivo;
- `restrições`: direitos, reputação, segurança, áudio e acesso público;
- `hipóteses_e_pendências`: sinais ainda fracos e validações necessárias.

## Saída mínima — `trend_opportunity_packet`

- `snapshot_em`: data e fuso da pesquisa;
- `classificação`: trend, formato, áudio, tema sazonal, estética ou post isolado;
- `mecânica`: unidade repetida, elementos invariantes e variações permitidas;
- `evidências`: ocorrências independentes com URL, perfil, plataforma e data;
- `leitura`: estágio, confiança e janela de uso, todos apoiados ou rotulados como hipótese;
- `decisão`: usar agora, pode render, acompanhar, descartar ou não é trend;
- `aplicação_csc`: vínculo com público/editoria, matéria-prima e ângulo proposto;
- `produção_e_risco`: esforço, recursos, áudio, direitos, segurança e alternativa sem som;
- `fatos_institucionais`: referências, classes temporais, conflitos e data de verificação;
- `pendências`: evidência, recurso ou aprovação que falta.

## Regras de continuidade

- Não encaminhar uma ocorrência isolada como trend confirmada.
- A janela de uso é hipótese datada, não promessa de viralização.
- `csc-social-content` pode executar a oportunidade sem repetir a pesquisa, mas deve revalidar fatos temporais e requisitos atuais de produção.
- Preservar autoria, riscos e limitações de acesso junto com a recomendação.
