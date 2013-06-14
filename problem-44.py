#!/usr/bin/env python

# Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The
# first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
# difference, 70 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum
# and difference is pentagonal and D = |Pk Pj| is minimised; what is
# the value of D?

def pentagonal(n):
    return (3 *(n**2) - n) / 2

pents=[pentagonal(i) for i in xrange(1, 20000)]

pentset=set(pents)

seen=()
pentindices=[]
for i in xrange(len(pents)):
    for j in xrange(i+1, len(pents)):
        pdiff = pents[j] - pents[i]
        if pdiff in pentset:
            psum = pents[j] + pents[i]
            if psum in pentset:
                pentindices.append((i,j))

for i in pentindices:
    print i, pents[i[0]], pents[i[1]], pents[i[1]] - pents[i[0]]