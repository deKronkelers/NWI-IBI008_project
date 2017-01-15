#!/bin/bash
# author: Hendrik Werner s4549775

# Print statistics about the data
echo -n "Nr of tweets with hashtags: "
wc -l ../data/prepared.csv | cut -d" " -f1

echo -n "Nr of tweets with at least two hashtags: "
grep -P "(#\w+(.*)?){2,}" ../data/prepared.csv -c

sortedHashtags=$(grep -Po "#\w+" ../data/prepared.csv | sort | uniq -ic)

echo -n "Nr of unique hashtags: "
echo "$sortedHashtags" | wc -l

echo "10 Most used hashtags:"
echo "$sortedHashtags" | sort -rg | head -n10
