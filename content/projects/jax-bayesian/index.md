---
title: Bayesian Inference with JAX
date: 2026-11-02
links:
  - type: site
    url: https://github.com/OlehSavchuk/JAX-accelerated-Bayesian
tags:
  - Bayesian Inference
  - JAX
  - NumPyro
  - MCMC
  - Heavy-Ion Collisions
---

I use JAX and NumPyro to run Bayesian inference on a model of transverse momentum correlations measured by the STAR collaboration. The notebook rewrites the model's Poisson sums as fixed-domain integrals so they can be evaluated accurately in float64 under JAX, then samples the posterior with NUTS (four chains) and produces posterior-predictive bands and corner plots.
<!--more-->
