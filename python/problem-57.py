#!/usr/bin/env python

# It is possible to show that the square root of two can
# be expressed as an infinite continued fraction.
#
# 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# By expanding this for the first four iterations, we get:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408,
# but the eighth expansion, 1393/985, is the first example
# where the number of digits in the numerator exceeds the number
# of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain
# a numerator with more digits than denominator?


def gen_fracs(n):
    fracs = [(1,1)]
    for i in xrange(1, n+1):
        last_frac = fracs[-1]
        new_frac = (2 * last_frac[1] + last_frac[0], last_frac[0] + last_frac[1])
        fracs.append(new_frac)

    return fracs

fracs = gen_fracs(1000)

count = 0
for i in xrange(0, 1001):
    frac = fracs[i]
    num = frac[0]
    den = frac[1]
    if len(str(num)) > len(str(den)):
        count += 1

print count

