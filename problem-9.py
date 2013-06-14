#!/usr/bin/env python

# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# a^2 + b^2 = c^2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def compute_triples(n):
    tuples=[]
    for i in xrange(1,n):
        a = 2 * i + 1
        b = 2*i*(i+1)
        c = 2*i*(i+1)+1
        tuples.append((a,b,c))
    return tuples


def compute_triples2(an, bn):
    tuples=[]
    for a in xrange(1, an):
        for b in xrange(1, bn):
            c = a + b
            d = b + c
            
            s1 = 2 * b * c
            s2 = a * d
            s3 = b**2 + c**2

            tuples.append((s1,s2,s3))

    return tuples
            

def compute_triples_sums(triples):
    sums={}
    for t in triples:
        sumt=t[0] + t[1] + t[2]
        if sumt not in sums:
            sums[sumt]=[]
        sums[sumt].append(t)
    return sums

#triples = compute_triples(1000000)
triples = compute_triples2(100,100)
triples_sums = compute_triples_sums(triples)

for s,t in triples_sums.items():
    if s == 1000:
        print s,t, t[0][0] * t[0][1] * t[0][2]


