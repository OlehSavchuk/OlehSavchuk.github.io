---
title: ML for Femtoscopy
date: 2026-11-16
links:
  - type: site
    url: https://github.com/OlehSavchuk/ML-for-Femtoscopy
tags:
  - Normalizing Flow
  - Machine Learning
  - Heavy-Ion Collisions
---
I fit a trainable normalizing flow to a measured or model three-dimensional correlation function in order to recover the emission source that produced it. The flow is pushed through a differentiable, interpolated pair-interaction kernel and trained so that the resulting correlation function matches the target.

I compare Gaussian, RealNVP, spline and sinh-arcsinh flows and a Lévy-stable source with trainable stability parameters, in both TensorFlow Probability and PyTorch. A separate direct density fit, which skips the correlator, shows how well each flow can reproduce the source itself.
<!--more-->
