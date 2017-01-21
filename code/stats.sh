#!/bin/bash
# author: Hendrik Werner s4549775

# Print statistics about the data
echo -n "Nr of tweets with hashtags: "
wc -l ../data/prepared.csv | cut -d" " -f1

echo -n "Nr of tweets with at least two hashtags: "
grep -P "#\w+.*?#\w+" ../data/prepared.csv -c

sortedHashtags=$(cut -d" " -f2- ../data/prepared.csv | tr " " "\n" | sort)
sortedHashtagsFreq=$(echo "$sortedHashtags" | uniq -ic)

echo -n "Nr of distinct hashtags: "
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

for nr in {2..20}; do
	echo "$nr $(grep -P "(#\w+\b.*?){$nr}" ../data/prepared.csv -c)"
done > ../data/stats/hashtagFrequenciesCount.txt

for nr in {1..20}; do
	echo "$nr $(grep -iP "(#\w+\b)(.*?\1\b){$nr}" ../data/prepared.csv -c)"
done > ../data/stats/hashtagRepetitionsCount.txt
