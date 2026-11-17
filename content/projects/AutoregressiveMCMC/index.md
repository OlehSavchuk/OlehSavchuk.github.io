---
title: Autoregressive Sampling for Lattice Field Theory
date: 2026-11-17
links:
  - type: site
    url: https://github.com/OlehSavchuk/AutoregressiveModel
tags:
  - Machine Learning
  - Probability & Statistics
  - MCMC
---
I train an autoregressive neural network (a MADE-style model in TensorFlow) to reproduce the probability density of a one-dimensional lattice φ⁴ field theory, so that independent configurations can be drawn directly instead of from a slowly decorrelating Markov chain. Each site is a mixture of two Gaussians conditioned on all previous sites, which lets the model capture the double-well structure of the field that a single Gaussian cannot represent, and the network is trained on the reverse KL divergence against the lattice action.

The picture compares the field distribution at one site: the two-Gaussian autoregressive model follows the bimodal Metropolis reference, while the best unimodal (multivariate Gaussian) model produces a single broad peak. I also rewrote the sampler to update the hidden layer incrementally, which makes sampling much faster.
<!--more-->
