#!/usr/bin/env python

# The first known prime found to exceed one million digits was
# discovered in 1999, and is a Mersenne prime of the form 269725931;
# it contains exactly 2,098,960 digits. Subsequently other Mersenne
# primes, of the form 2p1, have been found which contain more digits.
#
# However, in 2004 there was found a massive non-Mersenne prime which
# contains 2,357,207 digits: 2843327830457+1.
#
#
# Find the last ten digits of this prime number.

n=1
for i in xrange(7830457):
    n <<= 1
    n %= 10000000000

n = 28433 * n + 1

print str(n)[-10:]
