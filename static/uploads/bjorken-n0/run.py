import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
from bjorken_n0 import *
plt.rcParams.update({"xtick.direction":"in","ytick.direction":"in","xtick.top":True,"ytick.right":True,
    "xtick.minor.visible":True,"ytick.minor.visible":True,"font.size":11,"mathtext.fontset":"cm","font.family":"serif"})
par=Params(); bg=Background(par)
sv=Solver(bg,L=12.0,N=1200,dt=0.005)
tau0=par.tau0
taus=np.linspace(1.0,par.tau_end,101)[1:]   # 100 frames
o=sv.propagate(tau0,list(taus))
SIG_G=0.05   # source width of Green's functions
SIG_C=0.10   # coarse-graining width of the correlator
eta=sv.eta
dE=sv.L/sv.N
G={}
G["B"]=sv.to_eta(o["B"],SIG_G); G["Q"]=sv.to_eta(o["Q"],SIG_G); G["px"]=sv.to_eta(o["x"],SIG_G)
L=o["long"]
for i,nm in enumerate(["ee","epz","pze","pzpz"]): G[nm]=sv.to_eta(L[i],SIG_G)
# --- correlators: R_ab = tau C_ab / sqrt(Gam_aa Gam_bb)(tau); initial = local equilibrium (smeared delta)
g0=bg.gamma(tau0)
def gam(t): return bg.gamma(t)
gau=lambda s: np.exp(-0.5*(eta/s)**2)/(np.sqrt(2*np.pi)*s)
loc=gau(SIG_C)
def corr_scalar(ph,key):
    # ph: Fourier-space propagator (nsn,N), real
    fk=ph**2*np.exp(-0.5*(sv.k*SIG_C)**2)
    c=sv.to_eta(fk,0.0)
    out=np.zeros_like(c)
    for j,t in enumerate(taus):
        out[j]=(t/tau0)*gam(tau0)[key]/gam(t)[key]*c[j]
    return out
R={}
R["BB"]=corr_scalar(o["B"],"BB"); R["QQ"]=corr_scalar(o["Q"],"QQ")
R["pxpx"]=corr_scalar(o["x"],"pp")
# longitudinal: C_ab(k)=sum_c Gam0_c Phi_ac conj(Phi_bc)
Gm0={"e":g0["ee"],"p":g0["pp"]}
Phi=lambda a,c: L[{("e","e"):0,("e","p"):1,("p","e"):2,("p","p"):3}[(a,c)]]
def corr_long(a,b):
    fk=sum(Gm0[c]*Phi(a,c)*np.conj(Phi(b,c)) for c in "ep")*np.exp(-0.5*(sv.k*SIG_C)**2)
    c=sv.to_eta(fk,0.0)
    ga={"e":"ee","p":"pp"}
    out=np.zeros_like(c)
    for j,t in enumerate(taus):
        gt=gam(t); out[j]=(t/tau0)/np.sqrt(gt[ga[a]]*gt[ga[b]])*c[j]/1.0
    return out/ (1.0)  # Gm0 carried in fk (not normalised by Gam0 here)
R["ee"]=corr_long("e","e"); R["pzpz"]=corr_long("p","p"); R["epz"]=corr_long("e","p")
np.savez("results_n0_bjorken.npz",eta=eta,tau=taus,**{"G_"+k:v for k,v in G.items()},**{"R_"+k:v for k,v in R.items()})

# --- sanity: integrals
print("int R_BB dEta at tau=11:",R["BB"][-1].sum()*dE, "expected Gam0 tau0/ (Gam tau) *... ")
# window susceptibility ratio
def win(Rk,Y):
    m=np.abs(eta)<=Y
    return Rk[:,m].sum(axis=1)*dE
Ys=[0.5,1.0,2.0,4.0]
# local-term balancing part
W={k:R[k]-loc[None,:] for k in ["BB","QQ","pxpx"]}

