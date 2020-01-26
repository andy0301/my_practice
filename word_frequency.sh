#!/bin/bash

###################
# Write a bash script to calculate the frequency of each
# word in a text file 'words.txt'
# you may assume:
# - words.txt contains only lowercase characters and space ' ' characters.
# - Each word must consist of lowercase characters only
# - Words are separated by one or more whitespace characters.
# example:
# the words.txt has the following content:
#    the day is sunny the the
#    the sunny is is

cat words.txt | while read line;do echo $line | awk '{for(i=1;i<=NF;i++) print $i}' | sed 's/ //g';done | sort | uniq -c | awk '{print $2" "$1}'