# Revisão: marketingskills — conteúdo, social e edição

- Origem: Corey Haines / `coreyhaines31/marketingskills`
- Repositório: https://github.com/coreyhaines31/marketingskills
- Commit de referência: `7868cb9251fad80a73d26e488a5ad5f6c4a9f335`
- Arquivos analisados: `skills/content-strategy/SKILL.md` (`3a54e3f7b0b23d35d1e4c7f2f608fa947d19061f`), `skills/social/SKILL.md` (`ab1d083ef4a9dd2a91c1eaedfb5cb745c3055d24`) e `skills/copy-editing/SKILL.md` (`33110f4bb1be5f2152f838d95191705328760ddd`)
- Licença: MIT
- Data: 2026-08-14
- Revisor: Codex, a pedido da proprietária do repositório
- Decisão: somente referência

## Finalidade

Biblioteca ampla de marketing. O recorte analisado trata de estratégia de conteúdo, social orgânico e revisão por passes.

## Escopo da revisão

Foram analisados os três `SKILL.md` selecionados e a licença. Referências, scripts e demais Skills do repositório não foram auditados para instalação.

## Ideias aproveitáveis

- carregar o contexto de marca antes de planejar;
- separar estratégia ampla, execução social e edição;
- associar pilares a objetivo, necessidade de público e matéria-prima;
- planejar reaproveitamento a partir de uma peça de origem;
- revisar em passes focados, preservando mensagem e voz;
- relacionar calendário à capacidade de produção.

## Riscos e incompatibilidades

- orientação centrada em SaaS e geração de leads não representa uma instituição comunitária de ensino;
- frequências fixas por plataforma envelhecem e ignoram capacidade;
- fórmulas de hook e emoção podem produzir voz genérica ou exagerada;
- parte do listening depende de navegação, comandos e fontes externas não desejadas;
- a Skill social mistura estratégia, redação, calendário, listening e análise em um escopo amplo demais para nossa arquitetura.

## Sobreposição

Os métodos se distribuem entre `csc-channel-strategy`, `csc-trends-radar`, `csc-seo-blog` e `editor-anti-aies`. Instalar o pacote criaria gatilhos sobrepostos.

## Alterações incorporadas

- o contexto passou a ser fornecido por `csc-marketing-context`, com site oficial obrigatório;
- estratégia, radar, SEO e revisão foram separados;
- benchmarks e frequências fixas foram substituídos por capacidade e hipóteses;
- integrações e rotinas de social listening foram excluídas;
- o reaproveitamento exige função distinta por canal, não simples cópia.

## Testes

Foram adicionados casos de canal sem função, frequência sem dados, pilares sinônimos, calendário sem estratégia e redação solicitada no lugar errado.

## Atribuição

- https://github.com/coreyhaines31/marketingskills/blob/7868cb9251fad80a73d26e488a5ad5f6c4a9f335/skills/content-strategy/SKILL.md
- https://github.com/coreyhaines31/marketingskills/blob/7868cb9251fad80a73d26e488a5ad5f6c4a9f335/skills/social/SKILL.md
- https://github.com/coreyhaines31/marketingskills/blob/7868cb9251fad80a73d26e488a5ad5f6c4a9f335/skills/copy-editing/SKILL.md
