#!/bin/bash
# author: Hendrik Werner s4549775

# Extract only relevant information. This includes the sentiment and the
# hashtags used for each tweet.
cut -d, -f2,4- ../data/filteredHashtag.csv\
	| grep -Po "^[01],|#\w+"\
	| paste -sd" "\
	| sed -r "s/ ([01],)/\n\1/g"\
	> ../data/prepared.csv
