#!/usr/bin/env python

# The arithmetic sequence, 1487, 4817, 8147, in which each of the
# terms increases by 3330, is unusual in two ways: (i) each of the
# three terms are prime, and, (ii) each of the 4-digit numbers are
# permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or
# 3-digit primes, exhibiting this property, but there is one other
# 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in
# this sequence?


from math import sqrt

def getprimes(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x !=0]

fourdp=getprimes(10000)

# group palindromic primes by creating a key 
# that is the sorted digits
pmap={}
for p in fourdp:
    ds=list(str(p))
    ds.sort()
    pk="".join(ds)

    if pk not in pmap:
        pmap[pk]=[]
        
    pmap[pk].append(p)

# group tuples by palindromic key and difference
diffs={}
for k,pl in pmap.items():
    pl.sort()

    for i in xrange(len(pl)):
        for j in xrange(i, len(pl)):
            diff = pl[j] - pl[i]
            if diff != 0:
                if (k, diff) not in diffs:
                    diffs[(k,diff)] = []
                diffs[(k,diff)].append( (pl[i], pl[j]) )

# simple function to test if the tuples produced
# by the grouping algorithm above form a sequence
# this would men (a,b), (b, c), (c, d)
def tuples_form_sequence(ts):
    for i in xrange(len(ts) - 1):
        if ts[i][1] != ts[i+1][0]:
            return False       
    return True

# forms a sequence from the tuples where
# if tuples = [(a,b), (b,c), (c,d)]
# then seq = [a,b,c]
def sequence_from_tuples(ts):
    rseq=[ts[0][0]]
    for t in ts:
        rseq.append(t[1])
    return rseq

# find all the sequences that are interesting
for dk,df in diffs.items():
    if tuples_form_sequence(df):
        tseq = sequence_from_tuples(df)
        if len(tseq) > 2:
            print tseq
