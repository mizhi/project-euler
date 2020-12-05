#!/usr/bin/env python

# We shall say that an n-digit number is pandigital if it makes use of
# all the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

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

def permute(s):
    if len(s) > 1:
        r=[]
        for i in range(len(s)):
            r.extend([s[i] + rsi for rsi in permute(s[:i] + s[i+1:])])
        return r
    return [s]


# trick is to use divisibility rules.
# 9+8+7+6+5+4+3+2+1=45 which is divisible by 3.  Thus there are no 9-digit pandigital primes
# 8+7+6+5+4+3+2+1=36 which is divisible by 3.  Thus there are no 8-digit pandigital primes
#
# 6+5+4+3+2+1=21 and the same rule applies.  There are no 6-digit pandigital primes
# 5+4+3+2+1=15.  Again, there are no 5-digit pandigital primes
#
# It is also the case that
# 3+2+1=6 so there are no 3 digit pandigital primes.
# 2+1=3 so, same rule applies.
#
# we are left with something that is easily brute forced the rest of the way.  We can
# actually speed it up significantly by removing the evens and those divisible by 3. 
primes = getprimes(7654321)
pdns=["7654321", "4321"]

for pdn in pdns:
    print pdn
    pansp=[int(i) for i in permute(pdn)]
    pans = [i for i in pansp if i % 2 != 0 and i % 3 != 0]

    pans.sort(reverse=True)
    
    print "Searching..."
    for p in pans:
        if p in primes:
            print "Found: ", p
            break
