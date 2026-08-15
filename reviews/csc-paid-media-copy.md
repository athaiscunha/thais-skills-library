# Revisão: csc-paid-media-copy

- Origem: arquivo `csc-paid-media-copy.zip` fornecido pela usuária
- SHA-256 do arquivo original: `ba8d40a83fb85f2783673fd2e6b36313cd16b00e545b4381a2695e25f2370f55`
- Licença: uso interno, criação própria
- Data: 2026-08-14
- Revisor: Codex, com direção da usuária
- Decisão: aprovada com alterações
- Versão aprovada: 0.2.0

## Finalidade

Criar, revisar e validar copy de mídia paga da Católica SC para Meta Ads, Google Search responsivo e Google Performance Max.

## Arquivos analisados

Foram lidos os 13 arquivos do pacote original: `SKILL.md`, nove referências, um script Python, a configuração de interface e o ícone SVG. O arquivo compactado não contém links simbólicos, binários ou caminhos que escapem da pasta da Skill.

## Riscos encontrados

- A configuração `agents/openai.yaml` usava um campo antigo chamado `policy.products`, não documentado no formato atual.
- Os caminhos dos ícones e os valores textuais não seguiam integralmente a convenção atual da configuração.
- O script depende de um runtime Python 3, embora use somente a biblioteca padrão e não instale dependências.

Não foram encontrados comandos destrutivos, chamadas de rede, acesso a segredos, gravação de arquivos, execução remota ou permissões amplas.

## Alterações realizadas

- Atualização de `agents/openai.yaml` para o formato atual.
- Inclusão de método para iteração de copy com evidência de campanha, sem atribuir causalidade indevida.
- Inclusão de contexto compartilhado com controle de versão, temporalidade e rastreabilidade.
- Inclusão de dois testes de aceitação para dados comparáveis e insuficientes.

## Testes

- Integridade do ZIP e inventário de arquivos.
- Verificação de frontmatter, nome, descrição e configuração de interface.
- Verificação de todas as referências internas e do ícone.
- Varredura estática de padrões perigosos e dados sensíveis.
- Teste positivo do auditor de assets.
- Teste negativo com limite excedido e duplicação normalizada.

## Resultado

A versão 0.2.0 foi aprovada para permanecer na biblioteca. A instalação nas duas máquinas deve ocorrer somente depois da revisão do PR e da entrada em `main`.
