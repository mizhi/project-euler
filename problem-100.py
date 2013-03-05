#!/usr/bin/env python

# If a box contains twenty-one coloured discs, composed of fifteen
# blue discs and six red discs, and two discs were taken at random, it
# can be seen that the probability of taking two blue discs, P(BB) =
# (15/21)x(14/20) = 1/2.
#
# The next such arrangement, for which there is exactly 50% chance of
# taking two blue discs at random, is a box containing eighty-five
# blue discs and thirty-five red discs.
#
# By finding the first arrangement to contain over 10^(12) =
# 1,000,000,000,000 discs in total, determine the number of blue discs
# that the box would contain.


import math

#N = 10

N = 1000000000000

while True:
    A = 2.0
    B = -2.0
    N2 = N*N
    C = - float(N2 - N)

    SQRTN = math.sqrt(B*B - 4.0 * A * C)

    BLUE = (-B + SQRTN) / (2.0 * A)

    if BLUE == int(BLUE):
        RED = N - BLUE
        print "N = ", N
        print "\tBLUE = %f" % (BLUE)
        print "\tRED  = %f" % (RED)
        print "\t%f" % ((BLUE / N) * ((BLUE - 1) / (N - 1)))
        break
 
    N += 1



b = 85
n = 120
while n < 10**12:
  b,n = 3*b + 2*n - 2, 4*b + 3*n - 3
print "Answer to PE100 = ",b
