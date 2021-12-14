#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def wordcount(filepath):

    # open the file and get the words in the file

    with open(filepath) as f:
        wordlist = f.read().split()
        wordlist.sort()
        worddict = {}
        for word in wordlist:
            worddict[word] = wordlist.count(word)


        newlist = sortwords(list(worddict.keys()),worddict)
        space = len(newlist[0])
        for word in newlist:
            space = max(space,len(word))

        for word in newlist:
            print(word + ':' + ' ' * (space-len(word)+1) + '*' * worddict[word])


def sortwords(wordlist, dict):
    wordlist.sort()
    length = len(wordlist)
    for i in range(length, 1, -1):
        for j in range(1,i):
            if dict[wordlist[j]] > dict[wordlist[j - 1]]:
                temp = wordlist[j]
                wordlist[j] = wordlist[j - 1]
                wordlist[j - 1] = temp
    return wordlist

if __name__ == '__main__':
    wordcount('../files/test3')