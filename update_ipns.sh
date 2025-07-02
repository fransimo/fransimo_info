#!/bin/bash

cd /Volumes/Seagate_4T/syncthing/servers_scripts/ipfs

curl -s https://fransimo.info/cid.txt -o new_cid.txt

new_cid=` cat new_cid.txt `
old_cid=` cat old_cid.txt `

# Compare the files
if [ "$new_cid" != "$old_cid" ] ; then
    echo "CID has changed."
    echo $new_cid
    curl -s https://fransimo.info/build.car -o /tmp/build.car
    rm ~/ipfs/staging/build.car
    mv /tmp/build.car ~/ipfs/staging/
    /usr/local/bin/docker exec ipfs_host ipfs dag import /export/build.car
    /usr/local/bin/docker exec ipfs_host ipfs name publish --key=k51qzi5uqu5dhiu7v9v01yb6i69yu4luny793hwl19knqbqdgv97x7s949h0h1 --lifetime 48h --ttl 48h $new_cid
    cp new_cid.txt old_cid.txt
else
    echo "CID has not changed."
fi