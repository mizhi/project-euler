#!/usr/bin/env python

# The Fibonacci sequence is defined by the recurrence relation:
#
#     Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        fminus2 = 1
        fminus1 = 1
        t = 0
        for i in xrange(3,n+1):
            t = fminus1 + fminus2
            fminus2 = fminus1
            fminus1 = t
        return t

n=10
while True:
    fibn=fib(n)
    if len(str(fibn)) >= 1000:
        break
    n += 1

print n, fib(n)
