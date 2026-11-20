"""Linearised Bjorken hydrodynamics at zero net baryon density (n0 = 0).

Equation of state: ideal quantum gas of pions (Bose) and nucleons + antinucleons (Fermi), mu = 0.
Background: ideal Bjorken flow, s*tau = const, T(tau0) = T0.
Perturbations depend on (tau, eta) only.  Fields (all densities per unit volume):

    de      energy density
    pz      longitudinal momentum density  (P_eta; pz = M_z * u, u = tau * delta u^eta)
    px, py  transverse momentum densities
    B, Q    baryon and electric charge densities

Linearised Navier-Stokes equations (Landau frame), derived from nabla_mu T^{mu nu} = 0 in Milne coordinates:

    d_tau de = -(1+cs2) de/tau - (1 - a) d_eta pz / tau
    d_tau pz = -2 pz/tau - cs2 d_eta de / tau + (a/tau) d_eta^2 pz,          a  = 4 eta_s / (3 tau M_z)
    d_tau px = -px/tau + d_x d_eta^2 px,                                       d_x = eta_s / (M_x tau^2)
    d_tau n  = -n/tau + D/tau^2 d_eta^2 n                                      (n = B, Q;  B and Q do not couple to e, pz at n0 = 0)

with M_z = e + P - 4 eta_s/(3 tau),  M_x = e + P + 2 eta_s/(3 tau).  The longitudinal sector is the n0 = 0 limit of the
equations in bj_flow.cpp (bj_flow-n0 repository); the transverse equation is derived the same way.

All equations are solved exactly in Fourier space in eta (coefficients do not depend on eta): scalar sectors analytically,
the (de, pz) sector with a 2x2 matrix exponential per mode and a second-order midpoint rule in tau.
Units: fm and GeV, hbar c = 0.19733 GeV fm; the code works in fm^-1 for T and in fm for tau.
"""
import numpy as np
from dataclasses import dataclass

HBARC = 0.1973269804  # GeV fm

# --------------------------------------------------------------------------- equation of state
# species: (mass GeV, statistics +1 Bose / -1 Fermi, g_total, sum g B^2, sum g Q^2, sum g B Q)
SPECIES = {
    "pions":    dict(m=0.13804, stat=+1, g=3, gB2=0, gQ2=2, gBQ=0),      # pi+, pi-, pi0 (only pi+- carry Q)
    "nucleons": dict(m=0.93827, stat=-1, g=8, gB2=8, gQ2=4, gBQ=4),      # p, n, pbar, nbar (2 spins each)
}

_X, _W = np.polynomial.legendre.leggauss(600)


def _species_thermo(m, stat, T):
    """per degree of freedom, mu = 0.  Returns P, e, c_v (=de/dT), chi_unit (= dn/dmu per unit g q^2), all in GeV^4/GeV^3 units."""
    pmax = 40.0 * T + 3.0 * m
    p = 0.5 * pmax * (_X + 1.0)
    w = 0.5 * pmax * _W
    E = np.sqrt(p * p + m * m)
    x = E / T
    meas = w * p * p / (2 * np.pi ** 2)          # d^3p/(2 pi)^3 -> p^2 dp / (2 pi^2)
    ex = np.exp(-x)
    if stat > 0:
        f = 1.0 / np.expm1(x)
        P = -T * np.sum(meas * np.log1p(-ex))
        corr = f * (1.0 + f)
    else:
        f = 1.0 / (np.exp(x) + 1.0)
        P = T * np.sum(meas * np.log1p(ex))
        corr = f * (1.0 - f)
    e = np.sum(meas * E * f)
    cv = np.sum(meas * E * E * corr) / T ** 2
    chi = np.sum(meas * corr) / T
    return P, e, cv, chi


