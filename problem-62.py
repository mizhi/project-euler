#!/usr/bin/env python

# The cube, 41063625 (3453), can be permuted to produce two other
# cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the
# smallest cube which has exactly three permutations of its digits
# which are also cube.
#
# Find the smallest cube for which exactly five permutations of its
# digits are cube.

from math import sqrt

# def permute(s):
#     if len(s) > 1:
#         r=[]
#         for i in range(len(s)):
#             r.extend([s[i] + rsi for rsi in permute(s[:i] + s[i+1:])])
#         return r
#     return [s]

cubes=[str(x**3) for x in xrange(1, 10000)]

print "Going through cubes"
perms={}
for c in cubes:
    cpl = list(c)
    cpl.sort()
    cps = "".join(cpl)
    if cps not in perms:
        perms[cps]=[]
    perms[cps].append(c)

print "Looking for 5"
for c in cubes:
    cpl = list(c)
    cpl.sort()
    cps = "".join(cpl)

    if len(perms[cps]) == 5:
        print c
        break
    
