#!/usr/bin/env python


# The number 3797 has an interesting property. Being prime itself, it
# is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
# work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

def trunctable(pnum, pset):
    if pnum in [2,3,5,7]:
        return False

    # easy case
    if pnum not in pset:
        return False

    # from left
    pnums=str(pnum)
    for i in xrange(len(pnums)):
        pq = int(pnums[i:])
        if pq not in pset:
            return False

    # from right
    for i in xrange(len(pnums), 0, -1):
        pq = int(pnums[:i])
        if pq not in pset:
            return False

    return True


ps = getprimes(1000000)
pset = set(ps)

tps = [p for p in ps if trunctable(p, pset)]

print tps
print sum(tps)
