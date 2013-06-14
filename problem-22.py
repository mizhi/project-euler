#!/usr/bin/env python


# Using names.txt (right click and 'Save Link/Target As...'), a 46K
# text file containing over five-thousand first names, begin by
# sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
# list. So, COLIN would obtain a score of 938 53 = 49714.
#
# What is the total of all the name scores in the file?

import fileinput
import sys;

fi=fileinput.input(sys.argv[1])
names=[]
for line in fileinput.input():
    names=line.replace('"', '').split(',')
fi.close()

names.sort()

def char_value(c):
    return ord(c) - ord('A') + 1

def name_value(s):
    return sum([char_value(c) for c in s])

def name_score(nms, name):
    return name_value(name) * (nms.index(name) + 1)

print sum([name_score(names, name) for name in names])
