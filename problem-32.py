#!/usr/bin/env python

# The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from math import sqrt
import sys
import random

def pandigital(o1, o2, p):
    ds=set([str(d) for d in xrange(1, 10)])
    
    for d in str(o1):
        if d in ds:
            ds.remove(d)
        else:
            return False

    for d in str(o2):
        if d in ds:
            ds.remove(d)
        else:
            return False

    for d in str(p):
        if d in ds:
            ds.remove(d)
        else:
            return False

    return len(ds) == 0

pds=[]
for i in xrange(1,10000):
    for j in xrange(1, i):
        p = i * j
        tlen = len(str(i)) + len(str(j)) + len(str(p))
        if tlen == 9: 
            if pandigital(i,j,p):
                if p not in pds:
                    pds.append(p)

print sum(pds)

