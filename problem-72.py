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
# It can be seen that there are 21 elements in this set.
#
# How many elements would be contained in the set of reduced proper
# fractions for d <= 1,000,000?

from math import sqrt, floor
import sys

def getprimes(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x !=0]

maxd = 1000000
primes=getprimes(maxd)
primeset=set(primes)

def primefactorization(n, cache={}):
    global primes, primeset
    
    if n == 1:
        return {1:1}

    if n in cache:
        return cache[n]

    if n in primeset:
        cache[n] = {n:1}

    # we know that at least one of these
    # primes must divide n if we're here
    for p in primes:
        if n % p == 0:
            res = primefactorization(n / p).copy()
            if p not in res:
                res[p] = 0
            res[p] += 1
            cache[n] = res
            return res

def totient(n):
    if n == 1:
        return 1

    pfact = primefactorization(n)
    rp = 1.0
    for p in pfact.keys():        
        if p != 1:
            rp = rp * (1 - 1.0/float(p))
        
    rp *= n
    
    return rp
    


count = 0
for d in xrange(1, maxd + 1):
    if d % 100000 == 0: print '*'
    count += totient(d)

print count - 1
