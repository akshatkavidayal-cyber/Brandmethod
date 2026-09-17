# Brand Method

Akshat Kavidayal's portfolio lives at [akshatkavidayal-cyber.github.io/Brandmethod](https://akshatkavidayal-cyber.github.io/Brandmethod/). It connects brand marketing and FMCG consumer insight with business development, partnerships and professional AV. The [professional work](https://akshatkavidayal-cyber.github.io/Brandmethod/work/) is clearly separated from [independent editorial analysis](https://akshatkavidayal-cyber.github.io/Brandmethod/insights/). GitHub Pages builds the site with `scripts/build.py` when the manual `Publish coordinated release` workflow is run.

## Site map and continuation

`scripts/professional.py` holds the public professional pages: brand marketing, business development, work and three experience summaries, research, searchable résumé, insights and contact. `scripts/build.py` renders them alongside the original eight essays and generates metadata, structured data, sitemap and a 404 page. The résumé uses verified facts from Akshat's supplied CV. `scripts/build_cv.py` creates a public, employer-neutral PDF in `assets/` without the private phone number or job-specific wording. An analytics account has not been configured. Read [CONTENT_SYSTEM.md](CONTENT_SYSTEM.md) for the editorial/release workflow and [SEO_STRATEGY.md](SEO_STRATEGY.md) for search intent, 30 article opportunities and Search Console setup.

## Edit an article

The first two pieces live in `content/from-linkedin.json`; the other six live in `content/studies.json`. Each article has a title, short description, opening, a `story` array, a limitation note and source links. The story is edited block by block, in the order that best suits that particular case:

- `{"type": "heading", "text": "..."}`
- `{"type": "paragraph", "text": "..."}`
- `{"type": "list", "items": ["...", "..."]}`
- `{"type": "aside", "label": "...", "text": "..."}`

Use only the blocks the story needs. Give each heading its own point of view. Avoid reusing a numbered analysis framework across articles. If a brand mark is available, put its filename in `logo` and keep the asset in `assets/`. See `assets/LOGOS.md` for the current marks and their sources.

Edit `site.json` for the site introduction and LinkedIn link. The About page copy and layout are in `scripts/build.py`; styling is in `assets/styles.css`. Run `python3 scripts/build.py` to preview changes locally. On GitHub, edit the files directly, then run the manual publishing workflow after reviewing the generated site.

## Editorial and social release

Research leads run on Monday, Wednesday and Friday from free public feeds. They are leads, not publishable articles. Check original brand or company sources, dates and product details; distinguish an opinion from a measured result; include limitations and links. Write the article in Akshat's own voice. Review the website, LinkedIn and Instagram drafts together.

The website can be published through GitHub Pages. LinkedIn and Instagram posting are separate steps and are not automated or connected here. When those routes are available, publish the website, verify its public URL, then post the social adaptations in one coordinated release session. Record the live links. Do not imply a social post went live unless it did.
