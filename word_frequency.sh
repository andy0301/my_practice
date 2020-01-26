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
# Your script should output the following, sorted by descending frequency:
#   the 4
#   is 3
#   sunny 2
#   day 1

 # finally use awk '{print | "$1 sort -r"}' print out the results sorted by descending frequency number
cat words.txt | while read line;do echo $line | awk '{for(i=1;i<=NF;i++) print $i}' ;done | sort | uniq -c | awk '{print |"$1 sort -r"}' | awk '{print $2" "$1}'