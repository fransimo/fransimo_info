#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recolecta datos de artículos Markdown (Hugo u otros) y genera un Excel
con columnas: file_path, title, lang, description, content_text.
Compatible con Python 3.9.
"""
import argparse
import re
from pathlib import Path
from typing import Optional, Tuple, Dict, Any, List

import frontmatter
from unidecode import unidecode
import pandas as pd

# ---------- Utilidades de limpieza ----------

CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`]+`")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
HEADING_RE = re.compile(r"^#{1,6}\s+.*$", re.M)
HTML_TAG_RE = re.compile(r"<[^>]+>")  # por si hay HTML embebido
SHORTCODE_RE = re.compile(r"{{[<%].*?[>%]}}", re.S)  # Hugo shortcodes {{< … >}} o {{% … %}}

def strip_markdown(md: str) -> str:
    """Convierte el cuerpo Markdown a texto plano razonable."""
    if not md:
        return ""
    txt = md
    txt = CODE_FENCE_RE.sub(" ", txt)
    txt = INLINE_CODE_RE.sub(" ", txt)
    txt = IMAGE_RE.sub(" ", txt)
    txt = LINK_RE.sub(r"\1", txt)
    txt = SHORTCODE_RE.sub(" ", txt)
    txt = HEADING_RE.sub(" ", txt)
    txt = HTML_TAG_RE.sub(" ", txt)
    # bullets/quotes muy básicos
    txt = re.sub(r"^\s*[-*+]\s+", " ", txt, flags=re.M)
    txt = re.sub(r"^\s*>\s+", " ", txt, flags=re.M)
    # compresión de espacios
    txt = re.sub(r"\s+", " ", txt).strip()
    return txt

H1_RE = re.compile(r"^#\s+(.+)$", re.M)

def first_h1(md: str) -> Optional[str]:
    m = H1_RE.search(md or "")
    return m.group(1).strip() if m else None

# ---------- Inferencia de idioma ----------

def infer_lang_from_frontmatter(meta: Dict[str, Any]) -> Optional[str]:
    for key in ("lang", "language", "locale"):
        val = meta.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip().lower()
    # a veces hay lista de idiomas
    val = meta.get("languages")
    if isinstance(val, list) and val:
        first = str(val[0]).strip().lower()
        if first in ("es", "es-es", "spanish"):
            return "es"
        if first in ("en", "en-us", "english"):
            return "en"
    return None

def infer_lang_from_path(path: Path, sample_text: str) -> str:
    low = path.as_posix().lower()
    name = path.name.lower()
    if name.endswith(".es.md") or "/es/" in low:
        return "es"
    if name.endswith(".en.md") or "/en/" in low:
        return "en"
    # Heurística por acentos si no hay pistas
    lowtxt = unidecode(sample_text or "").lower()
    return "es" if re.search(r"[áéíóúñÁÉÍÓÚÑ]".lower(), sample_text or "") else "en"

# ---------- Filtrado de candidatos ----------

def is_candidate_article(path: Path, include_indexes: bool=False, include_taxonomies: bool=False) -> bool:
    p = path.as_posix().lower()
    if path.suffix.lower() != ".md":
        return False
    if not include_taxonomies and any(seg in p for seg in ("/tags/", "/tag/", "/categories/", "/category/", "/series/")):
        return False
    if not include_indexes and (p.endswith("/_index.md") or p.endswith("/index.md")):
        return False
    return True

# ---------- Extracción por archivo ----------

def extract_from_file(path: Path) -> Tuple[str, str, str, str, str]:
    """
    Devuelve (file_path, title, lang, description, content_text)
    """
    post = frontmatter.load(str(path))
    meta = post.metadata or {}
    raw_content = post.content or ""

    title = None
    # preferir front-matter title; si no, primer H1
    for key in ("title", "name", "pagetitle"):
        val = meta.get(key)
        if isinstance(val, str) and val.strip():
            title = val.strip()
            break
    if not title:
        h1 = first_h1(raw_content)
        if h1:
            title = h1
    if not title:
        title = path.stem  # último recurso

    # description tal cual está en front-matter (no fabricar)
    description = ""
    desc_val = meta.get("description")
    if isinstance(desc_val, str):
        description = desc_val.strip()

    # idioma
    lang = infer_lang_from_frontmatter(meta)
    if not lang:
        # leer una pequeña muestra para inferir por acentos si hace falta
        sample = raw_content[:1200]
        lang = infer_lang_from_path(path, sample)

    # cuerpo en texto plano
    content_text = strip_markdown(raw_content)

    return (str(path), title, lang, description, content_text)

# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser(description="Vuelca metadatos y contenido de artículos MD a Excel.")
    ap.add_argument("--roots", nargs="+", default=["content", "src/content"],
                    help="Directorios raíz a revisar (por orden).")
    ap.add_argument("--include-indexes", action="store_true",
                    help="Incluir _index.md / index.md.")
    ap.add_argument("--include-taxonomies", action="store_true",
                    help="Incluir taxonomías (tags/categories/series).")
    ap.add_argument("--out", default="articles_dump.xlsx",
                    help="Ruta de salida del Excel (.xlsx).")
    args = ap.parse_args()

    roots = [Path(r) for r in args.roots]
    md_files: List[Path] = []
    for r in roots:
        if r.exists():
            md_files.extend(r.rglob("*.md"))

    rows = []
    for p in sorted(md_files):
        if not is_candidate_article(p, include_indexes=args.include_indexes, include_taxonomies=args.include_taxonomies):
            continue
        try:
            row = extract_from_file(p)
            rows.append(row)
        except Exception as e:
            # No detenemos el proceso por un archivo problemático
            rows.append((str(p), "(ERROR al leer título)", "", "", f"[ERROR] {e}"))

    df = pd.DataFrame(rows, columns=["file_path", "title", "lang", "description", "content_text"])
    # Guardar Excel
    df.to_excel(args.out, index=False)
    print(f"✔ Hecho: {len(df)} filas escritas en {args.out}")

if __name__ == "__main__":
    main()
