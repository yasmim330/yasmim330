# Reel sex 13/11: 100 BPM, Lá maior, groove leve com violão sintético (pluck) e virada de página.
from trilib import *
D=16.0;T=Track(D,seed=44);r=T.rng;B=60/100;bar=4*B
prog=[[57,61,64],[54,57,61],[50,54,57],[52,56,59]]  # A F#m D E
mel=[76,78,81,80,76,73,76,78]
s=0.0;i=0
while s<12.4:
    c=prog[i%4];sec=0 if s<2.9 else (1 if s<8.3 else 2)
    T.add(pad([n+12 for n in c],bar+.1,1500+sec*400),s,.34)
    for k in range(8):
        tt=s+k*B/2
        if tt>=12.4: break
        T.add(pluck(c[[0,1,2,1][k%4]]+12,.4,2400,7),tt,.16,-.4 if k%2 else .4)
        if sec>=1:
            if k%4==0: T.add(kick(),tt,.75)
            if k%4==2: T.add(snap(r),tt,.4)
            T.add(shaker(r),tt+B/4,.22)
            T.add(bass(c[0]-12,.28),tt,.35 if k%2==0 else .2)
        if sec==2 and k%2==0: T.add(bell(mel[(i*4+k//2)%8],.6),tt,.18,.2)
    s+=bar;i+=1
T.add(riser(r,1.0),1.9,.5);T.add(whoosh(r,.6),2.6,.5)
for x in np.arange(4.0,4.8,.08): T.add(tick(r),x,2.0)
T.add(pop(600),5.1,.5);T.add(pop(560),5.7,.5)
T.add(whoosh(r,.9,up=False),7.85,.7);T.add(click(r),8.3,.6)
T.add(chime(85),9.0,.4);T.add(pop(900),10.0,.4)
T.add(impact(r),12.4,.6);T.add(pad([45,57,61,64,69],3.6,1700),12.4,.6)
for k,m in enumerate([76,81,85]): T.add(bell(m),12.45+k*.4,.3)
T.save('tri_r4.wav')
