#!/usr/bin/env python

# The number, 1406357289, is a 0 to 9 pandigital number because it is
# made up of each of the digits 0 to 9 in some order, but it also has
# a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this
# way, we note the following:
#
#     * d2d3d4=406 is divisible by 2
#     * d3d4d5=063 is divisible by 3
#     * d4d5d6=635 is divisible by 5
#     * d5d6d7=357 is divisible by 7
#     * d6d7d8=572 is divisible by 11
#     * d7d8d9=728 is divisible by 13
#     * d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.
def chooseperm(s, length):
    """Finds all the substrings of length length that are created by
    characters in s"""
    if length == 1:
        return [c for c in s]
    else:
        rets=[]

        for i in xrange(len(s)):
            char = s[i]
            news = s[:i] + s[i+1:]
            retsp = chooseperm(s, length - 1)
            rets.extend([char + p for p in retsp])

        return rets  

def pandigital(o1):
    ds=set([str(d) for d in xrange(0, 10)])
    
    for d in str(o1):
        if d in ds:
            ds.remove(d)
        else:
            return False

    return len(ds) == 0


ps=chooseperm("0123456789", 3)
pdivs = [17,13,11,7,5,3,2]

# build up a map of divisors and sets of 
# numbers
divmap={}
for p in ps:
    for pd in pdivs:
        if int(p) % pd == 0:
            if pd not in divmap:
                divmap[pd] = set()
            divmap[pd].add(p)

# incrementally builds a list of strings for which the
# substring divisibility property holds.
# These strings are not, however, guaranteed to be pandigital.
# and in fact, will not be, since the first digit will not have
# been placed on the number
workingset=None
for pd in pdivs:
    nd = divmap[pd]

    if not workingset:
        workingset = list(nd)
    else:        
        newset = []
        for wn in workingset:
            for n in nd:
                if n[-2:] == wn[:2]:
                    newset.append(n[0] + wn)
        workingset = newset

# this part builds the final list of pandigital numbers for which
# the substring divisibility property holds
numbers = [str(i) + w for i in xrange(1,10) for w in workingset if pandigital(str(i) + w)]

print sum([int(n) for n in numbers])
