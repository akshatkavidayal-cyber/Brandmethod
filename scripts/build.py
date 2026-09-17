#!/usr/bin/env python3
"""Build the static portfolio from reviewed case-study data."""

import html
import json
import shutil
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree

from professional import professional_pages

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
ASSETS = ROOT / "assets"
CONFIG = json.loads((ROOT / "site.json").read_text())
BASE = CONFIG["base_url"].rstrip("/") + "/"


def e(value):
    return html.escape(str(value), quote=True)


def shell(title, description, body, depth=0, path="", kind="WebPage", extra_schema=None):
    root = "../" * depth
    canonical = BASE + path
    nav = f'''<header class="site-header"><a class="wordmark" href="{root}" aria-label="Brand Method home"><img class="brand-mark" src="{root}favicon.svg" alt="" width="44" height="44"><span>BRAND<br>METHOD</span></a><nav aria-label="Main navigation"><a href="{root}work/">Work</a><a href="{root}insights/">Insights</a><a href="{root}about/">About</a><a href="{root}resume/">Résumé</a><a href="{root}contact/">Contact</a></nav></header>'''
    contact = f'<a href="mailto:{e(CONFIG["contact_email"])}">Get in touch</a><br>' if CONFIG.get("contact_email") else ""
    linkedin = f'<a href="{e(CONFIG["linkedin_url"])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><br>' if CONFIG.get("linkedin_url") else ""
    footer = f'''<footer class="site-footer"><div><strong>BRAND METHOD</strong><p>By {e(CONFIG['author'])}. Marketing decisions, examined.</p></div><div>{contact}{linkedin}<a href="{root}contact/">Contact Akshat</a><p>Independent editorial analysis. No affiliation with brands discussed in Insights.</p></div></footer>'''
    person = {"@type":"Person","@id":BASE+"#akshat","name":CONFIG["author"],"url":BASE+"about/","description":"Brand Marketing & Business Development across FMCG, consumer and technology.","image":BASE+"akshat-portrait.webp","alumniOf":{"@type":"CollegeOrUniversity","name":"emlyon business school"},"knowsAbout":["Brand marketing","FMCG","Consumer insights","Business development","Strategic partnerships","Professional audiovisual technology"],"sameAs":[CONFIG["linkedin_url"],"https://github.com/akshatkavidayal-cyber"]}
    page = {"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":BASE+"#website","name":"Brand Method","url":BASE,"publisher":{"@id":BASE+"#akshat"}},person,{"@type":kind,"@id":canonical+"#page","url":canonical,"name":title,"description":description,"isPartOf":{"@id":BASE+"#website"},"author":{"@id":BASE+"#akshat"}}]}
    if kind == "ProfilePage":
        page["@graph"][-1]["mainEntity"] = {"@id":BASE+"#akshat"}
    if extra_schema:
        page["@graph"][-1].update(extra_schema)
    schema = json.dumps(page, ensure_ascii=False).replace("<", "\\u003c")
    full_title = f"{title} | Akshat Kavidayal · Brand Method"
    verification = f'<meta name="google-site-verification" content="{e(CONFIG["google_site_verification"])}">' if not path and CONFIG.get("google_site_verification") else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#291d37"><meta name="description" content="{e(description)}">{verification}<title>{e(full_title)}</title><link rel="canonical" href="{e(canonical)}"><meta property="og:type" content="{'article' if kind == 'Article' else 'website'}"><meta property="og:title" content="{e(full_title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{e(canonical)}"><meta property="og:site_name" content="Brand Method"><meta property="og:image" content="{e(BASE + 'akshat-portrait.webp')}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(full_title)}"><meta name="twitter:description" content="{e(description)}"><link rel="icon" href="{root}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{root}styles.css"><script type="application/ld+json">{schema}</script></head><body><a class="skip-link" href="#main">Skip to content</a>{nav}<main id="main">{body}</main>{footer}<script src="{root}main.js" defer></script></body></html>'''


