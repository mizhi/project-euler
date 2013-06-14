#!/usr/bin/env python

# Find the number of integers 1 n 107, for which n and n + 1 have the
# same number of positive divisors. For example, 14 has the positive
# divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

from math import sqrt
import sys

sieve=[0 for i in xrange(0,10**7)]
for i in xrange(2,len(sieve)):
    for j in xrange(i, len(sieve), i):
        sieve[j] += 1

print "Sieve done."

count = 0
for i in xrange(2, len(sieve) - 1):
    if sieve[i] == sieve[i+1]:
        count += 1

print count


sys.exit(0)


####
# naive method
def getprimes(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x !=0]


def divisors(n):
    divs=[1,n]
    i = 2
    maxn = sqrt(n)
    while i <= maxn:
        if n % i == 0:
            res = n / i
            divs.append(i)
            if i != res:
                divs.append(res)
        i += 1
    return divs

primes=getprimes(10**7)
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

def numdivs(n):
    pf = primefactorization(n)
    
    dn = 1
    for p,m in pf.items():
        if p != 1:
            dn *= (m + 1)

    return dn

numposdivs=0
lastndivs=None
for i in xrange(2, 10**7):
    if i in primeset:
        lastndivs=2
    else:
        newdivs=numdivs(i)
        if newdivs == lastndivs:
            numposdivs += 1
            print i, numposdivs
        lastndivs = newdivs

print "***", numposdivs