col=["#1b9e77","#d95f02","#7570b3","#e7298a","#66a61e","#e6ab02"]
# --- Fig 1: Green's functions at snapshots
snaps=[2.0,4.0,7.0,11.0]
idx=[int(np.argmin(abs(taus-s))) for s in snaps]
panels=[("B","$G_{BB}=G_{QQ}$ (charge)"),("px","$G_{p_xp_x}=G_{p_yp_y}$"),("ee","$G_{\\epsilon\\epsilon}$"),
        ("epz","$G_{\\epsilon P_\\eta}$"),("pze","$G_{P_\\eta\\epsilon}$"),("pzpz","$G_{P_\\eta P_\\eta}$")]
fig,axs=plt.subplots(2,3,figsize=(13,7))
for ax,(k,lab) in zip(axs.ravel(),panels):
    for c,i in zip(col,idx):
        ax.plot(eta,G[k][i].real if np.iscomplexobj(G[k]) else G[k][i],color=c,label=f"$\\tau={taus[i]:.0f}$ fm/c")
    ax.set_xlim(-3,3); ax.set_xlabel("$\\eta-\\eta'$"); ax.set_title(lab); ax.axhline(0,color="k",lw=0.4)
axs[0,0].legend(frameon=False,fontsize=9)
fig.suptitle("Green's functions $G_{ab}(\\eta-\\eta';\\tau|\\tau_0=1)$, $n_0=0$, $\\pi+N$ gas, $T_0=160$ MeV, $\\eta/s=0.2$",y=0.995)
fig.tight_layout(); fig.savefig("fig_green_functions.png",dpi=160)
# --- Fig 2: correlators
fig,axs=plt.subplots(2,3,figsize=(13,7))
for ax,(k,lab) in zip(axs.ravel(),[("pxpx","$\\tau C_{p_xp_x}/\\Gamma_{pp}$"),("BB","$\\tau C_{BB}/\\Gamma_{BB}$"),("QQ","$\\tau C_{QQ}/\\Gamma_{QQ}$"),
      ("ee","$\\tau C_{\\epsilon\\epsilon}/\\Gamma_{\\epsilon\\epsilon}$"),("pzpz","$\\tau C_{P_\\eta P_\\eta}/\\Gamma_{pp}$"),("epz","$\\tau C_{\\epsilon P_\\eta}/\\sqrt{\\Gamma\\Gamma}$")]):
    for c,i in zip(col,idx): ax.plot(eta,R[k][i],color=c,label=f"$\\tau={taus[i]:.0f}$")
    ax.plot(eta,loc,"k--",lw=0.8,label="local eq." if k=="pxpx" else None)
    ax.set_xlim(-3,3); ax.set_xlabel("$\\Delta\\eta$"); ax.set_title(lab)
axs[0,0].legend(frameon=False,fontsize=9)
fig.tight_layout(); fig.savefig("fig_correlations.png",dpi=160)
# --- Fig 3: susceptibilities
fig,axs=plt.subplots(1,3,figsize=(15,4.6))
tt=np.linspace(1,11,60); th=[bg.gamma(t) for t in tt]
ax=axs[0]
ax.plot(tt,[g["BB"]/bg.T(t)*HBARC**0 for g,t in zip(th,tt)],label="$\\chi_B$")  # placeholder replaced below
ax.cla()
Tg=np.array([bg.T(t) for t in tt])/HBARC
for key,lab in [("BB","$\\chi_{B}$"),("QQ","$\\chi_{Q}$"),("BQ","$\\chi_{BQ}$")]:
    ax.plot(tt,np.array([g[key] for g in th])/Tg/ (1.0),label=lab)   # fm^-2
