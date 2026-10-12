# Validador determinístico de candidatura

Usar `scripts/validar_candidatura.py` para conferir um JSON local antes da revisão final. Requer Python 3.10 ou superior e somente a biblioteca padrão. Não instala pacotes, não usa rede e não altera a candidatura nem os anexos.

```powershell
python scripts/validar_candidatura.py caminho/para/candidatura.json
```

O relatório JSON vai para a saída padrão. Códigos de saída: **0** = nenhuma falha detectada nas verificações configuradas; **1** = falhas ou pendências; **2** = entrada/configuração inválida ou arquivo JSON inacessível. Erro de uso da linha de comando segue o comportamento padrão do `argparse` (código 2 e ajuda textual). Código 0 não significa habilitação, aprovação nem inscrição realizada.

## Preparar a entrada

Copiar `assets/candidatura-exemplo.json` para a pasta de trabalho da candidatura. O exemplo é **inteiramente fictício** e falha intencionalmente: há pendência explícita e falta um anexo real. Ele não estabelece limites, itens elegíveis ou exigências de qualquer edital.

1. Ler edital, anexos e retificações vigentes. Substituir `regras.fonte` pela identificação precisa das fontes, versões e itens utilizados; manter o mapeamento por regra na matriz de conformidade da candidatura.
2. Configurar apenas regras comprovadas. Não tratar ausência de regra no JSON como ausência de obrigação no edital. As quatro seções `regras.fonte`, `regras.campos`, `regras.orcamento` e `regras.anexos` são obrigatórias; listas/objetos podem estar vazios quando isso for justificado.
3. Preencher `campos`, `orcamento`, `anexos` e `pendencias`. Manter toda informação não confirmada em `pendencias`; não retirar pendências apenas para obter código 0.
4. Executar e corrigir as falhas; revisar os avisos e depois conferir os dados e arquivos efetivamente enviados ao portal.

## Esquema e significado

O JSON deve ter `versao: 1` e as cinco seções do exemplo. Chaves desconhecidas são recusadas, exceto nomes livres em `campos`, regras de campos e limites por categoria. Chaves JSON duplicadas também são recusadas. Nomes/IDs/fontes/categorias são sensíveis a maiúsculas e não são corrigidos automaticamente.

| Seção | Campos e comportamento |
|---|---|
| `regras.campos.NOME` | `obrigatorio` booleano obrigatório; `min_caracteres` e `max_caracteres` inteiros opcionais. Valores em `campos` devem ser texto. Campo obrigatório ausente, vazio ou só com espaços falha. Mínimo de campo opcional só é aplicado se ele estiver preenchido. |
| `regras.orcamento` | `fonte_solicitacao` texto obrigatório. `teto_solicitacao` e `teto_total` são limites absolutos opcionais. `categorias_permitidas` e `fontes_permitidas` são listas opcionais; quando informadas, rejeitam valores fora delas. |
| `regras.orcamento.limites_categoria` | Objeto opcional `{"categoria": "valor"}`. Cada teto absoluto se aplica à soma da categoria **em todas as fontes**. Não usar para regra cujo denominador ou alcance seja diferente. |
| `orcamento` | `valor_solicitado` e lista `itens` obrigatórios; `total_declarado` opcional para verificar a soma global. |
| `orcamento.itens[]` | `id`, `descricao`, `quantidade`, `valor_unitario`, `categoria`, `fonte` e `elegivel` obrigatórios. `total_declarado` opcional; compara com quantidade × unitário. IDs duplicados falham. |
| `elegivel` | Declaração de revisão externa: `true`, `false` ou `null`. `null` gera pendência impeditiva. `false` em item financiado pela fonte da solicitação gera erro. O script não decide elegibilidade. |
| `regras.anexos[]` | `id` e `obrigatorio` obrigatórios; `extensoes` e `max_bytes` opcionais. Extensões em minúsculas com ponto, por exemplo `[".pdf", ".jpg"]`. Tamanho em bytes; não confundir MB e MiB. |
| `anexos[]` | `id` e `caminho` obrigatórios. Caminho relativo à pasta do JSON. Não aceita caminho absoluto, unidade, `..` nem link que resolva fora dessa pasta. IDs duplicados, arquivo ausente, diretório, zero bytes, excesso de tamanho e extensão divergente geram erros. |
| `pendencias` | Lista obrigatória de textos; cada entrada vira um erro explícito. Vazia somente quando as pendências reais estiverem resolvidas. |

### Orçamento e fontes de financiamento

Usar números JSON ou, preferencialmente, strings decimais com ponto, como `"1234.56"`; não usar `R$`, vírgula decimal ou separador de milhar. Valores negativos, booleanos, `NaN` e infinito não são aceitos. O cálculo usa `Decimal`, sem conversão para ponto flutuante e sem arredondamento automático. Se o edital prescrever arredondamento, aplicar e documentar a regra antes da conferência. Quantidades fracionárias são permitidas.

O valor solicitado deve ser igual à soma dos itens com `elegivel: true` **e** `fonte` igual a `regras.orcamento.fonte_solicitacao`. Itens de recursos próprios/outras fontes integram o total do projeto, mas não a solicitação. Se uma despesa tiver financiamento compartilhado, dividir em linhas com IDs distintos, detalhando as parcelas e evitando duplicar o custo integral.

O teto da solicitação se aplica ao valor solicitado; o teto total, a todas as fontes. O script soma também por categoria e por fonte. Quando não consegue calcular um item, deixa totais dependentes como `null`, em vez de apresentar soma parcial como total. Elegibilidade pendente deixa a soma elegível como `null`. Valores declarados divergentes falham; o relatório conserva os totais calculados quando calculáveis. Quantidade/valor zero geram aviso, sem inventar proibição do edital.

Há somente um limite técnico para cada número de entrada: até 100 algarismos e expoente decimal entre −100 e 100. Não é limite financeiro do edital. Percentuais, tributos, contrapartidas mínimas, limites por função ou cruzamentos entre fontes não são inferidos: conferir separadamente e registrar pendências quando aplicável.

### Texto, anexos e relatório

A contagem de caracteres usa `len()` do Python: **pontos de código Unicode**, incluindo espaços e quebras, sem normalização. Não equivale necessariamente a grafemas visíveis, bytes ou unidades UTF-16. Emoji composto e letra com acento combinante podem produzir contagens diferentes no portal; CRLF também pode diferir de LF. O contador do formulário e a regra oficial precisam ser conferidos.

Extensão correta não demonstra formato real, legibilidade, integridade, validade, assinatura nem conteúdo do arquivo. O script inspeciona metadados locais; não abre PDF, não valida certificado, não examina documento pessoal e não confirma upload. Arquivo repetido em IDs diferentes gera aviso; `anexos_bytes` conta cada caminho resolvido uma vez. Campos e anexos sem regra geram avisos de cobertura incompleta.

O resultado contém `erros`, `avisos`, `verificacoes` e `total`. Cada erro/aviso identifica `codigo`, `caminho` no JSON e `mensagem`; valores monetários calculados saem como strings decimais. O relatório pode reproduzir textos de pendências, nomes e identificadores: tratá-lo com a mesma privacidade da candidatura.

**Limitação central:** o script não lê o edital para descobrir regras e não prova que a configuração está completa ou fiel. Não verifica mérito, orçamento de mercado, cronograma, acessibilidade efetiva, autenticidade, enquadramento legal, direitos autorais ou aderência territorial. Não atribui nota nem estima chance de seleção. Usar junto da matriz de conformidade, revisão documental e revisão crítica da candidatura.
