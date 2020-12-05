#!/usr/bin/env python

# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#     192 1 = 192
#     192 2 = 384
#     192 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2,
# 3, 4, and 5, giving the pandigital, 918273645, which is the
# concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be
# formed as the concatenated product of an integer with (1,2, ... , n)
# where n 1?

def permute(s):
    if len(s) > 1:
        r=[]
        for i in range(len(s)):
            r.extend([s[i] + rsi for rsi in permute(s[:i] + s[i+1:])])
        return r
    return [s]

def partition(s, n):
    if n == len(s):
        return [[d for d in s]]
    elif n == 1:
        return [[s]]
    else:
        ret=[]
        maxl = len(s) - (n - 1)
        for i in xrange(1, maxl + 1):
            part = s[:i]
            partless = s[i:]

            pdivs = partition(partless, n - 1)
            for pd in pdivs:
                news = [part]
                news.extend(pd)
                ret.append(news)

        return ret

# like divs, except returns tuples of (begin,end) indices where the
def partition_indices(s, n):
    if n == len(s):
        return [[(i, i+1) for i in xrange(len(s))]]
    elif n == 1:
        return [[(0, len(s) + 1)]]
    else:
        ret=[]
        maxl = len(s) - (n - 1)
        for i in xrange(1, maxl + 1):
            #part = s[:i]
            #partless = s[i:]

            part = (0, i)
            partless = s[i:]

            pdivs = partition_indices(partless, n - 1)
            for pd in pdivs:
                news = [part]
                for t in pd:
                    news.append( (part[1] + t[0], part[1] + t[1]))
                ret.append(news)

        return ret

# returns list of nums that are the quotients of the divisors of a tuple
# the length of nlist.
#
# Thus, if nlist is [2, 4, 6]
#
# The returned value is
# [1,2,2] which are the results after dividing 2/1, 4/2, and 6/3
def ndivlist(nlist):
    t=[0 for n in nlist]

    for i in xrange(1,len(nlist) + 1):
        if nlist[i - 1] % i == 0:
            t[i-1] = nlist[i - 1] / i
        else:
            return None
    return t


# gather up potential pan digitals
# know it has to be greater than 918273645
nine_perms = ["9" + s for s in permute("12345678") if int(s) > 18273645]
nine_perms.sort(reverse=True)

pset={}
for i in xrange(2, len(nine_perms[0]) + 1):
    pset[i] = partition_indices(nine_perms[0], i)


for nps,ps in pset.items():
    for perm in nine_perms:
        for p in ps:
            nums = [int(perm[t[0]:t[1]]) for t in p]           
            ndl = ndivlist(nums)
            if ndl:
                if ndl.count(ndl[0]) == len(ndl):
                    print perm, nums, ndl
