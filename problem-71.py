#!/usr/bin/env python

# Consider the fraction, n/d, where n and d are positive integers. If
# nd and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d 8 in ascending
# order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
# 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that 2/5 is the fraction immediately to the left of
# 3/7.
#
# By listing the set of reduced proper fractions for d 1,000,000 in
# ascending order of size, find the numerator of the fraction
# immediately to the left of 3/7.

from math import sqrt, floor
import sys

def bingcd(u,v):
    shift = 0

    if u == 0 or v == 0:
        return u|v
    
    while (u|v) & 1 == 0:
        u >>= 1
        v >>= 1
        shift += 1

    while (u & 1) == 0:
        u >>= 1

    while (v & 1) == 0:
        v >>= 1

    if u < v:
        v -= u
    else:
        diff = u - v
        u = v
        v = diff
    
    v >>= 1

    while v != 0:
        while (v & 1) == 0:
            v >>= 1
        
        if u < v:
            v -= u
        else:
            diff = u - v
            u = v
            v = diff
    
        v >>= 1

    return u << shift

maxd = 1000000
pfact = (2, 7) # represents the best guess
pfactr = float(pfact[0]) / float(pfact[1])

for d in xrange(maxd, 0, -1):
    maxn = int((3.0/7.0) * d)
    minn = int(pfactr * d)

    for n in xrange(maxn, minn-1, -1):
        if bingcd(n,d) == 1:
            newpfactr = float(n) / float(d)
            # a closer ratio means it's nearer 3/7
            if newpfactr > pfactr and newpfactr < 3.0/7.0:
                print "Setting new pfactr (new: %f, old: %f) for (n: %d, d: %d)" % (newpfactr, pfactr, n, d)
                pfact = (n, d)
                pfactr = newpfactr

print pfact, pfactr, 3.0/7.0
