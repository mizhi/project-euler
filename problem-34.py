#!/usr/bin/env python

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def fact(n):
    prod=1
    for i in xrange(n, 1, -1):
        prod *= i
    return prod

def sumfact(num, fd=None):
    if not fd:
        fd = {}
        for i in xrange(10):
            fd[str(i)] = fd[i] = fact(i)

    fs = 0
    for d in str(num):
        fs += fd[d]

    return fs

maxd = 99
sfmaxd = sumfact(maxd)

while maxd <= sfmaxd:
    maxd = maxd * 10 + 9
    sfmaxd = sumfact(maxd)

maxd = sfmaxd

ns = []
i = 3
while i < maxd:
    sf = sumfact(i)

    if i == sf:
        print i, sf
        ns.append(i)

    i += 1

print sum(ns)
