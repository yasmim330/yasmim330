from common import page
css='''
.top{left:72px;right:72px;top:250px;display:flex;justify-content:space-between;align-items:center}
.top .pill{font-size:22px;padding:9px 18px;letter-spacing:.08em}
.hook{left:72px;right:72px;top:700px}
.hook h1{font-size:126px;font-weight:700;letter-spacing:-.055em;line-height:1}
.hook p{font-family:var(--mono);font-size:28px;color:var(--muted);margin-top:44px;letter-spacing:.06em}
.ttl{left:72px;right:72px;top:400px;font-size:70px;font-weight:700;letter-spacing:-.045em;line-height:1.03}
.paper{position:absolute;width:560px;padding:30px 34px;border-radius:22px;background:linear-gradient(180deg,#1a1a20,#131317);border:1px solid var(--line-2);box-shadow:0 40px 80px -30px rgba(0,0,0,.95)}
.paper .bx{font-family:var(--mono);font-size:22px;color:var(--acc-2);letter-spacing:.08em}
.paper b{display:block;font-size:34px;font-weight:700;letter-spacing:-.02em;margin:8px 0 14px}
.paper .ln{height:10px;border-radius:5px;background:rgba(255,255,255,.07);margin-top:10px}
.paper .pill{font-size:21px;padding:7px 14px;margin-top:18px}
.sub2{left:72px;right:72px;top:1400px;font-size:34px;font-weight:600;color:var(--ink-2)}
.app{left:72px;right:72px;top:600px;padding:0;overflow:hidden}
.wh{display:flex;align-items:center;justify-content:space-between;padding:26px 34px;border-bottom:1px solid var(--line)}
.wh b{font-size:31px;font-weight:600}
.ai{font-family:var(--mono);font-size:21px;color:var(--acc-2);border:1px solid var(--acc-line);background:var(--acc-soft);border-radius:999px;padding:7px 16px}
.rw{position:relative;display:grid;grid-template-columns:1fr auto;align-items:center;gap:16px;padding:44px 34px;border-bottom:1px solid var(--line)}
.rw .n{font-size:33px;font-weight:600}
.rw .m{font-family:var(--mono);font-size:22px;color:var(--muted);margin-top:6px}
.rw .pill{font-size:22px;padding:9px 16px}
.pill.red{background:rgba(255,97,97,.12);color:var(--red);border-color:rgba(255,97,97,.28)}
.wait{font-family:var(--mono);font-size:22px;color:var(--faint)}
.beam{position:absolute;left:0;right:0;height:130px;background:linear-gradient(180deg,transparent,rgba(255,122,26,.16),transparent);border-top:2px solid rgba(255,154,77,.0);pointer-events:none}
.beam::after{content:"";position:absolute;left:0;right:0;top:50%;height:2px;background:linear-gradient(90deg,transparent,var(--acc),transparent);box-shadow:0 0 18px var(--acc)}
.sum{display:flex;gap:34px;padding:32px 34px;font-family:var(--mono);font-size:26px;color:var(--muted)}
.sum b{color:var(--ink);font-weight:600}
.end{left:72px;right:72px;top:620px}
.end h2{font-size:120px;font-weight:700;letter-spacing:-.05em;line-height:1.02}
.end p{font-size:36px;color:var(--ink-2);font-weight:600;margin-top:40px;line-height:1.32}
.sig{left:72px;top:1380px;display:flex;align-items:center;gap:16px;font-size:30px;color:var(--muted)}
.sig svg{width:56px;height:56px;color:#fff}.sig b{color:var(--ink);font-weight:600}
'''
def paper(id,x,y,rot,box,name,pill,cls):
    return f'<div class="paper" id="{id}" style="left:{x}px;top:{y}px;--r:{rot}deg"><span class="bx">{box}</span><b>{name}</b><div class="ln" style="width:90%"></div><div class="ln" style="width:70%"></div><div class="ln" style="width:80%"></div><span class="pill {cls}">{pill}</span></div>'
