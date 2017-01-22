# author: Hendrik Werner s4549775
import random

import nltk.classify.util
from collections import namedtuple
from nltk.classify import NaiveBayesClassifier, maxent
from sklearn.model_selection import train_test_split

Tweet = namedtuple("DataPoint", ["sentiment", "hashtags"])

data = []

# Load the prepared data set
for line in open("../data/prepared.csv"):
    split_line = line.strip().split(sep=", ")
    data.append(Tweet(
        int(split_line[0])
        , set(split_line[1].lower().split())
    ))

# Remove outliers from the data set
unique_hashtags = set()
for line in open("../data/hashtagsUsedInSingleTweet.txt"):
    unique_hashtags.add(line.strip().lower())

for tweet in data:
    tweet.hashtags.difference_update(
        {h for h in tweet.hashtags if h in unique_hashtags}
    )

data = filter(lambda d: d.hashtags, data)


# Train classifiers

# Extract a feature set containing the hashtags from a tweet
def tweet_features(tweet: Tweet):
    return dict.fromkeys(tweet.hashtags, True)


labeled_tweets = [(tweet_features(t), t.sentiment) for t in data]
train, test = train_test_split(labeled_tweets)

classifier = NaiveBayesClassifier.train(train)
print("Naive Bayes accuracy:", nltk.classify.accuracy(classifier, test))
classifier.show_most_informative_features()

max_ent = maxent.MaxentClassifier.train(train, max_iter=10)
print("Maxent accuracy:", nltk.classify.accuracy(max_ent, test))
max_ent.show_most_informative_features()
