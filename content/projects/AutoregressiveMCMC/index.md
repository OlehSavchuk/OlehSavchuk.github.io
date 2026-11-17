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
I train an autoregressive neural network (a MADE-style model in TensorFlow) to sample a one-dimensional lattice φ⁴ field theory directly, so that configurations are independent draws rather than a slowly decorrelating Markov chain. Each site is a two-Gaussian mixture conditioned on all previous sites, and the network is trained on the reverse KL divergence against the lattice action.

I rewrote the sampler so that it updates the hidden layer incrementally instead of re-running the full network at every site, which cuts the cost of a sampling pass by roughly two orders of magnitude in a NumPy reference test. The repository also contains a Metropolis reference simulation that shows the slow tunnelling between the two wells that motivates the approach.
<!--more-->
