# Instalação dos plugins em outra máquina

O caminho recomendado é adicionar o marketplace público `thais-skills` uma única vez e escolher quais pacotes instalar. O marketplace oferece:

1. `thais-skills-library`: as oito Skills da biblioteca, incluindo editais culturais;
2. `seo-auditor-phd`: a Skill especialista em auditoria SEO on-page.

Os dois pacotes são independentes e não incluem conectores, MCPs, automações ou credenciais. É possível instalar apenas um deles ou ambos.

## Jeito mais simples

Na outra máquina, abra uma tarefa nova no Codex e cole este pedido para instalar os dois pacotes:

> Adicione e valide o marketplace do repositório público `athaiscunha/thais-skills-library`, usando a branch `main`. Instale os plugins `thais-skills-library` e `seo-auditor-phd` do marketplace `thais-skills`. Confirme as versões instaladas e oriente a abertura de uma nova tarefa para carregar as nove Skills. Não instale Skills de terceiros e não altere o conteúdo dos pacotes.

O Codex deve fazer a instalação e devolver uma confirmação com os nove nomes. Você não precisa copiar pasta por pasta.

## O que será instalado com os dois pacotes

1. `csc-marketing-context`
2. `csc-paid-media-copy`
3. `editor-anti-aies`
4. `csc-channel-strategy`
5. `csc-seo-blog`
6. `csc-trends-radar`
7. `csc-social-content`
8. `editais-cultura`
9. `seo-auditor-phd`

Se você quiser somente o auditor SEO, peça:

> Adicione o marketplace do repositório público `athaiscunha/thais-skills-library`, na branch `main`, e instale apenas `seo-auditor-phd@thais-skills`. Valide a instalação e me avise quando eu puder abrir uma nova tarefa para usar a Skill.

## Usar a Skill de editais culturais

A versão `1.1.0` de `thais-skills-library` inclui `editais-cultura`. Para atualizar somente esse pacote, execute:

```sh
codex plugin marketplace upgrade thais-skills
codex plugin add thais-skills-library@thais-skills
```

Abra uma tarefa nova e peça: “Pesquise oportunidades culturais atuais em Curitiba, no Paraná e em chamadas nacionais. Podemos criar um projeto para o edital; priorize elegibilidade, critérios demonstráveis e execução viável.” A Skill também pode ser acionada no Codex com `$editais-cultura`. Criar ou instalar a Skill não inscreve projetos nem autoriza declarações e envios em nome de proponentes.

## Verificação final

Depois da instalação, feche a tarefa usada para instalar e abra uma nova. Skills e plugins são carregados no início da tarefa.

No Codex, peça:

> Liste as Skills instaladas pelo marketplace Skills da Thais e confirme que são nove: as oito da biblioteca e o SEO Auditor PhD.

Você também pode testar uma Skill explicitamente, por exemplo:

```text
$csc-paid-media-copy
```

Para testar o auditor SEO:

```text
$seo-auditor-phd
```

No ChatGPT, quando a superfície instalada expuser as Skills do plugin no seletor, use o menu de `@` para escolher a Skill específica. A disponibilidade pode variar conforme plano, superfície e forma de instalação.

## Comandos equivalentes

Esta seção serve para diagnóstico; o pedido acima é suficiente na rotina normal.

```sh
codex plugin marketplace add athaiscunha/thais-skills-library --ref main
codex plugin add thais-skills-library@thais-skills
codex plugin add seo-auditor-phd@thais-skills
```

O marketplace versionado no repositório usa `source: local` com caminhos relativos dentro de `./plugins/`. Isso é intencional: depois que o marketplace do repositório é adicionado, cada plugin é resolvido dentro da cópia desse marketplace.

## Plano B: instalação individual das Skills da biblioteca

Se uma superfície ainda não oferecer suporte ao plugin/marketplace desse repositório, instale as pastas desejadas de `skills/` individualmente a partir do mesmo repositório. Esse plano mantém o GitHub como fonte de verdade, mas exige instalar as Skills uma por uma. Para o `seo-auditor-phd`, prefira o pacote completo em `plugins/seo-auditor-phd`, pois ele inclui referências, analisador, testes e avaliações que fazem parte da entrega.

## Observação sobre ChatGPT e Codex

A sintaxe de invocação explícita é diferente:

- ChatGPT: selecione a Skill pelo menu `@`, quando ela estiver disponível na superfície atual;
- Codex: use `$nome-da-skill`.

Os arquivos `agents/openai.yaml` usam prompts neutros, sem `@` ou `$`, para que o mesmo pacote seja portátil entre as superfícies.

Fontes oficiais: documentação de Skills, plugins e manifesto de plugins da OpenAI.