body='''<div class="grid"></div><div class="glow" id="g1" style="width:1100px;height:1100px"></div>
<div class="abs top" id="top"><div class="brand"><svg><use href="#logo"/></svg><b>Fiscal Hub</b></div><span class="pill acc">NOVIDADE</span></div>
<div class="abs hook" id="hook"><h1><span class="metal" style="display:block" id="h1">Nem toda nota</span><span class="acc-t" id="h2">passa no coletor.</span></h1><p id="hp">E QUANDO NÃO PASSA, QUEM CONFERE?</p></div>
<div id="A"><div class="abs ttl" id="ta"><span class="metal" style="display:block">A do CEASA,</span><span class="acc-t">por exemplo.</span></div>'''+\
paper('p1',72,640,-3,'CEASA · BOX 12','HORTI VALE VERDE','nota em papel','mut')+\
paper('p2',448,860,2.5,'CEASA · BOX 7','FRUTAS SOL NASCENTE','foto no celular','mut')+\
paper('p3',110,1090,-1.5,'CEASA · BOX 3','VERDURAS BOA COLHEITA','chega depois','mut')+\
'''<div class="abs sub2" id="sa">Entra no sistema por outro caminho.<br>E é aí que alguma fica pra trás.</div></div>
<div id="B"><div class="abs ttl" id="tb" style="top:390px"><span class="metal" style="display:block">Agora a IA confere</span><span class="acc-t">uma por uma.</span></div>
<div class="abs card app" id="app">
 <div class="wh"><b>Conferência CEASA</b><span class="ai">IA · conferindo</span></div>
 <div style="position:relative" id="rows">
  <div class="beam" id="beam"></div>
  <div class="rw" id="w1"><div><div class="n">HORTI VALE VERDE</div><div class="m">box 12 · nota em papel</div></div><span class="wait" id="x1">aguardando</span></div>
  <div class="rw" id="w2"><div><div class="n">FRUTAS SOL NASCENTE</div><div class="m">box 7 · foto no celular</div></div><span class="wait" id="x2">aguardando</span></div>
  <div class="rw" id="w3"><div><div class="n">VERDURAS BOA COLHEITA</div><div class="m">box 3 · chegou depois</div></div><span class="wait" id="x3">aguardando</span></div>
 </div>
 <div class="sum" id="sm"><span><b>1</b> lançada</span><span><b>1</b> com diferença</span><span><b>1</b> faltando</span></div>
</div></div>
<div class="abs end" id="end"><h2><span class="metal" style="display:block">A IA confere.</span><span class="acc-t">Você decide.</span></h2>
<p>Nota do CEASA conferida com os<br>lançamentos, sem nenhuma ficar pra trás.</p></div>
<div class="abs sig" id="sig"><svg><use href="#logo"/></svg><span><b>Fiscal Hub</b> · conferência CEASA com IA</span></div>'''
code='''
const RES=[['grn','lançada ✓'],['yel','valor diferente'],['red','não lançada']];
function render(t){bg(t);
 $('g1').style.left=(200+Math.sin(t*.42)*170)+'px';$('g1').style.top=(350+Math.cos(t*.31)*220)+'px';
 appear($('top'),t,0,.45,20);
 appear($('h1'),t,.1,.5,60,2.8,.35);appear($('h2'),t,.5,.5,60,2.8,.35);appear($('hp'),t,1.1,.45,20,2.8,.35);
 $('hook').style.display=t<2.85?'block':'none';
 const Aon=t>=2.8&&t<6.4;$('A').style.display=Aon?'block':'none';
 if(Aon){const out=6.3;appear($('ta'),t,2.85,.45,30,out,.3);
  ['p1','p2','p3'].forEach((p,i)=>{const el=$(p);const a=3.2+i*.45;const k=eo(P(t,a,a+.5));const o=1-P(t,out-.3,out);
   const r=parseFloat(el.style.getPropertyValue('--r'));const fl=Math.sin(t*1.6+i)*6;
   el.style.opacity=k*o;el.style.transform=`translateY(${((1-k)*120+fl).toFixed(1)}px) rotate(${(r*(.6+.4*k)).toFixed(2)}deg)`;});
  appear($('sa'),t,4.8,.45,24,out,.3);}
 const Bon=t>=6.4&&t<12.6;$('B').style.display=Bon?'block':'none';
 if(Bon){const out=12.5;appear($('tb'),t,6.45,.45,30,out,.3);
  const ai=eo(P(t,6.7,7.2));$('app').style.opacity=ai*(1-P(t,out-.3,out));$('app').style.transform=`translateY(${(1-ai)*90}px)`;
  const bk=P(t,7.4,10.6);const H=$('rows').offsetHeight;$('beam').style.top=(-65+bk*(H))+'px';$('beam').style.opacity=bk>0&&bk<1?1:0;
  [8.3,9.35,10.4].forEach((a,i)=>{const x=$('x'+(i+1));if(t>=a){x.className='pill '+RES[i][0];x.textContent=RES[i][1];x.style.transform=`scale(${back(P(t,a,a+.3)).toFixed(3)})`}else{x.className='wait';x.textContent=t>=7.3?'conferindo…':'aguardando';x.style.transform='none'}});
  appear($('sm'),t,10.9,.4,16);if(t<10.9)$('sm').style.opacity=0;
  $('app').querySelector('.ai').textContent=t>=10.8?'IA · conferido':'IA · conferindo';
 }
 const e=$('end');e.style.opacity=t>=12.55?1:0;
 [...e.querySelectorAll('h2 span')].forEach((s,i)=>appear(s,t,12.6+i*.4,.45,50));appear(e.querySelector('p'),t,13.7,.45,24);
 appear($('sig'),t,14.2,.45,20);if(t<12.5)$('sig').style.opacity=0;
}'''
open('reel3.html','w').write(page('Reel CEASA',1080,1920,css,body,code,17))
