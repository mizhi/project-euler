#!/usr/bin/env python

# A googol (10100) is a massive number: one followed by one-hundred
# zeros; 100100 is almost unimaginably large: one followed by
# two-hundred zeros. Despite their size, the sum of the digits in each
# number is only 1.

# Considering natural numbers of the form, ab, where a, b 100, what is
# the maximum digital sum?

max_sum = 0
for a in xrange(100):
    for b in xrange(100):
        n=a**b
        ds = sum([int(d) for d in str(n)])

        if ds > max_sum:
            max_sum = ds

print max_sum
