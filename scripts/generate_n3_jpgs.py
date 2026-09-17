from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import textwrap
R=Path(__file__).parents[1]; O=R/'slides'; A=R/'assets'; O.mkdir(exist_ok=True)
F='/Windows/Fonts/arial.ttf'; B='/Windows/Fonts/arialbd.ttf'; font=lambda n,b=False:ImageFont.truetype(B if b else F,n)
S=[
('CAPA','Deepfake em publicidade',['Maratona Tech 2026 · Nível 3','Caso brasileiro: uso não autorizado de imagem e voz sintética atribuído a Marcos Palmeira.'],'template-capa-002.png'),
('PROBLEMA DIGITAL','Qual é o problema?',['Publicidade digital pode simular o endosso de uma pessoa real usando IA.','O caso circulou no Instagram e promovia um kit de ferramentas.','Relevância: imagem, voz, confiança e possível pagamento são envolvidos.'],'template-icones-ilustracoes-029.png'),
('ARTEFATO DIGITAL','O conteúdo analisado',['Reconstituição esquemática baseada na reportagem: vídeo com imagem prévia do ator + voz sintética + oferta comercial.','A reportagem da CNN Brasil é a evidência disponível; o arquivo original do anúncio não foi recuperado.','Não é possível afirmar hash, metadados, autoria ou perícia quadro a quadro.'],'visual-deepfake-cc-by-sa-2.0.jpg'),
('PERFIL PROFISSIONAL','Quem pode ajudar?',['Jornalista de verificação e pesquisador de segurança digital: localizam a origem, comparam fontes, preservam evidências e explicam limites.','A atuação combina comunicação, pensamento computacional, proteção de dados e responsabilidade pública.'],'template-icones-ilustracoes-007.png'),
('RELATÓRIO TÉCNICO · 1','Descrição do problema digital',['O ator afirmou à CNN Brasil que sua imagem foi usada sem autorização em um golpe publicitário com IA.','Onde: perfil no Instagram. Quem foi impactado primeiro: o titular da imagem e usuários expostos ao anúncio.','Fonte: CNN Brasil, 08 jun. 2024.'],'template-icones-ilustracoes-018.png'),
('RELATÓRIO TÉCNICO · 2','Identificação da causa-raiz',['Causa-raiz provável: combinação de mídia sintética, identidade pública reutilizável, distribuição algorítmica e incentivo econômico ao clique.','Fatores do modelo N3: uso indevido de IA, busca por engajamento, falta de verificação e desinformação intencional.','Autoria do golpe permanece hipótese.'],'template-icones-ilustracoes-026.png'),
('RELATÓRIO TÉCNICO · 3','Diagnóstico dos riscos sociais',['Informacional: fala inexistente parece autêntica.','Econômico: usuário pode pagar ou fornecer dados.','Emocional: confiança e urgência reduzem a checagem.','Coletivo: enfraquece a confiança em imagens e vozes como evidência.'],'template-icones-ilustracoes-049.png'),
('RELATÓRIO TÉCNICO · 4','Fundamentação da análise',['Dados pessoais: imagem e voz identificáveis.','Conceitos: deepfake, alteração intencional, algoritmo, rastro digital e desinformação ampliada.','Base: Mirsky e Lee (2021); Vaccari e Chadwick (2020); Rößler et al. (2019); LGPD (Brasil, 2018).'],'template-icones-ilustracoes-075.png'),
('RELATÓRIO TÉCNICO · 5','Recomendações públicas',['Usuário: não pagar nem informar dados; confirmar em canal oficial; guardar URL e denunciar.','Escola: ensinar triangulação, cadeia de evidências e proteção da imagem/voz.','Plataforma: revisar anúncios, preservar evidências, rotular mídia sintética e responder às denúncias.'],'template-icones-ilustracoes-040.png'),
('CAMPANHA · 1','Público e linguagem',['Público: estudantes, famílias e comunidade escolar.','Linguagem: direta, não sensacionalista, visual e acessível.','Mensagem central: rosto conhecido não é prova de autorização.'],'template-icones-ilustracoes-100.png'),
('CAMPANHA · 2','Explicação técnica simplificada',['Deepfake é conteúdo audiovisual alterado ou criado com IA para parecer que uma pessoa disse ou fez algo.','No caso, a aparência de fala foi associada a uma oferta comercial que o ator declarou não ter autorizado.'],'visual-deepfake-cc-by-sa-2.0.jpg'),
('CAMPANHA · 3','Impactos destacados',['Fraude econômica, coleta indevida de dados, desinformação e perda de confiança.','A campanha orienta sem culpar vítimas e sem expor dados pessoais.'],'template-icones-ilustracoes-106.png'),
('CAMPANHA · 4','Peça visual da campanha',['PARE · CONFIRME · DENUNCIE','1. Pause antes de clicar. 2. Confirme no canal oficial. 3. Não forneça dados. 4. Denuncie e preserve o link.','Peça de conscientização; não é anúncio real.'],'template-icones-ilustracoes-007.png'),
('CONCLUSÃO','Aprendizados principais',['Fato, evidência, inferência e hipótese precisam ser separados.','Imagem e voz podem ser reutilizadas para fabricar autoridade.','A resposta mais segura é confirmação independente antes de compartilhar ou pagar.'],'template-capa-002.png'),
('REFERÊNCIAS','Fontes utilizadas',['CNN BRASIL (2024). Marcos Palmeira: rosto do ator é usado com IA em golpe no Instagram.','MIRSKY; LEE (2021). The creation and detection of deepfakes. ACM Computing Surveys.','VACCARI; CHADWICK (2020). Deepfakes and disinformation. Social Media + Society.','BRASIL (2018). Lei Geral de Proteção de Dados. ANPD (2023). Guia orientativo. NIST (2023). AI Risk Management Framework.'],'template-icones-ilustracoes-107.png')]
def diagram(d, i):
    # Diagramas autorais: visualizam relações documentadas sem reproduzir mídia jornalística protegida.
    groups={2:['IMAGEM/VOZ','OFERTA','USUÁRIO'],3:['VÍDEO PRÉVIO','VOZ SINTÉTICA','ANÚNCIO'],5:['RELATO','CIRCULAÇÃO','IMPACTO'],6:['IA','IDENTIDADE','INCENTIVO'],7:['CONTEÚDO','CONFIANÇA','DANO'],8:['CONCEITO','EVIDÊNCIA','LIMITE'],9:['PAUSAR','CONFIRMAR','DENUNCIAR']}
    labels=groups.get(i)
    if not labels:return
    for n,label in enumerate(labels):
        x=735+n*365; y=820
        d.rounded_rectangle((x,y,x+315,y+70),radius=18,fill=(16,42,67),outline=(246,195,68),width=3)
        d.text((x+18,y+20),label,font=font(24,1),fill=(255,255,255))
        if n<2:d.line((x+315,y+35,x+365,y+35),fill=(246,195,68),width=5)