def card(study, index):
    category = study.get("category", study["lens"].split(" & ")[0])
    label = "FROM MY LINKEDIN NOTES" if study.get("origin", "").startswith("Expanded from Akshat's LinkedIn") else f"{index:02d} / FIELD NOTE"
    mark = f'<img class="cover-logo" src="{e(study["logo"])}" alt="" loading="lazy">' if study.get("logo") else f'<span class="cover-mark">{e(study["brand"])}</span>'
    return f'''<a class="study-card study-card--{e(study['slug'].split('-')[0])}" href="studies/{e(study['slug'])}.html" data-category="{e(category.lower())}" data-industry="{e(study['industry'].lower())}"><div class="card-cover" aria-hidden="true">{mark}<span class="cover-number">{index:02d}</span></div><div class="card-top"><span class="card-index">{label}</span><span class="card-brand">{e(study['brand'])}</span></div><div class="card-body"><p class="eyebrow">{e(study['industry'])} <span aria-hidden="true">/</span> {e(study['lens'])}</p><h3>{e(study['title'])}</h3><p>{e(study['dek'])}</p></div><div class="card-bottom"><span>Read the analysis</span><span aria-hidden="true">↗</span></div></a>'''


def render_home(studies, site):
    cards = "".join(card(study, i) for i, study in enumerate(studies, 1))
    brand_links = "".join(f'<a href="studies/{e(study["slug"])}.html">{e(study["brand"])}</a>' for study in studies)
    body = f'''<section class="hero"><div class="hero-content"><p class="eyebrow light">AKSHAT KAVIDAYAL <span class="separator">/</span> BRAND MARKETING & BUSINESS DEVELOPMENT</p><h1>I turn consumer insight into <em>brands people choose.</em></h1><p class="hero-intro">FMCG · Consumer · Technology · Global Marketing · Partnerships. {e(site['intro'])}</p><div class="hero-actions"><a class="hero-link" href="work/">View my work <span aria-hidden="true">↗</span></a><a class="hero-link" href="resume/">View résumé <span aria-hidden="true">↗</span></a></div></div><div class="hero-visual" role="img" aria-label="Abstract editorial question mark in mint and melon against an aubergine background"><div class="hero-image"></div><span class="visual-caption">MARKETING / CONSUMER / CULTURE / TECHNOLOGY</span></div></section>
    <section class="professional-intro"><p class="eyebrow">TWO SIDES OF THE SAME CURIOSITY</p><div class="focus-grid"><a href="brand-marketing/"><span>01 / FMCG & CONSUMER</span><h2>Brand marketing</h2><p>Global brand work, consumer insight, brand equity and communications strategy.</p><strong>Explore the practice ↗</strong></a><a href="business-development/"><span>02 / B2B & TECHNOLOGY</span><h2>Business development</h2><p>Partnerships, channels, go-to-market and professional audio and AV.</p><strong>Explore the practice ↗</strong></a></div><p class="professional-note">My editorial studies below are independent analysis. <a href="work/">See professional work and research separately ↗</a></p></section>
    <div class="brand-strip" aria-label="Brands in the archive"><span>IN THE ARCHIVE</span><div>{brand_links}</div></div>
    <section class="intro-strip" aria-label="Editorial focus"><span>Close reads of brands, products and the things that don't quite add up.</span></section>
    <section class="studies-section" id="studies"><div class="section-heading"><div><p class="eyebrow">THE ARCHIVE</p><h2>Recent dissections<span class="period">.</span></h2></div><p>Campaigns, products and launches through a practical marketing lens.</p></div><div class="filter-row" role="group" aria-label="Filter case studies"><button class="filter active" type="button" data-filter="all" aria-pressed="true">All studies <span>{len(studies):02d}</span></button><button class="filter" type="button" data-filter="campaign" aria-pressed="false">Campaigns</button><button class="filter" type="button" data-filter="product" aria-pressed="false">Products</button></div><div class="study-grid">{cards}</div><p class="filter-empty" hidden>No studies in this category yet.</p></section>
    <section class="method-teaser"><p class="eyebrow light">A NOTE FROM AKSHAT</p><h2>It caught my eye.<br><em>Here’s why.</em></h2><p>Some brand ideas I love. Some frustrate me. Every one here made me stop, ask a question, and form an opinion.</p><a href="about.html">More about me <span aria-hidden="true">↗</span></a></section>'''
    return shell("Brand Marketing & Business Development", "Akshat Kavidayal works across FMCG brand marketing, consumer insight, technology partnerships and business development. Explore professional work and independent brand analysis.", body)


