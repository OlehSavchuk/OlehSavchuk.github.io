---
title: Plots
type: page
---

Here is a collection of my interactive visualizations and physics simulations.

**Jump to:** [Heavy-ion collision dynamics](#heavy-ion-collision-dynamics) · [Net-proton fluctuations](#net-proton-fluctuations) · [Transverse momentum correlations](#transverse-momentum-correlations)

<style>
  .plot-frame { display: block; width: 100%; max-width: 680px; margin: 0 auto 40px auto; border: 1px solid rgba(128,128,128,.35); border-radius: 8px; }
  .sim-frame  { display: block; width: 80%; height: 60vh; margin: 0 auto 40px auto; background-color: black; border-radius: 8px; border: 0; }
  details.plot-box { border: 1px solid rgba(128,128,128,.35); border-radius: 10px; margin: 0 0 18px 0; padding: 0 16px; }
  details.plot-box > summary { cursor: pointer; font-weight: 600; font-size: 1.1rem; padding: 14px 0; list-style-position: outside; }
  details.plot-box[open] > summary { border-bottom: 1px solid rgba(128,128,128,.35); margin-bottom: 14px; }
  details.plot-box .plot-frame, details.plot-box .sim-frame { margin-bottom: 20px; }
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
