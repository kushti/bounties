#!/bin/sh

token=`cat ../secrets/token.txt`

rm node.csv

githubCsvTools -t $token -o $1 -r $2 -f $3-temp.csv -a number,title,labels

csvgrep -c labels -r "B-|Bounty" $3-temp.csv > $3.csv

rm $3-temp.csv

mv $3.csv ../data/$3.csv