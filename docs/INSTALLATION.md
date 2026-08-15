# Instalação das sete Skills em outra máquina

O caminho recomendado é instalar **um único plugin**. Ele contém as sete Skills aprovadas e não inclui conectores, MCPs, automações ou Skills de terceiros.

## Jeito mais simples

Na outra máquina, abra uma tarefa nova no Codex e cole este pedido:

> Instale e valide o pacote de Skills do repositório público `athaiscunha/thais-skills-library`, usando a branch `main`. Configure o marketplace `thais-skills`, instale o plugin `thais-skills-library` e confirme que as sete Skills estão disponíveis em uma nova tarefa. Não instale Skills de terceiros e não altere o conteúdo das Skills.

O Codex deve fazer a instalação e devolver uma confirmação com os sete nomes. Você não precisa copiar pasta por pasta.

## O que será instalado

1. `csc-marketing-context`
2. `csc-paid-media-copy`
3. `editor-anti-aies`
4. `csc-channel-strategy`
5. `csc-seo-blog`
6. `csc-trends-radar`
7. `csc-social-content`

## Verificação final

Depois da instalação, feche a tarefa usada para instalar e abra uma nova. Skills e plugins são carregados no início da tarefa.

No Codex, peça:

> Liste as Skills da Biblioteca de Skills da Thais disponíveis nesta tarefa e confirme que são sete.

Você também pode testar uma Skill explicitamente, por exemplo:

```text
$csc-paid-media-copy
```

No ChatGPT, quando a superfície instalada expuser as Skills do plugin no seletor, use o menu de `@` para escolher a Skill específica. A disponibilidade pode variar conforme plano, superfície e forma de instalação.

## Comandos equivalentes

Esta seção serve para diagnóstico; o pedido acima é suficiente na rotina normal.

```sh
codex plugin marketplace add athaiscunha/thais-skills-library --ref main
codex plugin add thais-skills-library@thais-skills
```

O marketplace versionado no repositório usa `source: local` com caminho relativo `./plugins/thais-skills-library`. Isso é intencional: depois que o marketplace do repositório é adicionado, o plugin é resolvido dentro da cópia desse marketplace.

## Plano B: instalação individual

Se uma superfície ainda não oferecer suporte ao plugin/marketplace desse repositório, instale as sete pastas de `skills/` individualmente a partir do mesmo repositório. Esse plano mantém o GitHub como fonte de verdade, mas exige instalar as Skills uma por uma.

## Observação sobre ChatGPT e Codex

A sintaxe de invocação explícita é diferente:

- ChatGPT: selecione a Skill pelo menu `@`, quando ela estiver disponível na superfície atual;
- Codex: use `$nome-da-skill`.

Os arquivos `agents/openai.yaml` usam prompts neutros, sem `@` ou `$`, para que o mesmo pacote seja portátil entre as superfícies.

Fontes oficiais: documentação de Skills, plugins e manifesto de plugins da OpenAI.
