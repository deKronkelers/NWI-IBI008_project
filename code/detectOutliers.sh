#!/bin/bash
# author: Hendrik Werner s4549775

# Find hashtags that were only used in a single tweet.
cut -d" " -f2- ../data/prepared.csv | while read line; do
	tr " " "\n" <<< "$line" | sort -fu
done | sort -f | uniq -iu > ../data/hashtagsUsedInSingleTweet.txt
