# Sincronização entre as duas máquinas

O repositório remoto é a fonte de verdade. Não edite a cópia instalada pelo Codex: toda melhoria nasce em `skills/`, passa por revisão e chega à branch `main`.

## Atualizar uma máquina

Na máquina que precisa receber a versão nova, abra uma tarefa no Codex e cole:

> Atualize o marketplace privado `thais-skills` a partir da branch `main` de `athaiscunha/thais-skills-library`, reinstale ou atualize o plugin `thais-skills-library`, valide as sete Skills e me avise quando eu puder abrir uma nova tarefa para usá-las. Não instale Skills de terceiros.

Depois da confirmação, abra uma tarefa nova. Skills e plugins são carregados no início da tarefa, por isso uma conversa que já estava aberta pode continuar usando a versão anterior.

## Comandos equivalentes

```sh
codex plugin marketplace upgrade thais-skills
codex plugin add thais-skills-library@thais-skills
```

Se o marketplace tiver sido cadastrado a partir de uma cópia local autenticada, primeiro atualize essa cópia a partir de `main` e depois reinstale o plugin.

## Ao melhorar uma Skill

1. Edite somente a versão canônica em `skills/<nome-da-skill>/`.
2. Gere novamente o pacote instalável:

   ```sh
   python3 scripts/sync_plugin_bundle.py
   ```

3. Execute a validação:

   ```sh
   python3 evals/run_static_checks.py
   ```

4. Publique por branch e PR.
5. Depois do merge em `main`, atualize o plugin nas duas máquinas com o pedido acima.

O diretório `plugins/thais-skills-library/skills/` é uma cópia de distribuição gerada. Não deve ser editado à mão; a validação reprova qualquer divergência em relação a `skills/`.

## Regras para evitar versões diferentes

1. `main` é a única versão aprovada para uso cotidiano.
2. Faça a mudança primeiro no repositório, nunca na instalação local.
3. Atualize as duas máquinas depois de cada versão publicada.
4. Se o Codex não enxergar a mudança, abra uma tarefa nova antes de diagnosticar a instalação.
5. Em caso de conflito, não force nem sobrescreva: compare as versões e preserve a fonte revisada.
