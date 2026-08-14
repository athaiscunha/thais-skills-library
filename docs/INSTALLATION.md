# Instalação em uma máquina

Repita este procedimento nas duas máquinas. O GitHub guarda a versão oficial; cada computador mantém um clone local e atalhos para as Skills aprovadas.

## Pré-requisitos

- Git instalado.
- Acesso ao repositório privado `athaiscunha/thais-skills-library`.
- Codex desktop, CLI ou extensão.

## 1. Clonar a biblioteca

Com SSH configurado no GitHub:

```sh
mkdir -p "$HOME/Documents/Skills"
git clone git@github.com:athaiscunha/thais-skills-library.git "$HOME/Documents/Skills/thais-skills-library"
```

Ou com HTTPS:

```sh
mkdir -p "$HOME/Documents/Skills"
git clone https://github.com/athaiscunha/thais-skills-library.git "$HOME/Documents/Skills/thais-skills-library"
```

## 2. Disponibilizar as Skills ao Codex

A documentação oficial informa que Skills pessoais podem ser descobertas em `$HOME/.agents/skills` e que pastas de Skills podem ser links simbólicos.

Depois que houver Skills aprovadas em `skills/`, execute:

```sh
mkdir -p "$HOME/.agents/skills"

for skill_dir in "$HOME/Documents/Skills/thais-skills-library"/skills/*; do
  [ -f "$skill_dir/SKILL.md" ] || continue
  skill_name="$(basename "$skill_dir")"
  ln -sfn "$skill_dir" "$HOME/.agents/skills/$skill_name"
done
```

Esse comando cria um atalho para cada Skill; não duplica os arquivos. Quando o clone for atualizado, o Codex passa a usar a versão nova.

## 3. Verificar

- No Codex CLI ou na extensão, use `/skills` ou digite `$` para procurar a Skill.
- Se uma alteração não aparecer, reinicie o Codex.

## Segunda máquina

Repita exatamente os três passos. Não copie pastas manualmente entre computadores: clone o mesmo repositório e mantenha cada clone atualizado conforme [SYNC.md](SYNC.md).

Fonte: [documentação oficial de Skills do Codex](https://developers.openai.com/codex/skills).
