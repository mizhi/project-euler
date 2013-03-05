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
# It can be seen that there are 3 fractions between 1/3 and 1/2.
#
# How many fractions lie between 1/3 and 1/2 in the sorted set of
# reduced proper fractions for d 10,000?



from math import sqrt, floor, ceil
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


def getprimes(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x !=0]

maxd = 10000

min_factr = 1.0 / 3.0
max_factr = 1.0 / 2.0

primeset=set(getprimes(maxd))

nums = 0
for d in xrange(1, maxd + 1):
    if d % 1000 == 0: print d
    minn = int(ceil(min_factr * d)) 
    maxn = int(floor(max_factr * d))

    for n in xrange(minn, maxn + 1):
        r = float(n) / float(d)
        if r > min_factr and r < max_factr:
            if n in primeset or d in primeset:
                nums += 1
            elif bingcd(n, d) == 1:
                nums += 1

print nums
