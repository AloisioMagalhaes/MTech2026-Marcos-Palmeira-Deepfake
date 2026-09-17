# Auditoria de acessibilidade visual e web

Validação realizada em 17 set. 2026, com referência às WCAG 2.2.

| Verificação | Resultado |
|---|---|
| Contraste texto escuro/painel claro | 14,08:1 — WCAG AAA |
| Contraste texto auxiliar/painel claro | 5,78:1 — WCAG AA |
| Contraste azul de títulos/painel claro | 3,72:1 — AA para texto grande; títulos têm 28 px em negrito |
| Slides | 15 JPGs, todos 1920×1080 |
| Texto alternativo | 15 de 15 imagens com `alt` |
| Navegação | Skip link, navegação por âncoras, foco visível e teclado |
| Movimento | Respeita `prefers-reduced-motion` |
| Impressão | Um slide por página em formato 16:9 |

## Revisão WCAG do HTML

- Identidade visual: fundo azul-claro, superfícies quase brancas, texto azul-marinho e links azul-escuro.
- Contraste-alvo: texto normal mínimo de 4,5:1; texto grande mínimo de 3:1; o amarelo não é usado como cor única para texto.
- Foco: contorno escuro de 4 px com deslocamento de 4 px, visível também em navegação por teclado.
- Responsividade: `clamp()` para tipografia e espaçamentos, flexbox na pilha de slides e quebra para viewport móvel.
- Preferências: suporte a `prefers-reduced-motion` e `prefers-contrast: more`.

O texto principal usa cor #102A43 sobre #F7FBFF. Os JPGs continuam sendo imagens; os atributos `alt` oferecem uma descrição resumida para leitores de tela, enquanto o conteúdo detalhado permanece visualmente dentro dos próprios slides.
