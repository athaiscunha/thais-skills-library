# Estado manual do radar

## Finalidade

Manter continuidade entre rodadas sem conectar contas, monitorar plataformas ou transformar fatos temporais em regra da Skill. Usar um histórico fornecido pela usuária ou pelo projeto; não pressupor que a conversa atual contém todas as rodadas anteriores.

## Entrada mínima

Quando houver histórico, ler somente os campos necessários:

| Campo | Função |
|---|---|
| id | identificador estável da mecânica |
| mecânica | unidade repetida, sem depender do apelido ou áudio |
| primeira observação | data em que entrou no radar |
| última checagem | data da evidência mais recente |
| status anterior | usar, acompanhar, descartar, utilizada ou arquivada |
| decisão CSC | ação tomada e motivo |
| uso | data, editoria e link, quando publicado |
| dependências | áudio, pessoa, captação, aprovação ou fato |
| próxima revisão | condição que justificaria nova checagem |

Identificar a trend pela mecânica. Mudança de nome, áudio ou exemplo não cria item novo quando a estrutura continua igual.

## Regras de continuidade

- Não recomendar novamente item utilizado sem virada substantiva.
- Não transformar `descartada` em proibição permanente; reabrir somente quando evidência, risco ou aplicação mudar.
- Atualizar estágio e validade com evidência nova, sem apagar a leitura anterior.
- Distinguir `não encontrada no histórico fornecido` de `nunca utilizada`.
- Se nenhum histórico for fornecido, declarar a limitação e não afirmar ausência de repetição.
- Não alterar arquivo de histórico sem solicitação explícita.

## Bloco de atualização

Quando a usuária pedir continuidade ou registro, devolver ao fim da rodada um bloco pronto para incorporar ao histórico:

```text
id:
mecânica:
primeira observação:
última checagem:
status anterior:
status atual:
evidência que mudou:
decisão CSC:
uso ou motivo de descarte:
dependências:
próxima revisão:
```

Registrar links e datas no relatório da rodada. No histórico, preservar somente o necessário para reconhecer, comparar e decidir; não copiar toda a pesquisa.

## Dados e segurança

Não guardar credenciais, cookies, conteúdo privado, nomes de contas pessoais, dados sensíveis ou material sem autorização. Usar links públicos e descrições mínimas. Se um exemplo deixar de ser acessível, manter data, plataforma e síntese da mecânica com a limitação registrada.
