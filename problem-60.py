#!/usr/bin/env python

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any
# two primes and concatenating them in any order the result will
# always be prime. For example, taking 7 and 109, both 7109 and 1097
# are prime. The sum of these four primes, 792, represents the lowest
# sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two
# primes concatenate to produce another prime.

import sys
from math import sqrt, log, ceil

def getprimes(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x !=0]

def prime(n):
    if n % 2 == 0:
        return False
    
    for i in xrange(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


n=10**7
maxp = 10**(ceil(log(n, 10) / 2))

primes = [p for p in getprimes(n)]
primeset = set(primes)

cprimes = [p for p in primes if int(p) <= maxp]

def catprime(n1, n2):
    global primeset, primes
    ns1 = str(n1)
    ns2 = str(n2)
    t1 = int(ns1 + ns2)
    t2 = int(ns2 + ns1)

    tprime1 = None
    tprime2 = None

    if t1 > primes[-1]:
        tprime1 = prime(t1)
    else:
        tprime1 = t1 in primeset

    if t2 > primes[-1]:
        tprime2 = prime(t2)
    else:
        tprime2 = t2 in primeset

    return tprime1 and tprime2

def allcatprimes(cp, n):
    global primeset

    for i in cp:
        if i != n and not catprime(i, n):
                return False
    return True


wlist = []
sols=[]
for i in xrange(len(cprimes)):
    wlist.append(cprimes[i])
    for j in xrange(i+1, len(cprimes)):
        if allcatprimes(wlist, cprimes[j]):
            wlist.append(cprimes[j])
            for k in xrange(j+1, len(cprimes)):
                if allcatprimes(wlist, cprimes[k]):
                    wlist.append(cprimes[k])
                    for l in xrange(k+1, len(cprimes)):
                        if allcatprimes(wlist, cprimes[l]):
                            wlist.append(cprimes[l])
                            for m in xrange(l+1, len(cprimes)):
                                if allcatprimes(wlist, cprimes[m]):
                                    wlist.append(cprimes[m])
                                    print '===========', wlist, sum([int(p) for p in wlist])
                                    sols.append(wlist[:])
                                    wlist.pop()
                            wlist.pop()
                    wlist.pop()
            wlist.pop()
    wlist.pop()

print sols
