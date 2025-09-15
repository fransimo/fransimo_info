#!/usr/bin/env python3
# tools/fix_og_descriptions.py
import argparse, os, re
from pathlib import Path
from typing import Optional

import frontmatter
from unidecode import unidecode

def strip_markdown(md: str) -> str:
    md = re.sub(r"```.+?```", " ", md, flags=re.S)
    md = re.sub(r"`[^`]+`", " ", md)
    md = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", md)            # imágenes
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)         # links
    md = re.sub(r"^#+\s.*$", " ", md, flags=re.M)            # headings
    md = re.sub(r"{[^}]+}", " ", md)                         # shortcodes simples
    md = re.sub(r"\s+", " ", md).strip()
    return md

def first_meaningful_paragraph(md_text: str, min_len=80) -> str:
    parts = [p.strip() for p in re.split(r"\n\s*\n", md_text) if p.strip()]
    for p in parts:
        if p.startswith(("-", "*", ">")):
            continue
        txt = strip_markdown(p)
        if len(txt) >= min_len:
            return txt
    return strip_markdown(md_text)

def smart_truncate(txt: str, max_len=160, min_len=140) -> str:
    txt = re.sub(r"\s+", " ", txt).strip()
    if len(txt) <= max_len:
        return txt
    window = txt[min_len:max_len]
    m = re.search(r"[.!?](?:\s|$)", window)
    if m:
        return (txt[:min_len + m.start() + 1]).strip()
    cut = txt.rfind(" ", min_len, max_len)
    if cut == -1:
        cut = max_len
    return txt[:cut].rstrip(" .,!?:;") + "."

def looks_like_menu_garbage(txt: str) -> bool:
    bad = ("search", "menu", "copyright", "privacy", "cookies")
    low = unidecode(txt.lower())
    return any(w in low for w in bad)

def infer_lang_from_path(p: Path) -> str:
    name = p.name.lower()
    if name.endswith(".es.md") or "/es/" in p.as_posix():
        return "es"
    if name.endswith(".en.md") or "/en/" in p.as_posix():
        return "en"
    sample = ""
    try:
        sample = p.read_text(encoding="utf-8", errors="ignore")[:1000]
    except Exception:
        pass
    return "es" if re.search(r"[áéíóúñÁÉÍÓÚÑ]", sample) else "en"

def compute_candidate_description(post: frontmatter.Post, lang: str) -> Optional[str]:
    body = post.content or ""
    text = first_meaningful_paragraph(body)
    if not text or looks_like_menu_garbage(text):
        return None
    # tono formal: evita verbos promocionales al inicio
    text = re.sub(r"^(Descubre|Explora|Conoce|Learn|Discover|Explore)\b[:,]?\s+",
                  "", text, flags=re.I)
    return smart_truncate(text, max_len=160, min_len=140)

def current_og_length(post: frontmatter.Post) -> int:
    desc = post.get("description")
    if isinstance(desc, (list, dict)):
        desc = None
    if desc and isinstance(desc, str):
        return len(desc.strip())
    body_txt = strip_markdown(post.content or "")
    # estimación para decidir si el OG fabricado por el tema será largo
    return len(body_txt[:400])

def is_article_candidate(path: Path) -> bool:
    low = path.as_posix().lower()
    if any(seg in low for seg in ("/tags/", "/categories/", "/series/", "/_index", "/index.md")):
        return False
    return path.suffix.lower() == ".md"

def process_file(path: Path, threshold: int, dry_run: bool):
    try:
        post = frontmatter.load(str(path))  # acepta ruta como str
    except Exception as e:
        return False, f"[SKIP] {path}: no se pudo leer front-matter ({e})"
    if not is_article_candidate(path):
        return False, f"[SKIP] {path}: no es artículo"
    og_len = current_og_length(post)
    if og_len <= threshold:
        return False, f"[OK]   {path}: OG<=threshold ({og_len})"
    lang = infer_lang_from_path(path)
    suggestion = compute_candidate_description(post, lang)
    if not suggestion or len(suggestion) < 80:
        return False, f"[SKIP] {path}: sin párrafo útil para proponer descripción"
    if isinstance(post.get("description"), str) and len(post["description"].strip()) <= threshold:
        return False, f"[OK]   {path}: ya tiene description adecuada"
    post["description"] = suggestion
    if dry_run:
        return True, f"[DRY]  {path}: '{suggestion}'"
    # GUARDAR: abrir archivo y usar frontmatter.dump con file handle
    try:
        with open(path, "w", encoding="utf-8") as f:
            frontmatter.dump(post, f)
    except TypeError:
        # versiones antiguas de python-frontmatter pueden requerir .dumps + write
        data = frontmatter.dumps(post)
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)
    return True, f"[WRITE]{path}: '{suggestion}'"

def main():
    ap = argparse.ArgumentParser(description="Fija descripciones OG concisas en Markdown (Hugo).")
    ap.add_argument("--roots", nargs="+", default=["content", "src/content"],
                    help="Directorios raíz a revisar")
    ap.add_argument("--threshold", type=int, default=200, help="Umbral de longitud OG")
    ap.add_argument("--min-chars", type=int, default=80, help="Mínimo de texto para aceptar un párrafo")
    ap.add_argument("--dry-run", action="store_true", help="No escribe; solo informa")
    args = ap.parse_args()

    changed = 0
    for root in args.roots:
        rootp = Path(root)
        if not rootp.exists():
            continue
        for path in rootp.rglob("*.md"):
            ok, msg = process_file(path, args.threshold, args.dry_run)
            print(msg)
            if ok and not args.dry_run:
                changed += 1
    print(f"\nHecho. Archivos modificados: {changed}")

if __name__ == "__main__":
    main()
