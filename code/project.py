# author: Hendrik Werner s4549775
import nltk.classify.util
from collections import namedtuple
from nltk.classify import NaiveBayesClassifier

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
    unique_hashtags.add(line.strip())

for tweet in data:
    tweet.hashtags.difference_update(
        {h for h in tweet.hashtags if h in unique_hashtags}
    )

data = list(filter(lambda d: d.hashtags, data))


# Train a classifier

# Extract a feature set containing the hashtags from a tweet
def tweet_features(tweet: Tweet):
    return dict.fromkeys(tweet.hashtags, True)


labeled_tweets = [(tweet_features(t), t.sentiment) for t in data]
classifier = NaiveBayesClassifier.train(labeled_tweets)
print("Accuracy: ", nltk.classify.accuracy(classifier, labeled_tweets))
classifier.show_most_informative_features()