def paragraphs(items):
    return "".join(f"<p>{e(item)}</p>" for item in items)


def story_blocks(blocks):
    rendered = []
    for block in blocks:
        kind = block["type"]
        if kind == "heading":
            rendered.append(f'<h2 class="story-heading">{e(block["text"])}</h2>')
        elif kind == "paragraph":
            rendered.append(f'<p>{e(block["text"])}</p>')
        elif kind == "list":
            items = "".join(f'<li>{e(item)}</li>' for item in block["items"])
            rendered.append(f'<ul class="story-list">{items}</ul>')
        elif kind == "aside":
            rendered.append(f'<aside class="story-aside"><span>{e(block["label"])}</span><p>{e(block["text"])}</p></aside>')
        else:
            raise ValueError(f"Unknown story block: {kind}")
    return "".join(rendered)


def render_study(study):
    sources = "".join(f'<li><a href="{e(item["url"])}" target="_blank" rel="noopener noreferrer">{e(item["label"])} <span aria-hidden="true">↗</span></a></li>' for item in study["sources"])
    origin = e(study.get("origin", "Independent analysis"))
    rail_mark = f'<img class="article-logo" src="../{e(study["logo"])}" alt="{e(study["brand"])} logo" loading="lazy">' if study.get("logo") else f'<div class="rail-number">{e(study["brand"][0])}<span>.</span></div>'
    related = '<a href="../brand-marketing/">Brand marketing practice ↗</a><a href="../work/">Professional work ↗</a>'
    if study['brand'].lower() in ('vaseline', 'daddy', 'duolingo'):
        related += '<a href="../research/influencer-selection-fmcg/">Influencer selection research ↗</a>'
    body = f'''<article class="article"><div class="article-topline"><a href="../insights/" class="back-link">← All insights</a><span>FIELD NOTE / {e(study['brand']).upper()}</span></div><header class="article-header"><p class="eyebrow">{e(study['industry'])} <span aria-hidden="true">/</span> {e(study['lens'])}</p><h1>{e(study['title'])}</h1><p class="article-dek">{e(study['dek'])}</p><div class="article-meta"><span>{e(study['date'])}</span><span>{origin}</span></div></header><div class="article-layout"><aside class="article-rail">{rail_mark}<p>BRAND<br>{e(study['brand']).upper()}</p><p>ANALYSIS<br>{e(study['lens']).upper()}</p></aside><div class="article-content"><p class="article-opening">{e(study['opening'])}</p><div class="story-body">{story_blocks(study['story'])}</div><section class="source-block"><p class="section-number">SOURCE NOTES</p><h2>What the sources can and cannot tell us</h2><p>{e(study['limitation'])}</p><ul>{sources}</ul></section><section class="related-links"><p class="section-number">EXPLORE THE LENS</p><div class="inline-links">{related}</div></section></div></div><div class="article-end"><a href="../insights/">← Back to all insights</a></div></article>'''
    return shell(study["title"], study["dek"], body, depth=1, path=f"studies/{study['slug']}.html", kind="Article", extra_schema={"headline":study["title"],"datePublished":study["date"],"mainEntityOfPage":BASE+f"studies/{study['slug']}.html"})


