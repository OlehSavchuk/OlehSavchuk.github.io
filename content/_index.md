---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-05-18
type: landing

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/Oleh_Savchuk_CV.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded

  - block: markdown
    content:
      title: '📚 My Research'
      subtitle: ''
      text: |-
        I am a theoretical physicist who turns complex, stochastic phenomena into rigorous mathematical models and scalable computational workflows. I design probabilistic models and implement them as optimized, parallelized software.

        Using Bayesian inference and machine learning, I extract signal from noisy, high-variance data. My toolkit is high-performance C++ and Python, with a focus on robust numerical methods, algorithmic optimization, and predictive data analysis.

        I am now looking to apply these skills to quantitative finance. If you would like to collaborate or talk, please [get in touch](mailto:savchukolegv@gmail.com).
    design:
      columns: '1'

  - block: markdown
    id: skills
    content:
      title: '🛠️ Skills'
      subtitle: ''
      text: |-
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem;">
        <div style="border:1px solid rgba(128,128,128,.35);border-radius:12px;padding:1.1rem 1.25rem;">
        <h3 style="margin:0 0 .6rem;font-size:1.05rem;">Programming &amp; HPC</h3>
        <p style="margin:0;line-height:1.9;">C++ · Boost · Python · Pybind11 · CUDA · OpenMP · MPI · Fortran · Java · C</p>
        </div>
        <div style="border:1px solid rgba(128,128,128,.35);border-radius:12px;padding:1.1rem 1.25rem;">
        <h3 style="margin:0 0 .6rem;font-size:1.05rem;">Statistics &amp; Machine Learning</h3>
        <p style="margin:0;line-height:1.9;">Bayesian inference · MCMC (NUTS) · Emulators · Normalizing flows · JAX · NumPyro · PyTorch · TensorFlow · Keras</p>
        </div>
        <div style="border:1px solid rgba(128,128,128,.35);border-radius:12px;padding:1.1rem 1.25rem;">
        <h3 style="margin:0 0 .6rem;font-size:1.05rem;">Physics &amp; Simulation</h3>
        <p style="margin:0;line-height:1.9;">Transport models (UrQMD, SMASH) · Monte Carlo · Numerical methods</p>
        </div>
        <div style="border:1px solid rgba(128,128,128,.35);border-radius:12px;padding:1.1rem 1.25rem;">
        <h3 style="margin:0 0 .6rem;font-size:1.05rem;">Analysis &amp; Tools</h3>
        <p style="margin:0;line-height:1.9;">pandas · Polars · ROOT · Mathematica · MATLAB · Maple · LaTeX · Data visualization</p>
        </div>
        <div style="border:1px solid rgba(128,128,128,.35);border-radius:12px;padding:1.1rem 1.25rem;">
        <h3 style="margin:0 0 .6rem;font-size:1.05rem;">Quantitative Finance</h3>
        <p style="margin:0;line-height:1.9;">Limit order book matching (C++20) · Backtesting · Momentum strategies · Sharpe ratio · Return and drawdown analysis</p>
        </div>
        </div>
        <p style="margin:1rem 0 0;font-size:.9rem;opacity:.75;">My quantitative finance skills come from self-directed projects, listed below.</p>
    design:
      columns: '1'

  - block: collection
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - projects
        featured_only: false
    design:
      view: article-grid
      columns: 2

  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2

  - block: collection
    content:
      title: Recent Publications
      text: ''
      # Show only the latest papers here; the Publications page lists everything
      count: 8
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation

  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      filters:
        folders:
          - events
    design:
      view: card

---
