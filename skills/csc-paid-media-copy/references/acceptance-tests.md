# Testes de aceitação

Usar em mudanças da skill e auditorias do método.

## A | Meta Reels com cinco variações

Entrada: curso específico, Reel narrado, cartela final com oferta, cinco títulos, cinco textos e uma descrição.

Aprovar somente se:

- títulos e textos não forem pares fixos;
- houver ao menos três hipóteses sustentadas;
- oferta não colidir em título, texto, descrição e cartela;
- descrição funcionar com todos os títulos;
- textos forem econômicos;
- curso, modalidade e oferta forem factuais.

## B | Modalidade saturada

Se houver título `Aulas Online ao Vivo`, vários textos repetindo modalidade e descrição `Online ao vivo | 360h`, redistribuir funções antes de entregar.

## C | Oferta saturada

Se a cartela já trouxer 50% OFF na primeira mensalidade e 20% nas demais, permitir o reforço estratégico necessário em um asset. Não fazer o banco inteiro depender da condição.

## D | Search responsivo

Aprovar somente se:

- keyword aparecer onde melhorar relevância;
- títulos não forem 15 paráfrases;
- descrições acrescentarem informação;
- combinação de três títulos não acumular três CTAs ou ofertas;
- contagens estiverem corretas;
- eventual fixação estiver justificada.

## E | Performance Max em dois modelos

Testar um pedido com `descrições` e outro com `descrição curta + descrições longas`.

Aprovar somente se:

- a skill preservar o modelo do pedido;
- títulos longos acrescentarem significado;
- descrições forem autossuficientes;
- banco cobrir territórios diferentes sem quotas artificiais;
- recombinação não gerar repetição multicamada;
- volumes e limites corresponderem ao modelo escolhido.

## F | Informação temporal conflitante

Se site, campanha e briefing divergirem em data, turma, valor, modalidade ou prazo, usar a prioridade do `SKILL.md`. Havendo empate ou ambiguidade, suspender o dado e pedir confirmação.

## G | Revisão crítica

Dado um banco parcialmente bom, aprovar somente se a skill:

- preservar assets úteis;
- nomear problemas pelo efeito;
- devolver o banco inteiro corrigido;
- revisar combinações após as trocas;
- não confundir qualidade pré-veiculação com performance comprovada.

## H | Briefing insuficiente

Se faltarem dados para a terceira hipótese, usar somente territórios sustentados. Não inventar prova, benefício ou urgência.

## I | Escopo de produto

Executar um pedido de Pós e outro de Graduação.

Aprovar somente se:

- carregar as heurísticas de `product-pos.md` no primeiro;
- não transferir público, objeções ou benefícios da Pós para o segundo;
- exigir briefing ou fonte atual quando o outro produto não estiver documentado.

## J | Voz social

Dado um texto principal em que a instituição fala de si, aprovar somente se a Católica SC estiver em primeira pessoa do singular. Não exigir pronome em título nominal, pergunta ou comando.

## K | Contagem automatizada

Fornecer ao `scripts/audit_assets.py` uma linha válida, uma acima do limite e duas duplicadas.

Aprovar somente se o script:

- marcar corretamente a linha válida;
- falhar na linha acima do limite;
- detectar a duplicação normalizada;
- sair com código diferente de zero.
