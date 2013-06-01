#!/usr/bin/env python

# Euler published the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the
# consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41
# = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2
# + 41 + 41 is clearly divisible by 41.
#
# Using computers, the incredible formula n^2 - 79n + 1601 was
# discovered, which produces 80 primes for the consecutive values n =
# 0 to 79. The product of the coefficients, 79 and 1601, is 126479.
#
# Considering quadratics of the form:
#
#     n^2 + an + b, where |a| 1000 and |b| 1000
#
#     where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for
# consecutive values of n, starting with n = 0.
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

def makefun(a,b):
    return lambda n: (n*n) + (a*n) + b

psp = getprimes(1000)
psab = psp
psab.extend([-p for p in psp])

ps = set(getprimes(100000))

longesta = 0
longestb = 0
longestp = 0
for a in psab:
    for b in psab:
        f = makefun(a,b)
        n = 0
        while True:
            r = f(n)
            if r not in ps:
                break
            n += 1

        if n > longestp:
            print n, a, b
            longestp = n
            longesta = a
            longestb = b

print longestp, longesta, longestb, longesta * longestb
