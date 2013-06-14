#!/usr/bin/env python

# The decimal number, 585 = 10010010012 (binary), is palindromic in
# both bases.
#
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not
# include leading zeros.)


def tobins(n):
    l=[]
    if n < 0:
        raise ValueError, "must be a positive integer"

    while n > 0:
        l.append(str(n & 1))
        n = n >> 1
    l.reverse()
    return "".join(l).lstrip("0")

def ispalindrome(s):
    return s == s[::-1]

nums=[]
for i in xrange(1,1000000):
    decs=str(i)
    bins=tobins(i)

    if ispalindrome(decs) and ispalindrome(bins):
        nums.append(i)

print sum(nums)
