#!/bin/bash
grep -P "#\w+" < data/SentimentAnalysisDataset.csv > data/filteredHashtag.csv
