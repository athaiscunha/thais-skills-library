# Skills aprovadas

Este diretório contém somente Skills revisadas e prontas para uso.

## Catálogo

| Skill | Versão | Origem | Finalidade |
|---|---:|---|---|
| [`csc-marketing-context`](csc-marketing-context/) | 0.1.0 | criação própria | Contexto rastreável da Católica SC com documentos e checagem obrigatória do site oficial |
| [`csc-paid-media-copy`](csc-paid-media-copy/) | 0.3.0 | criação própria | Copy de mídia paga da Católica SC para Meta Ads, Google Search e Performance Max |

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
- ter passado pela revisão de terceiros quando não for criação própria.

Skills da Católica SC também devem seguir [../docs/SOURCE_POLICY.md](../docs/SOURCE_POLICY.md): documentos são fontes formais, a consulta atual a `catolicasc.org.br` é obrigatória e integrações externas não fazem parte da arquitetura.

Antes de adicionar uma Skill externa, siga [../docs/THIRD_PARTY_REVIEW.md](../docs/THIRD_PARTY_REVIEW.md).
