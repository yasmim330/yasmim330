# Reel seg 09/11 CEASA: 110 BPM, Mi menor, pulso de sintetizador e "varredura" da IA.
from trilib import *
D=17.0;T=Track(D,seed=93);r=T.rng;B=60/110;bar=4*B
prog=[[52,55,59],[48,52,55],[43,47,50],[50,54,57]]  # Em C G D
s=0.0;i=0
while s<12.55:
    c=prog[i%4];sec=0 if s<2.8 else (1 if s<6.4 else 2)
    T.add(pad([n+12 for n in c],bar+.1,1300+sec*500),s,.38)
    for k in range(16):
        tt=s+k*B/4
        if tt>=12.55: break
        if sec>=1 and k%2==0: T.add(pluck(c[(k//2)%3]+24,.18,3000+sec*900,16),tt,.09,-.3 if k%4 else .3)
        if k%4==0:
            if sec>=1: T.add(kick(),tt,.8)
            T.add(bass(c[0]-12,.3),tt,.4)
        if sec==2 and k%4==2: T.add(hat(r),tt,.2,.3)
        if sec==2 and k in (4,12): T.add(clap(r),tt,.3)
    s+=bar;i+=1
T.add(impact(r),0,.5);T.add(riser(r,1.0),1.8,.5)
T.add(whoosh(r,.7),2.5,.55);T.add(whoosh(r,.7),6.1,.55)
for k in range(3): T.add(pop(650+k*120),3.2+k*.45,.45)
T.add(pop(900),6.7,.4)
# varredura
tt=t_(3.2);sweep=np.sin(2*np.pi*np.cumsum(300+500*np.abs(np.sin(np.pi*tt/1.06)))/SR)*.06*np.sin(np.pi*tt/3.2)
T.add(sweep,7.4,1.0)
T.add(chime(83),8.3,.45);T.add(pop(700),9.35,.5);T.add(pop(500),10.4,.55);T.add(click(r),10.4,.6)
T.add(pop(1000),10.9,.4)
T.add(impact(r),12.55,.7);T.add(pad([40,52,59,64,67],4.4,1700),12.55,.6)
T.add(bell(76),12.6,.35);T.add(bell(83),13.0,.35);T.add(chime(88),14.2,.3)
T.save('tri_r3.wav')
