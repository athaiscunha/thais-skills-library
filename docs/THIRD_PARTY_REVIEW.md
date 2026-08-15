# Revisão de Skills de terceiros

Nenhuma Skill externa pode ser copiada diretamente para `skills/`. Primeiro ela deve ser analisada e registrada em `reviews/`.

## 1. Identificar a origem

Registre:

- nome e finalidade;
- autor ou organização;
- URL do repositório;
- tag ou commit exato analisado;
- licença;
- data da revisão;
- arquivos incluídos.

Sem licença clara, a Skill não deve ser redistribuída neste repositório.

## 2. Ler todos os arquivos

A revisão inclui `SKILL.md`, scripts, referências, assets, configurações e arquivos ocultos relevantes. Não execute scripts antes de entender o que fazem.

## 3. Verificar segurança

Procure especialmente por:

- leitura ou envio de senhas, tokens, cookies, histórico ou arquivos pessoais;
- chamadas de rede e destinos externos não necessários;
- comandos destrutivos ou que alterem grandes áreas do computador;
- instalação silenciosa de programas ou dependências;
- instruções que tentem ignorar permissões, políticas ou pedidos da usuária;
- conteúdo que peça para copiar, publicar ou transmitir dados sem autorização;
- código ofuscado, downloads dinâmicos ou execução remota;
- permissões mais amplas que a finalidade declarada;
- publicidade obrigatória, respostas roteirizadas sobre prompts do sistema ou instruções sem relação com a finalidade declarada.

## 4. Verificar qualidade e sobreposição

Confirme que:

- o gatilho da `description` é claro;
- a Skill resolve uma tarefa específica;
- as instruções possuem entradas, passos e saída definidos;
- ela não duplica nem contradiz uma Skill existente;
- dependências e limitações estão documentadas;
- exemplos não carregam dados, marcas ou fatos desatualizados como regras gerais.

## 5. Adaptar e testar

Quando a ideia for aproveitável:

1. preserve atribuição e licença;
2. remova componentes desnecessários;
3. limite permissões e escopo;
4. adapte linguagem, nomenclatura e fluxo;
5. teste chamadas explícitas e implícitas;
6. verifique pelo menos um caso normal e um caso que não deve ativar a Skill.

## 6. Registrar a decisão

Use uma destas decisões:

- **aprovada:** pode ser adicionada como revisada;
- **aprovada com alterações:** somente a versão adaptada e retestada pode ser adicionada;
- **somente referência:** ideias podem ser reexpressas, mas a Skill não foi aprovada para instalação;
- **rejeitada:** não instalar nem copiar.

Crie `reviews/<nome-da-skill>.md` com este modelo:

```markdown
# Revisão: <nome>

- Origem:
- Commit ou tag:
- Licença:
- Data:
- Revisor:
- Decisão: aprovada | aprovada com alterações | somente referência | rejeitada

## Finalidade

## Arquivos analisados

## Riscos encontrados

## Sobreposição com Skills existentes

## Alterações realizadas

## Testes

## Observações e atribuição
```

Somente uma decisão **aprovada** ou **aprovada com alterações** permite criar a pasta correspondente em `skills/`.
