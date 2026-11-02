from common import page
css='''

.sl{display:none;position:absolute;inset:0}.sl.on{display:block}
.top{left:72px;right:72px;top:64px;display:flex;justify-content:space-between;align-items:center}
.top .mono{font-size:24px;color:var(--muted);letter-spacing:.06em}
.top .mono b{color:var(--acc-2);font-weight:600}
.k{left:72px;top:190px;font-family:var(--mono);font-size:24px;color:var(--acc-2);letter-spacing:.1em}
h1{left:72px;right:72px;top:236px;font-size:76px;font-weight:700;letter-spacing:-.045em;line-height:1.03}
h1.big{top:240px;font-size:128px;line-height:.98}
.sub{left:72px;right:72px;font-size:34px;font-weight:600;color:var(--ink-2);line-height:1.34}
.flow{left:0;right:0;top:1190px;height:60px}
.flow .ln{position:absolute;left:0;right:0;top:29px;height:2px;background:linear-gradient(90deg,var(--line-2),var(--acc-line),var(--line-2))}
.flow .nd{position:absolute;top:12px;width:36px;height:36px;margin-left:-18px;border-radius:50%;background:var(--bg);border:2px solid var(--line-2)}
.flow .nd.on{border-color:var(--acc);background:var(--acc);box-shadow:0 0 22px var(--acc)}
.flow .nd.past{border-color:var(--acc-line);background:var(--acc-soft)}
.swipe{right:72px;top:1268px;font-family:var(--mono);font-size:22px;color:var(--muted)}
.foot{left:72px;top:1268px;font-family:var(--mono);font-size:22px;color:var(--faint)}
.card{padding:34px 38px}
.lbl{font-family:var(--mono);font-size:21px;color:var(--muted);letter-spacing:.06em;margin-bottom:10px}
.big-d{font-family:var(--mono);font-size:58px;font-weight:600;color:var(--ink)}
.pill{font-size:23px;padding:9px 18px}
.pill.red{background:rgba(255,97,97,.12);color:var(--red);border-color:rgba(255,97,97,.28)}
.kv{display:flex;justify-content:space-between;align-items:center;padding:22px 0;border-top:1px solid var(--line);font-size:30px;font-weight:600}
.kv .mono{font-size:32px;color:var(--ink)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.arrow{font-family:var(--mono);color:var(--acc);font-size:40px;text-align:center}
.tip{left:72px;right:72px;top:1030px;display:flex;gap:18px;align-items:flex-start;font-size:29px;color:var(--ink-2);font-weight:500;line-height:1.35}
.tip i{flex:none;font-style:normal;font-family:var(--mono);font-size:20px;color:#140800;background:var(--acc);border-radius:8px;padding:6px 10px;margin-top:4px;font-weight:600}
.feat{display:grid;grid-template-columns:64px 1fr;gap:22px;align-items:center;padding:26px 0;border-top:1px solid var(--line)}
.feat .ic{width:64px;height:64px;border-radius:18px;background:var(--acc-soft);border:1px solid var(--acc-line);display:grid;place-items:center;font-family:var(--mono);font-size:24px;color:var(--acc-2);font-weight:600}
.feat b{display:block;font-size:31px;font-weight:600}
.feat span{display:block;font-size:24px;color:var(--muted);margin-top:4px}
'''
def flow(i):
    xs=[140,300,460,620,780,940]
    nd=''.join(f'<div class="nd {"on" if j==i else ("past" if j<i else "")}" style="left:{x}px"></div>' for j,x in enumerate(xs))
    return f'<div class="abs flow"><div class="ln"></div>{nd}</div>'
def top(i):
    return f'<div class="abs top"><div class="brand"><svg><use href="#logo"/></svg><b>Fiscal Hub</b></div><span class="mono"><b>{i+1:02d}</b> / 06</span></div>'
