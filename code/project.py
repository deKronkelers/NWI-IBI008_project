# author: Hendrik Werner s4549775
from collections import namedtuple

Tweet = namedtuple("DataPoint", ["sentiment", "hashtags"])

data = []

# Load the prepared data set
for line in open("../data/prepared.csv"):
    split_line = line.strip().split(sep=", ")
    data.append(Tweet(
        int(split_line[0])
        , set(split_line[1].split())
    ))

# Remove outliers from the data set
unique_hashtags = set()
for line in open("../data/hashtagsUsedInSingleTweet.txt"):
    unique_hashtags.add(line.strip())

for tweet in data:
    tweet.hashtags.difference_update(
        {h for h in tweet.hashtags if h in unique_hashtags}
    )

data = list(filter(lambda d: d.hashtags, data))
