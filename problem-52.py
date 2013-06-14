#!/usr/bin/env python

# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and
# 6x, contain the same digits.

def samedigits(x,y):
    xs = list(str(x))
    ys = list(str(y))
    xs.sort()
    ys.sort()
    return xs == ys

n = 1
while True:
    print n
    n2 = n * 2
    if samedigits(n, n2):
        n3 = n * 3
        if samedigits(n2, n3):            
            n4 = n * 4
            if samedigits(n3, n4):
                n5 = n * 5
                if samedigits(n4, n5):                    
                    n6 = n * 6
                    if samedigits(n5, n6):
                        break
    n += 1

print n
