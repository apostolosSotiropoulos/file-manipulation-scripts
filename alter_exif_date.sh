#!/bin/bash

for f in *.jpg
do
	# in case no exif exists add one:
	# jhead -mkexif $f
	jhead -ds2015:11:07 $f

done
