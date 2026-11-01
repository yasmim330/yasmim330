# Reel seg 02/11: 116 BPM, Ré menor, eletrônico leve. Duas metades: "sem lista" tensa, "com lista" aberta.
from trilib import *
T=Track(15.0,seed=21);r=T.rng;B=60/116
CH_A=[[50,53,57],[46,50,53],[48,52,55],[45,49,52]]   # Dm Bb C A (tenso)
CH_B=[[50,53,57,62],[46,50,53,58],[41,45,48,53],[48,52,55,60]] # Dm Bb F C (aberto)
t=0.0;bar=4*B
# intro 0-3: pad + kick suave
T.add(impact(r),0.0,.55);T.add(pad([62,65,69],3.2),0.0,.5)
for k in range(6): T.add(pluck(74 if k%2 else 69,.3,2600),0.25+k*B,.12,.3 if k%2 else -.3)
T.add(riser(r,.8),2.2,.6)
# A 3.0-7.9: baixo pulsado, arpejo inquieto, chimbal
s=3.0;i=0
while s<7.9:
    c=CH_A[i%4]
    T.add(pad([n+12 for n in c],bar+.1),s,.38)
    for k in range(8):
        tt=s+k*B/2
        if tt>=7.9: break
        T.add(bass(c[0]-12),tt,.4); T.add(pluck(c[k%3]+24,.25,3800,12),tt,.13,-.4 if k%2 else .4)
        if k%2==0: T.add(kick(),tt,.75)
        else: T.add(hat(r),tt,.2,.3)
    s+=bar;i+=1
# B 7.9-12.4: abre, palmas, melodia
s=7.9;i=0;mel=[74,77,76,72,74,81,79,77]
while s<12.4:
    c=CH_B[i%4]
    T.add(pad([n+12 for n in c],bar+.1,2000),s,.42)
    for k in range(8):
        tt=s+k*B/2
        if tt>=12.4: break
        T.add(bass(c[0]-12+(12 if k%4==2 else 0)),tt,.42)
        if k%2==0: T.add(kick(),tt,.85)
        T.add(hat(r),tt+B/4,.18,.3)
        if k in (2,6): T.add(clap(r),tt,.32)
        if k%2==0: T.add(marimba(mel[(i*4+k//2)%8]),tt,.22,.2)
    s+=bar;i+=1
# final 12.4-15
T.add(impact(r),12.35,.7);T.add(pad([50,57,62,65,69],2.7,1800),12.35,.6)
for k,m in enumerate([74,77,81]): T.add(bell(m),12.4+k*.3,.35)
T.add(chime(86),13.8,.4)
# efeitos sincronizados
for a in (3.0,7.9): T.add(whoosh(r,.7),a-.35,.6)
T.add(pop(700),.45,.4);T.add(pop(900),.1,.3)
for a in (4.55,5.4,6.25,7.1): T.add(pop(1000),a,.55); T.add(click(r),a,.5)
for k,a in enumerate((8.75,9.15,9.55,9.95)): T.add(pop(650+k*150),a,.5)
T.add(chime(81),10.6,.4)
T.save('tri_r1.wav')
