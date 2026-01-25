#!/bin/bash

# Función para mover archivos con git mv
move_file() {
    local src=$1
    local dest=$2
    local dir=$(dirname "$dest")

    # Crear el directorio si no existe
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
    fi

    echo "Moviendo: $src -> $dest"
    git mv "$src" "$dest"
}

echo "--- Iniciando reorganización de archivos ---"

# CASO 1: Ficheros simples (index y _index)
# Buscamos archivos que sean exactamente index.md o _index.md
for f in index.md _index.md; do
    if [ -f "$f" ]; then
        # Extraemos el nombre base y añadimos .en.md
        base="${f%.md}"
        move_file "$f" "${base}.en.md"
    fi
done

# CASO 2: Ficheros por fecha (YYYY-MM-DD.md o YYYY-MM-DD.lang.md)
# Este regex busca patrones de fecha al inicio del nombre del archivo
for f in [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]*.md; do
    if [ -f "$f" ]; then
        # Caso A: Archivo de idioma específico (ej: 2024-03-10.es.md)
        if [[ $f =~ ^([0-9-]{10})\.([a-z]{2})\.md$ ]]; then
            folder="${BASH_REMATCH[1]}"
            lang="${BASH_REMATCH[2]}"
            move_file "$f" "${folder}/index.${lang}.md"

        # Caso B: Archivo principal/inglés (ej: 2024-03-10.md)
        elif [[ $f =~ ^([0-9-]{10})\.md$ ]]; then
            folder="${BASH_REMATCH[1]}"
            move_file "$f" "${folder}/index.md"
        fi
    fi
done

echo "--- Proceso finalizado ---"