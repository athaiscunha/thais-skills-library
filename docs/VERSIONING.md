# Versionamento e convenções

## Fonte oficial

- `main` representa a versão mais recente revisada e utilizável.
- Mudanças incompletas ou experimentais não devem permanecer em `main`.
- Versões estáveis da biblioteca recebem tags no formato `vMAJOR.MINOR.PATCH`.

## SemVer

- **PATCH**: correção ou esclarecimento sem alterar o comportamento esperado.
- **MINOR**: nova Skill ou capacidade compatível.
- **MAJOR**: mudança incompatível que exige adaptação ou reinstalação.

Exemplos: `v0.1.0`, `v0.2.0`, `v1.0.0`.

Enquanto a biblioteca estiver sendo montada, use versões `0.x.y`. A primeira biblioteca estável pode receber `v1.0.0`.

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
feat(csc-seo): adicionar fluxo de auditoria
fix(csc-paid-media): impedir afirmações sem fonte
docs: explicar sincronização da segunda máquina
security(skill-name): remover chamada externa desnecessária
```

## Mudanças em uma Skill

A pasta da Skill deve permanecer autocontida. Se uma alteração muda o modo de usar a Skill, registre a migração no próprio `SKILL.md` ou em `references/`.
