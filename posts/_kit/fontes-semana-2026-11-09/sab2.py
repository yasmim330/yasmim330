from common import page
css='''
.top{left:72px;right:72px;top:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{font-size:19px;padding:9px 18px;letter-spacing:.08em}
h1{left:72px;right:72px;top:170px;font-size:78px;font-weight:700;letter-spacing:-.045em;line-height:1.03}
.note{position:absolute;width:440px;padding:28px 30px;border-radius:20px;background:linear-gradient(180deg,#1a1a20,#131317);border:1px solid var(--line-2);box-shadow:0 30px 60px -25px rgba(0,0,0,.95)}
.note .n{font-family:var(--mono);font-size:22px;color:var(--acc-2);letter-spacing:.06em}
.note p{font-size:30px;font-weight:600;line-height:1.25;margin-top:10px}
.note.hi{background:var(--acc-soft);border-color:var(--acc-line)}
.tape{position:absolute;top:-14px;left:50%;width:110px;height:28px;margin-left:-55px;background:rgba(255,154,77,.35);border-radius:4px;transform:rotate(-3deg)}
svg.ar{position:absolute;left:0;top:0}
.foot{left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:24px}
.foot p{font-size:27px;font-weight:600;color:var(--ink-2)}.foot p b{color:var(--acc-2);font-weight:600}
.foot .mono{font-size:20px;color:var(--muted)}
'''
body='''<div class="grid"></div><div class="glow" style="width:900px;height:900px;left:350px;top:-300px"></div><div class="glow" style="width:600px;height:600px;left:-200px;top:850px;opacity:.5"></div>
<div class="abs top"><div class="brand"><svg><use href="#logo"/></svg><b>Fiscal Hub</b></div><span class="pill acc">BASTIDOR</span></div>
<h1 class="abs"><span class="metal" style="display:block">O rascunho da</span><span class="acc-t">conferência do CEASA</span></h1>
<svg class="ar" width="1080" height="1350"><g fill="none" stroke="#ff9a4d" stroke-width="3" stroke-dasharray="3 12" stroke-linecap="round">
<path d="M520 520 C 620 540, 640 560, 620 600"/><path d="M600 790 C 560 840, 520 850, 470 880"/><path d="M518 1040 C 550 1050, 572 1045, 594 1030"/></g></svg>
<div class="note" style="left:72px;top:400px;transform:rotate(-2deg)"><span class="tape"></span><span class="n">01 · O PROBLEMA</span><p>Nota do CEASA não passa no coletor.</p></div>
<div class="note" style="left:568px;top:600px;transform:rotate(2deg)"><span class="tape"></span><span class="n">02 · O CAMINHO</span><p>Ela entra no sistema por outro caminho, e às vezes fica pra trás.</p></div>
<div class="note" style="left:72px;top:880px;transform:rotate(-1.5deg)"><span class="tape"></span><span class="n">03 · A IDEIA</span><p>A IA cruza com os lançamentos e mostra o que falta ou não bate.</p></div>
<div class="note hi" style="left:600px;top:930px;width:400px;transform:rotate(2.5deg)"><span class="tape"></span><span class="n">04 · A REGRA</span><p>A IA aponta.<br>Quem decide é o fiscal.</p></div>
<div class="abs foot"><p>Como vocês controlam hoje<br><b>as notas do CEASA?</b></p><span class="mono">conta nos comentários ↓</span></div>'''
open('sab2.html','w').write(page('Bastidor CEASA',1080,1350,css,body))
