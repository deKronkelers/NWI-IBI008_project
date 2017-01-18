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
