---
title: Plots
type: page
---

Here is a collection of my interactive visualizations and physics simulations.

**Jump to:** [Heavy-ion collision dynamics](#heavy-ion-collision-dynamics) · [Local thermal nonequilibrium](#local-thermal-nonequilibrium) · [Net-proton fluctuations](#net-proton-fluctuations) · [Transverse momentum correlations](#transverse-momentum-correlations)

<style>
  .plot-frame { display: block; width: 100%; max-width: 680px; margin: 0 auto 40px auto; border: 1px solid rgba(128,128,128,.35); border-radius: 8px; }
  .sim-frame  { display: block; width: 80%; height: 60vh; margin: 0 auto 40px auto; background-color: black; border-radius: 8px; border: 0; }
  details.plot-box { border: 1px solid rgba(128,128,128,.35); border-radius: 10px; margin: 0 0 18px 0; padding: 0 16px; }
  details.plot-box > summary { cursor: pointer; font-weight: 600; font-size: 1.1rem; padding: 14px 0; list-style-position: outside; }
  details.plot-box[open] > summary { border-bottom: 1px solid rgba(128,128,128,.35); margin-bottom: 14px; }
  details.plot-box .plot-frame, details.plot-box .sim-frame { margin-bottom: 20px; }
  .neq-media { display: block; width: 100%; max-width: 100%; height: auto; margin: 0 auto 20px auto; border-radius: 6px; background: #fff; }
  details.plot-box summary sub, details.plot-box summary sup { font-size: .7em; }
</style>

## Heavy-Ion Collision Dynamics

<details class="plot-box">
<summary>Time Evolution of Single UrQMD Events</summary>



These interactive 3D plots show the time evolution of single UrQMD events for Au+Au collisions at impact parameter b = 4.8 fm and beam energy 400 AMeV.

#### Event 1

<iframe class="sim-frame" loading="lazy" src="/uploads/urqmd_event_1.html" frameborder="0"></iframe>

#### Event 2

<iframe class="sim-frame" loading="lazy" src="/uploads/urqmd_event_2.html" frameborder="0"></iframe>

#### Event 3

<iframe class="sim-frame" loading="lazy" src="/uploads/urqmd_event_3.html" frameborder="0"></iframe>

</details>

## Local Thermal Nonequilibrium

In a collision the matter is not in local thermal equilibrium: the momentum distribution in each small cell is not isotropic. Here I coarse-grain UrQMD Au+Au events onto a spacetime grid ([Coarse-Graining-UrQMD](https://github.com/OlehSavchuk/Coarse-Graining-UrQMD)), boost every particle into the local rest frame of the cell it falls in ([UrQMD-Local-Momentum-Anisotropy](https://github.com/OlehSavchuk/UrQMD-Local-Momentum-Anisotropy)), and measure the rest-frame momentum tensor cell by cell. The anisotropy is e<sub>ii</sub> = 3 T<sup>ii</sup> / (T<sup>xx</sup> + T<sup>yy</sup> + T<sup>zz</sup>): e<sub>ii</sub> = 1 means an isotropic (locally equilibrated) cell, and the three components always sum to 3. All maps show the transverse (x, y) plane at z ≈ 0, as a function of time.

<details class="plot-box">
<summary>Local Momentum Anisotropy e<sub>xx</sub>, e<sub>yy</sub>, e<sub>zz</sub></summary>

Early on, the collision region is strongly squeezed in the transverse directions and stretched along the beam axis (e<sub>zz</sub> well above 1, e<sub>xx</sub> and e<sub>yy</sub> well below 1). The anisotropy relaxes toward 1 as the system expands. The bottom row of the figure shows the transverse difference e<sub>xx</sub> − e<sub>yy</sub>.

<video class="neq-media" controls loop muted playsinline preload="none" src="/uploads/local-nonequilibrium/anisotropy_diagonal.mp4"></video>

<img class="neq-media" loading="lazy" src="/uploads/local-nonequilibrium/anisotropy_diagonal.png" alt="Local momentum anisotropy e_xx, e_yy, e_zz and e_xx - e_yy in the transverse plane at several times">

</details>

<details class="plot-box">
<summary>Longitudinal vs Transverse Momentum</summary>

Top: the difference between the longitudinal and the average transverse momentum width, in MeV/c. Bottom: the ratio ⟨p<sub>z</sub><sup>2</sup>⟩ / (⟨p<sub>T</sub><sup>2</sup>⟩/2). A value of 1 means the longitudinal and transverse widths agree, as in local equilibrium. The longitudinal excess is largest in the central region and fades by about 40–60 fm/c.

<video class="neq-media" controls loop muted playsinline preload="none" src="/uploads/local-nonequilibrium/longitudinal_vs_transverse.mp4"></video>

<img class="neq-media" loading="lazy" src="/uploads/local-nonequilibrium/longitudinal_vs_transverse.png" alt="Longitudinal minus transverse momentum width and their ratio in the transverse plane at several times">

</details>

<details class="plot-box">
<summary>Local Momentum Widths</summary>

The rest-frame momentum width √⟨p<sub>i</sub><sup>2</sup>⟩ in MeV/c along x, y and z. The x and y widths are similar, the z width is much larger early on, and the three converge as the system expands and cools.

<video class="neq-media" controls loop muted playsinline preload="none" src="/uploads/local-nonequilibrium/momentum_width.mp4"></video>

<img class="neq-media" loading="lazy" src="/uploads/local-nonequilibrium/momentum_width.png" alt="Local momentum widths along x, y and z in the transverse plane at several times">

</details>

<details class="plot-box">
<summary>Temperatures: Isotropic, Transverse and Longitudinal</summary>

Effective temperatures from the rest-frame momentum widths, for cells with density above 0.02 fm<sup>-3</sup> and nucleon mass m = 0.938 GeV: T = ⟨p<sup>2</sup>⟩/3m (isotropic), T<sub>tr</sub> = ⟨p<sub>T</sub><sup>2</sup>⟩/2m and T<sub>z</sub> = ⟨p<sub>z</sub><sup>2</sup>⟩/m. Left: each cell as a point in the (T, T<sub>tr</sub>) plane, with the dashed line marking equal temperatures. Right: the cell averages as a function of time. T<sub>z</sub> exceeds T<sub>tr</sub> during the compression and expansion, and they approach each other at late times.

<img class="neq-media" loading="lazy" src="/uploads/local-nonequilibrium/temperatures.png" alt="Transverse versus isotropic temperature per cell (left) and cell-averaged temperatures versus time (right)">

</details>

<details class="plot-box">
<summary>Transverse Anisotropy ε = (T<sub>x</sub> − T<sub>y</sub>)/(T<sub>x</sub> + T<sub>y</sub>)</summary>

The anisotropy within the transverse plane, shown as maps and as a function of time averaged over regions of different radius.

<video class="neq-media" controls loop muted playsinline preload="none" src="/uploads/local-nonequilibrium/transverse_anisotropy.mp4"></video>

<img class="neq-media" loading="lazy" src="/uploads/local-nonequilibrium/transverse_anisotropy.png" alt="Transverse momentum anisotropy epsilon in the transverse plane at several times">

<img class="neq-media" loading="lazy" src="/uploads/local-nonequilibrium/transverse_anisotropy_vs_t.png" alt="Transverse anisotropy epsilon versus time for cells within 4, 8 and 12 fm">

</details>

<details class="plot-box">
<summary>Off-Diagonal Components e<sub>xy</sub>, e<sub>xz</sub>, e<sub>yz</sub></summary>

The off-diagonal rest-frame momentum correlations, e<sub>ij</sub> = 3 ⟨p<sub>i</sub> p<sub>j</sub>⟩ / (⟨p<sub>x</sub><sup>2</sup>⟩ + ⟨p<sub>y</sub><sup>2</sup>⟩ + ⟨p<sub>z</sub><sup>2</sup>⟩), shown in the xy plane (top three rows) and in the xz plane (bottom three rows). They vanish in an equilibrated cell, and here they show a quadrupole pattern that dies out at late times.

<video class="neq-media" controls loop muted playsinline preload="none" src="/uploads/local-nonequilibrium/offdiagonal.mp4"></video>

<img class="neq-media" loading="lazy" src="/uploads/local-nonequilibrium/offdiagonal.png" alt="Off-diagonal momentum anisotropy components in the xy and xz planes at several times">

</details>

## Net-Proton Fluctuations

<details class="plot-box">
<summary>Net-Baryon Fluctuations Affected by Deconfinement</summary>



These interactive plots show how cumulants, fluctuations, and correlations of conserved charges change in the stochastic model I introduced in [arXiv:2407.17670](https://arxiv.org/abs/2407.17670).

<iframe class="plot-frame autosize" loading="lazy" src="/uploads/net_proton_cumulant_model.html" frameborder="0" style="height: 2300px;"></iframe>

</details>

<details class="plot-box">
<summary>Bayesian Inference of Fluctuations</summary>



I use Bayes' theorem to infer the parameters of the model from [arXiv:2407.17670](https://arxiv.org/abs/2407.17670).

<iframe class="plot-frame autosize" loading="lazy" src="/uploads/Bayesian fit.html" frameborder="0" style="height: 3500px;"></iframe>

</details>

## Transverse Momentum Correlations

<details class="plot-box">
<summary>Bayesian Inference of Transverse Momentum Correlations</summary>



I use a simple model in which sources fragment in the transverse plane, each splitting into several particles while conserving the source's transverse momentum. The observed correlations are driven by the number of sources and the number of particles each one splits into.

The strong correlation seen at low energies is likely caused by inelastic 2→2 scatterings that produce pairs with equal transverse momentum. At higher energies, these particles instead become resonances that undergo splittings. Around 4 GeV, resonances form (or, by hadron-parton duality, very heavy resonances that split into many particles). When this happens, reproducing the data requires a dip in the number of sources together with an increase in the number of splittings.

<iframe class="plot-frame autosize" loading="lazy" src="/uploads/pT correlator_ Glauber sources, strings or quarks.html" frameborder="0" style="height: 2900px;"></iframe>

</details>

<script src="/js/iframe-autosize.js"></script>
