# Skills aprovadas

Este diretório contém somente Skills revisadas e prontas para uso.

No estado inicial, ele não contém nenhuma Skill executável.

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

Antes de adicionar uma Skill externa, siga [../docs/THIRD_PARTY_REVIEW.md](../docs/THIRD_PARTY_REVIEW.md).
