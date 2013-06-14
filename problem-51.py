#!/usr/bin/env python


# By replacing the 1^(st) digit of *3, it turns out that six of the
# nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3^(rd) and 4^(th) digits of 56**3 with the same
# digit, this 5-digit number is the first example having seven primes
# among the ten generated numbers, yielding the family: 56003, 56113,
# 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the
# first member of this family, is the smallest prime with this
# property.
#
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an
# eight prime value family.
from math import sqrt
import re
import sys

def getprimes(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x !=0]

def group_primes(ps):
    group_dict = {}
    for p in ps:
        pk = len(str(p))
        if not group_dict.has_key(pk):
            group_dict[pk] = []
        group_dict[pk] += [p]
    return group_dict

primes = getprimes(10000000)
prime_groups = group_primes(primes)
del prime_groups[1], prime_groups[2], prime_groups[3], prime_groups[4], prime_groups[5]

candidates=[]
candidates_rexes=[]
for prime in prime_groups[6]:
    prime_str = str(prime)

    for i in xrange(0, 10):
        i_str = str(i)
        if prime_str.count(i_str, 0, len(prime_str)) >= 3:
            prime_str_m = prime_str.replace(i_str, r'(\d)', 1)
            prime_str_m = prime_str_m.replace(i_str, r'(\1)')
            candidates.append(int(prime_str))
            candidates_rexes.append(re.compile(prime_str_m))

for i in xrange(len(candidates)):
    count = 1
    c_rex = candidates_rexes[i]
    for j in xrange(len(candidates)):
        if i != j:
            if c_rex.match(str(candidates[j])):
                count += 1

                if count == 8:
                    print candidates[i]
                    sys.exit()
