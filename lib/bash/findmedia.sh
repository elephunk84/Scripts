#!/bin/bash

cd /mnt/LOCAL/PrivStore/Videos/Clips
importfolder="/mnt/LOCAL/PrivStore/Videos/import"

function findmedia {
	find . -type f -name '*.flv' -exec cp -ruv {} "$importfolder" ';'
	find . -type f -name '*.mp4' -exec cp -ruv {} "$importfolder" ';'
}

echo "Finding Media"
findmedia
cd ${importfolder}
for file in *.flv
do 
	ffmpeg -i $file -acodec copy -vcodec copy ${file%.flv}.mp4 
	rm -rf ${file}
done
chmod 777 ./*
