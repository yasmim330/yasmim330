# Kit de posts do Fiscal Hub

Esta pasta guarda a mídia dos posts agendados no Metricool para a @sanktortech.
O Metricool puxa cada imagem e vídeo pelo link público:
`https://raw.githubusercontent.com/yasmim330/yasmim330/main/posts/AAAA-MM-DD/arquivo`

## Identidade
- Fundo grafite `#08080A`, cards `#131317`.
- Laranja Hub `#FF7A1A` e laranja claro `#FF9A4D` como o único destaque de cada peça.
- Cores de status (vermelho, amarelo, azul, verde) só em elementos de interface.
- Geist Bold nos títulos com efeito metálico prateado (classe `.metal`), Geist SemiBold nos subtítulos, Geist Mono em valores, datas e paginação.
- Elementos: hexágono como logo, grade fina com brilho laranja (`.grid` e `.glow`), pills de status e linha de fluxo.
- `brand.css` e `fonts/` têm tudo isso pronto. Os arquivos `exemplo-*.html` são modelos de Reels, feed e stories.

## Formatos
- Feed: 1080×1350 PNG.
- Story: 1080×1920 PNG. Nada importante nos 250 px de cima nem nos 340 px de baixo.
- Reels: 1080×1920 MP4, H.264 + AAC, 30 fps, de 12 a 21 s, áudio em torno de −14 LUFS. Nada importante nos 400 px de baixo.
- Trilha sempre original, gerada com `trilha.py` (sem música de terceiros).

## Tom das legendas
- Tom de colega do fiscal: humano, direto, frases curtas, nem formal demais nem gíria demais.
- Evitar palavras com cara de IA: revolucionar, potencializar, descubra, jornada, transformar, eficiência, otimizar, solução completa, inovador, "não é apenas…, é…", travessões longos, emojis em excesso.
- No máximo um emoji por legenda, de 5 a 8 hashtags de nicho no fim.
- Nunca mostrar nome real de fornecedor, valor ou NF reais, nem o nome do supermercado.
