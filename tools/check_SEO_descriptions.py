# filename: build_og_description_fixes.py
import re, sys, time
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import pandas as pd

ROOT = "https://fransimo.info/"
EN_SITEMAP = "https://fransimo.info/en/sitemap.xml"

ROOT = "http://localhost:1313/"
EN_SITEMAP = "http://localhost:1313/en/sitemap.xml"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; MetaDescFixer/1.0)"}
TIMEOUT = 20

def get(url):
    r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    return r.text

def parse_sitemap(url):
    xml = get(url)
    soup = BeautifulSoup(xml, "xml")
    # determine if index or urlset
    loc_tags = []
    if soup.find("sitemapindex"):
        for sm in soup.find_all("sitemap"):
            loc = sm.find("loc")
            if loc and "/en/" in loc.text:
                loc_tags.extend(parse_sitemap(loc.text))
    elif soup.find("urlset"):
        for u in soup.find_all("url"):
            loc = u.find("loc")
            if loc:
                loc_tags.append(loc.text.strip())
    else:
        # fallback: collect all <loc>
        for loc in soup.find_all("loc"):
            loc_tags.append(loc.text.strip())
    # normalise & dedup
    seen, urls = set(), []
    for u in loc_tags:
        if u not in seen:
            seen.add(u)
            urls.append(u)
    return urls

def textblocks(soup):
    # remove nav/aside/footer/scripts
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "form"]):
        tag.decompose()
    # Prefer structured containers
    candidates = []
    for sel in [
        "article", "main", "div.book-page", "div.markdown", "section",
        "div.content", "div.container", "div"
    ]:
        for el in soup.select(sel):
            txt = " ".join(el.get_text(" ", strip=True).split())
            if len(txt) > 80:
                candidates.append(txt)
    # fallback to body
    if not candidates and soup.body:
        txt = " ".join(soup.body.get_text(" ", strip=True).split())
        if len(txt) > 80:
            candidates.append(txt)
    return candidates

def smart_truncate(txt, max_len=160):
    txt = re.sub(r"\s+", " ", txt).strip().replace("“","\"").replace("”","\"").replace("’","'")
    if len(txt) <= max_len:
        return txt
    # try to end at sentence boundary between 140 and max_len
    cut = max_len
    for m in re.finditer(r"[\.!\?]\s", txt[:max_len][120:]):
        cut = 120 + m.start() + 1
    if cut < 140:  # couldn’t find boundary; fall back to last space
        sp = txt.rfind(" ", 140, max_len)
        cut = sp if sp != -1 else max_len
    return txt[:cut].rstrip(" .,!?:;") + "."

def build_suggested_description(html):
    soup = BeautifulSoup(html, "lxml")
    # Compose a meaningful base text from the first strong paragraph-like block
    blocks = textblocks(soup)
    if not blocks:
        return None
    # Prefer block that mentions the topic more than menu items
    blocks.sort(key=lambda t: -len(t))
    base = blocks[0]
    # Avoid repeating cookie/legal/tooltips
    base = re.sub(r"(Accept all cookies|Privacy|Search|Menu).*?$", "", base, flags=re.I)
    # Trim very long leading breadcrumbs if present
    base = re.sub(r"^(?:[A-Za-z0-9#\s\-\|>:/]+){0,2}\s", "", base)
    return smart_truncate(base, 160)

def get_head_meta(html):
    soup = BeautifulSoup(html, "lxml")
    head = soup.find("head") or soup
    def meta(prop, attr="property"):
        t = head.find("meta", attrs={attr: prop})
        return t.get("content").strip() if t and t.get("content") else None
    og_desc = meta("og:description") or head.find("meta", attrs={"name":"description"})
    og_desc = (og_desc.get("content").strip() if hasattr(og_desc, "get") else og_desc) or ""
    og_title = meta("og:title") or (head.title.get_text(strip=True) if head.title else "")
    og_type  = meta("og:type") or ""
    canonical = head.find("link", rel=re.compile("^canonical$", re.I))
    canonical = canonical.get("href").strip() if canonical and canonical.get("href") else None
    return canonical, og_title, og_desc, og_type

def main():
    print("Fetching sitemap (EN)…")
    urls = parse_sitemap(EN_SITEMAP)
    print(f"Found {len(urls)} URLs")
    rows = []
    for i, url in enumerate(urls, 1):
        try:
            html = get(url)
            canonical, og_title, og_desc, og_type = get_head_meta(html)
            og_len = len(og_desc or "")
            if og_len > 200:
                suggested = build_suggested_description(html) or ""
                rows.append({
                    "canonical": canonical or url,
                    "title": og_title or "",
                    "suggested_description": suggested,
                    "original_og_description_length": og_len,
                    "og_type": og_type or "",
                    "source_url": url
                })
            if i % 10 == 0:
                print(f"  …{i} / {len(urls)}")
        except Exception as e:
            print(f"[WARN] {url} -> {e}")
            continue

    df = pd.DataFrame(rows, columns=[
        "canonical","title","suggested_description",
        "original_og_description_length","og_type","source_url"
    ])
    out = "og_description_fixes.xlsx"
    df.to_excel(out, index=False)
    print(f"Done. Wrote {len(df)} rows to {out}")

if __name__ == "__main__":
    main()

# pip install requests bs4 pandas lxml openpyxl

