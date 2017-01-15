#!/bin/bash
# author: Hendrik Werner s4549775

grep -P "#\w+"\
	< ../data/SentimentAnalysisDataset.csv\
	> ../data/filteredHashtag.csv