def render_about(site, depth=0):
    root = "../" * depth
    body = f'''<article class="about-page about-personal">
    <header class="about-opening"><div class="about-opening-copy"><p class="eyebrow">A NOTE FROM AKSHAT</p><h1>I have opinions.<br><em>Quite a few.</em></h1><p>About the brands I love. The products that frustrate me. And the decisions everyone seems to be talking around.</p></div><figure class="about-portrait"><img src="{root}akshat-portrait.webp" alt="Portrait of Akshat Kavidayal" width="1200" height="1600" fetchpriority="high"><figcaption><span>AKSHAT KAVIDAYAL</span><span>THE PERSON BEHIND THE OPINIONS</span></figcaption></figure></header>
    <div class="about-intro"><p class="about-kicker">HI, I'M AKSHAT.</p><div><p class="about-lead">I'm a marketer who can get stuck on one small detail long after everyone else has moved on.</p><p>Why did that packaging choice feel generous? Why did that campaign travel? Why does a product look brilliant in a presentation and feel irritating in real life?</p><p>Some brand ideas make me want to tell everyone about them. Others bother me enough that I have to work out why. And sometimes the most interesting part is the thing nobody seems to be saying.</p></div></div>
    <section class="about-belief"><p class="eyebrow">WHY THIS EXISTS</p><h2>That is what I write about here.</h2><p>Brand Method is my space to pull apart campaigns, products and the choices behind them. I start with the thing that made me stop, look at what the brand actually did, and make an argument about what it means. I say where I think it works, where it loses me, and what I would try next.</p><p>These are my opinions, grounded in public evidence and open to being challenged. I would rather ask a better question than pretend to have a perfect answer.</p></section>
    <div class="about-signoff"><p class="about-signature">See something worth arguing about?</p><div><a href="{root}index.html#studies">Read the case studies <span aria-hidden="true">↗</span></a><a href="{e(site['linkedin_url'])}" target="_blank" rel="noopener noreferrer">Find me on LinkedIn <span aria-hidden="true">↗</span></a></div></div>
    </article>'''
    body = body.replace('<div class="about-signoff">', f'<section class="about-professional"><p class="eyebrow">THE WORK BEHIND THE OPINIONS</p><h2>Marketing, consumer, culture and technology.</h2><p>My background spans global brand marketing with Danone / Activia, professional audio and AV, B2B technology and business development. I completed an MSc in International Marketing & Business Development at emlyon business school, with research into how FMCG brand managers select influencers.</p><div class="inline-links"><a href="{root}work/">Professional work ↗</a><a href="{root}research/influencer-selection-fmcg/">The research ↗</a><a href="{root}resume/">Résumé ↗</a></div></section><div class="about-signoff">')
    return shell("About Akshat Kavidayal", "Meet Akshat Kavidayal: an opinion-led marketer across FMCG brand marketing, consumer insight, technology and business development.", body, depth=depth, path="about/", kind="ProfilePage")


def main():
    site = json.loads((ROOT / "site.json").read_text())
    studies = sorted(json.loads((ROOT / "content/from-linkedin.json").read_text()) + json.loads((ROOT / "content/studies.json").read_text()), key=lambda study: study["date"], reverse=True)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(exist_ok=True)
    (OUT / "studies").mkdir(exist_ok=True)
    for asset in ASSETS.iterdir():
        if asset.is_file() and asset.name != "type-options.html":
            shutil.copy2(asset, OUT / asset.name)
    (OUT / "index.html").write_text(render_home(studies, site))
    (OUT / "about.html").write_text(render_about(site))
    (OUT / "about").mkdir(exist_ok=True)
    (OUT / "about" / "index.html").write_text(render_about(site, depth=1))
    for path, title, description, body in professional_pages(studies, site):
        target = OUT / path / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(shell(title, description, body, depth=len(Path(path).parts), path=path+"/"))
    for study in studies:
        (OUT / "studies" / f"{study['slug']}.html").write_text(render_study(study))
    urls = ["", "about/"] + [path + "/" for path, _, _, _ in professional_pages(studies, site)] + [f"studies/{s['slug']}.html" for s in studies]
    root = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for path in urls:
        SubElement(SubElement(root, "url"), "loc").text = BASE + path
    ElementTree(root).write(OUT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
    (OUT / "404.html").write_text(shell("Page not found", "That page could not be found.", '<section class="pro-page"><h1>Lost the thread?</h1><p>That page is not here. Try the work or insights index.</p><div class="inline-links"><a href="/Brandmethod/work/">Work ↗</a><a href="/Brandmethod/insights/">Insights ↗</a></div></section>', path="404.html", extra_schema={"@type":"WebPage"}).replace('<meta name="description"', '<meta name="robots" content="noindex"><meta name="description"'))
    print(f"Built {len(studies)} studies in {OUT}")


if __name__ == "__main__":
    main()
