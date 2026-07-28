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
        I am a theoretical physicist grounded in numerical and statistical workflows. My work rotates around building complex theoretical models that are then implemented numerically as a part of statistical/Bayesian analysis workflows that use various experimental data from high and low energy heavy-ion collision experiments. This creates an intersection of high-energy and particle physics, many-body theory, quantum fields, software engineering, and statistics. I am very proud to be able to work in such a dynamic and evolving field that builds upon the legacy of virtually all previous discoveries. Additionally, I am passionate about new techniques such as artificial intelligence, machine learning, quantum computing, robotics, and automation.
        
        If you wish to collaborate, please feel free to reach out to me.
    design:
      columns: '1'
  - block: collections
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

  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 10
      # Filter on criteria
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: card
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
---
