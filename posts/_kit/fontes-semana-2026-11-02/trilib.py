"""Trilhas originais sintetizadas (sem samples). Adaptado de posts/_kit/trilha.py."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR=44100
class Track:
    def __init__(s,dur,seed=1):
        s.dur=dur;s.N=int(SR*dur);s.L=np.zeros(s.N);s.R=np.zeros(s.N);s.rng=np.random.default_rng(seed)
    def add(s,sig,at,gain=1.0,pan=0.0):
        i=int(at*SR)
        if i>=s.N or i<0: return
        x=sig[:s.N-i]*gain
        s.L[i:i+len(x)]+=x*np.sqrt((1-pan)/2)*1.414; s.R[i:i+len(x)]+=x*np.sqrt((1+pan)/2)*1.414
    def save(s,path,fade=0.6):
        mix=np.stack([s.L,s.R],1); mix=np.tanh(mix*0.9)
        fi=int(fade*SR); mix[-fi:]*=np.linspace(1,0,fi)[:,None]
        mix/=np.abs(mix).max()*1.05; wavfile.write(path,SR,(mix*32767).astype(np.int16))
def t_(d): return np.arange(int(d*SR))/SR
def hz(m): return 440*2**((m-69)/12)
def env(n,a,r):
    e=np.ones(n);ai=max(1,int(a*SR));ri=max(1,int(r*SR));e[:ai]=np.linspace(0,1,ai);e[-ri:]*=np.linspace(1,0,ri);return e
def filt(x,kind,f,order=2): return sosfilt(butter(order,f,btype=kind,fs=SR,output='sos'),x)
def pad(notes,d,cut=1400):
    tt=t_(d);s=np.zeros_like(tt)
    for m in notes:
        for det in (-0.12,0,0.12):
            f=hz(m)*2**(det/12);s+=2*((tt*f)%1)-1
    return filt(s,'low',cut)*env(len(tt),0.35,0.5)/(len(notes)*3)
def pluck(m,d=0.35,bright=3200,dec=9):
    tt=t_(d);f=hz(m);s=np.sign(np.sin(2*np.pi*f*tt))*.5+np.sin(2*np.pi*2*f*tt)*.5
    return filt(s,'low',bright)*np.exp(-tt*dec)
def marimba(m,d=0.5):
    tt=t_(d);f=hz(m)
    s=np.sin(2*np.pi*f*tt)*np.exp(-tt*7)+0.5*np.sin(2*np.pi*4*f*tt)*np.exp(-tt*28)+0.2*np.sin(2*np.pi*10*f*tt)*np.exp(-tt*60)
    return s*0.7
def bell(m,d=1.0):
    tt=t_(d);f=hz(m);return (np.sin(2*np.pi*f*tt)+.35*np.sin(2*np.pi*2.76*f*tt)*np.exp(-tt*3))*np.exp(-tt*3.5)*.35
def bass(m,d=0.24,cut=600):
    tt=t_(d);f=hz(m);s=np.sin(2*np.pi*f*tt)+.35*(2*((tt*f)%1)-1);return filt(s,'low',cut)*env(len(tt),.005,.06)
def kick():
    tt=t_(.35);f=45+110*np.exp(-tt*28);return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*7)*1.1
def hat(rng,d=.05): tt=t_(d);return filt(rng.standard_normal(len(tt)),'high',7500)*np.exp(-tt*70)
def shaker(rng,d=.08): tt=t_(d);return filt(rng.standard_normal(len(tt)),'band',[4000,9000])*np.sin(np.pi*np.linspace(0,1,len(tt)))*.5
def clap(rng):
    tt=t_(.22);n=filt(rng.standard_normal(len(tt)),'band',[900,3500]);return n*np.exp(-tt*18)*(1+.6*np.exp(-((tt-.012)*300)**2))*.8
def snap(rng):
    tt=t_(.12);return filt(rng.standard_normal(len(tt)),'band',[1500,5000])*np.exp(-tt*45)*.8
def whoosh(rng,d=.7,up=True):
    tt=t_(d);n=rng.standard_normal(len(tt));out=np.zeros_like(n);seg=512
    for i in range(0,len(n),seg):
        k=i/len(n);fc=300+(5000 if up else 3000)*(k if up else 1-k)
        out[i:i+seg]=filt(n[i:i+seg],'band',[fc*.6,min(fc*1.6,18000)])[:len(out[i:i+seg])]
    return out*np.sin(np.pi*np.linspace(0,1,len(tt)))**1.5*.6
def pop(f0=900):
    tt=t_(.14);f=f0*(1+.8*np.exp(-tt*40));return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*30)*.55
def click(rng): tt=t_(.03);return filt(rng.standard_normal(len(tt)),'high',2500)*np.exp(-tt*220)*.6
def tick(rng): tt=t_(.02);return filt(rng.standard_normal(len(tt)),'band',[2500,6000])*np.exp(-tt*300)*.22
def chime(m):
    tt=t_(1.2);f=hz(m);s=np.sin(2*np.pi*f*tt)+.4*np.sin(2*np.pi*2.01*f*tt)+.15*np.sin(2*np.pi*3.02*f*tt);return s*np.exp(-tt*4)*.35
def riser(rng,d):
    tt=t_(d);s=filt(rng.standard_normal(len(tt)),'high',1500)*(tt/d)**2;f=200+800*(tt/d)**2
    return (s+.3*np.sin(2*np.pi*np.cumsum(f)/SR)*(tt/d)**2)*.35
def impact(rng):
    tt=t_(1.6);f=38+80*np.exp(-tt*10);b=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*2.5)
    return (b+filt(rng.standard_normal(len(tt)),'low',2500)*np.exp(-tt*6)*.5)*.9
def tape_stop(m,d=.5):
    tt=t_(d);f=hz(m)*np.linspace(1,.2,len(tt));return np.sin(2*np.pi*np.cumsum(f)/SR)*np.linspace(1,0,len(tt))*.4
