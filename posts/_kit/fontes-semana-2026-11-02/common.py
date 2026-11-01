LOGO='''<svg width="0" height="0" style="position:absolute"><symbol id="logo" viewBox="0 0 100 100">
<path d="M50 7 L87 28.5 V71.5 L50 93 L13 71.5 V28.5 Z" fill="none" stroke="currentColor" stroke-width="5.5" stroke-linejoin="round"/>
<path d="M50 47 V25 M50 47 L28 36 M50 47 L72 36 M50 47 L28 63 M50 47 L72 63 M50 47 V68" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" opacity=".75"/>
<g fill="currentColor"><circle cx="50" cy="24" r="5.2"/><circle cx="27.5" cy="35.5" r="5.2"/><circle cx="72.5" cy="35.5" r="5.2"/><circle cx="27.5" cy="63.5" r="5.2"/><circle cx="72.5" cy="63.5" r="5.2"/>
<rect x="41.5" y="38.5" width="17" height="17" rx="3" fill="#ff7a1a"/><path d="M42 67.5 H58 L50 82 Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></g></symbol></svg>'''
JS='''const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const P=(t,a,b)=>cl((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3), eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const back=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
function appear(el,t,a,dur=.5,dy=40,out=null,od=.35){const i=eo(P(t,a,a+dur));let o=i,y=(1-i)*dy,bl=(1-i)*12;
 if(out!=null){const k=eio(P(t,out-od,out));o*=1-k;bl+=k*12;y-=k*20}
 el.style.opacity=o;el.style.filter=bl>.05?`blur(${bl.toFixed(2)}px)`:'none';el.style.transform=`translateY(${y.toFixed(1)}px)`}
function popIn(el,t,a,dur=.35){const k=P(t,a,a+dur);el.style.opacity=k>0?Math.min(1,k*3):0;el.style.transform=`scale(${k>0?back(k).toFixed(3):.6})`}
const metals=[...document.querySelectorAll('.metal')];
function bg(t){metals.forEach(m=>m.style.backgroundPosition=`${(130-((t*40)%260)).toFixed(1)}% 0`);
 const g=document.querySelector('.grid'); if(g) g.style.backgroundPosition=`0 ${(-t*10).toFixed(1)}px`;}
'''
TAIL='''<script>{JS}
{CODE}
window.render=render;
const q=new URLSearchParams(location.search);if(q.has('t'))render(parseFloat(q.get('t')));
else{const t0=performance.now();(function L(){render(((performance.now()-t0)/1000)%{DUR});requestAnimationFrame(L)})()}
</script></body></html>'''
def page(title,w,h,css,body,code=None,dur=15):
    s=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="brand.css"><style>html,body{{width:{w}px;height:{h}px}}
.stage{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:radial-gradient(1100px 900px at 50% 38%,#0f0f12,#08080a 70%)}}
.abs{{position:absolute}}
.brand{{display:flex;align-items:center;gap:14px}}.brand svg{{width:54px;height:54px;color:#fff}}.brand b{{font-size:29px;font-weight:600;letter-spacing:-.02em}}
{css}</style></head><body><div class="stage" id="stage">{LOGO}{body}</div>'''
    if code is None: return s+'</body></html>'
    return s+TAIL.replace('{JS}',JS).replace('{CODE}',code).replace('{DUR}',str(dur))
