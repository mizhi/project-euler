#!/usr/bin/env python

# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2x7
# 15 = 3x5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2**2x7x23
# 645 = 3x5x43
# 646 = 2x17x19.
#
# Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?

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

min_n = 10
max_n = 1000000
primes = getprimes(max_n)
prime_set = set(primes)
print "Got primes..."

found_f = []
found_f_dict = {}

def primefactorization(n):
    global primes, prime_set, found_f, found_f_dict

    res={}
    q = n
    
    # first thing we do is look for the factorization in our cache
    if n in found_f_dict:
        return found_f_dict[n]

    for i in found_f:
        if n % i == 0:
            res = found_f_dict[i].copy()
            q = q / i
            break

    while q > 1:
        if q in prime_set:
            if q not in res:
                res[q] = 0
            res[q] += 1
            q = q / q
        else:
            j = 0
            while primes[j] <= sqrt(q):
                p = primes[j]
                if q % p == 0:
                    q = q / p
                    if p not in res:
                        res[p] = 0
                    res[p] += 1
                    break
                j += 1
    
    found_f.insert(0, n)
    found_f_dict[n] = res
    
    return res

nonprime_regions = []
working_set = []
for i in xrange(min_n, max_n):
    if i in prime_set:
        if len(working_set) > 3:
            nonprime_regions.append(working_set)
        working_set = []
    else:
        working_set.append(i)

print "Computed working sets...", len(nonprime_regions)

four_fact_nums = []
i = 0
while len(four_fact_nums) != 4 and i < len(nonprime_regions):
    working_set = nonprime_regions[i]

    four_fact_nums = []
    j = 0
    while len(four_fact_nums) != 4 and j < len(working_set):
        pfact = primefactorization(working_set[j])

        if len(pfact.keys()) == 4:
            four_fact_nums.append(working_set[j])
        else:
            four_fact_nums = []

        if len(four_fact_nums) == 4:
            break
        
        j += 1
              

    if len(four_fact_nums) >= 2:
        print i, len(four_fact_nums)

    if len(four_fact_nums) == 4:
        break

    i += 1
    if i % 100 == 0: 
        print "Working set: ", i, max(working_set)

print four_fact_nums
