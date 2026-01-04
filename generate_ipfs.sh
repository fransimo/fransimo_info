#!/usr/bin/env bash

rm -fR public/

docker run --rm -it \
  -v $(pwd):/src \
  -p 1313:1313 \
  -e HUGO_ENVIRONMENT=ipfs \
  hugomods/hugo:0.152.2 --gc --minify # --ignoreCache