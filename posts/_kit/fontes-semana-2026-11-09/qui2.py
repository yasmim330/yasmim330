from common import page
css='''
.top{left:72px;right:72px;top:64px;display:flex;justify-content:space-between;align-items:center}
.top .pill{font-size:19px;padding:9px 18px;letter-spacing:.08em}
.k{left:72px;top:170px;font-family:var(--mono);font-size:24px;color:var(--acc-2);letter-spacing:.1em}
.q{left:72px;right:150px;top:226px;background:#1b1b21;border:1px solid var(--line-2);border-radius:34px 34px 34px 8px;padding:34px 40px}
.q small{display:block;font-family:var(--mono);font-size:20px;color:var(--muted);letter-spacing:.06em;margin-bottom:12px}
.q p{font-size:52px;font-weight:700;letter-spacing:-.035em;line-height:1.08}
.a{left:150px;right:72px;top:510px;background:var(--acc-soft);border:1px solid var(--acc-line);border-radius:34px 34px 8px 34px;padding:34px 40px}
.a small{display:block;font-family:var(--mono);font-size:20px;color:var(--acc-2);letter-spacing:.06em;margin-bottom:12px}
.a p{font-size:33px;font-weight:600;line-height:1.3;color:var(--ink)}
.a p b{color:var(--acc-2);font-weight:600}
.al{left:72px;right:72px;top:860px;padding:26px 30px}
.al .lbl{font-family:var(--mono);font-size:19px;color:var(--muted);letter-spacing:.06em;margin-bottom:14px}
.msg{display:flex;gap:14px;align-items:flex-start;padding:16px 18px;border-radius:14px;font-size:25px;font-weight:500;line-height:1.3;margin-top:10px}
.msg.yel{background:rgba(242,201,76,.08);border:1px solid rgba(242,201,76,.25);color:var(--yel)}
.msg.red{background:rgba(255,97,97,.08);border:1px solid rgba(255,97,97,.25);color:var(--red)}
.msg i{font-style:normal;font-weight:700}
.foot{left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:24px}
.foot p{font-size:26px;font-weight:600;color:var(--ink-2)}.foot p b{color:var(--acc-2);font-weight:600}
.foot .mono{font-size:20px;color:var(--muted)}
'''
body='''<div class="grid"></div><div class="glow" style="width:800px;height:800px;left:-260px;top:-260px"></div><div class="glow" style="width:700px;height:700px;left:600px;top:700px;opacity:.6"></div>
<div class="abs top"><div class="brand"><svg><use href="#logo"/></svg><b>Fiscal Hub</b></div><span class="pill acc">PERGUNTA DE QUEM CHEGA NOVO · 1/3</span></div>
<div class="abs q"><small>NOVATO NO FISCAL</small><p>A nota chegou faz 5 dias. Lanço com a data de hoje?</p></div>
<div class="abs a"><small>QUEM JÁ TÁ HÁ MAIS TEMPO</small><p>Não. A data de recebimento é <b>o dia em que a mercadoria chegou</b>. É dela que sai o prazo dos boletos.</p></div>
<div class="abs card al"><div class="lbl">E SE ERRAR, O FISCAL HUB AVISA</div>
<div class="msg yel"><i>!</i><span>Recebimento de 9 dias atrás (03/11). Confirme se está correto.</span></div>
<div class="msg red"><i>×</i><span>A data de recebimento não pode estar no futuro.</span></div></div>
<div class="abs foot"><p>Lembra da sua primeira semana?<br><b>Marca quem chegou agora.</b></p><span class="mono">parte 2 em breve</span></div>'''
open('qui2.html','w').write(page('Post quinta',1080,1350,css,body))
