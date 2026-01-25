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
  local file="$1"

  # English: allow foo.md OR foo_en.md
  if [[ "$SRC_LANG" == "en" ]]; then
    [[ "$file" =~ \.md$ ]] && [[ ! "$file" =~ _[a-z]{2}\.md$ || "$file" =~ _en\.md$ ]]
  else
    [[ "$file" =~ _${SRC_LANG}\.md$ ]]
  fi
}

target_filename() {
  local file="$1"

  if [[ "$file" =~ _[a-z]{2}\.md$ ]]; then
    echo "${file%_*}_${TGT_SUFFIX}.md"
  else
    echo "${file%.md}_${TGT_SUFFIX}.md"
  fi
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

    ollama run "$MODEL" \
      "$(cat "$file")" \
      > "$out"
  fi
done < <(find "$CONTENT_DIR" -type f -name "*.md" -print0)

echo "Translation completed."
