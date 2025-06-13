# Hisorty

- Use wordpress pligin to export site
  - https://github.com/benbalter/wordpress-to-jekyll-exporter  ( <= this works! )
  - https://github.com/SchumacherFM/wordpress-to-hugo-exporter ( <= this FAILS! )
- import https://gohugo.io/commands/hugo_import/
```
hugo import jekyll /Users/fran/Downloads/export fransimo_info_v3
```

# clone

git clone git@github.com:fransimo/fransimo_info.git
git submodule update --init --recursive


# rendering with docker

https://hub.docker.com/r/klakegg/hugo/

## buid
docker run --rm -it \
  -v $(pwd):/src \
  klakegg/hugo:0.101.0-ext

## server 
docker run --rm -it \
  -v $(pwd):/src \
  -p 1313:1313 \
  klakegg/hugo:0.101.0-ext \
  server


# ipfs

w3 space info > space.info
w3 key create --json > ci-key.json
AUDIENCE=$(jq -r .did ci-key.json)
w3 delegation create $AUDIENCE -c space/blob/add -c space/index/add -c filecoin/offer -c upload/add --base64 > proof.key
W3_PROOF=$(cat proof.key )
w3 space add $W3_PROOF
