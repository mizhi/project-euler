#!/usr/bin/env python

# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum of the
# proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
# that 28 is a perfect number.
#
# A number whose proper divisors are less than the number is called
# deficient and a number whose proper divisors exceed the number is
# called abundant.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two
# abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest number
# that cannot be expressed as the sum of two abundant numbers is less
# than this limit.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

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

def classify(n):
    divs=proper_divisors(n)
    sumdivs=sum(divs)    
    if sumdivs < n:
        return 'deficient'
    elif sumdivs == n:
        return 'perfect'
    elif sumdivs > n:
        return 'abundant'

def abundant_can_sum(abundant_set, n):
    for j in abundant_set:
        if j >= n:
            break
        diff = n - j
        if diff in abundant_set:
            return True
    return False


abundant = [n for n in xrange(28123) if classify(n) == 'abundant']
abundant_set = set(abundant)

nsum=[]
for i in xrange(1,28123):
    if not abundant_can_sum(abundant_set, i):
        nsum.append(i)

print len(nsum)

        

print sum(nsum)
