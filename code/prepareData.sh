#!/bin/bash
# author: Hendrik Werner s4549775

# Extract only relevant information. This includes the sentiment and the
# hashtags used for each tweet.
cut -d, -f1,3 --complement ../data/filteredHashtag.csv\
	| grep -Po "^[01],|#\w+"\
	| paste -d" "\
	| sed -r "s/ ([01],)/\n\1/g"\
	> ../data/prepared.csv
