#!/usr/bin/env python

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2*1^2
# 15 = 7 + 2*2^2
# 21 = 3 + 2*3^2
# 25 = 7 + 2*3^2
# 27 = 19 + 2*2^2
# 33 = 31 + 2*1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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

primes = getprimes(10000)
squares = [x**2 for x in xrange(1,1000)]

def sum2timessquare(n):
    global primes, squares

    for sq in squares:
        if 2*sq >= n:
            break

        np = n - 2 * sq

        if np in primes:
            return True

    return False


for i in xrange(9, 10000, 2):
    if i in primes: 
        continue
    if not sum2timessquare(i):        
        print i
        break
