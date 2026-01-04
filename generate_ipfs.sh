#!/usr/bin/env bash

rm -fR public/

docker run --rm -it \
  -v $(pwd):/src \
  -p 1313:1313 \
  -e HUGO_ENVIRONMENT=ipfs \
  hugomods/hugo:0.152.2 --gc --minify # --ignoreCache

rc=$?
if [[ $rc != 0 ]]; then
  echo Error during site generation
  exit $rc
fi

npx ipfs-car pack public --output build.car
rc=$?
if [[ $rc != 0 ]]; then
  echo Error during CAR generation
  exit $rc
fi

npx ipfs-car hash build.car > new_cid.txt

new_cid=` cat new_cid.txt `
old_cid=` cat old_cid.txt `
old_delete_cid=` cat old_delete_cid `

mv /tmp/build.car ~/ipfs/staging/

docker exec ipfs_host ipfs dag import /export/build.car
docker exec ipfs_host ipfs name publish --key=k51qzi5uqu5dhiu7v9v01yb6i69yu4luny793hwl19knqbqdgv97x7s949h0h1 --lifetime 48h --ttl 48h $new_cid
docker exec ipfs_host ipfs pin rm $old_delete_cid

cp old_cid.txt old_delete_cid.txt
cp new_cid.txt old_cid.txt