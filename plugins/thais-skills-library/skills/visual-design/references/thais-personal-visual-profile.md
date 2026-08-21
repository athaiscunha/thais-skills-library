# Perfil visual pessoal da Thais

## Ativação

Usar este perfil quando a usuária identificar a entrega como projeto pessoal, marca pessoal, trabalho autoral ou material pessoal sem uma identidade externa. Não ativar somente porque ela pediu que algo fosse feito “para mim”. Não ativar em trabalhos da Católica SC, de cliente, parceiro ou outra marca sem pedido explícito.

Se a frase “meu projeto” puder significar apenas “projeto sob minha gestão”, e a paleta alterar materialmente a entrega, confirmar em uma pergunta curta.

## Paleta canônica

Usar estes valores exatos como fonte de verdade:

| Token | Nome | Hex | Papel preferencial |
|---|---|---:|---|
| `magenta-acido` | Magenta ácido | `#FF00A8` | acento principal, ênfase, sinal, CTA e gesto expressivo |
| `verde-cerceta-acido` | Verde-cerceta ácido | `#00E0B2` | acento secundário, contraste, dado, estado e contraponto |
| `tinta` | Tinta | `#111111` | texto principal, fundo escuro, estrutura e alto contraste |
| `papel` | Papel | `#F7F4EE` | fundo claro principal e respiro |
| `cinza` | Cinza | `#6B6B6B` | texto secundário, legenda, linha e informação de apoio |

Tokens sugeridos para implementação:

```css
--thais-magenta-acido: #FF00A8;
--thais-verde-cerceta-acido: #00E0B2;
--thais-tinta: #111111;
--thais-papel: #F7F4EE;
--thais-cinza: #6B6B6B;
```

## Princípio de uso

Esta é uma paleta autoral de alto contraste entre base quase preta, papel quente e dois acentos ácidos. Preservar sua personalidade gráfica sem obrigar todas as cores a aparecerem em toda peça.

Usar normalmente:

- `papel` ou `tinta` como campo dominante;
- o outro como texto e estrutura;
- um ácido como acento dominante;
- o segundo ácido como contraponto seletivo;
- `cinza` para informação secundária, nunca para enfraquecer excessivamente a hierarquia.

Alternar qual ácido domina conforme o conteúdo e o formato. Não reduzir o perfil a uma fórmula fixa de fundo papel + título preto + detalhe magenta. Variar escala, proporção, recorte, tipografia e composição mantendo reconhecimento.

## Contraste verificado

Relações aproximadas WCAG entre as cores:

- `papel` / `tinta`: `17.20:1` — adequado para texto normal;
- `tinta` / `verde-cerceta-acido`: `11.06:1` — adequado para texto normal;
- `tinta` / `magenta-acido`: `5.23:1` — adequado para texto normal;
- `papel` / `cinza`: `4.85:1` — adequado para texto normal;
- `papel` / `magenta-acido`: `3.29:1` — usar apenas em texto grande ou elemento gráfico, não em corpo pequeno;
- `papel` / `verde-cerceta-acido`: `1.55:1` — não usar para texto;
- `magenta-acido` / `verde-cerceta-acido`: `2.12:1` — não usar como par texto/fundo;
- `tinta` / `cinza`: `3.54:1` — não usar para corpo pequeno; reservar a texto grande ou elementos não essenciais.

Preferir texto `tinta` sobre fundos ácidos. Sobre fundo `tinta`, `papel`, magenta e verde-cerceta funcionam com boa separação. Validar novamente se houver transparência, gradiente, imagem ou variação de cor.

## Derivações permitidas

- Criar tints misturando uma cor canônica com `papel` e shades com `tinta` quando o sistema exigir profundidade, estados ou séries.
- Identificar derivados como extensões, não como novas cores canônicas.
- Não introduzir novo matiz apenas para “completar” a paleta.
- Quando uma cor funcional externa for necessária — alerta, sucesso, dado categórico ou requisito de acessibilidade — usá-la de forma semântica, declarar a exceção e não transformá-la em cor de identidade.
- Evitar gradiente entre magenta e verde-cerceta como recurso automático; usar somente quando houver função conceitual e resultado cromático controlado.

## Linguagem visual associada

A paleta não determina sozinha a estética. Combiná-la ao padrão de minimalismo preciso:

- tipografia com presença e composição apurada;
- escala e espaço mais importantes que decoração;
- contraste ácido usado como pontuação, tensão ou campo expressivo;
- grid claro, com liberdade para assimetria intencional;
- imagens autorais, específicas ou fortemente editadas;
- poucos elementos recorrentes, com comportamento consistente;
- acabamento contemporâneo sem simular estética de startup, rave ou cyberpunk por causa das cores ácidas.

## Proibições de automatismo

- Não usar as duas cores ácidas em proporções iguais em toda peça.
- Não usar magenta para codificar “feminino” nem verde-cerceta para “tecnologia”.
- Não transformar toda interface em fundo preto com neon.
- Não adicionar roxo, azul-elétrico ou amarelo apenas por associação com a paleta.
- Não usar o cinza para texto essencial em fundo escuro.
- Não sacrificar legibilidade para preservar uma combinação.
- Não levar esta paleta para outro cliente sem autorização.

## Handoff do modo pessoal

Além dos arquivos usuais, registrar quais cores foram usadas como base, acento, texto e estado; listar derivados; incluir tokens; indicar combinações acessíveis; e sinalizar qualquer exceção funcional.
