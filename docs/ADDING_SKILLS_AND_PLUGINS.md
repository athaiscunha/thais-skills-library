# Como adicionar Skills e plugins

Este guia mantém o repositório escalável sem misturar fontes canônicas, cópias instaladas e pacotes de distribuição.

## 1. Escolha o tipo de inclusão

Use uma **Skill canônica da biblioteca** quando a capacidade fizer parte do conjunto compartilhado e deva ser instalada junto com `thais-skills-library`. Nesse caso, a fonte fica em `skills/<nome>/` e o bundle em `plugins/thais-skills-library/skills/` é gerado automaticamente.

Use um **plugin independente** quando a capacidade tiver ciclo de vida, versão, testes ou público próprios; quando reunir várias Skills relacionadas; ou quando puder ganhar scripts, assets, MCPs ou apps específicos. Nesse caso, a fonte de verdade fica diretamente em `plugins/<nome-do-plugin>/`.

Não mantenha a mesma Skill como fonte editável nos dois lugares.

## 2. Adicionar uma Skill à biblioteca

1. Crie `skills/<nome-em-hyphen-case>/SKILL.md` com frontmatter `name` e `description`.
2. Inclua `agents/openai.yaml` e `references/acceptance-tests.md`, conforme o contrato atual da biblioteca.
3. Roteie no `SKILL.md` todas as referências, scripts e assets usados.
4. Acrescente exatamente três casos a `evals/cases.json`: `activation`, `non_activation_or_failure` e `adversarial`.
5. Atualize a lista de Skills no `README.md`, em `docs/INSTALLATION.md` e onde houver uma contagem atual informativa. As regras e os validadores devem calcular a cobertura pelo número de Skills, sem congelar uma contagem fixa.
6. Gere novamente o pacote:

   ```sh
   python3 scripts/sync_plugin_bundle.py
   ```

7. Atualize a versão de `plugins/thais-skills-library/.codex-plugin/plugin.json`. Uma nova Skill normalmente é uma versão MINOR.
8. Execute a validação estática e os forward-tests proporcionais ao risco.

## 3. Adicionar um plugin independente

1. Use o `plugin-creator` disponível no Codex para criar o scaffold e a entrada de marketplace. A partir da raiz do repositório, o fluxo equivalente é:

   ```sh
   python <caminho-do-plugin-creator>/scripts/create_basic_plugin.py <nome-do-plugin> \
     --path plugins \
     --marketplace-path .agents/plugins/marketplace.json \
     --with-marketplace
   ```

2. Complete `plugins/<nome>/.codex-plugin/plugin.json` sem placeholders e mantenha `name` idêntico ao nome da pasta.
3. Coloque cada Skill em `plugins/<nome>/skills/<nome-da-skill>/` e mantenha referências e scripts dentro do pacote.
4. Inclua testes automatizados para transformações determinísticas e avaliações para decisões editoriais ou agentivas.
5. Documente o pacote em `README.md`, `plugins/README.md`, `docs/INSTALLATION.md` e `docs/SYNC.md`.
6. Execute:

   ```sh
   python3 evals/run_static_checks.py
   python <caminho-do-plugin-creator>/scripts/validate_plugin.py plugins/<nome-do-plugin>
   ```

7. Execute também os testes específicos do pacote. O comando deve ficar documentado no próprio plugin ou em `docs/EVALUATION.md`.

O helper do `plugin-creator` deve ser preferido para criar a entrada inicial do marketplace. Não edite a configuração instalada do Codex nem use a pasta de cache como fonte.

## 4. Checklist antes do commit

- [ ] Pasta, manifesto, entrada de marketplace e Skills usam os nomes corretos.
- [ ] O manifesto tem versão SemVer, descrição e caminhos que existem.
- [ ] Não há plugin órfão nem entrada de marketplace sem pacote.
- [ ] Não há segredos, dados privados, caches, `__pycache__` ou metadados locais de instalação.
- [ ] Documentação de instalação, atualização e uso foi revisada.
- [ ] Testes específicos passaram.
- [ ] `python3 evals/run_static_checks.py` passou sem erros.
- [ ] O validador oficial passou em todo plugin alterado.
- [ ] A versão foi atualizada quando houve mudança de comportamento.
- [ ] O diff foi revisado e não contém arquivos alheios à entrega.

## 5. Publicar e testar a instalação

Use commits no formato `tipo(escopo): descrição`. Depois que a mudança aprovada chegar à `main`, atualize o marketplace e reinstale somente o pacote afetado:

```sh
codex plugin marketplace upgrade thais-skills
codex plugin add <nome-do-plugin>@thais-skills
```

Abra uma tarefa nova para confirmar que Skills e ferramentas da versão publicada foram carregadas.
