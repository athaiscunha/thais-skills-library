# Instalação das dez Skills em outra máquina

O caminho recomendado é instalar **um único plugin**. Ele contém as dez Skills aprovadas e não inclui conectores, MCPs, automações ou Skills de terceiros.

## Jeito mais simples

Na outra máquina, abra uma tarefa nova no Codex e cole este pedido:

> Instale e valide o pacote de Skills do repositório público `athaiscunha/thais-skills-library`, usando a branch `main`. Configure o marketplace `thais-skills`, instale o plugin `thais-skills-library` e confirme que as dez Skills estão disponíveis em uma nova tarefa. Não instale Skills de terceiros e não altere o conteúdo das Skills.

O Codex deve fazer a instalação e devolver uma confirmação com os dez nomes. Você não precisa copiar pasta por pasta.

## O que será instalado

1. `csc-marketing-context`
2. `csc-paid-media-copy`
3. `editor-anti-aies`
4. `csc-channel-strategy`
5. `csc-seo-blog`
6. `csc-trends-radar`
7. `csc-social-content`
8. `csc-campaign-360`
9. `csc-visual-design`
10. `visual-design`

## Verificação final

Depois da instalação, feche a tarefa usada para instalar e abra uma nova. Skills e plugins são carregados no início da tarefa.

No Codex, peça:

> Liste as Skills da Biblioteca de Skills da Thais disponíveis nesta tarefa e confirme que são dez.

Você também pode testar uma Skill explicitamente, por exemplo:

```text
$thais-skills-library:csc-paid-media-copy
```

O prefixo é o namespace do plugin nesta instalação. Para evitar erro de digitação ou acomodar outra superfície, digite `$` ou use `/skills` e selecione o nome que o Codex exibir.

No ChatGPT, quando a superfície instalada expuser as Skills do plugin no seletor, use o menu de `@` para escolher a Skill específica. A disponibilidade pode variar conforme plano, superfície e forma de instalação.

## Comandos equivalentes

Esta seção serve para diagnóstico; o pedido acima é suficiente na rotina normal.

```sh
codex plugin marketplace add athaiscunha/thais-skills-library --ref main
codex plugin add thais-skills-library@thais-skills
```

O marketplace versionado no repositório usa `source: local` com caminho relativo `./plugins/thais-skills-library`. Isso é intencional: depois que o marketplace do repositório é adicionado, o plugin é resolvido dentro da cópia desse marketplace.

## Plano B: instalação individual

Se uma superfície ainda não oferecer suporte ao plugin/marketplace desse repositório, instale as dez pastas de `skills/` individualmente a partir do mesmo repositório. Esse plano mantém o GitHub como fonte de verdade, mas exige instalar as Skills uma por uma.

## Observação sobre ChatGPT e Codex

A sintaxe de invocação explícita é diferente:

- ChatGPT: use `@` para selecionar o plugin ou uma Skill interna, quando disponível na superfície atual;
- Codex: use `$` ou `/skills` para selecionar o nome carregado; Skills empacotadas podem aparecer como `$thais-skills-library:nome-da-skill`.

Os arquivos `agents/openai.yaml` identificam a Skill canônica em seus prompts. O host pode acrescentar o namespace do plugin ao nome de invocação sem alterar o `name` declarado no `SKILL.md`.

Fontes oficiais: documentação de Skills, plugins e manifesto de plugins da OpenAI.
