#!/usr/bin/env

# A permutation is an ordered arrangement of objects. For example,
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all
# of the permutations are listed numerically or alphabetically, we
# call it lexicographic order. The lexicographic permutations of 0, 1
# and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1,
# 2, 3, 4, 5, 6, 7, 8 and 9?



def permute(s):
    if len(s) > 1:
        r=[]
        for i in range(len(s)):
            r.extend([s[i] + rsi for rsi in permute(s[:i] + s[i+1:])])
        return r
    return [s]

perms=permute("0123456789")

perms.sort()

print perms[999999]
