#!/usr/bin/env python

# Consider quadratic Diophantine equations of the form:
#
# x^2 - Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 649^2 - 13*180^2 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
# 3^(2) ? 2x2^(2) = 1
# 2^(2) ? 3x1^(2) = 1
# 9^(2) ? 5x4^(2) = 1
# 5^(2) ? 6x2^(2) = 1
# 8^(2) ? 7x3^(2) = 1
#
# Hence, by considering minimal solutions in x for D ? 7, the largest x is obtained when D=5.
#
# Find the value of D ? 1000 in minimal solutions of x for which the largest value of x is obtained.

from math import sqrt



def diophantinex(D, sqs):
    """Gets the smallest positive integer x solution possible with D.
    D: the D in x^2 - Dy^2 = 1
    """
    for y in xrange(1, 1000):
        ysq = sqs[y]
        cxsq = 1 + D * ysq
        if cxsq in sqs:
            return sqrt(cxsq)

    return None

def maxdiophantinex(Ds):
    """Find the maximum minimum x solution for all the Ds in Ds
    Ds: List of D to find minimum x for using diophantinex
    """
    maxx = 0
    maxD = 0
    sqs = [x**2 for x in xrange(0,10**5)]
    for D in Ds:
        print D
        cmaxx = diophantinex(D, sqs)
        if cmaxx > maxx:
            maxx = cmaxx
            maxD = D

    return maxD

print maxdiophantinex(xrange(1,1001))
