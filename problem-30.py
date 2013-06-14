#!/usr/bin/env python

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#     1634 = 1^4 + 6^4 + 3^4 + 4^4
#     8208 = 8^4 + 2^4 + 0^4 + 8^4
#     9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1^4 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def build_power_cache(power):
    retc={}
    for i in xrange(10):
        retc[i] = i**power
    return retc

power_cache = build_power_cache(5)

t=0
for j in range(10, 30*power_cache[9] + 1):        
    sumpows = sum([power_cache[int(d)] for d in str(j)])
    if j == sumpows:
        t += j

print t