for i,(k,t,ps,img) in enumerate(S,1):
 bg=Image.open(A/'template-capa-002.png').convert('RGB').resize((1920,1080))
 im=bg.copy(); d=ImageDraw.Draw(im); d.rectangle((0,0,1920,18),fill=(47,128,237)); d.rectangle((0,1062,1920,1080),fill=(246,195,68)); d.rounded_rectangle((680,110,1850,1000),radius=28,fill=(247,251,255,238)); d.rounded_rectangle((70,220,650,850),radius=32,fill=(255,255,255),outline=(199,215,229),width=5); d.rounded_rectangle((82,232,638,838),radius=26,outline=(246,195,68),width=3); a=Image.open(A/img).convert('RGBA'); a.thumbnail((520,560)); ax=360-a.width//2; ay=535-a.height//2; im.paste(a,(ax,ay),a); d.text((740,170),k,font=font(28,1),fill=(47,128,237)); d.text((740,225),t,font=font(58,1),fill=(16,42,67)); y=350
 for p in ps:
  for line in textwrap.wrap(p,52):d.text((740,y),line,font=font(29),fill=(16,42,67));y+=43
  y+=20
 diagram(d,i)
 if img.startswith('visual-'): d.text((110,790),'ILUSTRAÇÃO CC BY-SA 2.0 · MINISTERIE VAN BUITENLANDSE ZAKEN',font=font(13,1),fill=(16,42,67))
 d.text((1800,1015),f'{i}/15',font=font(24,1),fill=(72,102,129));im.save(O/f'slide-{i:02d}.jpg',quality=94,optimize=True)

