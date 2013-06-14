#!/usr/bin/env python

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


ns = range(1,101)
sqns = [n * n for n in ns]

ns_sum = sum(ns)
sqns_sum = sum(sqns)

diff = (ns_sum * ns_sum) - sqns_sum

print diff
