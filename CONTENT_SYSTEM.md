# Brand Method — content and discovery system

## Identity and audience

Akshat Kavidayal — Brand Marketing & Business Development, across FMCG, consumer and technology. Global marketing, partnerships and strategy are the connective skills. The primary readers are brand/consumer marketing recruiters and hiring managers; the second audience is B2B technology, professional audio/AV and partnership teams. The site should also reward curious marketers who came for an opinion, not a résumé.

The homepage makes the role legible quickly. `/about/` stays a human, opinion-led introduction. `/resume/` is a searchable overview and must be updated from a verified public CV before specific titles, dates or results are added. `/work/` is professional experience; `/insights/` and `/studies/` are independent analysis. Never imply an independent brand study was commissioned work.

## Four editorial pillars

1. **Brand & FMCG:** distinctiveness, brand equity, global-to-local communications, shelf and category.
2. **Consumer & culture:** behavior, creative execution, social listening, creator fit and cultural relevance.
3. **Commercial partnerships:** B2B buying, channels, distributor and go-to-market questions.
4. **Technology & AV:** audio, professional AV, technical products and the human use case.

Use one primary pillar and optional secondary connection. Avoid thin category landing pages until there are several substantive articles for each.

## Voice and quality

Start from a particular observation or friction. State an argument, show what the brand actually did, support it with dated and linked primary/public evidence, distinguish inference from fact, and explain what evidence is missing. Use the article's natural structure; never force every piece into observed/interpreted/challenged/test. Write like Akshat: curious, opinionated, specific, sometimes irritated, never artificially certain. No fake metrics or invented campaign outcomes. Brand logos belong to their owners and are used only to identify independently discussed brands; keep attribution in `assets/LOGOS.md`.

Do not publish confidential employer information, client names, internal slides, unpublished strategy, proprietary data, specific brand-health figures or results without a public source and permission. Treat a professional project as a public, generalized experience summary until Akshat verifies details.

## Article process

1. Capture raw thought/link in the **private** workbench at `akshatkavidayal-cyber/Brandmethod-workbench`; preserve the original observation and date.
2. Research free original sources first: brand releases, campaign assets, public reports, product pages, official interviews, and credible reporting. Record URLs, publication dates, what each source actually supports and uncertainty.
3. Check fit with one pillar and whether a fresh argument exists. Stop or defer weak leads. Research automation in `.github/workflows/research.yml` proposes leads; it does not publish.
4. Draft a substantive article with a search-intent-aware title, descriptive opening, natural subheads, source limitation, source links and independent opinion. No generic filler. Confirm dates and claims.
5. Create a LinkedIn adaptation with one hook, the central argument, a clear link to the live article and an invitation to discuss. Create a 5–7 panel Instagram carousel: observation, visual evidence, tension, interpretation, implication, source/link card. Use original typography/collage or licensed/public assets, not recreated brand ads. A link in an Instagram caption is generally not a clickable website route; use the profile link or story link where available.
6. Add the approved article to `content/studies.json` or `content/from-linkedin.json`, images to `assets/`, and connect it to the most relevant practice/work/research page plus 1–2 related essays. Add an article-specific link from an existing page where it reads naturally. `scripts/build.py` generates canonicals, metadata, structured data and sitemap.
7. Run `python3 scripts/build.py`, inspect copy, sources, links and mobile layout, then trigger the manual `Publish coordinated release` workflow. Verify the public page before publishing social adaptations. Record live URLs in the private workbench. LinkedIn/Instagram do not currently auto-publish; don't mark drafts as live.

The private workbench contains editorial rules and the Duolingo carousel pilot. It remains separate from the public repo. Human approval is required for a new public article and social posting. Do not turn scheduled research leads into unreviewed site content.

## Search and internal links

One page, one reader question. Use a distinct descriptive title and meta description. Mention role, industry and capability naturally where factual. The professional pages link to relevant work; work links to practice, research and résumé; research links to influencer strategy and brand marketing; insights link back to relevant practice/research. Add related essays by topic, not by keyword count. Rebuild the sitemap after every content change. Keep old `.html` article URLs stable.

`site.json` holds the production base URL and the Google Search Console ownership tag. Do not remove the tag while this property is in use. A future custom domain requires changing the URL and redeploying. This is a GitHub Pages project site at `/Brandmethod/`: `sitemap.xml` there is valid for those descendants, but `/Brandmethod/robots.txt` is **not** the host-root robots file for `github.io`. All pages are implicitly crawlable; submit the sitemap directly to Search Console. The old `/about.html` stays available and canonically points to `/about/`; it is a duplicate compatibility page, not an HTTP redirect.

## Release and measurement

The publishing workflow is manually dispatched, preserving a review point. Google Search Console URL-prefix ownership was verified on 2026-09-17 for `https://akshatkavidayal-cyber.github.io/Brandmethod/` and its sitemap was submitted. Google initially displayed “Couldn't fetch” for that sitemap even though its public XML rendered with 20 URLs; recheck the Sitemaps report after processing before treating discovery as healthy. Manual indexing was requested for home, brand marketing and business development. Search Console measures organic queries, clicks, impressions and landing pages once data is available. No visitor analytics beacon is installed without a configured account/measurement ID. If adding free privacy-conscious analytics later, document vendor, data captured, retention and consent implications; track résumé PDF downloads (once one exists), case visits, outbound LinkedIn and contact actions only after it is configured. This HTML résumé has no fake download button.

## For future Work sessions

Read this document, `README.md`, `SEO_STRATEGY.md`, the private workbench, `site.json`, `scripts/build.py` and the relevant content JSON first. Compare remote GitHub `main` before editing: this local checkout has an older Git history and should not be pushed blindly. Keep facts and independently sourced commentary separate. Research, draft, review, publish the site, verify it, then prepare or publish social content through authorized channels. Report exact live URLs and any step still awaiting account access.
