#!/bin/bash
# author: Hendrik Werner s4549775

# Print statistics about the data
echo -n "Nr of tweets with hashtags: "
wc -l ../data/prepared.csv | cut -d" " -f1

echo -n "Nr of tweets with at least two hashtags: "
grep -P "#\w+.*?#\w+" ../data/prepared.csv -c

echo -n "Nr of tweets that contain the same hashtag at least twice: "
grep -iP "(#\w+\b).*?\1\b" ../data/prepared.csv -c

sortedHashtags=$(grep -Po "#\w+" ../data/prepared.csv | sort)
sortedHashtagsFreq=$(echo "$sortedHashtags" | uniq -ic)

echo -n "Nr of unique hashtags: "
wc -l <<< "$sortedHashtagsFreq"

echo -n "Nr of hashtags only used once: "
grep "^\s*1 " -c <<< "$sortedHashtagsFreq"

echo "10 Most used hashtags:"
sort -rg <<< "$sortedHashtagsFreq" | head -n10

# Write some statistics to disk to plot them
awk '{print length}' <<< "$sortedHashtags" | sort -g | uniq -c\
	> ../data/stats/hashtagFrequencyLength.txt

uniq -i <<< "$sortedHashtags" | awk '{print length}' | sort -g | uniq -c\
	> ../data/stats/hashtagFrequencyLengthNoDup.txt