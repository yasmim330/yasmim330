# Reel sex 06/11: 124 BPM, Sol maior, house leve com pluck saltitante. Tutorial em 3 passos.
from trilib import *
D=19.0;T=Track(D,seed=62);r=T.rng;B=60/124;bar=4*B
prog=[[55,59,62],[52,55,59],[48,52,55],[50,54,57]]  # G Em C D
mel=[79,83,81,79,78,79,74,76,79,86,83,81]
s=0.0;i=0
while s<D-2.6:
    c=prog[i%4];sec=0 if s<2.6 else (1 if s<9.4 else 2)
    T.add(pad([n+12 for n in c],bar+.1,1600+sec*400),s,.36)
    for k in range(8):
        tt=s+k*B/2
        if tt>=D-2.6: break
        if sec>=1:
            T.add(bass(c[0]-12,.2),tt+B/4 if k%2==0 else tt,.38)   # baixo no contratempo
            if k%2==0: T.add(kick(),tt,.8)
            T.add(hat(r),tt+B/4,.16,.25)
            if k in (2,6): T.add(clap(r),tt,.3)
        T.add(pluck(c[(k*2)%3]+24,.22,4200,14),tt,.11 if sec==0 else .13,-.35 if k%2 else .35)
        if sec==2 and k%2==0: T.add(marimba(mel[(i*4+k//2)%12]),tt,.2,.15)
    s+=bar;i+=1
T.add(riser(r,1.2),1.5,.5)
T.add(impact(r),D-2.6-.5+.5-0.5+0.5-0.5,.0)
T.add(impact(r),15.9,.65);T.add(pad([43,55,62,67,71],3.1,1800),15.9,.6)
for k,m in enumerate([79,83,86]): T.add(bell(m),16.0+k*.3,.32)
T.add(chime(91),17.4,.35)
# efeitos
T.add(pop(800),.1,.35);T.add(pop(950),.5,.35);T.add(pop(1100),.9,.4)
for a in (2.6,6.4,9.4): T.add(whoosh(r,.6),a-.3,.5)
for x in np.arange(3.5,4.1,.12): T.add(tick(r),x,2.2)
T.add(click(r),4.6,.9);T.add(pop(1000),4.8,.45);T.add(pop(1150),5.1,.45)
for x in np.arange(7.0,7.8,.08): T.add(tick(r),x,2.0)
for k in range(3): T.add(pop(800+k*150),8.3+k*.25,.45)
for k in range(3): T.add(pop(700+k*180),9.9+k*.45,.5)
T.add(click(r),12.85,1.0);T.add(chime(86),12.9,.45);T.add(chime(91),13.02,.3)
T.add(whoosh(r,.7),15.6,.55)
T.save('tri_r2.wav')
