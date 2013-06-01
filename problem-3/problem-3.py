#!/usr/bin/env python

# making a trivial change
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

from math import sqrt

def getprimes(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x !=0]


#n=13195
n=600851475143

primes = getprimes(int(sqrt(n)))

prime_factors=[p for p in primes if n % p == 0]

print prime_factors
