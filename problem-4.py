#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

max_n = 999 * 999

def palindrome_number(n):
    ns=str(n)
    return ns == ns[::-1]

pnumbers = [n for n in xrange(max_n + 1) if palindrome_number(n)]

pnumber_div=[]
for pn in pnumbers:
    for n in xrange(999, 100, -1):
        if pn % n == 0:
            n2 = pn / n
            if len(str(n2)) == 3:
                pnumber_div.append((n, n2, pn))

print pnumber_div[-1]
