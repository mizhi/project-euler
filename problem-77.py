#!/usr/bin/env python

# It is possible to write ten as the sum of primes in exactly five different ways:
#
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
#
# What is the first value which can be written as the sum of primes in
# over five thousand different ways?
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

def change_combos(n, coins = [200, 100, 50, 20, 10, 5, 2, 1]):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if len(coins) == 1 and n % coins[0] == 0:
        return 1

    if len(coins) == 0:
        return 0

    coin_used = coins[0]
    remaining_coins = coins[1:]

    canusemaxc = n / coin_used

    maxcpossibilities = [i * coin_used for i in xrange(0, canusemaxc + 1)]
        
    return sum([change_combos(n - p, remaining_coins) for p in maxcpossibilities])


primes = getprimes(5000)

primes.sort(reverse=True)

i = 10
while True:
    cc = change_combos(i, primes)
    print i, cc
    if cc > 5000:
        break
    i += 1


