#!/bin/bash

for file in *.jpg; do
  # Extraer la fecha de creación en formato YYYYMMDD usando exiftool
  date=$(exiftool -d "%Y%m%d" -DateTimeOriginal -S -s "$file" | awk '{print $1}')

  # Verificar si la variable date está vacía
  if [ -z "$date" ]; then
    echo "No se encontró fecha para $file, saltando..."
    continue
  fi

  # Extraer la extensión y el nombre base
  extension="${file##*.}"
  basename="${file%.*}"

  # Crear el nuevo nombre con la fecha al inicio
  newname="${date}_${basename}.${extension}"

  # Renombrar usando git mv
  git mv "$file" "$newname"

  echo "Renombrado: $file -> $newname"
done
