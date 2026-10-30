"""Trilha original do Reels de fornecedores (21 s, 120 BPM, Lá menor).
Sintetizada do zero: sem samples, sem risco de direitos autorais."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 44100
DUR = 16.5
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)
BEAT = 0.5  # 120 BPM
rng = np.random.default_rng(7)

def t_(d): return np.arange(int(d * SR)) / SR
def hz(m): return 440 * 2 ** ((m - 69) / 12)
def add(sig, at, gain=1.0, pan=0.0):
    i = int(at * SR)
    if i >= N: return
    s = sig[: N - i] * gain
    L[i:i + len(s)] += s * np.sqrt((1 - pan) / 2) * 1.414
    R[i:i + len(s)] += s * np.sqrt((1 + pan) / 2) * 1.414
def env(n, a, r):
    e = np.ones(n); ai = max(1, int(a * SR)); ri = max(1, int(r * SR))
    e[:ai] = np.linspace(0, 1, ai); e[-ri:] *= np.linspace(1, 0, ri); return e
def filt(x, kind, f, order=2):
    return sosfilt(butter(order, f, btype=kind, fs=SR, output='sos'), x)

# ---- instrumentos ----
def pad(notes, d):
    tt = t_(d); s = np.zeros_like(tt)
    for m in notes:
        for det in (-0.12, 0.0, 0.12):
            f = hz(m) * 2 ** (det / 12)
            s += (2 * ((tt * f) % 1) - 1)  # serra
    s = filt(s, 'low', 1400, 2)
    return s * env(len(tt), 0.35, 0.5) / (len(notes) * 3)
def pluck(m, d=0.35):
    tt = t_(d); f = hz(m)
    s = np.sign(np.sin(2 * np.pi * f * tt)) * 0.5 + np.sin(2 * np.pi * 2 * f * tt) * 0.5
    s = filt(s, 'low', 3200, 2)
    return s * np.exp(-tt * 9)
def bass(m, d=0.24):
    tt = t_(d); f = hz(m)
    s = np.sin(2 * np.pi * f * tt) + 0.35 * (2 * ((tt * f) % 1) - 1)
    s = filt(s, 'low', 600, 2)
    return s * env(len(tt), 0.005, 0.06)
def kick():
    tt = t_(0.35); f = 45 + 110 * np.exp(-tt * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-tt * 7) * 1.1
def hat(d=0.05):
    tt = t_(d); return filt(rng.standard_normal(len(tt)), 'high', 7500) * np.exp(-tt * 70)
def clap():
    tt = t_(0.22); n = filt(rng.standard_normal(len(tt)), 'band', [900, 3500])
    e = np.exp(-tt * 18) * (1 + 0.6 * np.exp(-((tt - 0.012) * 300) ** 2))
    return n * e * 0.8
# ---- efeitos ----
def whoosh(d=0.7, up=True):
    tt = t_(d); n = rng.standard_normal(len(tt)); out = np.zeros_like(n)
    seg = 512
    for i in range(0, len(n), seg):
        k = i / len(n); fc = 300 + (5000 if up else 3000) * (k if up else 1 - k)
        out[i:i + seg] = filt(n[i:i + seg + 0], 'band', [fc * 0.6, min(fc * 1.6, 18000)])[:len(out[i:i + seg])]
    e = np.sin(np.pi * np.linspace(0, 1, len(tt))) ** 1.5
    return out * e * 0.6
def pop(f0=900):
    tt = t_(0.14); f = f0 * (1 + 0.8 * np.exp(-tt * 40))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 30) * 0.55
def click():
    tt = t_(0.03); return filt(rng.standard_normal(len(tt)), 'high', 2500) * np.exp(-tt * 220) * 0.6
def tick():
    tt = t_(0.02); return filt(rng.standard_normal(len(tt)), 'band', [2500, 6000]) * np.exp(-tt * 300) * 0.22
def chime(m):
    tt = t_(1.2); f = hz(m)
    s = np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(2 * np.pi * 2.01 * f * tt) + 0.15 * np.sin(2 * np.pi * 3.02 * f * tt)
    return s * np.exp(-tt * 4) * 0.35
def riser(d):
    tt = t_(d); n = rng.standard_normal(len(tt))
    s = filt(n, 'high', 1500) * (tt / d) ** 2
    f = 200 + 800 * (tt / d) ** 2
    s += 0.3 * np.sin(2 * np.pi * np.cumsum(f) / SR) * (tt / d) ** 2
    return s * 0.35
def impact():
    tt = t_(1.6); f = 38 + 80 * np.exp(-tt * 10)
    b = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 2.5)
    n = filt(rng.standard_normal(len(tt)), 'low', 2500) * np.exp(-tt * 6) * 0.5
    return (b + n) * 0.9


# ---- Halloween: Ré menor, 96 BPM, caixinha de música + drone ----
BEAT=60/96
def bell(m,d=1.4):
    tt=t_(d);f=hz(m)
    s=np.sin(2*np.pi*f*tt)+0.5*np.sin(2*np.pi*2.76*f*tt)*np.exp(-tt*6)+0.25*np.sin(2*np.pi*5.4*f*tt)*np.exp(-tt*10)
    return s*np.exp(-tt*3.2)*0.4
def drone(m,d):
    tt=t_(d);f=hz(m);s=np.zeros_like(tt)
    for det in(-0.08,0,0.08): s+=np.sin(2*np.pi*f*2**(det/12)*tt)+0.3*np.sin(2*np.pi*2*f*2**(det/12)*tt)
    s=filt(s,'low',500,2)*(1+0.25*np.sin(2*np.pi*0.3*tt))
    return s*env(len(tt),0.8,1.0)/4
def stinger():
    out=np.zeros(int(0.9*SR))
    for m in (74,75,80):
        tt=t_(0.9);out+=(2*((tt*hz(m))%1)-1)*np.exp(-tt*4)
    return filt(out,'band',[400,4000])*0.18
MEL=[74,77,81,80, 77,74,73,76, 74,77,81,84, 82,81,77,76]
add(drone(38,16.5),0,0.9)
add(pad([62,65,69],16.5),0,0.25)
for i,m in enumerate(MEL*3):
    at=0.2+i*BEAT/2
    if at>13.0: break
    add(bell(m),at,0.5 if at<3 else 0.38,(-0.3 if i%2 else 0.3))
for k in range(int(13/BEAT)):
    at=3.0+k*BEAT
    if at>=13.0: break
    add(kick(),at,0.55 if k%2==0 else 0.3)
    add(hat(),at+BEAT/2,0.14,0.3)
for a in (3.0,6.4,9.8): add(whoosh(0.7),a-0.35,0.55); add(stinger(),a+0.6,1.0); add(click(),a+0.6,0.8)
for a in (3.0,6.4,9.8): add(chime(81),a+1.7,0.45); add(pop(900),a+2.0,0.55)
add(chime(76),0.3,0.5); add(pop(600),0.35,0.5)
add(riser(1.2),12.0,0.9); add(impact(),13.2,1.0)
add(pad([50,57,62,65,69],3.4),13.2,0.6)
for i,m in enumerate([74,77,81,86]): add(bell(m,2.0),13.4+i*0.3,0.45)
add(chime(86),14.5,0.4)
mix=np.stack([L,R],1); mix=np.tanh(mix*0.9)
fi=int(0.8*SR); mix[-fi:]*=np.linspace(1,0,fi)[:,None]
mix/=np.abs(mix).max()*1.05
wavfile.write('trilha-halloween.wav',SR,(mix*32767).astype(np.int16)); print('ok')