def thermo(T):
    """T in GeV -> dict of P, e (GeV^4), s (GeV^3), cv (GeV^3), cs2, chiB, chiQ, chiBQ (GeV^2)."""
    P = e = cv = chiB = chiQ = chiBQ = 0.0
    for sp in SPECIES.values():
        Pi, ei, cvi, chii = _species_thermo(sp["m"], sp["stat"], T)
        P += sp["g"] * Pi
        e += sp["g"] * ei
        cv += sp["g"] * cvi
        chiB += sp["gB2"] * chii
        chiQ += sp["gQ2"] * chii
        chiBQ += sp["gBQ"] * chii
    s = (e + P) / T
    return dict(P=P, e=e, s=s, cv=cv, cs2=s / cv, chiB=chiB, chiQ=chiQ, chiBQ=chiBQ)


# --------------------------------------------------------------------------- background and coefficients
@dataclass
class Params:
    T0: float = 0.160       # GeV at tau0
    tau0: float = 1.0       # fm/c
    tau_end: float = 11.0
    eta_over_s: float = 0.2
    D_const: float = 2.0 / (2.0 * np.pi)   # D = D_const / T  (T in fm^-1), same form as the repository tables


class Background:
    def __init__(self, par: Params, nT=240):
        self.par = par
        Ts = np.linspace(0.030, 0.200, nT)
        th = [thermo(T) for T in Ts]
        self.Ts = Ts
        keys = th[0].keys()
        self.tab = {k: np.array([t[k] for t in th]) for k in keys}
        s0 = np.interp(par.T0, Ts, self.tab["s"])
        self.s0tau0 = s0 * par.tau0 / HBARC ** 3  # fm^-3 * fm  (s in fm^-3)
        self._sT = self.tab["s"] / HBARC ** 3        # fm^-3, increasing with T

    def T(self, tau):
        s = self.s0tau0 / np.asarray(tau)
        return np.interp(s, self._sT, self.Ts)       # GeV

    def interp(self, key, tau):
        return np.interp(self.T(tau), self.Ts, self.tab[key])

    def coeffs(self, tau):
        """all coefficients at proper time tau (fm/c); arrays allowed."""
        par = self.par
        T = self.T(tau)                  # GeV
        Tfm = T / HBARC                  # fm^-1
        cs2 = self.interp("cs2", tau)
        x = par.eta_over_s / (tau * Tfm)  # eta/(tau * (e+P)) * ... = (eta/s)/(tau T)
        Mz_rel = 1.0 - 4.0 / 3.0 * x      # M_z / (e+P)
        Mx_rel = 1.0 + 2.0 / 3.0 * x
        a = (4.0 / 3.0) * x / Mz_rel
        dx = par.eta_over_s / (Tfm * tau ** 2) / Mx_rel   # eta_s/(M_x tau^2)
        D = par.D_const / Tfm                              # fm
        return dict(T=T, Tfm=Tfm, cs2=cs2, a=a, dx=dx, D=D, Mz_rel=Mz_rel, Mx_rel=Mx_rel)

    # equilibrium weights Gamma_aa(tau) = <da da> per unit volume * volume
    def gamma(self, tau):
        T = self.T(tau)
        Tfm = T / HBARC
        w = self.interp("s", tau) * T / HBARC ** 4               # e+P in fm^-4 (T s)
        cv = self.interp("cv", tau) / HBARC ** 3                 # fm^-3
        return dict(
            ee=Tfm ** 2 * cv,                                   # T^2 c_v         [fm^-5]
            pp=Tfm * w,                                          # T (e+P)         [fm^-5]
            BB=Tfm * self.interp("chiB", tau) / HBARC ** 2,      # T chi_B         [fm^-3]
            QQ=Tfm * self.interp("chiQ", tau) / HBARC ** 2,
            BQ=Tfm * self.interp("chiBQ", tau) / HBARC ** 2,
        )


