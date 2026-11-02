from common import page
css='''
.brand{left:50%;top:290px;transform:translateX(-50%)}
.k{left:0;right:0;top:420px;text-align:center;font-family:var(--mono);font-size:28px;color:var(--acc-2);letter-spacing:.1em}
h1{left:70px;right:70px;top:476px;text-align:center;font-size:88px;font-weight:700;letter-spacing:-.045em;line-height:1.03}
.tiles{left:90px;right:90px;top:780px;display:flex;flex-direction:column;gap:26px}
.tile{display:grid;grid-template-columns:100px 1fr;align-items:center;height:150px;border-radius:30px;background:var(--panel);border:1px solid var(--line-2);padding:0 36px;position:relative}
.tile .L{font-family:var(--mono);font-size:56px;font-weight:600;color:var(--muted)}
.tile b{font-size:40px;font-weight:600;letter-spacing:-.02em}
.tile span{display:block;font-size:25px;color:var(--muted);margin-top:4px;font-weight:500}
.tile.hi{border-color:var(--acc);background:var(--acc-soft);box-shadow:0 0 0 6px rgba(255,122,26,.08)}
.tile.hi .L{color:var(--acc)}
.cta{left:50%;top:1400px;transform:translateX(-50%);font-size:32px;padding:20px 34px;white-space:nowrap}
'''
body='''<div class="grid"></div><div class="glow" id="g1" style="width:1000px;height:1000px"></div>
<div class="abs brand" id="br"><svg><use href="#logo"/></svg><b>Fiscal Hub</b></div>
<div class="abs k" id="k">CEASA · ISSO OU AQUILO</div>
<h1 class="abs"><span class="metal" style="display:block" id="t1">A nota do CEASA</span><span class="acc-t" id="t2">chega aí como?</span></h1>
<div class="abs tiles">
<div class="tile" id="a"><span class="L">A</span><div><b>No papel</b><span>dobrada junto com a mercadoria</span></div></div>
<div class="tile" id="b"><span class="L">B</span><div><b>Foto no celular</b><span>alguém manda depois</span></div></div>
<div class="tile" id="c"><span class="L">C</span><div><b>Dias depois</b><span>e aí ninguém lembra de lançar</span></div></div>
</div>
<span class="abs pill acc cta" id="cta">Responde com a letra no direct ↗</span>'''
code='''
function render(t){bg(t);
 $('g1').style.left=(40+Math.sin(t*.5)*200)+'px';$('g1').style.top=(700+Math.cos(t*.4)*200)+'px';
 appear($('br'),t,0,.4,20);appear($('k'),t,.2,.4,20);appear($('t1'),t,.4,.45,40);appear($('t2'),t,.8,.45,40);
 ['a','b','c'].forEach((x,i)=>{appear($(x),t,1.4+i*.25,.45,60);
   const cyc=t>=3.0&&t<7.6?Math.floor((t-3.0)/.75)%3:-1;const on=cyc===i||(t>=7.6);
   $(x).classList.toggle('hi',on&&t<7.6);
   if(t>=3.0) $(x).style.transform=`translateY(0) scale(${(cyc===i&&t<7.6)?1.03:1})`;});
 const k=eo(P(t,7.6,8.1));const c=$('cta');c.style.opacity=k;
 c.style.transform=`translateX(-50%) translateY(${(1-k)*30}px) scale(${1+(t>8.1?.04*Math.max(0,Math.sin(t*5)):0)})`;
}'''
open('story2.html','w').write(page('Story CEASA',1080,1920,css,body,code,10))
