#!/usr/bin/env python

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom
# right diagonal, but what is more interesting is that 8 out of the 13
# numbers lying along both diagonals are prime; that is, a ratio of
# 8/13 62%.
#
# If one complete new layer is wrapped around the spiral above, a
# square spiral with side length 9 will be formed. If this process is
# continued, what is the side length of the square spiral for which
# the ratio of primes along both diagonals first falls below 10%?


import sys
from math import sqrt
import random

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

def probablyprime(n,k, rand=random.Random()):
    for i in xrange(0,k):
        np = rand.randint(1, n-1)
        if np**(n-1) % n != 1:
            return False
    return True


def sumspiral(n):
    if n == 1:
        return 1
    else:
        nsq = n*n
        # edge = nsq + (nsq - (n-1)) + (nsq - (n-1) * 2) + (nsq - (n-1) * 3)
        edge = 4 * nsq - (6 * n) + 6
        return edge + sumspiral(n - 2)

def spiralpc(n, pset):
    """Returns a tuple of (#primes,#composite)
    """
    if n == 1:
        return (0, 1)
    else:
        rpc = spiralpc(n - 2, pset)
        return (rpc[0] + numprimes, rpc[1] + numcomposite)

n = 3
numprimes = 0
numcomposite = 1
primeset=set(getprimes(90000000))
maxp = max(primeset)
while True:
    maxn = n**2
#    if maxn >= maxp:      
#        maxp += 2000000
#        print "Getting %d primes..." % (maxp)
#        primeset = set(getprimes(maxp))
#        maxp = max(primeset)
#        print "Done."

    ns = [maxn - (n - 1) * i for i in xrange(0, 4)]
    
    if maxn >= maxp:
        numprimest = sum([1 for i in ns if prime(i)])
    else:
        numprimest = sum([1 for i in ns if i in primeset])

    numprimes += numprimest
    numcomposite += (4 - numprimest)
    
    r = float(numprimes) / (numprimes + numcomposite)
    print n, numprimes, numcomposite, r
    if r  < 0.10:
        break
    n += 2

print "*** ", n