# --------------------------------------------------------------------------- propagators in Fourier space
def _expm2(A11, A12, A21, A22, h):
    """exp(A h) for 2x2 arrays of complex numbers (vectorised over modes)."""
    tr2 = 0.5 * (A11 + A22)
    d2 = (0.5 * (A11 - A22)) ** 2 + A12 * A21          # Delta^2
    Dl = np.sqrt(d2.astype(complex))
    small = np.abs(Dl * h) < 1e-8
    shc = np.where(small, h, np.sinh(Dl * h) / np.where(small, 1.0, Dl))
    ch = np.cosh(Dl * h)
    pref = np.exp(tr2 * h)
    M11 = pref * (ch + shc * (A11 - tr2))
    M12 = pref * shc * A12
    M21 = pref * shc * A21
    M22 = pref * (ch + shc * (A22 - tr2))
    return M11, M12, M21, M22


class Solver:
    def __init__(self, bg: Background, L=10.0, N=1000, dt=0.005):
        self.bg, self.dt = bg, dt
        self.N, self.L = N, L
        self.eta = (np.arange(N) - N // 2) * (L / N)
        self.k = 2 * np.pi * np.fft.fftfreq(N, d=L / N)

    def propagate(self, tau1, snapshots, sectors=("long", "x", "B", "Q")):
        """propagator from tau1 to each tau in `snapshots` (sorted).  Returns dict of Fourier-space arrays:
        'long' -> (4, nsnap, N)  [Phi_ee, Phi_epz, Phi_pze, Phi_pzpz];  'x','B','Q' -> (nsnap, N)."""
        bg, k, dt = self.bg, self.k, self.dt
        N = self.N
        nsn = len(snapshots)
        out = {}
        # transverse and charge: integrating factor
        for name in ("x", "B", "Q"):
            if name not in sectors:
                continue
            ph = np.zeros((nsn, N))
            tt = tau1
            logdil = 0.0       # -ln(tau/tau1)
            damp = np.zeros(N)
            j = 0
            snap = list(snapshots)
            while j < nsn:
                tn = min(snap[j], tt + dt)
                h = tn - tt
                if h > 0:
                    tm = 0.5 * (tt + tn)
                    c = bg.coeffs(tm)
                    rate = c["dx"] if name == "x" else c["D"] / tm ** 2
                    damp += rate * k ** 2 * h
                    tt = tn
                if abs(tt - snap[j]) < 1e-12:
                    ph[j] = (tau1 / tt) * np.exp(-damp)
                    j += 1
            out[name] = ph
        if "long" in sectors:
            M = np.zeros((4, nsn, N), dtype=complex)
            P11 = np.ones(N, complex); P12 = np.zeros(N, complex)
            P21 = np.zeros(N, complex); P22 = np.ones(N, complex)
            tt = tau1
            j = 0
            snap = list(snapshots)
            ik = 1j * k
            while j < nsn:
                tn = min(snap[j], tt + dt)
                h = tn - tt
                if h > 0:
                    tm = 0.5 * (tt + tn)
                    c = bg.coeffs(tm)
                    A11 = -(1 + c["cs2"]) / tm * np.ones(N)
                    A12 = -(1 - c["a"]) * ik / tm
                    A21 = -c["cs2"] * ik / tm
                    A22 = -2.0 / tm - (c["a"] / tm) * k ** 2
                    E11, E12, E21, E22 = _expm2(A11, A12, A21, A22, h)
                    P11, P12, P21, P22 = (E11 * P11 + E12 * P21, E11 * P12 + E12 * P22,
                                          E21 * P11 + E22 * P21, E21 * P12 + E22 * P22)
                    tt = tn
                if abs(tt - snap[j]) < 1e-12:
                    M[0, j], M[1, j], M[2, j], M[3, j] = P11, P12, P21, P22
                    j += 1
            out["long"] = M
        return out

    def to_eta(self, fk, sigma=0.0):
        """Fourier-space propagator -> eta-space Green function (source = Gaussian of width sigma, unit integral)."""
        fk = fk * np.exp(-0.5 * (self.k * sigma) ** 2)
        g = np.fft.ifft(fk, axis=-1).real * (self.N / self.L)
        return np.fft.fftshift(g, axes=-1)
