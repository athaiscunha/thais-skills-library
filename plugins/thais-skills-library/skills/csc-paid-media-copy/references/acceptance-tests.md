# Testes de aceitação

Usar em mudanças da skill e auditorias do método.

## Sumário

- Meta e recombinação
- Google Search e Performance Max
- Fontes, produtos e voz
- Iteração com dados
- Validação técnica e atualidade

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
- contar texto após normalização Unicode NFC;
- sair com código diferente de zero.

## L | Iteração com dados comparáveis

Dado um conjunto identificado de assets da mesma campanha, com período, exposição, conversões e métrica decisória, aprovar somente se a skill:

- separar padrões observados de explicações hipotéticas;
- distinguir conceito, execução e campo;
- estender ao menos um sinal promissor sem produzir apenas paráfrases;
- preservar uma hipótese exploratória sustentada;
- devolver copy pronta e validada, não apenas análise.

## M | Dados insuficientes ou incomparáveis

Dado um ranking sem volume de exposição, ou assets de públicos, ofertas e formatos diferentes, aprovar somente se a skill:

- não declarar vencedor nem causalidade;
- nomear a limitação relevante;
- usar os dados apenas como pista descritiva;
- pedir somente o dado que mudaria materialmente a próxima rodada;
- continuar por um caminho seguro quando houver fatos suficientes para criar copy.

## N | Briefing completo e site obrigatório

Dado um briefing com todos os campos necessários, aprovar somente se a skill:

- consultar a página oficial mais específica em `catolicasc.org.br`;
- registrar internamente URL e data;
- comparar nome, modalidade, oferta, vigência, local e CTA;
- não esconder divergência entre documento e página pública;
- marcar a saída como rascunho sem validação de atualidade se o site estiver indisponível.

## O | Especificação de plataforma sujeita a mudança

Dado um pedido cuja quantidade, limite, fixação ou modelo de campos seja material, aprovar somente se a Skill:

- priorizar o template atual fornecido pela usuária;
- consultar a documentação oficial vigente quando não houver modelo suficiente;
- distinguir padrão operacional da conta de limite técnico universal;
- declarar a referência datada usada quando a fonte atual estiver indisponível;
- não sobrescrever silenciosamente o modelo do briefing com uma tabela antiga da Skill.
