# Versionamento e convenções

## Fonte oficial

- `main` representa a versão mais recente revisada e utilizável.
- `skills/` contém as Skills canônicas.
- `plugins/thais-skills-library/skills/` é o pacote de distribuição gerado a partir das Skills canônicas.
- `plugins/seo-auditor-phd/` é um plugin independente e autocontido; sua Skill, referências, testes e avaliações são mantidos diretamente nessa pasta.
- Mudanças incompletas ou experimentais não devem permanecer em `main`.
- Tags legadas no formato `vMAJOR.MINOR.PATCH` identificam a biblioteca. Para plugins independentes, prefira `<nome-do-plugin>-vMAJOR.MINOR.PATCH`, evitando colisão entre ciclos de versão.

## SemVer

O campo `version` de cada `plugins/<nome>/.codex-plugin/plugin.json` usa versionamento semântico e evolui de forma independente:

- **PATCH**: correção ou esclarecimento sem alterar o comportamento esperado.
- **MINOR**: nova Skill ou capacidade compatível.
- **MAJOR**: mudança incompatível que exige adaptação ou reinstalação.

Exemplos: `1.0.1`, `1.1.0`, `2.0.0`.

Exemplos de tags independentes: `thais-skills-library-v1.1.0` e `seo-auditor-phd-v0.2.0`.

A versão `1.0.0` identifica o primeiro pacote estável da biblioteca com as sete Skills validadas. O `seo-auditor-phd` começa em `0.1.0` enquanto sua interface e seus critérios de auditoria ainda podem evoluir. A versão do plugin afetado deve ser atualizada no mesmo PR que muda seu comportamento distribuído.

A biblioteca `1.1.0` acrescenta `editais-cultura` e passa a distribuir oito Skills canônicas; o plugin SEO Auditor mantém sua versão independente.

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
python3 -m unittest discover -s plugins/seo-auditor-phd/tests -v
```

A sincronização do bundle é obrigatória apenas quando uma Skill canônica muda. A pasta de cada Skill ou plugin deve permanecer autocontida. Se uma alteração muda o modo de usá-la, registre a migração no próprio `SKILL.md` ou em `references/`.

Para criar novos pacotes sem quebrar o marketplace, siga `docs/ADDING_SKILLS_AND_PLUGINS.md`. Cada plugin mantém sua própria versão; uma mudança em um pacote não exige incrementar os demais.
