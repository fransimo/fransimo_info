#!/usr/bin/env bash
set -euo pipefail

# -----------------------------
# Usage
# -----------------------------
if [[ $# -ne 4 ]]; then
  echo "Usage: $0 <content_dir> <source_lang> <target_lang> <target_suffix>"
  echo "Example: $0 content en ca ca"
  exit 1
fi

CONTENT_DIR="$1"
SRC_LANG="$2"
TGT_LANG="$3"
TGT_SUFFIX="$4"

MODEL="gpt-oss-hugo-translate"

export OLLAMA_VARS_source_language="$SRC_LANG"
export OLLAMA_VARS_target_language="$TGT_LANG"


# -----------------------------
# File selection logic
# -----------------------------
is_source_file() {
  local file
  file="$(basename "$1")"

  case "$SRC_LANG" in
    en)
      [[ "$file" == "index.md" ]] ||
      [[ "$file" == "_index.md" ]] ||
      [[ "$file" == "index.en.md" ]] ||
      [[ "$file" == "_index.en.md" ]]
      ;;
    es)
      [[ "$file" == "index.es.md" ]] ||
      [[ "$file" == "_index.es.md" ]]
      ;;
    *)
      [[ "$file" == "index.${SRC_LANG}.md" ]] ||
      [[ "$file" == "_index.${SRC_LANG}.md" ]]
      ;;
  esac
}

target_filename() {
  local file base
  base="$(basename "$1")"

  case "$base" in
    index.md|index.en.md|index.es.md)
      echo "$(dirname "$1")/index.${TGT_SUFFIX}.md"
      ;;
    _index.md|_index.en.md|_index.es.md)
      echo "$(dirname "$1")/_index.${TGT_SUFFIX}.md"
      ;;
    *)
      echo "ERROR: unexpected filename $base" >&2
      return 1
      ;;
  esac
}


# -----------------------------
# Translation loop
# -----------------------------
while IFS= read -r -d '' file; do
  if is_source_file "$file"; then
    out="$(target_filename "$file")"

    if [[ -f "$out" ]]; then
      echo "Skipping existing: $out"
      continue
    fi

    echo "Translating: $file → $out"

    # ollama run "$MODEL" --vars "source_language=$SRC_LANG,target_language=$TGT_LANG" < $file > "$out"

    ollama run "$MODEL" <<EOF > "$out"
SOURCE LANGUAGE: $SRC_LANG
TARGET LANGUAGE: $TGT_LANG

$(cat "$file")
EOF

  else
    echo "$file"
  fi
done < <(find "$CONTENT_DIR" -type f -name "*.md" -print0)

echo "Translation completed."
