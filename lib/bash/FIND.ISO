#!/bin/bash

dirs=("/media/NFS/Software/Win_ISO/" "/media/NFS/Software/Linux_ISO/")
isofolder="/media/NFS/Software/template/iso/"

function findISO {
	find . -type f -name '*.iso' -exec cp -ruv {} "$isofolder" ';'
	find . -type f -name '*.ISO' -exec cp -ruv {} "$isofolder" ';'
}

echo "Finding ISO"
for dir in "${dirs[@]}"
do
	cd "$dir"
	findISO
	cd
done
