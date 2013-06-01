#!/usr/bin/env python

# n! means n  (n  1)  ...  3  2  1
#
# Find the sum of the digits in the number 100!

def fact(n):
    prod=1
    for i in xrange(n, 1, -1):
        prod *= i
    return prod

print sum([int(d) for d in str(fact(100))])
