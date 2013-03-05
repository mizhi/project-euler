#!/usr/bin/env python

# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
# nCr = n!/(r!(n-r)!),where r n, n! = n(n1)...321, and 0! = 1.
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many values of  nCr, for 1 n 100, are greater than one-million?

def fact(n):
    prod=1
    for i in xrange(n, 1, -1):
        prod *= i
    return prod

def choose(n,r):
    return fact(n) / (fact(r) * fact(n - r))

greater_than_million = 0

for n in xrange(1, 100+1):
    for r in xrange(1, n):
        if choose(n,r) > 1000000:
            greater_than_million += n - 2*r + 1
            break

print greater_than_million
