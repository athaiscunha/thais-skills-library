# Sincronização entre as duas máquinas

O repositório remoto é a fonte de verdade. Não edite a cópia instalada pelo Codex. Melhorias nas Skills da biblioteca nascem em `skills/`; melhorias no auditor SEO nascem em `plugins/seo-auditor-phd/`. Toda mudança passa por revisão e chega à branch `main` antes de ser sincronizada nas máquinas.

## Atualizar uma máquina

Na máquina que precisa receber a versão nova, abra uma tarefa no Codex e cole:

> Atualize o marketplace `thais-skills` a partir da branch `main` de `athaiscunha/thais-skills-library`, reinstale ou atualize os plugins `thais-skills-library` e `seo-auditor-phd`, valide as nove Skills e me avise quando eu puder abrir uma nova tarefa para usá-las. Não instale Skills de terceiros.

A versão `1.1.0` da biblioteca acrescenta `editais-cultura`; atualizar esse pacote é suficiente para receber a nova Skill, sem reinstalar o auditor SEO quando ele não mudou.

Depois da confirmação, abra uma tarefa nova. Skills e plugins são carregados no início da tarefa, por isso uma conversa que já estava aberta pode continuar usando a versão anterior.

## Comandos equivalentes

```sh
codex plugin marketplace upgrade thais-skills
codex plugin add thais-skills-library@thais-skills
codex plugin add seo-auditor-phd@thais-skills
```

Como o repositório é público, a instalação não depende de autenticação para leitura. O marketplace do repositório continua usando `source: local` porque o caminho do plugin é relativo à cópia instalada do próprio marketplace.

## Ao melhorar uma Skill da biblioteca

1. Edite somente a versão canônica em `skills/<nome-da-skill>/`.
2. Gere novamente o pacote instalável:

   ```sh
   python3 scripts/sync_plugin_bundle.py
   ```

3. Execute a validação:

   ```sh
   python3 evals/run_static_checks.py
   ```

4. Publique por branch e PR quando o fluxo exigir revisão; mudanças já aprovadas podem ser aplicadas diretamente à `main` conforme a política do repositório.
5. Depois da mudança em `main`, atualize o plugin nas duas máquinas com o pedido acima.

O diretório `plugins/thais-skills-library/skills/` é uma cópia de distribuição gerada. Não deve divergir de `skills/`; a validação deve reprovar qualquer diferença.

## Ao melhorar o SEO Auditor PhD

1. Edite somente `plugins/seo-auditor-phd/`; não altere a cópia instalada pelo Codex.
2. Execute os testes do analisador:

   ```sh
   python3 -m unittest discover -s plugins/seo-auditor-phd/tests -v
   ```

3. Execute `python3 evals/run_static_checks.py` e o validador oficial de plugins disponível no ambiente Codex.
4. Atualize a versão em `plugins/seo-auditor-phd/.codex-plugin/plugin.json` quando houver mudança de comportamento.
5. Publique a mudança na `main` e, em cada máquina, atualize o marketplace e reinstale `seo-auditor-phd@thais-skills`.

## Regras para evitar versões diferentes

1. `main` é a única versão aprovada para uso cotidiano.
2. Faça a mudança primeiro no repositório, nunca na instalação local.
3. Atualize nas duas máquinas somente os plugins afetados por cada versão publicada.
4. Se o Codex não enxergar a mudança, abra uma tarefa nova antes de diagnosticar a instalação.
5. Em caso de conflito, não force nem sobrescreva: compare as versões e preserve a fonte revisada.
