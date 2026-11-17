---
title: Dilepton Elliptic Flow from Hydrodynamics
date: 2026-11-16
links:
  - type: site
    url: https://github.com/OlehSavchuk/v2dileptons
tags:
  - Heavy-Ion Collisions
  - Dileptons
  - Software
---
This C++/OpenMP code computes the thermal dilepton yield and its elliptic flow v2 from a hydrodynamic or transport evolution of a heavy-ion collision. For every space-time cell it takes the temperature, baryon density and flow velocity, evaluates the in-medium ρ, ω and φ spectral functions, and integrates over the cells to give the yield as a function of invariant mass and transverse momentum.

I used it for two published papers (J. Phys. G 50, 125104 and Phys. Lett. B, arXiv:2302.13919), and the repository cites those and the spectral-function tables of Rapp et al.
<!--more-->
