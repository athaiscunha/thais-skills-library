# Revisão crítica, inspeção e QA

## Sumário

- Regra central e gates de conteúdo, estrutura e direção de arte
- Uso real, acessibilidade e integridade técnica
- Testes críticos e inspeção obrigatória
- Parecer, handoff e critério de parada

## Regra central

Revisar o artefato como se fosse recebido de outro designer. Não defender a primeira solução. A avaliação deve produzir uma destas decisões por gate:

- **passa:** pronto naquele critério;
- **revisar:** há falha corrigível antes da entrega;
- **reprovar:** a direção ou estrutura precisa ser refeita.

Não usar nota média para compensar falha crítica. Um artefato bonito com conteúdo errado, ilegível ou tecnicamente quebrado é reprovado.

## Gate 1 — conteúdo e objetivo

Verificar:

- objetivo, público, CTA e contexto de uso estão claros;
- fatos, dados, nomes, datas, cursos e terminologia são corretos e rastreáveis;
- o conteúdo foi editado para o formato, sem omitir o necessário;
- a peça estabelece uma prioridade inequívoca;
- a solução ajuda a próxima decisão ou ação;
- hipóteses, placeholders e pendências estão identificados;
- o visual não promete prova, imagem ou dado que não existe.

Reprovar quando a peça depende de invenção, disfarça fragilidade estratégica ou não tem mensagem prioritária.

## Gate 2 — estrutura

Verificar:

- há uma ordem de leitura intencional;
- o grid organiza sem engessar;
- blocos, páginas, cards, cenas ou slides cumprem funções distintas;
- o conjunto tem ritmo, transições e continuidade;
- a densidade corresponde ao modo real de consumo;
- a repetição cria sistema e não monotonia;
- o conteúdo cabe sem compressão artificial;
- elementos recorrentes permanecem estáveis.

Reprovar quando tudo recebe o mesmo peso, quando a sequência parece um template preenchido ou quando a estrutura obriga o usuário a reconstruir o raciocínio.

## Gate 3 — julgamento óptico e direção de arte

Verificar:

- hierarquia percebida antes da leitura detalhada;
- tipografia adequada ao tom e tecnicamente controlada;
- alinhamentos ópticos, não apenas matemáticos;
- margens, intervalos, quebras e entrelinhas consistentes;
- contraste e cor têm função;
- imagens possuem intenção, qualidade, enquadramento e direitos adequados;
- elementos decorativos sobrevivem ao teste de remoção;
- composição tem tensão e equilíbrio, não apenas centralização e simetria;
- o resultado é específico para a CSC, o conteúdo e o público;
- o minimalismo resulta de edição rigorosa, não de vazio.

Reprovar quando a peça parece banco de template, quando “sofisticação” depende de clichês de luxo ou quando qualquer marca poderia substituir a CSC sem perda perceptível.

## Gate 4 — uso real e acessibilidade

Inspecionar no tamanho de uso, não apenas ampliado no editor.

Verificar:

- leitura em celular, projetor, tela, impressão ou feed conforme o destino;
- tamanho mínimo e contraste suficientes;
- áreas seguras, cortes, sangrias e proporções corretas;
- gráficos não dependem apenas de cor;
- legendas, rótulos e CTAs permanecem visíveis;
- hierarquia funciona para leitura rápida e para leitura aprofundada, quando ambas são necessárias;
- linguagem visual não exclui ou estigmatiza públicos;
- redução de movimento ou alternativas estáticas existem quando aplicável.

## Gate 5 — integridade técnica

Verificar conforme o formato:

- dimensões, resolução, perfil de cor, peso e extensão;
- fontes incorporadas, disponíveis ou substituídas conscientemente;
- imagens sem distorção, pixelização ou compressão indevida;
- ausência de overflow, cortes, sobreposições e objetos fora da página;
- links, vídeos, animações, gráficos e exportações funcionando;
- elementos editáveis quando a continuidade exigir;
- nomes de arquivos e versões inequívocos;
- fonte editável e assets vinculados ou empacotados conforme combinado.

## Testes críticos rápidos

### Miniatura

Reduzir a peça ou visualizar o conjunto em grade. A prioridade, o ritmo e as anomalias devem aparecer sem ler o texto.

### Cinco segundos

Em cinco segundos, identificar assunto, tom e ação principal. Se tudo disputa atenção, revisar.

### Remoção

Retirar cada linha, ícone, fundo, caixa e ornamento em pensamento. Se nada funcional se perde, eliminar ou justificar.

### Troca de marca

Imaginar outro logotipo no lugar da CSC. Se a peça continuar igualmente plausível, falta especificidade de direção, conteúdo ou sistema.

### Tamanho real

Avaliar na escala provável: celular à distância normal, apresentação em tela inteira, documento a 100% e impressão de prova quando aplicável.

### Sistema

Testar o melhor, o pior e o caso mais longo: título extenso, imagem ruim, dado extremo, card adicional, tradução ou variação de formato. O sistema não pode funcionar apenas no exemplar ideal.

### Sem decoração

Remover mentalmente fundos, texturas e efeitos. Se a composição desmorona, a hierarquia estava sendo sustentada por decoração.

## Inspeção obrigatória

Quando houver arquivo ou artefato final:

1. gerar renderização ou exportação representativa;
2. inspecionar todas as páginas, slides, telas, cenas ou variações;
3. revisar o conjunto em miniaturas;
4. abrir casos críticos em tamanho real;
5. corrigir o arquivo-fonte;
6. renderizar novamente as partes alteradas e qualquer página afetada pelo sistema;
7. entregar somente a versão verificada.

Não substituir inspeção visual por checagem de código, lista de objetos ou ausência de erros do aplicativo.

## Revisão de trabalho recebido

Ao revisar um artefato existente, organizar o parecer por impacto:

1. falhas que comprometem objetivo, verdade ou uso;
2. falhas de narrativa e arquitetura;
3. falhas de hierarquia, legibilidade e consistência;
4. oportunidades de refinamento;
5. preferências opcionais.

Para cada ponto relevante, declarar: evidência observável, impacto, princípio violado e correção específica. Evitar críticas vagas como “falta impacto”, “está simples” ou “deixar mais moderno”.

## Handoff

Entregar ao próximo profissional, conforme aplicável:

- objetivo e prioridade da peça;
- dimensões, formatos, canais e derivações;
- grid, margens e áreas seguras;
- famílias tipográficas, pesos, tamanhos e funções;
- paleta usada e finalidade de cada cor;
- regras de imagem, ícone, gráfico, textura e movimento;
- copy final, alternativas e limites de caracteres;
- comportamento responsivo ou variações de proporção;
- assets, links, licenças e pendências;
- exemplos de uso correto e antíteses;
- status de aprovação e versão.

## Critério de parada

Parar quando todos os gates relevantes passam, o artefato está verificado no uso real e as iterações restantes seriam apenas variações de gosto sem ganho material. Não prolongar indefinidamente em busca de “perfeição” abstrata.
