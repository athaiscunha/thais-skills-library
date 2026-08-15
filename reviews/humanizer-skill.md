# Revisão: humanizer-skill

- Origem: Adam Boudjemaa / `Aboudjem/humanizer-skill`
- Repositório: https://github.com/Aboudjem/humanizer-skill
- Commit analisado: `9a7f35b7b9ad8c3abd71f10757ec9f91fb8ae165`
- Arquivo principal analisado: `skills/humanizer/SKILL.md` (`56a44d5073e25dd60fa4da860426dedca62e9ed4`)
- Licença: MIT
- Data: 2026-08-14
- Revisor: Codex, a pedido da proprietária do repositório
- Decisão: somente referência

## Finalidade

Detectar padrões associados a prosa gerada por modelos e reescrever em diferentes perfis de voz.

## Escopo da revisão

Foram lidos o `SKILL.md`, a licença e os trechos de referência relacionados a repetição. Esta não foi uma auditoria de instalação do pacote completo; scripts e site de documentação não foram aprovados nem executados.

## Ideias aproveitáveis

- tratar sinais como conjunto e evitar conclusão a partir de uma palavra;
- preservar fatos específicos, terminologia correta e marcas reais de voz;
- distinguir repetição técnica de alternância artificial de sinônimos;
- aplicar o teste de densidade: cada frase precisa acrescentar algo;
- proteger citações, código, títulos e amostras curtas de falsos positivos.

## Riscos e incompatibilidades

- lista extensa de padrões pode virar substituição mecânica;
- pontuação de “cheiro de IA” sugere precisão que a análise não possui;
- regras absolutas, como tolerância zero a um sinal de pontuação, criam falsos positivos;
- incentivo a “imperfeições humanas” pode fabricar voz e reduzir qualidade;
- foco em detector pode deslocar o objetivo de melhoria editorial.

## Sobreposição

Sobrepõe-se ao fluxo anterior `editor-anti-aies`. Por isso, não será instalada como segunda Skill.

## Alterações incorporadas

O `editor-anti-aies` foi reconstruído como criação própria. Foram incorporados princípios gerais de cautela, especificidade e densidade, com um método novo de mapeamento de proposição e função para detectar redundância semântica em português. Não foram copiadas a lista de 53 padrões, a pontuação, os perfis de voz ou o CLI.

## Testes

Os casos de repetição técnica, paráfrase redundante, refrão intencional, amostra curta e fato duvidoso foram incluídos nos testes de aceitação da Skill própria.

## Atribuição

Referência metodológica: https://github.com/Aboudjem/humanizer-skill/blob/9a7f35b7b9ad8c3abd71f10757ec9f91fb8ae165/skills/humanizer/SKILL.md
