from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
ROOT=Path(__file__).parents[1]; OUT=ROOT/'slides'; AS=ROOT/'assets'; OUT.mkdir(exist_ok=True)
font='/Windows/Fonts/arial.ttf'; bold='/Windows/Fonts/arialbd.ttf'
F=lambda size,weight=False: ImageFont.truetype(bold if weight else font,size)
slides=[
('MARATONA TECH 2026 · NÍVEL 3 · EXEMPLO DOCENTE','Deepfake em publicidade',['Caso brasileiro: uso não autorizado de imagem e voz sintética em anúncio atribuído a Marcos Palmeira.','Tema: alteração intencional de conteúdo, dados pessoais e desinformação ampliada.'],'template-capa-002.png'),
('1 · PROBLEMA DIGITAL','Quando a aparência de endosso é fabricada',['O que ocorreu: a CNN Brasil noticiou que Marcos Palmeira afirmou ter sido usado, sem autorização, em campanha criada com IA.','Onde circulou: perfil no Instagram promovendo um kit de ferramentas.','Por que importa: imagem e voz são dados pessoais; a publicidade pode induzir confiança e pagamento.'],'template-problema-001.png'),
('2 · ANÁLISE DO ARTEFATO','O que a evidência permite dizer?',['Confirmado: há registro jornalístico da alegação de uso não autorizado de imagem e voz reproduzida por IA.','Indício: material anterior do ator foi combinado com voz sintética.','Não demonstrado: arquivo mestre, hash, metadados, autoria do anunciante ou perícia independente.'],'template-artefato-001.png'),
('3 · JOGO DE ERROS + RECONHECIMENTO','Sinais que exigem verificação',['Fonte: perfil comercial sem vínculo comprovado com ator ou fabricante.','Promessa: pessoa conhecida usada como atalho de credibilidade.','Contexto: vídeo recortado ou dublado pode esconder data, origem e autorização.','Ação: interromper pagamento, confirmar em canal oficial e denunciar.'],'template-icones-ilustracoes-002.png'),
('4 · DIAGNÓSTICO','Causa-raiz e riscos sociais',['Causa-raiz provável: mídia sintética fabrica autoridade e é distribuída com incentivo econômico ao clique.','Riscos: perda financeira, coleta de dados, crença em fala inexistente e erosão da confiança em registros audiovisuais.','Hipóteses abertas: autoria, alcance, vítimas e fluxo de dados não podem ser inferidos.'],'template-problema-002.png'),
('5 · RECOMENDAÇÕES PÚBLICAS + CAMPANHA','Verifique antes de confiar',['Usuários: não pagar por link de anúncio; confirmar no site oficial; guardar URL e denunciar.','Escola: ensinar triangulação, proteção de imagem/voz e diferença entre fato, indício e hipótese.','Plataformas e poder público: preservar evidências, identificar mídia sintética e responder a denúncias.','Mensagem: rosto conhecido não é prova de autorização.'],'template-campanha-001.png'),
('6 · ORGANIZAÇÃO DO GRUPO','Divisão verificável do trabalho',['Pesquisa: localiza fontes e registra páginas, URLs e datas.','Análise: separa fato, evidência, hipótese e limite; mapeia dados, causa e impactos.','Comunicação: transforma diagnóstico em guia e campanha; revisa acessibilidade e créditos.','Todos revisam as conclusões e participam da apresentação.'],'template-icones-ilustracoes-003.png'),
('7 · CONCLUSÃO E REFERÊNCIAS','O que permanece válido?',['Mesmo que novos dados alterem detalhes do anúncio, continua válida a necessidade de confirmar autoria, autorização, contexto e destino dos dados antes de compartilhar ou pagar.','Referências: CNN Brasil (2024); Mirsky e Lee (2021); Vaccari e Chadwick (2020); Rößler et al. (2019); Brasil (2018); ANPD (2023); NIST (2023).','Fichamento completo: docs/fichamento-caso.md.'],'template-capa-001.png')]
bg=(247,251,255); navy=(16,42,67); blue=(47,128,237); muted=(72,102,129); gold=(246,195,68)
for i,(k,t,paras,imgname) in enumerate(slides,1):
    im=Image.new('RGB',(1920,1080),bg); d=ImageDraw.Draw(im); d.rectangle((0,0,1920,18),fill=blue); d.rectangle((0,1062,1920,1080),fill=gold)
    asset=Image.open(AS/imgname).convert('RGBA'); asset.thumbnail((510,510)); im.paste(asset,(110,285),asset)
    d.text((760,190),k,font=F(27,True),fill=blue); d.text((760,245),t,font=F(62,True),fill=navy); yy=370
    for p in paras:
        for line in textwrap.wrap(p,width=52): d.text((760,yy),line,font=F(29),fill=navy); yy+=43
        yy+=22
    d.text((1790,1015),f'{i}/8',font=F(24,True),fill=muted); im.save(OUT/f'slide-{i:02d}.jpg',quality=94,optimize=True)
