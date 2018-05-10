#!/bin/bash
# say we need to add .mp4 to all extentionless files under /home/foo
# 	copy script to /home/foo
#	/home/foo/addFileExtentionsToCurrentFolderFiles.s mp4
# 	rm /home/foo/addFileExtentionsToCurrentFolderFiles.sh
 
parentdir="$(dirname "$0")"
cd $parentdir

for filename in * ; do
	if [[ $filename != *.* ]]
	then
		mv "$filename" "$filename.$1"
	fi
done