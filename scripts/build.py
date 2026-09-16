#!/usr/bin/env python3
"""Build the static portfolio from reviewed case-study data."""

import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
ASSETS = ROOT / "assets"
CONFIG = json.loads((ROOT / "site.json").read_text())


def e(value):
    return html.escape(str(value), quote=True)


def shell(title, description, body, depth=0):
    root = "../" * depth
    nav = f'''<header class="site-header"><a class="wordmark" href="{root}index.html" aria-label="Brand Method home"><span class="mark">BM<span class="mark-dot">.</span></span><span>BRAND<br>METHOD</span></a><nav aria-label="Main navigation"><a href="{root}index.html">Case studies</a><a href="{root}about.html">About Akshat</a></nav></header>'''
    contact = f'<a href="mailto:{e(CONFIG["contact_email"])}">Get in touch</a><br>' if CONFIG.get("contact_email") else ""
    linkedin = f'<a href="{e(CONFIG["linkedin_url"])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><br>' if CONFIG.get("linkedin_url") else ""
    footer = f'''<footer class="site-footer"><div><strong>BRAND METHOD</strong><p>By {e(CONFIG['author'])}. Marketing decisions, examined.</p></div><div>{contact}{linkedin}<a href="{root}about.html">How these studies are made</a><p>Independent editorial analysis. No brand affiliation.</p></div></footer>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f4efdf"><meta name="description" content="{e(description)}"><title>{e(title)} · Brand Method</title><link rel="icon" href="{root}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{root}styles.css"></head><body>{nav}<main id="main">{body}</main>{footer}<script src="{root}main.js" defer></script></body></html>'''


def card(study, index):
    category = study["lens"].split(" & ")[0]
    label = "FROM MY LINKEDIN NOTES" if study.get("origin") else f"{index:02d} / FIELD NOTE"
    mark = f'<img class="cover-logo" src="{e(study["logo"])}" alt="" loading="lazy">' if study.get("logo") else f'<span class="cover-mark">{e(study["brand"])}</span>'
    return f'''<a class="study-card study-card--{e(study['slug'].split('-')[0])}" href="studies/{e(study['slug'])}.html" data-category="{e(category.lower())}" data-industry="{e(study['industry'].lower())}"><div class="card-cover" aria-hidden="true">{mark}<span class="cover-number">{index:02d}</span></div><div class="card-top"><span class="card-index">{label}</span><span class="card-brand">{e(study['brand'])}</span></div><div class="card-body"><p class="eyebrow">{e(study['industry'])} <span aria-hidden="true">/</span> {e(study['lens'])}</p><h3>{e(study['title'])}</h3><p>{e(study['dek'])}</p></div><div class="card-bottom"><span>Read the analysis</span><span aria-hidden="true">↗</span></div></a>'''


def render_home(studies, site):
    cards = "".join(card(study, i) for i, study in enumerate(studies, 1))
    brand_links = "".join(f'<a href="studies/{e(study["slug"])}.html">{e(study["brand"])}</a>' for study in studies)
    body = f'''<section class="hero"><div class="hero-content"><p class="eyebrow light">AKSHAT KAVIDAYAL <span class="separator">/</span> BRAND & MARKETING</p><h1>Wait. Why did<br><em>they do that?</em></h1><p class="hero-intro">{e(site['intro'])}</p><a class="hero-link" href="#studies">Explore my case studies <span aria-hidden="true">↗</span></a></div><div class="hero-visual" role="img" aria-label="Original editorial collage of unbranded objects from food, beauty, music and sport"><div class="hero-image"></div><span class="visual-caption">CAMPAIGNS / PRODUCTS / POSITIONING</span></div></section>
    <div class="brand-strip" aria-label="Brands in the archive"><span>IN THE ARCHIVE</span><div>{brand_links}</div></div>
    <section class="intro-strip" aria-label="Editorial focus"><span>01 &nbsp; Observe the move</span><span>02 &nbsp; Question the strategy</span><span>03 &nbsp; Propose a test</span></section>
    <section class="studies-section" id="studies"><div class="section-heading"><div><p class="eyebrow">THE ARCHIVE</p><h2>Recent dissections<span class="period">.</span></h2></div><p>Campaigns, products and launches through a practical marketing lens.</p></div><div class="filter-row" role="group" aria-label="Filter case studies"><button class="filter active" type="button" data-filter="all" aria-pressed="true">All studies <span>{len(studies):02d}</span></button><button class="filter" type="button" data-filter="campaign" aria-pressed="false">Campaigns</button><button class="filter" type="button" data-filter="product" aria-pressed="false">Products</button></div><div class="study-grid">{cards}</div><p class="filter-empty" hidden>No studies in this category yet.</p></section>
    <section class="method-teaser"><p class="eyebrow light">THE APPROACH</p><h2>Notice the move.<br><em>Question the logic.</em></h2><p>I start with what a brand actually did, ask what strategic problem it might solve, then push the thought one step further: what would I test?</p><a href="about.html">Meet Akshat <span aria-hidden="true">↗</span></a></section>'''
    return shell("Case studies", site["description"], body)


