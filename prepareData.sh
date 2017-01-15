#!/bin/bash
# Extract only relevant information. This includes the sentiment and the
# hashtags used for each tweet.
cut -d, -f1,3 --complement data/filteredHashtag.csv\
	| grep -Po "^\d,|#\w+"\
	| tr "\n" " "\
	| sed -r "s/ ([01],)/\n\1/g"\
	> data/prepared.csv
