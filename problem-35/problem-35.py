#!/usr/bin/env python

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

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

def rotations(n):
    digits=list(str(n))
    rs=[]

    digits_len = len(digits)
    for i in xrange(0, digits_len):
        d=digits.pop(0)
        digits.append(d)
        rs.append(int("".join(digits)))

    return rs

def all_prime(ns, ps):
    for n in ns:
        if n not in ps:
            return False
    return True

ps = set(getprimes(1000000))

cps=[]
for i in ps:
    if all_prime(rotations(i), ps):
        cps.append(i)

print cps, len(cps)
