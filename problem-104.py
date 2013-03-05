#!/usr/bin/env python


# The Fibonacci sequence is defined by the recurrence relation:
#
#     Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
#
# It turns out that F541, which contains 113 digits, is the first
# Fibonacci number for which the last nine digits are 1-9 pandigital
# (contain all the digits 1 to 9, but not necessarily in order). And
# F2749, which contains 575 digits, is the first Fibonacci number for
# which the first nine digits are 1-9 pandigital.
#
# Given that Fk is the first Fibonacci number for which the first nine
# digits AND the last nine digits are 1-9 pandigital, find k.
from math import sqrt
from math import floor
from sys import exit

def pandigital(o1):
    cs="123456789"
    o1s=list(str(o1))
    o1s.sort()
    return cs == "".join(o1s)

sqrt5 = sqrt(5)
phi = (1 + sqrt5) / 2
iphi = -1 / phi

lastphi = 1
lastphib = 0

lastiphi = 1
lastiphib = 0

def bigfib(n):
    global iphi, phi, sqrt5, lastphi, lastphib, lastiphi, lastiphib

    while lastphib < n:
        lastphi *= phi
        if lastphi > 10**9:
            lastphi /= 10
        lastphib += 1
        
    while lastiphib < n:
        lastiphi *= iphi
        if lastiphi > 10**9:
            lastiphi /= 10
        lastiphib += 1
        
    return int((lastphi - lastiphi) / sqrt5)

fn = 0
fn_1 = 1
fn_2 = 0
n = 2
while True:
    fn = fn_1 + fn_2
    fn %= 10**9
    fn_2, fn_1 = fn_1, fn

    if pandigital(fn):
        firstn = bigfib(n)

        if pandigital(firstn):
            break

    n += 1

print n

