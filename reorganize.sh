#!/bin/bash

echo "--- Iniciando reorganización (Método Directo) ---"

# 1. SOLUCIÓN CASO 1: index.md -> index.en.md
# Usamos tu comando que sí funciona para obtener la lista
find . -type f \( -name "index.md" -o -name "_index.md" \) | grep -v "\.en\.md" | while read -r f; do
    # Filtro extra: No tocar si ya está en una carpeta con fecha (YYYY-MM-DD)
    if echo "$f" | grep -Eq "/[0-9]{4}-[0-9]{2}-[0-9]{2}/"; then
        continue
    fi

    dir=$(dirname "$f")
    base=$(basename "$f" .md)
    target="$dir/${base}.en.md"

    echo "Renombrando: $f -> $target"
    git mv "$f" "$target"
done

# 2. SOLUCIÓN CASO 2: Fecha.md -> Carpeta/index.md
# Buscamos archivos que tengan el patrón de fecha
find . -maxdepth 2 -type f -name "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]*" | while read -r f; do
    dir=$(dirname "$f")
    file=$(basename "$f")

    # Extraer fecha: los primeros 10 caracteres (YYYY-MM-DD)
    date_folder=$(echo "$file" | cut -c 1-10)

    # Extraer el resto: lo que hay después de la fecha
    # Ejemplo: .es.md o .md
    rest=$(echo "$file" | cut -c 11-)

    new_dir="$dir/$date_folder"
    mkdir -p "$new_dir"

    if [ "$rest" = ".md" ]; then
        dest="$new_dir/index.md"
    else
        # Si es .es.md, quitamos el punto inicial para que quede index.es.md
        lang_part=$(echo "$rest" | sed 's/^\.//')
        dest="$new_dir/index.$lang_part"
    fi

    echo "Moviendo: $f -> $dest"
    git mv "$f" "$dest"
done

echo "--- Proceso completado ---"