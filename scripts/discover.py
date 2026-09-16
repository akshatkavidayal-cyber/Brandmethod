#!/usr/bin/env python3
"""Collect research leads from public RSS feeds; never generate or publish articles."""

import argparse
import datetime as dt
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEYWORDS = {
    "campaign": 3, "launch": 3, "brand": 2, "product": 2, "packaging": 3,
    "retail": 2, "advertising": 2, "ad": 1, "sku": 4, "pricing": 3,
    "partnership": 2, "creative": 2, "marketing": 2, "rebrand": 3,
}


def clean(value):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value or ""))).strip()


def get_text(element, names):
    for name in names:
        found = element.find(name)
        if found is not None and found.text:
            return clean(found.text)
    return ""


def get_link(element):
    link = get_text(element, ("link",))
    if link:
        return link
    for found in element.findall("{http://www.w3.org/2005/Atom}link"):
        if found.get("rel", "alternate") == "alternate" and found.get("href"):
            return found.attrib["href"]
    return ""


def fetch(feed):
    req = urllib.request.Request(feed["url"], headers={"User-Agent": "BrandMethodResearch/1.0 (+portfolio research queue)"})
    with urllib.request.urlopen(req, timeout=18) as response:
        data = response.read(2_000_000)
    root = ET.fromstring(data)
    entries = root.findall(".//item") or root.findall(".//{http://www.w3.org/2005/Atom}entry")
    for item in entries:
        title = get_text(item, ("title", "{http://www.w3.org/2005/Atom}title"))
        summary = get_text(item, ("description", "summary", "{http://www.w3.org/2005/Atom}summary"))
        url = get_link(item)
        if not title or not url:
            continue
        haystack = f"{title} {summary}".lower()
        score = sum(points for word, points in KEYWORDS.items() if re.search(rf"\b{re.escape(word)}\b", haystack))
        if score >= 3:
            yield {"title": title, "url": url, "source": feed["name"], "score": score}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="research/queue.md")
    args = parser.parse_args()
    feeds = json.loads((ROOT / "research/feeds.json").read_text())
    candidates, errors = [], []
    for feed in feeds:
        try:
            candidates.extend(fetch(feed))
        except (OSError, ET.ParseError, ValueError) as exc:
            errors.append(f"{feed['name']}: {type(exc).__name__}")
    seen, unique = set(), []
    for item in sorted(candidates, key=lambda x: -x["score"]):
        if item["url"] not in seen:
            unique.append(item)
            seen.add(item["url"])
    today = dt.date.today().isoformat()
    lines = [f"# Research candidates — {today}", "", "These are leads, not verified case studies. Open original brand sources before writing.", ""]
    if unique:
        for item in unique[:8]:
            lines += [f"- **{item['title']}** — [{item['source']}]({item['url']}) · relevance {item['score']}"]
    else:
        lines += ["No suitable candidates found in the configured feeds."]
    lines += ["", "## Review checklist", "", "1. Find the original brand announcement, product page or ad.", "2. Record the date, market, SKU or campaign details, and source links.", "3. Write an original thesis; separate facts from interpretation.", "4. State the uncertainty and one measurable test.", "5. Add the reviewed study to `content/studies.json` and merge to publish."]
    if errors:
        lines += ["", "Feed errors: " + ", ".join(errors)]
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(unique[:8])} leads to {output}")


if __name__ == "__main__":
    main()