def paragraphs(items):
    return "".join(f"<p>{e(item)}</p>" for item in items)


def render_study(study):
    facts = "".join(f"<li>{e(item)}</li>" for item in study["facts"])
    sources = "".join(f'<li><a href="{e(item["url"])}" target="_blank" rel="noopener noreferrer">{e(item["label"])} <span aria-hidden="true">↗</span></a></li>' for item in study["sources"])
    origin = e(study.get("origin", "Independent analysis"))
    opening = f'<p class="article-opening">{e(study["opening"])}</p>' if study.get("opening") else ""
    rail_mark = f'<img class="article-logo" src="../{e(study["logo"])}" alt="{e(study["brand"])} logo" loading="lazy">' if study.get("logo") else f'<div class="rail-number">{e(study["brand"][0])}<span>.</span></div>'
    body = f'''<article class="article"><div class="article-topline"><a href="../index.html" class="back-link">← All studies</a><span>FIELD NOTE / {e(study['brand']).upper()}</span></div><header class="article-header"><p class="eyebrow">{e(study['industry'])} <span aria-hidden="true">/</span> {e(study['lens'])}</p><h1>{e(study['title'])}</h1><p class="article-dek">{e(study['dek'])}</p><div class="article-meta"><span>{e(study['date'])}</span><span>{origin}</span></div></header><div class="article-layout"><aside class="article-rail">{rail_mark}<p>BRAND<br>{e(study['brand']).upper()}</p><p>ANALYSIS<br>{e(study['lens']).upper()}</p></aside><div class="article-content">{opening}<section class="thesis"><p class="eyebrow">THE TAKE</p><h2>{e(study['thesis'])}</h2></section><section><p class="section-number">01 / OBSERVED</p><h2>What happened</h2><ul class="fact-list">{facts}</ul></section><section><p class="section-number">02 / INTERPRETED</p><h2>Why it matters</h2>{paragraphs(study['analysis'])}</section><section><p class="section-number">03 / CHALLENGED</p><h2>Where the idea could fall short</h2><p>{e(study['weakness'])}</p></section><section class="test-block"><p class="section-number">04 / TEST NEXT</p><h2>One experiment I would run</h2><p>{e(study['test'])}</p></section><section class="source-block"><p class="section-number">SOURCE NOTES</p><h2>Evidence & limitations</h2><p>{e(study['limitation'])}</p><ul>{sources}</ul></section></div></div><div class="article-end"><a href="../index.html">← Back to all studies</a></div></article>'''
    return shell(study["title"], study["dek"], body, depth=1)


def render_about(site):
    body = f'''<article class="about-page"><div class="about-header"><p class="eyebrow light">AKSHAT KAVIDAYAL / BRAND & MARKETING</p><h1>I keep asking<br><em>why that worked.</em></h1><p>I'm interested in the point where consumer insight becomes a brand people choose. My work and interests span FMCG, audio and AV, partnerships, products and culture. This archive is where I make my thinking visible.</p></div><div class="about-grid"><div class="about-number">01<span>.</span></div><div><h2>Start with the original move</h2><p>I find the launch, advertisement, product page or company statement. What did the brand actually show, when, and where?</p></div><div class="about-number">02<span>.</span></div><div><h2>Separate fact from interpretation</h2><p>I describe observable choices first, then explain what they might mean for attention, positioning, behavior or growth. I label a hypothesis as a hypothesis.</p></div><div class="about-number">03<span>.</span></div><div><h2>End with a useful test</h2><p>Every case study closes with an experiment that could sharpen the decision. Public sources rarely reveal the full commercial result, so I keep the limits visible.</p></div></div><aside class="about-note"><p class="eyebrow">LET'S TALK</p><p>This is independent editorial analysis, built from public materials. I share more thinking on <a href="{e(site['linkedin_url'])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>. The portfolio is not affiliated with the brands discussed.</p></aside></article>'''
    return shell("Method", "How Brand Method researches and writes its marketing case studies.", body)


def main():
    site = json.loads((ROOT / "site.json").read_text())
    studies = json.loads((ROOT / "content/from-linkedin.json").read_text()) + json.loads((ROOT / "content/studies.json").read_text())
    OUT.mkdir(exist_ok=True)
    (OUT / "studies").mkdir(exist_ok=True)
    for asset in ASSETS.iterdir():
        if asset.is_file():
            shutil.copy2(asset, OUT / asset.name)
    (OUT / "index.html").write_text(render_home(studies, site))
    (OUT / "about.html").write_text(render_about(site))
    for study in studies:
        (OUT / "studies" / f"{study['slug']}.html").write_text(render_study(study))
    print(f"Built {len(studies)} studies in {OUT}")


if __name__ == "__main__":
    main()
