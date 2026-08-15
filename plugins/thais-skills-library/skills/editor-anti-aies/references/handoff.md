# Contrato de passagem

Usar este pacote para revisar linguagem sem perder fatos, função, voz ou limitações definidas pela Skill de origem.

## Entrada mínima

- `texto`: versão integral e sua estrutura;
- `modo_e_intensidade`: auditoria, revisão ou redação; leve, média ou profunda;
- `finalidade`: público, canal, gênero e ação esperada;
- `invariantes`: fatos, nomes, números, links, citações, termos e ressalvas intocáveis;
- `rastreabilidade`: fonte, data, classe temporal, status e conflito de cada alegação material, quando disponíveis;
- `voz`: registro, marcas autorais e escolhas deliberadas a preservar;
- `restrições`: tamanho, SEO, campos, compliance, formato e repetição funcional;
- `hipóteses_e_pendências`: trechos provisórios ou dúvidas que a edição não deve resolver.

## Saída mínima — `editorial_revision_packet`

- `texto_revisado`: versão pronta no formato solicitado;
- `invariantes_preservadas`: confirmação ou indicação precisa de qualquer risco;
- `mudanças_materiais`: somente cortes, fusões, reordenações ou ajustes que alteram a leitura;
- `repetições_deliberadas`: itens mantidos e sua função, quando a decisão não for óbvia;
- `alertas_factuais`: alegações duvidosas encaminhadas para apuração, sem correção por memória;
- `restrições_verificadas`: tamanho, SEO, campo ou compliance que continuem atendidos;
- `pendências`: decisão editorial ou factual que ainda impede aprovação.

## Regras de continuidade

- Não alterar fonte, data, classe, status ou conflito recebido; encaminhar a questão à Skill responsável.
- Não transformar hipótese em afirmação para deixar o texto mais fluido.
- Se a revisão quebrar limite, função de campo, palavra-chave necessária ou voz aprovada, manter a versão anterior e registrar o impasse.
- Entregar o texto, não um diagnóstico extenso, salvo quando o modo pedido for auditoria.
