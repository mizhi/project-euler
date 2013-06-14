#!/usr/bin/env python


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
        
def divided_by_all(n, divs):
    for d in divs:
        if not n % d == 0:
            return False
    return True

# The concept is this, this is the minimal set of numbers to test divisibility with since
# the factors of each of these numbers appears as another number in the entire set.
# For example, 20 is divisible by 10, 5, 4, 2 which means that if 20 is a factor, then 10, 5, 4, 2
# are also factors and we don't have to test them.
divs = [20, 19, 18, 17, 16, 14, 13, 11]

startn = 2520 
n = startn

while True:
    print "Testing: ", n
    if divided_by_all(n, divs):
        break
    n += startn

print "Found:", n
