#!/bin/bash

echo "--- Iniciando reorganización recursiva ---"

# 1. CASO 1: Ficheros simples (index.md / _index.md)
# Buscamos archivos que se llamen exactamente index.md o _index.md
find . -type f \( -name "index.md" -o -name "_index.md" \) | while read -r f; do
    # Evitamos procesar archivos que ya están dentro de carpetas de fecha (evita bucles)
    if [[ ! "$f" =~ [0-9]{4}-[0-9]{2}-[0-9]{2} ]]; then
        dir=$(dirname "$f")
        base=$(basename "$f" .md)
        echo "Procesando simple: $f"
        git mv "$f" "$dir/${base}.en.md"
    fi
done

# 2. CASO 2: Ficheros por fecha (Page Bundles)
# Buscamos archivos que empiecen por fecha YYYY-MM-DD
find . -type f -name "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]*.md" | while read -r f; do
    dir=$(dirname "$f")
    filename=$(basename "$f")

    # Caso A: Con idioma (ej: 2024-03-10.es.md)
    if [[ "$filename" =~ ^([0-9-]{10})\.([a-z]{2})\.md$ ]]; then
        date_folder="${BASH_REMATCH[1]}"
        lang="${BASH_REMATCH[2]}"

        mkdir -p "$dir/$date_folder"
        git mv "$f" "$dir/$date_folder/index.$lang.md"

    # Caso B: Sin idioma (ej: 2024-03-10.md)
    elif [[ "$filename" =~ ^([0-9-]{10})\.md$ ]]; then
        date_folder="${BASH_REMATCH[1]}"

        mkdir -p "$dir/$date_folder"
        git mv "$f" "$dir/$date_folder/index.md"
    fi
done

echo "--- Reorganización completada ---"