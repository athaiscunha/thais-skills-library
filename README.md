# Thais Skills Library

Repositório privado que funciona como **fonte de verdade** para as Skills pessoais e compartilhadas usadas nas duas máquinas.

As Skills instaladas localmente são cópias de trabalho. A versão oficial é sempre a que está neste repositório, na branch `main`.

## Estrutura

```text
.
├── README.md
├── docs/
│   ├── INSTALLATION.md
│   ├── SYNC.md
│   ├── THIRD_PARTY_REVIEW.md
│   └── VERSIONING.md
├── reviews/
│   ├── README.md
│   └── <nome-da-skill>.md
└── skills/
    ├── README.md
    └── <nome-da-skill>/
```

Cada Skill aprovada fica em:

```text
skills/<nome-da-skill>/
├── SKILL.md
├── scripts/       # opcional
├── references/    # opcional
├── assets/        # opcional
└── agents/
    └── openai.yaml # opcional
```

O arquivo `SKILL.md` é obrigatório e deve conter, no mínimo, `name` e `description`. Essa estrutura segue a [documentação oficial de Skills](https://developers.openai.com/codex/skills).

## Regras da biblioteca

1. `main` contém somente versões revisadas e utilizáveis.
2. Toda mudança nasce neste repositório; depois é sincronizada nas duas máquinas.
3. Cada Skill deve ter um propósito claro e não duplicar outra sem justificativa.
4. Nenhuma Skill de terceiros entra em `skills/` antes da revisão descrita em [docs/THIRD_PARTY_REVIEW.md](docs/THIRD_PARTY_REVIEW.md).
5. Nunca armazenar senhas, tokens, chaves de API, arquivos pessoais ou dados sensíveis.
6. Mudanças incompatíveis devem ser documentadas e versionadas.

## Começar

- Primeira instalação em cada máquina: [docs/INSTALLATION.md](docs/INSTALLATION.md)
- Rotina para manter as duas máquinas iguais: [docs/SYNC.md](docs/SYNC.md)
- Convenções de commits e versões: [docs/VERSIONING.md](docs/VERSIONING.md)
- Avaliação de Skills externas: [docs/THIRD_PARTY_REVIEW.md](docs/THIRD_PARTY_REVIEW.md)

## Skills disponíveis

- [`csc-paid-media-copy`](skills/csc-paid-media-copy/): criação, revisão e validação de copy de mídia paga da Católica SC para Meta Ads, Google Search e Performance Max.

Nenhuma Skill de terceiros está instalada. Ideias externas só entram depois de revisão, seleção e reescrita para o nosso contexto.
