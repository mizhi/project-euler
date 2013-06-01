#!/usr/bin/env python

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2= 0.5
# 1/3= 0.(3)
# 1/4= 0.25
# 1/5= 0.2
# 1/6= 0.1(6)
# 1/7= 0.(142857)
# 1/8= 0.125
# 1/9= 0.(1)
# 1/10= 0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def divprec(n, d, p):
    rds = []
    
    n = n * 10
    while len(rds) < p:
        if n < d:
            rds.append(str(0))
            n *= 10
        else:
            q = n / d
            rds.append(str(q))

            r = n % d
            newnp = (n - (q * d))
            if newnp == 0:
                break
            n = newnp * 10

    return "".join(rds)

def submatchn(s, repn):
    for i in xrange(0, len(s), len(repn)):
        ts = s[i:i+len(repn)]
        if ts != repn:
            # this takes care of the case where we may have foudn repetitions
            # throughout the entire string except for the last modulo len(repn) 
            # chars
            if len(ts) == len(repn):
                return False
            elif ts != repn[:len(ts)]:
                return False    

    # we're going to require at least 2 repeats before we call a cycle
    return (len(s) / len(repn) >= 2) 


def cycle(s):
    for i in xrange(len(s)):
        for j in xrange(i+1, len(s) + 1):
            if submatchn(s, s[i:j]):
                return s[i:j]

 
maxcl = 0
maxcd = 0
i = 3
while i < 1000:
    if i % 5 == 0:
        i += 2

    rs = divprec(1, i, 2000)
    rsc = cycle(rs)
    if rsc:
        rsclen = len(rsc)
        if rsclen >= maxcl:
            print 'Max so far at %d was %d long' % (i, rsclen)
            print '\t', rsc
            maxcl = rsclen
            maxcd = i
    i += 2

print maxcd, maxcl


