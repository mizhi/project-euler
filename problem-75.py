#!/usr/bin/env python

# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p 1000, is the number of solutions maximised?

def compute_triples(p):
    """Given a p, compute triples a,b,c such that a+b+c = p."""
    triples = set()
    for c in xrange(p, 1, -1):
        pp = p - c
        for b in xrange(pp-1, 1, -1):
            a = pp - b
            if a**2 + b**2 == c**2:
                tl = [a,b,c]
                tl.sort()
                triples.add(tuple(tl))

    if len(triples) == 0:
        return None

    return triples

def num_triples(p):
    count = 0
    for a in xrange(1, p):
        b = p * (p-2.0*a)/(2.0*(p-a))
        if a >= b:
            break
        if int(b) == b:
            count += 1
    return count


num_1t = 0
for i in xrange(2,2000000, 2):
    numts = num_triples(i)
    if numts == 1:
        num_1t += 1
        if num_1t % 1000 == 0:
            print i

print num_1t
