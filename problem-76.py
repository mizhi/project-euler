#!/usr/bin/env python

# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?

import sys
from math import floor

def change_combos_mem(n, coins = [200, 100, 50, 20, 10, 5, 2, 1], cache={}):
    if n < 0:
        return 0
    if (n == 0) or (len(coins) == 1 and n % coins[0] == 0):
        return 1

    if (n,coins[0]) in cache:
        return cache[(n, coins[0])]

    coin_used = coins[0]
    remaining_coins = coins[1:]

    canusemaxc = n / coin_used

    maxcpossibilities = [i * coin_used for i in xrange(0, canusemaxc + 1)]
        
    final_sum = sum([change_combos_mem(n - p, remaining_coins) for p in maxcpossibilities])

    cache[(n,coin_used)] = final_sum

    return cache[(n,coin_used)]

def eulerTransform(n, cache={0:1}):
    if n < 0:
        return 0

    if n in cache:
        return cache[n]

    s=0
    for k in xrange(1, n+1):
        sign = (-1)**(k+1)
        et1 = eulerTransform(n - (k*(3*k-1) >> 1))
        et2 = eulerTransform(n - (k*(3*k+1) >> 1))
        s += sign * (et1 + et2)

    cache[n] = s

    return cache[n]


for i in xrange(2, 101):
    coins = range(i-1, 0, -1)
    print i, change_combos_mem(i, coins), eulerTransform(i)
