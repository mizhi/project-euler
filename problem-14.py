#!/usr/bin/env python


# The following iterative sequence is defined for the set of positive integers:
#
# n= n/2 (n is even)
# n= 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 40 20 10 5 16 8 4 2 1
#
# It can be seen that this sequence (starting at 13 and finishing at
# 1) contains 10 terms. Although it has not been proved yet (Collatz
# Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

def getseq(n, cache={}):
    if n in cache:
        return cache[n]

    wn=n
    seq=[n]
    while wn != 1:
        if wn % 2 == 0:
            wn = wn / 2
        else:
            wn = 3 * wn + 1
        
        if wn in cache:
            seq.extend(cache[wn])
            wn = seq[-1]
        else:
            seq.append(wn)

    cache[n] = seq

    return seq


def getmaxseqlen(n, cache={}):
    if n in cache:
        return cache[n]

    wn=n
    seqlen=1
    while wn != 1:
        if wn % 2 == 0:
            wn = wn / 2
        else:
            wn = 3 * wn + 1
        
        if wn in cache:
            seqlen += cache[wn]
            wn = 1
        else:
            seqlen += 1

    cache[n] = seqlen

    return seqlen


maxseqnum = 0
maxlen = 0
for i in xrange(1, 999999):
    newseqlen = getmaxseqlen(i)
    if newseqlen > maxlen:
        maxlen = newseqlen
        maxseqnum = i

print maxseqnum
