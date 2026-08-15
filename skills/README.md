# Skills aprovadas

Este diretório contém somente Skills revisadas e prontas para uso.

## Catálogo

| Skill | Versão | Origem | Finalidade |
|---|---:|---|---|
| [`csc-marketing-context`](csc-marketing-context/) | 0.1.0 | criação própria | Contexto rastreável da Católica SC com documentos e checagem obrigatória do site oficial |
| [`csc-paid-media-copy`](csc-paid-media-copy/) | 0.3.0 | criação própria | Copy de mídia paga da Católica SC para Meta Ads, Google Search e Performance Max |
| [`editor-anti-aies`](editor-anti-aies/) | 0.1.0 | criação própria; reconstrução do fluxo anterior | Revisão e redação anti-AIês com preservação de voz e controle de redundância semântica |
| [`csc-channel-strategy`](csc-channel-strategy/) | 0.1.0 | criação própria | Estratégia de canais, sistema editorial, planejamento e medição sem integrações |
| [`csc-seo-blog`](csc-seo-blog/) | 0.1.0 | criação própria | Pesquisa, brief, redação e revisão de artigos SEO com fontes e consulta obrigatória ao site |
| [`csc-trends-radar`](csc-trends-radar/) | 0.1.0 | criação própria | Descoberta e triagem manual de trends atuais com evidência, risco e aplicação à CSC |
| [`csc-social-content`](csc-social-content/) | 0.1.0 | criação própria | Conteúdo orgânico pronto para produção, com narrativa, editorias recorrentes, fontes e controle de repetição |

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
