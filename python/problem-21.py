#!/usr/bin/env python


# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n).  If d(a) = b and d(b) = a, where
# a<>b, then a and b are an amicable pair and each of a and b are
# called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
# 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def proper_divisors(n):
    divs=[]
    i = 1
    maxn = n + 1
    while i < maxn:
        if n % i == 0:
            res = n / i
            divs.append(i)
            if i != res:
                divs.append(res)
            maxn = res
        i += 1

    divs.sort()
    return divs[:-1]

def amicable_number(a):
    b = sum(proper_divisors(a))
    pa = sum(proper_divisors(b))

    if pa == a and a != b:
        return b

    return None


nums=set([])
for i in xrange(1, 10000):
    b = amicable_number(i)
    if b != None:
        nums.add(i)
        nums.add(b)

print sum(nums)
