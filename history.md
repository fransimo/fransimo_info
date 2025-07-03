# Hisorty

- Use wordpress plugin to export site
  - https://github.com/benbalter/wordpress-to-jekyll-exporter  ( <= this works! )
  - https://github.com/SchumacherFM/wordpress-to-hugo-exporter ( <= this FAILS! )
- import https://gohugo.io/commands/hugo_import/
```
hugo import jekyll /Users/fran/Downloads/export fransimo_info_v3
```

# git clone

git clone git@github.com:fransimo/fransimo_info.git
git submodule update --init --recursive

# git security

[gitleaks](https://github.com/gitleaks/gitleaks)

brew install gitleaks  
gitleaks git -v .


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

# ipns

docker exec ipfs_host ipfs key gen fransimo_info
docker exec ipfs_host ipfs key export fransimo_info  --output=/export/fransimo_info.ipfs.key

# Key import
docker exec ipfs_host ipfs key import fransimo_info fransimo_info.ipfs.key

$ cp fransimo_info.ipfs.key ~/ipfs/staging/
$ docker exec ipfs_host ipfs key import fransimo_info /export/fransimo_info.ipfs.key

# ipns update

docker exec ipfs_host ipfs name publish --key=k51qzi5uqu5dhiu7v9v01yb6i69yu4luny793hwl19knqbqdgv97x7s949h0h1 --lifetime 48h --ttl 48h /ipfs/bafybeihqhzaiuxsgqtinuueuiqdhnvfixsfqiv3s72eecvb5zmcjxdkksq

