# Sincronização entre as duas máquinas

O repositório remoto é a fonte de verdade. Antes de trabalhar em qualquer máquina, atualize o clone local.

## Antes de usar ou editar

```sh
cd "$HOME/Documents/Skills/thais-skills-library"
git switch main
git pull --ff-only
```

## Depois de editar uma Skill

```sh
git status
git add skills/<nome-da-skill>
git commit -m "feat(<nome-da-skill>): descrever a mudança"
git push origin main
```

Para mudanças apenas de documentação, use `docs:` no início da mensagem.

## Na outra máquina

```sh
cd "$HOME/Documents/Skills/thais-skills-library"
git switch main
git pull --ff-only
```

Como as Skills são ligadas por atalhos, não é necessário reinstalá-las depois do `git pull`. Reinicie o Codex somente se a mudança não aparecer.

## Regras para evitar conflitos

1. Sempre execute `git pull --ff-only` antes de editar.
2. Não edite a mesma Skill simultaneamente nas duas máquinas.
3. Faça commits pequenos e com uma intenção clara.
4. Envie a mudança ao GitHub antes de continuar na outra máquina.
5. Se o Git avisar sobre conflito, não force nem sobrescreva: revise as duas versões antes de resolver.
