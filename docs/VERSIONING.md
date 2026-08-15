# Versionamento e convenções

## Fonte oficial

- `main` representa a versão mais recente revisada e utilizável.
- `skills/` contém as Skills canônicas.
- `plugins/thais-skills-library/skills/` é o pacote de distribuição gerado a partir das Skills canônicas.
- Mudanças incompletas ou experimentais não devem permanecer em `main`.
- Versões estáveis da biblioteca podem receber tags no formato `vMAJOR.MINOR.PATCH`.

## SemVer

O campo `version` de `plugins/thais-skills-library/.codex-plugin/plugin.json` usa versionamento semântico:

- **PATCH**: correção ou esclarecimento sem alterar o comportamento esperado.
- **MINOR**: nova Skill ou capacidade compatível.
- **MAJOR**: mudança incompatível que exige adaptação ou reinstalação.

Exemplos: `1.0.1`, `1.1.0`, `2.0.0`.

A versão `1.0.0` identifica o primeiro pacote estável com as sete Skills validadas. A versão deve ser atualizada no mesmo PR que muda o comportamento distribuído.

## Mensagens de commit

Use mensagens curtas no formato:

```text
tipo(escopo): descrição
```

Tipos recomendados:

- `feat`: nova Skill ou capacidade.
- `fix`: correção de comportamento.
- `docs`: documentação.
- `refactor`: reorganização sem mudança de comportamento.
- `chore`: manutenção do repositório.
- `security`: correção ou endurecimento de segurança.

Exemplos:

```text
feat(csc-seo-blog): adicionar fluxo de auditoria
fix(csc-paid-media-copy): impedir afirmações sem fonte
docs: explicar sincronização da segunda máquina
security(skill-name): remover chamada externa desnecessária
```

## Antes de publicar

```sh
python3 scripts/sync_plugin_bundle.py
python3 evals/run_static_checks.py
```

A pasta da Skill deve permanecer autocontida. Se uma alteração muda o modo de usá-la, registre a migração no próprio `SKILL.md` ou em `references/`.
