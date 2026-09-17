# Plano de assets e UX/UI — apresentação N3

## Prompt operacional revisado

> Revise o `PPT_Fase1_Modelo.pptx` como fonte visual. Extraia todos os objetos gráficos incorporados, preserve o original, gere um inventário com hash SHA-256, relacione cada asset ao slide de origem e selecione somente imagens/diagramas pertinentes à afirmação do slide. Use o fundo azul oficial como camada comum, cartões brancos com borda amarela para contraste e uma hierarquia visual 16:9. Cada slide deve conter uma ideia central, no máximo três blocos de evidência e uma legenda de fonte. Não invente conteúdo, não trate ilustração como evidência, não exponha dados pessoais e não inclua mídia sem licença ou atribuição documentada. Valide foco, contraste, leitura em 1920×1080 e redução para telas menores.

## Regras implementadas

1. Fundo azul do template em todos os slides.
2. Ilustração em cartão branco opaco, com borda amarela de 3–5 px, para separar ícones azuis do fundo.
3. Uma ilustração por seção, escolhida por função: alerta, artefato, evidência, causa, risco, fundamentação, recomendação, público e referências.
4. Texto convertido em frases curtas e hierarquizadas; evidência e limitação permanecem explícitas.
5. Não usar asset do template como prova do caso real.
6. Não inserir imagem de estudante, rosto identificável ou voz de menor.
7. Manter `alt` textual no HTML, navegação por teclado e foco visível.
8. Não utilizar `iframe`, scripts de terceiros, rastreadores ou reprodução automática.

## Extração realizada

O PPTX original contém 117 arquivos de mídia incorporados. Eles foram extraídos localmente para `assets-ppt-template-2026-09-17/`, com nomes sequenciais estáveis e `manifest.json` contendo origem e SHA-256. A pasta não é duplicada no GitHub porque soma aproximadamente 141,8 MB; os assets selecionados e já normalizados no diretório `assets/` continuam sendo os usados pela apresentação publicada.

## Matriz de encaixe

| Seção | Asset publicado | Função visual |
|---|---|---|
| Problema | `template-icones-ilustracoes-106.png` | alerta e risco |
| Artefato | `template-icones-ilustracoes-008.png` | dispositivo e mídia |
| Perfil | `template-icones-ilustracoes-007.png` | papéis de investigação |
| Causa | `template-icones-ilustracoes-018.png` | processo/algoritmo |
| Evidência | `template-icones-ilustracoes-026.png` | documento e verificação |
| Riscos | `template-icones-ilustracoes-049.png` | análise de impacto |
| Fundamentação | `template-icones-ilustracoes-075.png` | ciência e método |
| Recomendações | `template-icones-ilustracoes-040.png` | checklist de ação |
| Público | `template-icones-ilustracoes-100.png` | rede/comunidade |
| Referências | `template-icones-ilustracoes-107.png` | bibliografia |

## Validação

A seleção deve ser revisada visualmente em 1920×1080, 1366×768 e viewport móvel. O contraste deve ser conferido entre texto, cartão e fundo; caso um ícone azul perca distinção, ele deve permanecer dentro do cartão branco e receber contorno amarelo, sem alterar a informação original.
