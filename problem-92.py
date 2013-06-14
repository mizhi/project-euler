#!/usr/bin/env python

# A number chain is created by continuously adding the square of the
# digits in a number to form a new number until it has been seen
# before.
#
# For example,
#
# 44 32 13 10 1 1
# 85 89 145 42 20 4 16 37 58 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an
# endless loop. What is most amazing is that EVERY starting number
# will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?


def dsqsum(n):
    rs=0
    ds=str(n)
    for d in ds:
        rs += int(d)**2
    return rs

def nchain(n, cache={}):
    scn = cn = dsqsum(n)
    
    while True:
        if cn == 89 or cn == 1:
            cache[scn] = cn
            return cache[scn]

        if cn in cache:
            cache[scn] = cache[cn]
            return cache[cn]

        cn = dsqsum(cn)

count = 0
for i in xrange(1, 10**7):
    if nchain(i) == 89:
        count += 1


print count