ax.set_yscale("log"); ax.set_xlabel("$\\tau$ (fm/c)"); ax.set_ylabel("$\\chi=\\langle\\delta n\\delta n\\rangle/(TV)$ (fm$^{-2}$)"); ax.legend(frameon=False)
ax.set_title("equilibrium diagonal susceptibilities")
for a,(k,lab) in zip(axs[1:],[("BB","$B$ (and $Q$ similar)"),("pxpx","$p_x$")]):
    for c,Y in zip(col,Ys): a.plot(taus,win(R[k],Y),color=c,label=f"$|\\Delta\\eta|<{Y}$")
    a.plot(taus,R[k].sum(axis=1)*dE,"k",label="all $\\Delta\\eta$")
    a.set_xlabel("$\\tau$ (fm/c)"); a.set_ylabel("$\\int \\tau C\\,d\\Delta\\eta/\\Gamma(\\tau)$"); a.set_title("windowed susceptibility ratio: "+lab)
axs[1].legend(frameon=False,fontsize=9)
for a in axs: a.tick_params(which="both",top=True,right=True,direction="in")
fig.tight_layout(); fig.savefig("fig_susceptibilities.png",dpi=160)
# --- Fig 4: balancing part
fig,axs=plt.subplots(1,3,figsize=(15,4.4))
for a,(k,lab) in zip(axs,[("BB","$W_{BB}$"),("QQ","$W_{QQ}$"),("pxpx","$W_{p_xp_x}$")]):
    for c,i in zip(col,idx): a.plot(eta,W[k][i],color=c,label=f"$\\tau={taus[i]:.0f}$")
    a.set_xlim(-3,3); a.set_xlabel("$\\Delta\\eta$"); a.set_title(lab+"$=R-\\delta_\\sigma$ (balancing part)"); a.axhline(0,color="k",lw=0.4)
axs[0].legend(frameon=False,fontsize=9)
fig.tight_layout(); fig.savefig("fig_balancing.png",dpi=160)

# --- animations
def animate(fname,drawers,nrow,ncol,figsize,title):
    fig,axs=plt.subplots(nrow,ncol,figsize=figsize); axs=np.atleast_1d(axs).ravel()
    lines=[]; 
    for ax,(lab,data,ylim,ref) in zip(axs,drawers):
        ax.set_xlim(-3,3); ax.set_ylim(*ylim); ax.set_xlabel("$\\Delta\\eta$"); ax.set_title(lab); ax.axhline(0,color="k",lw=0.4)
        if ref is not None: ax.plot(eta,ref,"k--",lw=0.8)
        ln,=ax.plot(eta,data[0],color="#6A3FA0",lw=1.8); lines.append(ln)
    tx=fig.suptitle("")
    fig.tight_layout(rect=(0,0,1,0.95))
    w=FFMpegWriter(fps=20,codec="libx264",extra_args=["-pix_fmt","yuv420p","-crf","23","-preset","veryfast"])
    with w.saving(fig,fname,110):
        for j in range(len(taus)):
            for ln,(lab,data,ylim,ref) in zip(lines,drawers): ln.set_ydata(data[j])
            tx.set_text(f"{title}   $\\tau={taus[j]:.2f}$ fm/c  ($T={float(bg.T(taus[j]))*1000:.0f}$ MeV)")
            w.grab_frame()
    plt.close(fig)
mx=lambda a: 1.1*float(np.max(np.abs(a)))
animate("anim_pxpx_correlation.mp4",[("$\\tau C_{p_xp_x}/\\Gamma_{pp}$  (dashed: local equilibrium)",R["pxpx"],(-0.5,loc.max()*1.1),loc),
        ("balancing part $W_{p_xp_x}$",W["pxpx"],(W["pxpx"].min()*1.1,W["pxpx"].max()*1.2),None)],1,2,(10,4.2),"$p_xp_x$ correlation, ideal $\\pi N$ gas")
animate("anim_green_functions.mp4",[(l,(G[k].real),(G[k][0].min()*1.1 if k!="epz" else -0.3, 0.3*0+max(G[k][0].max(),1)*0.0+ (G[k][3:].max()*1.2)),None) for k,l in panels],2,3,(13,7),"Green's functions")
print("done")
