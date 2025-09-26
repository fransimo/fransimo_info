#!/usr/bin/env bash
set -euo pipefail

# Usage: ./emit_pictures.sh '20*.jpg'
# If no pattern is given, defaults to '20*.jpg'
pattern="${1:-20*.jpg}"

# Find matching files in the current directory (not recursive), sort them,
# and print Hugo picture shortcodes with the filename as src.
# Handles spaces and special chars safely.
find . -maxdepth 1 -type f -iname "$pattern" -print0 \
  | sort -z \
  | while IFS= read -r -d '' f; do
      printf '  {{< picture src="%s" >}}\n' "$(basename "$f")"
    done
