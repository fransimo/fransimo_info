#!/usr/bin/env bash

SRC_LANG="Spanish"
SRC_SUFFIX="es"
CONTENT_DIR="content/"
OLD_TAG="2026.1.4"
NEW_TAG="2026.1.5"

invalidate_translations_since_tag() {
  local tag="$1"
  shift
  local target_langs=("$@")

  if ! git rev-parse "$tag" >/dev/null 2>&1; then
    echo "ERROR: tag '$tag' does not exist" >&2
    return 1
  fi

  echo "Invalidating translations for source files ahead of tag: $tag"

  git diff --name-only "$tag"..HEAD -- "$CONTENT_DIR" \
    | grep -E '\.md$' \
    | while read -r file; do

        local base dir filename stem

        filename="$(basename "$file")"
        dir="$(dirname "$file")"

        # ---- source-language filter ----
        case "$SRC_SUFFIX" in
          en)
            case "$filename" in
              index.md|_index.md|index.en.md|_index.en.md) ;;
              *) continue ;;
            esac
            ;;
          *)
            case "$filename" in
              index.$SRC_SUFFIX.md|_index.$SRC_SUFFIX.md) ;;
              *) continue ;;
            esac
            ;;
        esac

        echo "Source changed: $file"

        # ---- compute stem (index / _index) ----
        if [[ "$filename" == _index* ]]; then
          stem="_index"
        else
          stem="index"
        fi

        # ---- delete translations ----
        for lang in "${target_langs[@]}"; do
          local translated="$dir/$stem.$lang.md"

          if [[ -f "$translated" ]]; then
            echo "  removing $translated"
            rm "$translated"
          fi
        done
    done
}

invalidate_translations_since_tag $OLD_TAG en ca it

./translate-hugo.sh content/ Spanish English es en
./translate-hugo.sh content/ Spanish Catalan es ca
./translate-hugo.sh content/ English Italian en it

#git commit -am "Update translations"
#git tag $NEW_TAG