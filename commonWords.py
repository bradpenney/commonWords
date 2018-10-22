#!/home/brad/anaconda3/bin/python

# 100 Most Common Words in a Given Text
# Excluding the most 100 common words in the English language

# Author: Brad Penney
# Purpose: Count the words frequency in a given Text

import operator
import sys

# Count the number of time each word appears in a given text
# https://www.w3resources.com/python-exercises/string/python-data-type-string-exercise-12.php
def wordCount(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

# Sort the dictionary produced by wordCount
def generateDictionary(dict):
    rawList = dict
    sortedList = {}
    for kv in sorted(rawList.items(), key=operator.itemgetter(1), reverse=True):
        sortedList[kv[0]]=kv[1]

    sortedList = {key:val for key, val in sortedList.items() if val >= 10}

    return sortedList

# Print the finished result
def printList(dict):
    for i in finalList:
        print ('{:15}'.format(i), finalList[i])

# Remove various punctuation & 100 most common English words from text
def stringScrub(str):
    text = str
    text = text.strip('\"')
    text = text.strip('\'')
    text = text.strip(';')
    text = text.replace(',',' ')
    text = text.replace('.','')
    text = text.replace('_', ' ')
    text = text.replace('&', ' ')
    text = text.replace('*',' ')
    # 100 most common words in the English language according to Wikipedia

    with open('MostCommonEnglishWords', 'r') as wordList:
        commonList=wordList.read().splitlines()

        for x in commonList:
            text = text.replace(" "+x+" ",'')

    return text

###### Begin Program #####

textToEvaluate = str(sys.argv[1])

with open(textToEvaluate, 'r') as theText:
    bookText=theText.read().replace('\n','')

text = stringScrub(bookText)

rawDict = (wordCount(text))

finalList = generateDictionary(rawDict)

printList(finalList)
