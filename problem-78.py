#!/usr/bin/env python


import sys
def eulerTransform(n, cache={0:1}):
    if n < 0:
        return 0

    if n in cache:
        return cache[n]

    s=0
    for k in xrange(1, n+1):
        sign = (-1)**(k+1)
        et1 = eulerTransform(n - (k*(3*k-1) >> 1))
        et2 = eulerTransform(n - (k*(3*k+1) >> 1))
        s += sign * (et1 + et2)
        # this speeds up the computation A LOT.
        if et1 <= 0: 
            break

    cache[n] = s % 10**7

    return cache[n]

n = 1
while True:
    parts=eulerTransform(n)
    print n, parts

    if parts % 1000000 == 0:
        break
    n += 1

print n
