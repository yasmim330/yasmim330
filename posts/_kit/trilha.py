"""Trilha original do Reels de fornecedores (21 s, 120 BPM, Lá menor).
Sintetizada do zero: sem samples, sem risco de direitos autorais."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 44100
DUR = 21.0
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

# ---- harmonia: Am F C G (1 compasso = 2 s) ----
CH = [[57, 60, 64], [53, 57, 60], [48, 55, 60, 64], [55, 59, 62]]
ROOT = [45, 41, 48, 43]
for bar in range(11):
    at = bar * 2.0; c = bar % 4
    lvl = 0.55 if at < 4 else (0.42 if at < 17 else 0.6)
    add(pad([n + 12 for n in CH[c]], 2.15), at, lvl * 0.9, 0)
    # arpejo em colcheias
    if at < 20:
        arp = [CH[c][0] + 12, CH[c][1] + 12, CH[c][2] + 12, CH[c][1] + 24]
        for k in range(8):
            g = 0.16 if at < 4 else 0.2
            add(pluck(arp[k % 4] + (12 if k == 7 else 0)), at + k * 0.25, g, -0.35 if k % 2 else 0.35)
    # baixo, bumbo, chimbal a partir da cena 2
    if 4 <= at < 20:
        for k in range(8):
            add(bass(ROOT[c] + (12 if k % 4 == 2 else 0)), at + k * 0.25, 0.42)
        for k in range(4):
            if not (at >= 14 and at < 16 and k >= 2 and False): add(kick(), at + k * BEAT, 0.85)
            add(hat(), at + k * BEAT + 0.25, 0.22, 0.3)
        if at >= 9:
            add(clap(), at + 0.5, 0.35); add(clap(), at + 1.5, 0.35)

# rufo e subida até o final
for i in range(16):
    add(clap(), 16.0 + i * 0.0625, 0.08 + 0.25 * i / 16)
add(riser(1.6), 15.4, 1.0)
add(impact(), 17.0, 1.0)
add(pad([45, 57, 60, 64, 69], 4.0), 17.0, 0.7)
add(pad([45, 52, 57, 60, 64], 2.2), 20.0, 0.5)
add(riser(1.0), 3.0, 0.6)

# ---- efeitos sincronizados com a imagem ----
for at in (4.0, 9.0, 14.0): add(whoosh(0.7), at - 0.35, 0.55)
add(whoosh(0.9), 0.0, 0.35)
add(chime(76), 1.0, 0.6)                 # logo
add(pop(700), 1.25, 0.5)                 # pill
# digitação
for x in np.arange(4.9, 6.0, 0.055): add(tick(), x + rng.uniform(0, .015), 1.0, rng.uniform(-.3, .3))
for x in np.arange(6.1, 7.0, 0.064): add(tick(), x + rng.uniform(0, .015), 1.0, rng.uniform(-.3, .3))
for x in np.arange(7.3, 7.65, 0.05): add(tick(), x, 1.0)
for x in np.arange(10.25, 10.7, 0.064): add(tick(), x, 1.0)
add(pop(1100), 7.05, 0.7); add(chime(81), 7.05, 0.35)  # CNPJ válido
add(click(), 7.85, 1.0); add(pop(800), 8.05, 0.5)      # cadastrar + toast
add(click(), 9.85, 1.0)                                 # selecionar fornecedor
add(pop(900), 10.75, 0.5)                               # prazo padrão
for k, at in enumerate((11.0, 11.35, 11.7)): add(pop(700 + k * 180), at, 0.75)  # boletos
add(chime(81), 12.2, 0.5); add(chime(88), 12.32, 0.35)   # confere com a NF
add(click(), 15.3, 1.0); add(pop(500), 15.4, 0.6)       # desativar
add(pop(800), 15.8, 0.45)                               # toast histórico
for k, at in enumerate((18.25, 18.7, 19.15)): add(pop(650 + k * 200), at, 0.6)  # linha de fluxo
add(chime(81), 19.15, 0.45)

mix = np.stack([L, R], 1)
mix = np.tanh(mix * 0.9)                    # cola suave
fade = np.ones(N); fi = int(0.6 * SR); mix[-fi:] *= np.linspace(1, 0, fi)[:, None]
mix /= np.abs(mix).max() * 1.05
wavfile.write('trilha.wav', SR, (mix * 32767).astype(np.int16))
print('trilha.wav', DUR, 's')
