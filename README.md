# Oleh Savchuk — Personal Website

Source for my academic website: [olehsavchuk.github.io](https://olehsavchuk.github.io).

I'm a theoretical physicist working on heavy-ion collisions, the equation of state of dense nuclear matter, and Bayesian inference. The site collects my publications, talks, projects, interactive plots, and CV.

## Site contents

| Path | Contents |
| :--- | :--- |
| `content/_index.md` | Homepage sections |
| `content/authors/` | Biography and profile |
| `content/publications/` | Publications (one folder per paper, with `cite.bib`) |
| `content/events/` | Talks and slides |
| `content/projects/` | Software and research projects |
| `content/plots/` | Interactive visualizations |
| `content/hobbies/` | Hobbies |
| `data/authors/me.yaml` | Education, experience, skills, and awards |
| `static/uploads/` | CV and interactive plot files |

## Local development

Requires [Hugo Extended](https://gohugo.io/installation/) (version pinned in `hugoblox.yaml`) and Node.js with pnpm.

```bash
pnpm install
hugo server
```

The site is then available at <http://localhost:1313>.

## Credits

Built with [Hugo](https://gohugo.io) and the [HugoBlox](https://github.com/HugoBlox/kit) Academic CV template, released under the [MIT License](./LICENSE.md).
