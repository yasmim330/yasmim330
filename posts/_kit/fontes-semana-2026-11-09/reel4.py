from common import page
css='''
.top{left:72px;right:72px;top:250px;display:flex;justify-content:space-between;align-items:center}
.top .mono{font-size:26px;color:var(--ink-2)}
.hook{left:72px;right:72px;top:680px}
.hook h1{font-size:120px;font-weight:700;letter-spacing:-.055em;line-height:1.02}
.day{left:72px;top:390px;display:flex;align-items:baseline;gap:22px}
.day .pill{font-size:26px;padding:10px 22px;font-family:var(--mono);letter-spacing:.06em}
.day h2{font-size:56px;font-weight:700;letter-spacing:-.04em}
.win{left:72px;right:72px;top:500px;padding:0;overflow:hidden}
.wh{display:flex;align-items:center;justify-content:space-between;padding:26px 34px;border-bottom:1px solid var(--line)}
.wh b{font-size:30px;font-weight:600}.wh .mono{font-size:22px;color:var(--muted)}
.wb{padding:30px 34px}
.lb{font-family:var(--mono);font-size:20px;color:var(--muted);letter-spacing:.06em;margin:0 0 10px}
.in{height:78px;border-radius:16px;background:#0d0d10;border:1px solid var(--line-2);display:flex;align-items:center;padding:0 24px;font-size:31px;font-weight:600;justify-content:space-between;margin-bottom:20px}
.in.focus{border-color:var(--acc);box-shadow:0 0 0 4px rgba(255,122,26,.15)}
.msg{display:flex;gap:14px;align-items:flex-start;padding:18px 20px;border-radius:14px;font-size:27px;font-weight:500;line-height:1.3;margin-top:12px;background:rgba(242,201,76,.08);border:1px solid rgba(242,201,76,.28);color:var(--yel)}
.msg i{font-style:normal;font-weight:700}
.list .it{display:grid;grid-template-columns:1fr auto;align-items:center;padding:30px 34px;border-bottom:1px solid var(--line)}
.list .n{font-size:30px;font-weight:600}.list .m{font-family:var(--mono);font-size:23px;color:var(--muted);margin-top:6px}
.list .pill{font-size:23px;padding:9px 16px}
.pill.red{background:rgba(255,97,97,.12);color:var(--red);border-color:rgba(255,97,97,.28)}
.list .it.hl{background:rgba(255,97,97,.05)}
.flip{position:absolute;left:0;right:0;top:0;bottom:0;background:#08080a;z-index:7;pointer-events:none}
.end{left:72px;right:72px;top:640px}
.end h2{font-size:116px;font-weight:700;letter-spacing:-.05em;line-height:1.02}
.end p{font-size:36px;color:var(--ink-2);font-weight:600;margin-top:40px;line-height:1.32}
.sig{left:72px;top:1380px;display:flex;align-items:center;gap:16px;font-size:30px;color:var(--muted)}
.sig svg{width:56px;height:56px;color:#fff}.sig b{color:var(--ink);font-weight:600}
'''
body='''<div class="grid"></div><div class="glow" id="g1" style="width:1100px;height:1100px"></div>
<div class="abs top" id="top"><div class="brand"><svg><use href="#logo"/></svg><b>Fiscal Hub</b></div><span class="mono" id="clk">sex · 13/11</span></div>
<div class="abs hook" id="hook"><h1><span class="metal" style="display:block" id="h1">Hoje tem nota.</span><span class="acc-t" id="h2">Amanhã tem</span><span class="acc-t" style="display:block" id="h3">vencimento.</span></h1></div>
<div id="A"><div class="abs day" id="da"><span class="pill acc">HOJE · SEX 13/11</span></div>
<div class="abs card win" id="wa" style="top:480px"><div class="wh"><b>Novo lançamento</b><span class="mono">recebimento 13/11</span></div>
<div class="wb"><div class="lb">FORNECEDOR</div><div class="in">FRIGORÍFICO SERRA AZUL</div>
<div class="lb">BOLETO 1 · VENCIMENTO</div><div class="in" id="iv"><span class="mono" id="vv">__/__/____</span><span class="mono" style="font-size:22px;color:var(--muted)" id="vd"></span></div>
<div class="msg" id="m1"><i>!</i><span>Boleto 1: vence em 1 dia(s) (14/11). Avise o financeiro.</span></div>
<div class="msg" id="m2"><i>!</i><span>Boleto 1: vencimento cai em sábado (14/11).</span></div></div></div></div>
<div id="B"><div class="abs day" id="db"><span class="pill acc">AMANHÃ · SÁB 14/11</span></div>
<div class="abs card win" id="wb" style="top:480px"><div class="wh"><b>Vencimentos</b><span class="mono">hoje</span></div>
<div class="list"><div class="it hl" id="l1"><div><div class="n">FRIGORÍFICO SERRA AZUL</div><div class="m">boleto 1 · 14/11 sáb</div></div><span class="pill red">vence hoje</span></div>
</div></div><div class="abs" id="l2" style="left:72px;right:72px;top:820px;font-size:38px;font-weight:600;color:var(--ink-2);line-height:1.3">O financeiro já sabia <span style="color:var(--acc-2)">desde ontem.</span><br>Sábado sem susto.</div></div>
<div class="flip" id="flip"></div>
<div class="abs end" id="end"><h2><span class="metal" style="display:block">Avisou hoje.</span><span class="acc-t">Amanhã ninguém corre.</span></h2>
<p>O aviso aparece na hora de lançar,<br>não no dia do vencimento.</p></div>
<div class="abs sig" id="sig"><svg><use href="#logo"/></svg><span><b>Fiscal Hub</b> · rotina fiscal de perecíveis</span></div>'''
code='''
function render(t){bg(t);
 $('g1').style.left=(250+Math.sin(t*.45)*170)+'px';$('g1').style.top=(300+Math.cos(t*.35)*230)+'px';
 appear($('top'),t,0,.45,20);
 appear($('h1'),t,.1,.45,60,2.9,.35);appear($('h2'),t,.6,.45,60,2.9,.35);appear($('h3'),t,.8,.45,60,2.9,.35);
 $('hook').style.display=t<2.95?'block':'none';
 $('clk').textContent=t<8.3?'sex · 13/11':'sáb · 14/11';
 const Aon=t>=2.9&&t<8.3;$('A').style.display=Aon?'block':'none';
 if(Aon){appear($('da'),t,3.0,.4,20);const wi=eo(P(t,3.1,3.6));$('wa').style.opacity=wi;$('wa').style.transform=`translateY(${(1-wi)*90}px)`;
  const d='14/11/2026',n=Math.floor(cl((t-4.0)/.08,0,d.length));$('vv').textContent=t<4?'__/__/____':d.slice(0,n)+'__/__/____'.slice(n);$('vd').textContent=t>=4.8?'sáb':'';
  $('iv').classList.toggle('focus',t>=3.9&&t<5.0);
  [['m1',5.1],['m2',5.7]].forEach(([m,a])=>{appear($(m),t,a,.35,24);if(t<a)$(m).style.opacity=0});}
 // virada de pagina 7.9-8.7
 const f=$('flip');const up=P(t,7.9,8.3),dn=P(t,8.3,8.7);f.style.opacity=up*(1-dn);
 const Bon=t>=8.3&&t<12.4;$('B').style.display=Bon?'block':'none';
 if(Bon){const out=12.3;appear($('db'),t,8.4,.4,20,out,.3);const wi=eo(P(t,8.5,9.0));$('wb').style.opacity=wi*(1-P(t,out-.3,out));$('wb').style.transform=`translateY(${(1-wi)*60}px)`;
  appear($('l1'),t,9.0,.4,24);appear($('l2'),t,10.0,.4,24);if(t<10)$('l2').style.opacity=0;
  $('l1').querySelector('.pill').style.transform=`scale(${1+.05*Math.max(0,Math.sin(t*6))})`;}
 if(Aon&&t>7.6){$('wa').style.opacity=1-P(t,7.6,7.95);$('da').style.opacity=1-P(t,7.6,7.95)}
 const e=$('end');e.style.opacity=t>=12.4?1:0;
 [...e.querySelectorAll('h2 span')].forEach((s,i)=>appear(s,t,12.45+i*.4,.45,50));appear(e.querySelector('p'),t,13.5,.45,24);
 appear($('sig'),t,14.0,.45,20);if(t<12.4)$('sig').style.opacity=0;
}'''
open('reel4.html','w').write(page('Reel hoje amanha',1080,1920,css,body,code,16))
