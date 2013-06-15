#!/usr/bin/env python

# making a trivial change
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

from math import sqrt
import itertools

from primes import infsieve

#n=13195
n=600851475143

max_n = int(sqrt(n))
print max(itertools.ifilter(lambda x: n % x == 0,
                            itertools.takewhile(lambda x: x <= max_n,
                                                infsieve())))
