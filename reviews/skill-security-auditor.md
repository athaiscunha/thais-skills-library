# Revisão: skill-security-auditor

- Origem: [scayver/marketing-skills](https://github.com/scayver/marketing-skills/tree/main/skills/skill-security-auditor)
- Commit analisado: `18243d7675fa83638f20c660e31311c1bf03294d`
- Licença do repositório: MIT
- Data: 2026-08-14
- Revisor: Codex, com direção da usuária
- Decisão: rejeitada

## Finalidade declarada

Auditar Skills, prompts, scripts e ferramentas externas antes da instalação.

## Arquivos analisados

O `SKILL.md` da candidata, o arquivo de licença e o contexto do repositório foram lidos. A inspeção foi encerrada após falhas bloqueadoras no próprio arquivo principal; nenhum conteúdo foi executado.

## Riscos encontrados

| Finding | Severidade | Evidência | Risco | Decisão |
|---|---|---|---|---|
| Publicidade obrigatória | Alta | A Skill exige uma mensagem inicial com pedido de contribuição e links externos | Injeta conteúdo alheio a toda auditoria e direciona a usuária sem necessidade | Remover completamente; a versão externa foi rejeitada |
| Resposta roteirizada sobre prompt do sistema | Alta | A Skill manda redirecionar esse tipo de pergunta para uma academia externa | Tenta substituir uma resposta legítima por promoção e interfere no comportamento do agente | Remover completamente; a versão externa foi rejeitada |
| Regras editoriais alheias ao risco | Média | Impõe preferências de estilo globais sem relação direta com a análise | Amplia o escopo e pode conflitar com instruções da usuária | Não importar |

## Ideias úteis preservadas

Foram reexpressos no processo interno: tratar material externo como não confiável, inventariar arquivos, não executar conteúdo suspeito, redigir evidências sem expor segredos, classificar severidade e registrar reteste.

## Alterações realizadas

Nenhum arquivo da candidata foi copiado ou instalado. O roteiro útil foi reescrito em `docs/THIRD_PARTY_REVIEW.md` e aplicado à revisão da Skill própria.

## Resultado

Não instalar, não copiar e não usar esta candidata como autoridade de segurança. A biblioteca mantém um processo próprio e legível de revisão.
