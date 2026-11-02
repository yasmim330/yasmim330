# Story ter 10/11: 120 BPM, Si bemol maior, synth-pop curtinho com "seletor" passando pelas opções.
from trilib import *
D=10.0;T=Track(D,seed=57);r=T.rng;B=0.5;bar=2.0
prog=[[58,62,65],[55,58,62],[51,55,58],[53,57,60]]  # Bb Gm Eb F
for i in range(5):
    s=i*bar;c=prog[i%4]
    T.add(pad([n+12 for n in c],bar+.1,1800),s,.36)
    for k in range(8):
        tt=s+k*.25
        T.add(pluck(c[k%3]+24,.2,4500,15),tt,.1,-.3 if k%2 else .3)
        if s>=1.4:
            if k%2==0: T.add(kick(),tt,.75)
            T.add(hat(r),tt+.125,.18,.3)
            if k in (2,6): T.add(clap(r),tt,.28)
            T.add(bass(c[0]-12,.2),tt,.35)
T.add(whoosh(r,.6),0,.4)
for k in range(3): T.add(pop(700+k*140),1.4+k*.25,.45)
for j in range(6): T.add(click(r),3.0+j*.75,.6);T.add(pop(1000+(j%3)*150),3.0+j*.75,.3)
T.add(chime(82),7.6,.45);T.add(chime(86),7.72,.3)
T.save('tri_s2.wav')
