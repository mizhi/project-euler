#!/usr/bin/env python

# Some positive integers n have the property that the sum [ n +
# reverse(n) ] consists entirely of odd (decimal) digits. For
# instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such
# numbers reversible; so 36, 63, 409, and 904 are reversible. Leading
# zeroes are not allowed in either n or reverse(n).

# There are 120 reversible numbers below one-thousand.

# How many reversible numbers are there below one-billion (109)?


from math import sqrt


def reverse(n):
    nl = list(str(n))
    nl.reverse()
    return int("".join(nl).lstrip("0"))

def allodd(n):
    for d in str(n):
        if int(d) in [0,2,4,6,8]:
            return False
    return True

num_rev = 0
for i in xrange(1, 1000000000):
    if str(i)[-1] != '0':
        ri = reverse(i)
        iri = i + ri
        if allodd(iri):
            num_rev += 1
            print i, ri, iri, num_rev
            

