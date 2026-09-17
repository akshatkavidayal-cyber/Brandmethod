"""Check generated page metadata, JSON-LD, sitemap, and local links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1] / 'dist'

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.metadata, self.schemas = [], {}, []
        self.canonical, self.h1, self.in_schema, self.buffer = None, 0, False, ''
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == 'a' and 'href' in data: self.links.append(data['href'])
        if tag in ('img', 'script', 'link') and ('src' in data or 'href' in data):
            self.links.append(data.get('src', data.get('href')))
        if tag == 'link' and data.get('rel') == 'canonical': self.canonical = data['href']
        if tag == 'meta': self.metadata[data.get('name', data.get('property', ''))] = data.get('content')
        if tag == 'h1': self.h1 += 1
        if tag == 'script' and data.get('type') == 'application/ld+json':
            self.in_schema, self.buffer = True, ''
    def handle_data(self, data):
        if self.in_schema: self.buffer += data
    def handle_endtag(self, tag):
        if tag == 'script' and self.in_schema:
            self.schemas.append(json.loads(self.buffer))
            self.in_schema = False

errors = []
files = list(root.rglob('*.html'))
for file in files:
    page = Page()
    page.feed(file.read_text())
    name = str(file.relative_to(root))
    if page.h1 != 1: errors.append((name, 'expected one h1'))
    if not page.canonical or not page.metadata.get('description') or not page.schemas:
        errors.append((name, 'missing metadata or JSON-LD'))
    for link in page.links:
        if not link or link.startswith(('mailto:', 'https://', 'http://', '#', 'data:')): continue
        path = urlsplit(link).path
        if not path: continue
        target = (root / path[len('/Brandmethod/'):] if path.startswith('/Brandmethod/') else file.parent / path).resolve()
        if target.is_dir(): target = target / 'index.html'
        if not target.exists(): errors.append((name, f'broken link: {link}'))
urls = [item.text for item in ET.parse(root / 'sitemap.xml').iter() if item.tag.endswith('loc')]
if len(urls) != len(set(urls)): errors.append(('sitemap.xml', 'duplicate URL'))
for url in urls:
    path = urlsplit(url).path
    target = root / path[len('/Brandmethod/'):]
    if target.is_dir(): target = target / 'index.html'
    if not target.exists(): errors.append(('sitemap.xml', f'missing target: {url}'))
if errors: raise SystemExit('\n'.join(f'{name}: {issue}' for name, issue in errors))
print(f'PASS: {len(files)} HTML pages, {len(urls)} sitemap URLs; metadata, JSON-LD and local links resolve')
