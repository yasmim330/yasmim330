# Story ter 03/11: 104 BPM, Fá maior, marimba + shaker, clima de quiz com relógio.
from trilib import *
T=Track(10.0,seed=33);r=T.rng;B=60/104
prog=[[53,57,60],[50,53,57],[46,50,53],[48,52,55]]  # F Dm Bb C
mel=[77,81,79,77,76,77,72,74]
for bar in range(5):
    s=bar*4*B
    if s>=10: break
    c=prog[bar%4]
    T.add(pad([n+12 for n in c],4*B+.1,1800),s,.32)
    for k in range(8):
        tt=s+k*B/2
        if tt>=10: break
        T.add(marimba(c[k%3]+24 if k%2 else c[0]+12),tt,.2,-.3 if k%2 else .3)
        T.add(shaker(r),tt+B/4,.25,.2)
        if k%2==0 and s>=4.6: T.add(kick(),tt,.7)
        if k in (2,6): T.add(snap(r),tt,.35)
        if s<4.6 and k%2==0: T.add(bass(c[0]-12,.4),tt,.3)
        elif s>=4.6: T.add(bass(c[0]-12),tt,.38)
# relogio 1.6-4.6
for x in np.arange(1.6,4.6,B/2): T.add(tick(r),x,2.2)
for a in (1.6,2.6,3.6): T.add(pop(1200),a,.35)
T.add(bell(84),4.6,.45)
# efeitos
T.add(whoosh(r,.6),0.0,.4)
for k,a in enumerate((1.6,1.78,1.96)): T.add(pop(700+k*120),a,.35)
for i in range(1,15): T.add(tick(r),4.9+i*.1,2.5)
T.add(riser(r,1.0),5.5,.5)
T.add(impact(r),6.5,.5);T.add(chime(84),6.5,.5);T.add(chime(88),6.62,.35);T.add(pop(1000),6.5,.5)
T.add(pop(800),7.0,.35)
T.save('tri_s.wav')
