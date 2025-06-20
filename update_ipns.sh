#!/bin/bash

curl -s https://fransimo.info/cid.txt -o new_cid.txt

new_cid=` cat new_cid.txt `
old_cid=` cat old_cid.txt `

# Compare the files
if ! cmp -s "$new_cid" "$old_cid"; then
    echo "CID has changed."
    echo $new_cid
    docker exec ipfs_host ipfs name publish --key=k51qzi5uqu5dhiu7v9v01yb6i69yu4luny793hwl19knqbqdgv97x7s949h0h1 --lifetime 48h --ttl 48h $new_cid
    cp "$NEW_FILE" "$OLD_FILE"
else
    echo "CID has not changed."
fi