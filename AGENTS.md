# Instruções para agentes e contribuidores

Este repositório é a fonte de verdade pública das Skills e dos plugins da Thaís. A branch `main` deve permanecer instalável, validada e livre de credenciais.

## Onde editar

- Para uma das Skills canônicas da biblioteca, edite `skills/<nome-da-skill>/` e depois execute `scripts/sync_plugin_bundle.py`.
- Para um plugin independente, edite somente `plugins/<nome-do-plugin>/`. A cópia instalada pelo Codex nunca é a fonte de verdade.
- Cada plugin em `plugins/` deve ter uma entrada de mesmo nome em `.agents/plugins/marketplace.json`; cada entrada deve apontar para `./plugins/<nome-do-plugin>`.
- Não altere arquivos de cache ou metadados locais de instalação.

## Requisitos de qualidade

- Preserve o nome em lower-case hyphen-case na pasta, no manifesto e no frontmatter da Skill.
- Mantenha `.codex-plugin/plugin.json` válido e atualize a versão SemVer quando o comportamento distribuído mudar.
- Inclua testes proporcionais ao risco e exemplos que não dependam de dados privados.
- Não invente métricas, resultados de testes ou compatibilidade não verificada.
- Não armazene tokens, chaves, cookies, dados pessoais, relatórios privados nem conteúdo protegido sem autorização.
- Documente como instalar, atualizar e testar qualquer capacidade nova.

## Antes de publicar

Execute, na raiz:

```sh
python3 evals/run_static_checks.py
```

Se uma Skill canônica mudou, execute antes:

```sh
python3 scripts/sync_plugin_bundle.py
```

Também execute o validador oficial de plugins para cada pacote alterado e os testes próprios desse pacote. Não faça commit ou push enquanto houver falha conhecida sem documentar e resolver a causa.

O fluxo completo para incluir novas capacidades está em `docs/ADDING_SKILLS_AND_PLUGINS.md`.
