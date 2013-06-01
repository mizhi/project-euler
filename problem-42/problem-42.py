#!/usr/bin/env python

# The nth term of the sequence of triangle numbers is given by, tn =
# (1/2)n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word
# value. For example, the word value for SKY is 19 + 11 + 25 = 55 =
# t10. If the word value is a triangle number then we shall call the
# word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K
# text file containing nearly two-thousand common English words, how
# many are triangle words?

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

def tn(n):
    return (n * (n + 1)) / 2

def compute_tnseq(maxn):
    return [tn(n) for n in xrange(1,maxn + 1)]


name_values=[name_value(name) for name in names]
tnseq=set(compute_tnseq(20))

tnames = [nv for nv in name_values if nv in tnseq]

print len(tnames)
