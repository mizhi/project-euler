#!/usr/bin/env python

# In England the currency is made up of pound, and pence, p, and there are eight coins in general circulation:
#
#     1p, 2p, 5p, 10p, 20p, 50p, 1pound (100p) and 2pound (200p).
#
# It is possible to make 2pounds in the following way:
#
#     1x1pound + 150p + 220p + 15p + 12p + 31p
#
# How many different ways can 2pound be made using any number of coins?


def change_combos(n, coins = [200, 100, 50, 20, 10, 5, 2, 1]):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if len(coins) == 1 and n % coins[0] == 0:
        return 1

    coin_used = coins[0]
    remaining_coins = coins[1:]

    canusemaxc = n / coin_used

    maxcpossibilities = [i * coin_used for i in xrange(0, canusemaxc + 1)]
        
    return sum([change_combos(n - p, remaining_coins) for p in maxcpossibilities])
        
print change_combos(5)
print change_combos(200)
