#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lee un Excel con la columna 'suggested_description' y actualiza
el front-matter 'description' de los .md indicados en 'file_path'.

- Mantiene el formato original de front-matter (YAML/TOML/JSON).
- Si el archivo no tiene front-matter, crea uno (YAML).
- Requiere Python 3.9.
"""

import argparse
import json
import os
from pathlib import Path
from typing import Tuple, Optional, Dict

import pandas as pd
import yaml  # PyYAML
import toml  # toml

# ---------- Utilidades de front-matter ----------

def _detect_front_matter(text: str) -> Tuple[Optional[str], Optional[int], Optional[int]]:
    """
    Detecta formato y offsets del front-matter.
    Devuelve: (fmt, start_idx, end_idx) donde fmt in {"yaml","toml","json"} o None.
    Los índices delimitan SOLO el bloque (sin el cuerpo).
    """
    if not text:
        return None, None, None

    # Normalizar saltos de línea
    t = text.lstrip()
    start_offset = len(text) - len(t)
    if t.startswith('---\n') or t.startswith('---\r\n'):
        # YAML
        delim = '\n---'
        end_pos = t.find(delim, 4)
        if end_pos != -1:
            end_pos += len(delim)
            return "yaml", start_offset, start_offset + end_pos
    if t.startswith('+++\n') or t.startswith('+++\r\n'):
        # TOML
        delim = '\n+++'
        end_pos = t.find(delim, 4)
        if end_pos != -1:
            end_pos += len(delim)
            return "toml", start_offset, start_offset + end_pos
    # JSON front-matter estilo Hugo: bloque inicial {}
    # Buscamos primer bloque {...} al inicio de archivo
    if t.startswith('{'):
        # hallar llaves balanceadas simples (no JSON streaming complejo)
        depth, end_idx = 0, None
        for i, ch in enumerate(t):
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    end_idx = i + 1
                    break
        if end_idx:
            return "json", start_offset, start_offset + end_idx

    return None, None, None

def _parse_front_matter(fmt: str, blob: str) -> Dict:
    if fmt == "yaml":
        data = yaml.safe_load(blob) or {}
        if not isinstance(data, dict):
            data = {}
        return data
    if fmt == "toml":
        data = toml.loads(blob or "") or {}
        if not isinstance(data, dict):
            data = {}
        return data
    if fmt == "json":
        data = json.loads(blob or "{}") or {}
        if not isinstance(data, dict):
            data = {}
        return data
    return {}

def _dump_front_matter(fmt: str, data: Dict) -> str:
    if fmt == "yaml":
        return "---\n" + yaml.safe_dump(
            data, sort_keys=False, allow_unicode=True, width=1000
        ).rstrip() + "\n---\n\n"
    if fmt == "toml":
        return "+++\n" + toml.dumps(data).rstrip() + "\n+++\n\n"
    if fmt == "json":
        return json.dumps(data, ensure_ascii=False, indent=2) + "\n\n"
    # default YAML si no hay formato
    return "---\n" + yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True, width=1000
    ).rstrip() + "\n---\n\n"

def read_markdown(path: Path) -> Tuple[str, Optional[str], Dict, str]:
    """
    Lee un .md y devuelve:
    - formato ("yaml"/"toml"/"json"/None)
    - bloque raw del front-matter (opcional)
    - dict del front-matter
    - cuerpo (texto del artículo)
    """
    text = path.read_text(encoding="utf-8", errors="ignore")
    fmt, s, e = _detect_front_matter(text)
    if fmt is None:
        return None, None, {}, text
    raw = text[s:e]
    # extraer solo el contenido del bloque (sin delimitadores)
    if fmt == "yaml":
        core = raw.strip()
        if core.startswith('---'):
            core = core[3:]
        if core.endswith('---'):
            core = core[:-3]
        core = core.strip()
    elif fmt == "toml":
        core = raw.strip()
        if core.startswith('+++'):
            core = core[3:]
        if core.endswith('+++'):
            core = core[:-3]
        core = core.strip()
    else:  # json
        core = raw.strip()
    meta = _parse_front_matter(fmt, core)
    body = text[e:].lstrip("\n\r")
    return fmt, raw, meta, body

def write_markdown(path: Path, fmt: Optional[str], meta: Dict, body: str) -> None:
    header = _dump_front_matter(fmt or "yaml", meta)
    out = header + (body or "").lstrip()
    path.write_text(out, encoding="utf-8")

# ---------- Aplicación desde Excel ----------

def load_excel_any(excel_path: str) -> pd.DataFrame:
    """
    Carga .xlsx o el error común .xlxs.
    Debe contener: file_path, suggested_description
    """
    p = Path(excel_path)
    if not p.exists():
        # Intentar corregir extensión errónea
        if p.suffix.lower() == ".xlxs":
            p2 = p.with_suffix(".xlsx")
            if p2.exists():
                p = p2
        else:
            p2 = p.with_suffix(".xlxs")
            if p2.exists():
                p = p2
    if not p.exists():
        raise FileNotFoundError(f"No se encontró el Excel en: {excel_path}")
    df = pd.read_excel(p)
    return df

def main():
    ap = argparse.ArgumentParser(description="Aplica 'suggested_description' desde Excel a los .md.")
    ap.add_argument("--excel", default="articles_with_suggestions_v2_reviewed.xlsx",
                    help="Ruta al Excel revisado (xlsx/xlxs).")
    ap.add_argument("--root", default=".", help="Raíz del repositorio (para resolver file_path).")
    ap.add_argument("--column", default="suggested_description",
                    help="Nombre de la columna con la descripción a aplicar.")
    ap.add_argument("--dry-run", action="store_true", help="Solo informa, no escribe archivos.")
    ap.add_argument("--backup", action="store_true", help="Crea copia .bak del .md antes de escribir.")
    ap.add_argument("--only-changed", action="store_true",
                    help="Solo escribe si el nuevo texto difiere del description actual.")
    args = ap.parse_args()

    df = load_excel_any(args.excel)

    # Validación mínima
    for col in ("file_path", args.column):
        if col not in df.columns:
            raise ValueError(f"Falta la columna '{col}' en el Excel.")

    root = Path(args.root).resolve()
    wrote, skipped, missing = 0, 0, 0

    for i, row in df.iterrows():
        file_path = str(row.get("file_path") or "").strip()
        suggested = row.get(args.column)
        if not file_path:
            skipped += 1
            print(f"[SKIP] Fila {i}: sin file_path.")
            continue
        # Aceptar NaN/None como vacío (no aplicar)
        if not isinstance(suggested, str) or not suggested.strip():
            skipped += 1
            print(f"[SKIP] {file_path}: sin {args.column}.")
            continue

        md_path = (root / file_path).resolve()
        if not md_path.exists():
            # Prueba también sin prefijo 'content/' si viniera relativo distinto
            alt = root / "content" / file_path
            if alt.exists():
                md_path = alt.resolve()
            else:
                missing += 1
                print(f"[MISS] No existe: {md_path}")
                continue

        fmt, raw, meta, body = read_markdown(md_path)
        current_desc = meta.get("description")
        new_desc = suggested.strip()

        if args.only_changed and isinstance(current_desc, str) and current_desc.strip() == new_desc:
            skipped += 1
            print(f"[OK  ] {file_path}: description ya coincide (sin cambios).")
            continue

        meta["description"] = new_desc

        if args.dry_run:
            print(f"[DRY ] {file_path}: '{new_desc}'")
            continue

        if args.backup:
            bak = md_path.with_suffix(md_path.suffix + ".bak")
            try:
                bak.write_text(md_path.read_text(encoding="utf-8"), encoding="utf-8")
            except Exception:
                pass

        write_markdown(md_path, fmt, meta, body)
        wrote += 1
        print(f"[WRITE] {file_path}: description actualizada.")

    print(f"\nResumen: escritos={wrote}, omitidos={skipped}, no_encontrados={missing}")

if __name__ == "__main__":
    main()