S=[]
extra_css=""".src{left:72px;right:72px;top:1268px;font-family:var(--mono);font-size:18px;color:var(--faint)}
.field{display:grid;grid-template-columns:1fr 1fr 1.2fr;gap:14px;margin-top:16px}
.fd{border-radius:16px;background:#0d0d10;border:1px solid var(--line-2);padding:16px 18px}
.fd small{display:block;font-family:var(--mono);font-size:18px;color:var(--muted);letter-spacing:.06em}
.fd b{display:block;font-family:var(--mono);font-size:28px;margin-top:6px;color:var(--ink)}
.fd.hi{border-color:var(--acc);background:var(--acc-soft)}.fd.hi small{color:var(--acc-2)}
.bubq{background:#1b1b21;border:1px solid var(--line-2);border-radius:26px 26px 26px 6px;padding:22px 28px;font-size:31px;font-weight:500;line-height:1.3}
.bubq small{display:block;font-family:var(--mono);font-size:18px;color:var(--muted);margin-bottom:8px;letter-spacing:.06em}
.bigd{font-family:var(--mono);font-size:120px;font-weight:600;color:var(--acc);letter-spacing:-.04em;line-height:1}
"""
S.append(f"""{top(0)}<div class="abs k">REFORMA TRIBUTÁRIA · SEM ENROLAÇÃO</div>
<h1 class="abs big" style="font-size:112px"><span class="metal" style="display:block">A nota ganhou</span><span class="metal" style="display:block">um código novo.</span><span class="acc-t">Sabe ler?</span></h1>
<div class="abs" style="left:72px;right:200px;top:760px"><div class="bubq"><small>SITUAÇÃO FICTÍCIA · 1º DIA NO FISCAL</small>“Que código é esse aqui no item da nota do laticínio?”</div></div>
<div class="abs sub" style="top:980px;font-size:30px">Arrasta que eu explico em 5 cards.</div>
{flow(0)}<span class="abs swipe">arrasta →</span>""")
S.append(f"""{top(1)}<div class="abs k">O NOME DELE</div>
<h1 class="abs"><span class="metal" style="display:block">cClassTrib.</span><span class="acc-t">Classificação tributária.</span></h1>
<div class="abs sub" style="top:430px">É o código que diz qual hipótese da<br>Lei Complementar 214/2025 vale para<br>aquele item, no IBS e na CBS.</div>
<div class="abs card" style="left:72px;right:72px;top:690px"><div class="lbl">ITEM DA NOTA · EXEMPLO VISUAL</div>
<div style="font-size:30px;font-weight:600">Iogurte natural 170 g</div>
<div class="field"><div class="fd"><small>NCM</small><b>····</b></div><div class="fd"><small>CST</small><b>···</b></div><div class="fd hi"><small>cCLASSTRIB</small><b>······</b></div></div></div>
<div class="abs tip" style="top:1040px"><i>NOTA</i><span>Os campos estão em branco de propósito. A classificação certa depende do produto e da operação.</span></div>
{flow(1)}<span class="abs swipe">arrasta →</span>""")
S.append(f"""{top(2)}<div class="abs k">ELE NÃO ANDA SOZINHO</div>
<h1 class="abs"><span class="metal" style="display:block">Anda junto</span><span class="acc-t">com o CST.</span></h1>
<div class="abs card" style="left:72px;right:72px;top:450px">
<div class="kv" style="border-top:0"><span>CST</span><span style="font-size:27px;color:var(--ink-2);font-weight:500">a situação do item</span></div>
<div class="kv"><span>cClassTrib</span><span style="font-size:27px;color:var(--ink-2);font-weight:500">o detalhe dentro dela</span></div>
<div class="kv"><span>Combinação</span><span style="font-size:27px;color:var(--ink-2);font-weight:500">cada CST aceita só alguns</span></div></div>
<div class="abs card" style="left:72px;right:72px;top:820px;padding:26px 34px;display:flex;justify-content:space-between;align-items:center">
<div style="font-size:28px;font-weight:600;line-height:1.3">Código que não combina<br>com o CST</div><span class="pill red">rejeição 1024</span></div>
{flow(2)}<span class="abs src">Fonte: NT 2025.002 (regras de validação)</span>""")
S.append(f"""{top(3)}<div class="abs k">DESDE QUANDO</div>
<div class="abs bigd" style="left:72px;top:250px">03/08/2026</div>
<div class="abs sub" style="top:410px">IBS e CBS destacados na NF-e passaram a ser<br>obrigatórios para quem está no regime normal.<br>O Simples Nacional entra em 2027.</div>
<div class="abs two" style="left:72px;right:72px;top:640px">
<div class="card"><div class="lbl">CBS EM 2026</div><div class="big-d" style="color:var(--acc-2)">0,9%</div><div style="font-size:24px;color:var(--muted);margin-top:8px">alíquota de teste</div></div>
<div class="card"><div class="lbl">IBS EM 2026</div><div class="big-d" style="color:var(--acc-2)">0,1%</div><div style="font-size:24px;color:var(--muted);margin-top:8px">alíquota de teste</div></div></div>
<div class="abs tip" style="top:960px"><i>2026</i><span>Ano de teste: quem cumpre as obrigações acessórias fica dispensado de recolher esses valores.</span></div>
{flow(3)}<span class="abs src">Fonte: LC 214/2025, art. 348 · Ato Conjunto RFB/CGIBS nº 4/2026</span>""")
S.append(f"""{top(4)}<div class="abs k">O DETALHE QUE PEGA</div>
<h1 class="abs"><span class="metal" style="display:block">Nota autorizada</span><span class="acc-t">não é nota certa.</span></h1>
<div class="abs card" style="left:72px;right:72px;top:450px">
<div class="kv" style="border-top:0"><span>O código existe na tabela?</span><span class="pill grn">a SEFAZ confere</span></div>
<div class="kv"><span>Combina com o CST?</span><span class="pill grn">a SEFAZ confere</span></div>
<div class="kv"><span>É o certo pra essa operação?</span><span class="pill yel">não confere</span></div></div>
<div class="abs tip" style="top:860px"><i>QUEM</i><span>Quem classifica é a empresa que emite a nota. O sistema só dá o campo, a escolha é dela.</span></div>
{flow(4)}<span class="abs src">Fonte: NT 2025.002 · LC 214/2025</span>""")
S.append(f"""{top(5)}<div class="abs k">E NO BALCÃO DO FISCAL?</div>
<h1 class="abs"><span class="metal" style="display:block">Repara no campo.</span><span class="acc-t">Dúvida? Contabilidade.</span></h1>
<div class="abs card" style="left:72px;right:72px;top:470px;padding:14px 38px">
<div class="feat" style="border-top:0"><span class="ic">01</span><div><b>Saber que o campo existe</b><span>IBS, CBS e a classificação de cada item</span></div></div>
<div class="feat"><span class="ic">02</span><div><b>Não “arrumar” nota de fornecedor</b><span>quem corrige é quem emitiu</span></div></div>
<div class="feat"><span class="ic">03</span><div><b>Levar a dúvida pra contabilidade</b><span>as regras ainda estão sendo atualizadas</span></div></div></div>
<div class="abs sub" style="top:1000px;font-size:29px">O Fiscal Hub cuida de nota, boleto e vencimento.<br>Classificação é com quem emite e com a contabilidade.</div>
{flow(5)}<span class="abs foot">@yassmim.dev</span>""")
body='<div class="grid"></div><div class="glow" id="g1" style="width:800px;height:800px;left:450px;top:-280px"></div><div class="glow" style="width:600px;height:600px;left:-250px;top:900px;opacity:.5"></div>'+''.join(f'<div class="sl" id="s{i+1}">{s}</div>' for i,s in enumerate(S))
body+='<script>const n=new URLSearchParams(location.search).get("s")||"1";document.getElementById("s"+n).classList.add("on");const g=document.getElementById("g1");g.style.left=(450-(n-1)*120)+"px";</script>'
open('car2.html','w').write(page('Carrossel classificacao',1080,1350,css+extra_css,body))
