# Google Ads | Performance Max

## Escolher o modelo de campos

O Google documenta atualmente um pool de 2 a 5 descrições de até 90 caracteres. Algumas interfaces, exports ou modelos operacionais ainda separam uma descrição curta de 60 caracteres e descrições longas de 90.

Inferir pelo pedido:

- `descrições`: usar o modelo atual unificado;
- `descrição curta` e `descrições longas`: usar o modelo separado;
- campos fornecidos em planilha ou mídia plan: preservar exatamente o modelo recebido;
- ausência de campo claro: usar o modelo atual unificado.

## Modelo atual unificado

| Campo | Mínimo | Máximo | Limite |
|---|---:|---:|---:|
| Títulos curtos | 3 | 15 | 30 caracteres |
| Títulos longos | 1 | 5 | 90 caracteres |
| Descrições | 2 | 5 | 90 caracteres |
| Nome da empresa | 1 | 1 | 25 caracteres |
| Caminhos | — | 2 | 15 caracteres cada |

Para `banco completo`, usar 15 títulos curtos, 5 títulos longos e 5 descrições, salvo template atual diferente.

## Modelo separado

Quando o pedido nomear os campos dessa forma:

| Campo | Volume padrão | Limite |
|---|---:|---:|
| Títulos curtos | 15 | 30 caracteres |
| Títulos longos | 5 | 90 caracteres |
| Descrição curta | 1 | 60 caracteres |
| Descrições longas | 4 | 90 caracteres |
| Nome da empresa | 1 | 25 caracteres |

Não converter silenciosamente um modelo no outro.

## Títulos curtos

- Aplicar Title Case.
- Incluir ao menos um título de até 15 caracteres quando houver formulação natural.
- Fazer cada título funcionar sozinho.
- Variar produto, aplicação, conteúdo, modalidade, diferencial, prova, marca, oferta e CTA conforme os fatos.
- Não multiplicar a mesma keyword sem nova função.

## Títulos longos

- Aplicar Title Case.
- Usar o espaço para acrescentar uma segunda camada de significado.
- Fazer sentido sem uma descrição ao lado.
- Evitar título curto alongado com abstração.

## Descrições

- Encerrar com pontuação.
- Fazer cada uma ser autossuficiente.
- Diversificar aplicação, conteúdo, logística, prova, condição e ação.
- Evitar que todas sejam versões da oferta.
- No modelo separado, tratar a descrição curta como síntese complementar, não slogan vazio.

## Nome da empresa e caminhos

- Usar `Católica SC` quando o nome da empresa for solicitado e compatível com a verificação do anunciante.
- Não inventar variações promocionais da marca.
- Tratar caminhos como exibição, sem inventar estrutura real de URL.

## Combinação

Testar títulos e descrições sem vizinho fixo. Rejeitar sequência com excesso de CTA, oferta, modalidade ou nome do produto. Considerar que um título longo pode aparecer sem descrição.

## Saída

Exibir a contagem correspondente a cada campo. Remover contagens apenas quando a usuária pedir versão limpa.

## Fontes oficiais consultadas

GOOGLE. *Performance Max campaigns specs and format requirements*. Google Ads Help, [s.d.]. Disponível em: <https://support.google.com/google-ads/answer/17091269>. Acesso em: 13 ago. 2026.

GOOGLE. *Set up your asset group and assets*. Google Ads Help, [s.d.]. Disponível em: <https://support.google.com/google-ads/answer/15865236>. Acesso em: 13 ago. 2026.
