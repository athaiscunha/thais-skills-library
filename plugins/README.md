# Plugins do marketplace Skills da Thais

Cada subpasta deste diretório é um pacote instalável e versionado de forma independente. O nome da pasta deve ser idêntico ao campo `name` de `.codex-plugin/plugin.json` e à entrada correspondente em `.agents/plugins/marketplace.json`.

## Contrato mínimo

```text
plugins/<nome-do-plugin>/
├── .codex-plugin/
│   └── plugin.json
└── skills/                     # quando o manifesto declarar "skills": "./skills/"
    └── <nome-da-skill>/
        └── SKILL.md
```

Um plugin pode incluir `references/`, `scripts/`, `assets/`, `agents/openai.yaml`, testes e avaliações dentro de sua própria pasta. Dependências externas, MCPs ou apps só devem ser adicionados quando forem realmente necessários, documentados e validados.

## Pacotes atuais

- `thais-skills-library`: bundle gerado das Skills canônicas de `skills/`, incluindo `editais-cultura` a partir da versão `1.1.0`; não editar a cópia interna manualmente.
- `seo-auditor-phd`: plugin independente e autocontido, com analisador local, testes e avaliações próprios.

## Regra de publicação

Nenhuma pasta em `plugins/` pode ficar sem entrada no marketplace, e nenhuma entrada do marketplace pode apontar para um pacote ausente. `python3 evals/run_static_checks.py` verifica essa correspondência automaticamente.

Veja `docs/ADDING_SKILLS_AND_PLUGINS.md` para o fluxo completo de criação, validação, versionamento e instalação.
