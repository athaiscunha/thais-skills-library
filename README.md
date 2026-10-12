# Thais Skills Library

Repositório público que funciona como **fonte de verdade** para as Skills e os plugins pessoais e compartilhados usados nas duas máquinas.

As cópias instaladas localmente são apenas cópias de trabalho. A versão oficial é sempre a que está neste repositório, na branch `main`.

O marketplace **Skills da Thais** distribui dois pacotes independentes:

- **Biblioteca de Skills da Thais** (`thais-skills-library`): reúne as sete Skills aprovadas da biblioteca;
- **SEO Auditor PhD** (`seo-auditor-phd`): audita SEO on-page de páginas, LPs e sites, com diagnóstico priorizado, recomendações concretas e limites explícitos para dados não disponíveis.

Para instalar ou atualizar os pacotes em outra máquina, veja [docs/INSTALLATION.md](docs/INSTALLATION.md).

## Estrutura

```text
.
├── AGENTS.md                    # regras para agentes e contribuidores
├── README.md
├── docs/
│   ├── ADDING_SKILLS_AND_PLUGINS.md
│   ├── EVALUATION.md
│   ├── INSTALLATION.md
│   ├── SOURCE_POLICY.md
│   ├── SYNC.md
│   ├── THIRD_PARTY_REVIEW.md
│   └── VERSIONING.md
├── evals/
│   ├── cases.json
│   └── run_static_checks.py
├── .agents/plugins/marketplace.json
├── plugins/
│   ├── README.md
│   ├── thais-skills-library/
│   │   ├── .codex-plugin/plugin.json
│   │   └── skills/           # pacote gerado das sete Skills
│   └── seo-auditor-phd/
│       ├── .codex-plugin/plugin.json
│       ├── skills/seo-auditor-phd/
│       ├── tests/            # testes automatizados do analisador local
│       └── evals/            # exemplo auditado e revisão crítica
├── scripts/
│   └── sync_plugin_bundle.py
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
7. Skills da Católica SC não devem depender de integrações com ferramentas externas.
8. Documentos fornecidos são fontes formais, e `catolicasc.org.br` deve ser consultado em toda tarefa da Católica SC.
9. Informações temporais não devem ser congeladas como regras permanentes.
10. Toda mudança de comportamento deve passar pela validação estática e pelos casos de avaliação proporcionais ao risco.
11. Plugins independentes ficam em `plugins/<nome-do-plugin>/`, mantêm versão e testes próprios e precisam ter uma entrada correspondente no marketplace.

## Como usar

Depois que o plugin estiver instalado e carregado na superfície compatível, as Skills podem ser acionadas automaticamente pelo pedido ou selecionadas explicitamente.

- No ChatGPT, selecione a Skill pelo menu de `@` quando ela estiver disponível nessa superfície.
- No Codex, use `$nome-da-skill`, por exemplo `$csc-paid-media-copy`.
- Ao chamar apenas o plugin, o modelo pode escolher uma Skill interna por roteamento semântico, mas a seleção explícita é preferível quando você quer garantir qual Skill será usada.

## Começar

- Instalação da biblioteca e dos plugins: [docs/INSTALLATION.md](docs/INSTALLATION.md)
- Inclusão de novas Skills e plugins: [docs/ADDING_SKILLS_AND_PLUGINS.md](docs/ADDING_SKILLS_AND_PLUGINS.md)
- Rotina para manter as duas máquinas iguais: [docs/SYNC.md](docs/SYNC.md)
- Política de fontes da Católica SC: [docs/SOURCE_POLICY.md](docs/SOURCE_POLICY.md)
- Convenções de commits e versões: [docs/VERSIONING.md](docs/VERSIONING.md)
- Validação e testes das Skills: [docs/EVALUATION.md](docs/EVALUATION.md)
- Avaliação de Skills externas: [docs/THIRD_PARTY_REVIEW.md](docs/THIRD_PARTY_REVIEW.md)

## Skills disponíveis

- [`csc-marketing-context`](skills/csc-marketing-context/): consolidação e auditoria de contexto, documentos e fontes oficiais da Católica SC.
- [`csc-paid-media-copy`](skills/csc-paid-media-copy/): criação, revisão e validação de copy de mídia paga da Católica SC para Meta Ads, Google Search e Performance Max.
- [`editor-anti-aies`](skills/editor-anti-aies/): auditoria, redação e revisão de linguagem artificial ou redundante, sem atribuir autoria nem apagar a voz.
- [`csc-channel-strategy`](skills/csc-channel-strategy/): estratégia e planejamento de canais e conteúdo, com ênfase em social orgânico.
- [`csc-seo-blog`](skills/csc-seo-blog/): pesquisa, brief, redação e revisão editorial de artigos SEO da Católica SC.
- [`csc-trends-radar`](skills/csc-trends-radar/): radar manual e atual de trends com evidência, validade, risco e adaptação institucional.
- [`csc-social-content`](skills/csc-social-content/): criação e revisão de conteúdo orgânico, editorias recorrentes e briefings prontos para produção.

## Plugins disponíveis

- [`thais-skills-library`](plugins/thais-skills-library/): pacote de distribuição das sete Skills canônicas listadas acima.
- [`seo-auditor-phd`](plugins/seo-auditor-phd/): auditoria SEO on-page de URL ou conteúdo colado, com análise semântica, técnica e editorial, score heurístico por dimensão, plano de ação por impacto/esforço e indicação clara dos dados externos necessários.

Nenhuma Skill de terceiros está instalada. Ideias externas só entram depois de revisão, seleção e reescrita para o nosso contexto.
