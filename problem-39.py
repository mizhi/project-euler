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

max_num_ts = 0
max_p = 0
for i in xrange(1,1000):
    triples = compute_triples(i)
    if triples:
        num_ts = len(triples)
        if num_ts > max_num_ts:
            max_num_ts = num_ts
            max_p = i

print max_p, max_num_ts
