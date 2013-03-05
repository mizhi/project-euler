#!/usr/bin/env python

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

primes=getprimes(10000000)
prime_set=set(primes)
max_prime = max(primes)

maxp_sum=1
maxp_sum_len=1

for i in xrange(len(primes)):
    newp_sum = primes[i]
    for j in xrange(i + 1, len(primes)):
        newp_sum += primes[j]
        if newp_sum > 1000000:
            break
        newp_sum_len = len(primes[i:j+1])
        if newp_sum_len >= maxp_sum_len:
            if newp_sum in prime_set:
                maxp_sum = newp_sum
                maxp_sum_len = newp_sum_len


print maxp_sum, maxp_sum_len
