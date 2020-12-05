#!/usr/bin/env python

# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
# 1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest
# chain of numbers that link back to 169; it turns out that there are
# only three such loops that exist:
#
# 169 363601 1454 169
# 871 45361 871
# 872 45362 872
#
# It is not difficult to prove that EVERY starting number will
# eventually get stuck in a loop. For example,
#
# 69 363600 1454 169 363601 ( 1454)
# 78 45360 871 45361 ( 871)
# 540 145 ( 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but
# the longest non-repeating chain with a starting number below one
# million is sixty terms.
#
# How many chains, with a starting number below one million, contain
# exactly sixty non-repeating terms?

factdict = { '0':1 }
for i in xrange(1, 10):
    factdict[str(i)] = i * factdict[str(i-1)]

def dfactsum(n):
    global factdict
    ds=str(n)
    return sum([factdict[d] for d in ds])

def chainlen(n, cache={}):
    if n in cache:
        return n
    
    chain=set([n])
    
    fs = dfactsum(n)
    while (fs not in chain) and (fs not in cache):
        chain.add(fs)
        fs = dfactsum(fs)
        
    chainlen = len(chain)
    if fs in cache:
        chainlen += cache[fs]

    cache[n] = chainlen

    return cache[n]


count = 0
for i in xrange(0, 1000000):
    if chainlen(i) == 60:
        count += 1


print count
