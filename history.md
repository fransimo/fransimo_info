# Hisorty

- Use wordpress pligin to export site
  - https://github.com/benbalter/wordpress-to-jekyll-exporter  ( <= this works! )
  - https://github.com/SchumacherFM/wordpress-to-hugo-exporter ( <= this FAILS! )
- import https://gohugo.io/commands/hugo_import/
```
hugo import jekyll /Users/fran/Downloads/export fransimo_info_v3
```


# redering with docker

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
