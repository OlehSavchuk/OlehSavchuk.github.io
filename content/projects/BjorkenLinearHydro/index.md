---
title: Crank-Nicolson Linear Hydrodynamics
date: 2026-11-17
featured: true
links:
  - type: site
    url: https://github.com/OlehSavchuk/bjorken-linear-hydro
tags:
  - Hydrodynamics
  - Heavy-Ion Collisions
  - Software
---
This C++ code evolves a small perturbation in each conserved density (energy, baryon number, electric charge, strangeness) on top of a one-dimensional Bjorken flow and records the response in spatial rapidity. The responses are the Green's functions from which I obtain correlations of conserved quantities at finite baryon density, for several equations of state.

I added Crank-Nicolson and Runge-Kutta solvers next to the original explicit one, validated them against it, and the Crank-Nicolson solver is about ten times faster at the same time step. The code was used for two of my papers (Phys. Rev. C 109, 024910 and arXiv:2402.12504), which are cited in the repository.
<!--more-->
