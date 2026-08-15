# Skills aprovadas

Este diretório contém somente Skills revisadas e prontas para uso.

## Catálogo

| Skill | Versão | Origem | Finalidade |
|---|---:|---|---|
| [`csc-marketing-context`](csc-marketing-context/) | 0.2.0 | criação própria | Contexto rastreável da Católica SC com documentos, site oficial e contrato de passagem |
| [`csc-paid-media-copy`](csc-paid-media-copy/) | 0.4.0 | criação própria | Copy de mídia paga com validação de campos atuais, recombinação e contrato de passagem |
| [`editor-anti-aies`](editor-anti-aies/) | 0.2.0 | criação própria; reconstrução do fluxo anterior | Revisão anti-AIês com preservação de voz, invariantes e função recebidas de outras Skills |
| [`csc-channel-strategy`](csc-channel-strategy/) | 0.2.0 | criação própria | Estratégia de canais e briefs executáveis com passagem estruturada para produção |
| [`csc-seo-blog`](csc-seo-blog/) | 0.2.0 | criação própria | Pesquisa e redação SEO com pacote rastreável para desdobramento em outros canais |
| [`csc-trends-radar`](csc-trends-radar/) | 0.2.0 | criação própria | Radar manual com evidência, histórico entre rodadas e encaminhamento para execução |
| [`csc-social-content`](csc-social-content/) | 0.2.0 | criação própria | Conteúdo orgânico com bloqueio de ancoragem decorativa e briefing completo de produção |

## Convenção de pastas

Use nomes em minúsculas, no formato `kebab-case`:

```text
skills/<nome-da-skill>/
├── SKILL.md
├── scripts/       # opcional
├── references/    # opcional
├── assets/        # opcional
└── agents/
    └── openai.yaml # opcional
```

## Requisitos mínimos

Cada `SKILL.md` deve:

- começar com frontmatter YAML;
- declarar `name` e `description`;
- explicar quando deve e quando não deve ser acionada;
- ter instruções claras, imperativas e focadas em uma tarefa;
- declarar dependências e permissões necessárias;
- evitar segredos, dados pessoais e fatos temporários embutidos;
- manter `references/acceptance-tests.md` e passar pela suíte em `../evals/` quando houver mudança de comportamento;
- definir contrato de passagem quando a Skill recebe ou entrega trabalho a outra;
- ter passado pela revisão de terceiros quando não for criação própria.

Skills da Católica SC também devem seguir [../docs/SOURCE_POLICY.md](../docs/SOURCE_POLICY.md): documentos são fontes formais, a consulta atual a `catolicasc.org.br` é obrigatória e integrações externas não fazem parte da arquitetura.

Antes de adicionar uma Skill externa, siga [../docs/THIRD_PARTY_REVIEW.md](../docs/THIRD_PARTY_REVIEW.md).
