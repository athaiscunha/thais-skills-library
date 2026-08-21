# Testes de aceitação da Skill

## Sumário

- Entrada, conteúdo denso e protótipos sociais
- Apresentações, calibração e ausência de manual
- Originalidade, legibilidade, dados e robustez do sistema
- Crítica, inspeção, acessibilidade e handoff

## Como testar

Executar cenários com materiais realistas. Avaliar decisões, perguntas, arquivos, renderizações e handoff. A presença de palavras como “minimalista”, “sofisticado”, “grid” ou “bom gosto” não comprova comportamento.

O teste passa apenas se:

- a Skill escolhe o modo correto;
- pergunta proativamente somente sobre lacunas materiais;
- não inventa dados nem regras de marca;
- produz o artefato quando solicitado;
- realiza autocrítica e inspeção visual;
- entrega especificação suficiente ao próximo profissional.

## Cenário 1 — pedido vago de post

**Entrada:** “Crie um post sofisticado para a Católica SC.”

**Esperado:** localizar objetivo, público, mensagem, canal e ativos; fazer perguntas agrupadas apenas sobre lacunas materiais; não assumir automaticamente fundo bege, serifas, paleta neutra ou estética de luxo; avançar com hipóteses identificadas quando seguro.

**Falha:** oferecer um quadrado genérico com logotipo, gradiente e frase sem estratégia.

## Cenário 2 — minimalismo com conteúdo denso

**Entrada:** peça com requisitos obrigatórios extensos.

**Esperado:** editar, agrupar e hierarquizar; propor formato alternativo se necessário; preservar informação obrigatória; usar espaço e tipografia com rigor.

**Falha:** remover conteúdo necessário ou reduzir a fonte até caber.

## Cenário 3 — protótipo de carrossel

**Entrada:** pauta e copy para oito cards.

**Esperado:** construir progressão, variar composições por função, demonstrar sistema, criar o protótipo no formato pedido, inspecionar tamanho móvel e entregar roteiro, assets e regras.

**Falha:** repetir o mesmo layout oito vezes ou entregar somente um briefing textual quando o protótipo foi pedido.

## Cenário 4 — deck ao vivo

**Entrada:** documento denso a ser apresentado em reunião.

**Esperado:** distinguir fala e leitura, reescrever títulos como mensagens, criar narrativa, mover detalhe para notas/anexo, variar famílias de slide, renderizar tudo e testar à distância.

**Falha:** converter cada seção do documento em um slide com bullets pequenos.

## Cenário 5 — referência classificada como base mínima

**Entrada:** link do deck “Planejamento Editorial Setembro 2026” e observação de que é apenas uma base do mínimo.

**Esperado:** preservar coerência, grid e organização como piso; superar legibilidade, repetição, placeholders, pílulas/cards automáticos, narrativa e especificidade; não copiar o estilo nem tratar o material como manual da marca.

**Falha:** replicar fundo, ornamentos e composição; afirmar que basta seguir o template.

## Cenário 6 — ausência de manual de marca

**Entrada:** pedido visual sem arquivos oficiais.

**Esperado:** procurar materiais disponíveis, preservar sinais confiáveis e identificar qualquer nova direção como proposta; pedir ativo apenas se sua falta for material.

**Falha:** inventar paleta, fontes e regras e apresentá-las como identidade oficial.

## Cenário 7 — referência de marca externa

**Entrada:** “Faça igual a esta campanha de outra universidade.”

**Esperado:** extrair princípios transferíveis, explicar limites e criar direção original apropriada à CSC.

**Falha:** copiar composição distintiva, ativos ou identidade do terceiro.

## Cenário 8 — revisão de peça bonita, mas ilegível

**Entrada:** arquivo visualmente polido com textos minúsculos.

**Esperado:** reprovar no gate de uso real, demonstrar impacto e propor correção específica; não deixar acabamento compensar falha funcional.

**Falha:** aprovar com base em gosto, harmonia ou aparência premium.

## Cenário 9 — relatório com dados

**Entrada:** relatório mensal com gráficos e tabelas.

**Esperado:** conferir origem, período e denominadores; explicitar takeaway; preservar integridade; construir hierarquia de leitura; renderizar todas as páginas.

**Falha:** decorar números, omitir fontes ou usar gráfico inadequado apenas por aparência.

## Cenário 10 — sistema sob estresse

**Entrada:** adaptar uma direção aprovada para título longo, pouco conteúdo, muito conteúdo e três proporções.

**Esperado:** manter reconhecimento e hierarquia com variações reais; identificar limites e especificar regras.

**Falha:** o sistema funcionar apenas no mockup principal.

## Cenário 11 — crítica vaga da usuária

**Entrada:** “Está simples e feio; quero algo sofisticado.”

**Esperado:** diagnosticar causas observáveis — hierarquia, tipografia, proporção, ritmo, imagem, acabamento, especificidade — e melhorar o artefato; não aplicar clichês de luxo.

**Falha:** somente trocar a fonte por serifa fina, reduzir elementos e adicionar dourado.

## Cenário 12 — inspeção técnica

**Entrada:** arquivo final gerado sem erro pelo software.

**Esperado:** abrir ou renderizar, inspecionar todas as saídas, corrigir falhas visuais e verificar novamente.

**Falha:** declarar pronto sem visualização.

## Cenário 13 — conflito entre beleza e acessibilidade

**Entrada:** contraste delicado e texto leve produzem aparência elegante, mas leitura fraca.

**Esperado:** priorizar legibilidade e encontrar refinamento por composição, tipografia e proporção.

**Falha:** preservar a aparência porque parece mais sofisticada.

## Cenário 14 — handoff

**Entrada:** artefato aprovado que seguirá para designer, editor ou mídia.

**Esperado:** entregar dimensões, hierarquia, tipografia, cores, grid, assets, copy, derivações, movimento, versões, pendências e status pertinentes.

**Falha:** entregar uma imagem isolada ou recomendações vagas que exigem reconstrução.
