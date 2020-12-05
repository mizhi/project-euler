#!/usr/bin/env python

# The most naive way of computing n15 requires fourteen multiplications:
#
# n n ... n = n15
#
# But using a "binary" method you can compute it in six multiplications:
#
# n n = n2
# n2 n2 = n4
# n4 n4 = n8
# n8 n4 = n12
# n12 n2 = n14
# n14 n = n15
#
# However it is yet possible to compute it in only five multiplications:
#
# n n = n2
# n2 n = n3
# n3 n3 = n6
# n6 n6 = n12
# n12 n3 = n15
#
# We shall define m(k) to be the minimum number of multiplications to
# compute nk; for example m(15) = 5.
#
# For 1 k 200, find m(k).

from  math import log, ceil, floor

def m(n):
    if n < 2: return 0
    if n == 2: return 1
    
    log2n = floor(log(n,2))
    plog2n = 2**log2n
    if (n - plog2n) != 0:
        return log2n + floor(log(n - 2**log2n, 2))
    else:
        return log2n + 1

for k in xrange(0, 16):
    print k, m(k)

print sum([m(k) for k in xrange(1, 201)])

