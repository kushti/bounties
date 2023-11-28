#!/bin/sh

token=`cat ../secrets/token.txt`

rm ../data/$3.csv

githubCsvTools -t $token -o $1 -r $2 -f $3-temp.csv -a number,title,labels

csvgrep -c labels -r "B-|Bounty" $3-temp.csv > $3-labels.csv

./labels-strip.py $3-labels.csv > $3.csv

rm $3-labels.csv

rm $3-temp.csv

mv $3.csv ../data/$3-raw.csv

csvjoin --left -c number ../data/$3-raw.csv ../data/paid/$3-paid.csv > ../data/$3.csv

rm ../data/$3-raw.csv