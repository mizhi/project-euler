#!/usr/bin/env python

# The fraction 49/98 is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly believe
# that 49/98 = 4/8, which is correct, is obtained by cancelling the
# 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of
# fraction, less than one in value, and containing two digits in the
# numerator and denominator.
#
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

def gcd(a,b):
    return a if b == 0 else gcd(b, a % b)

def naivesimplify(num,den):
    lnum = list(str(num))
    lden = list(str(den))

    snum = set(str(num))
    sden = set(str(den))

    common_digit = list(snum & sden)

    if common_digit:
        lnum.remove(common_digit[0])
        lden.remove(common_digit[0])
        return (int("".join(lnum)), int("".join(lden)))
    else:
        return None
       
nnum = 1
nden = 1
for num in xrange(10, 100):
    if num % 10 == 0: continue
    for den in xrange(num+1, 100):
        if den % 10 == 0: continue

        pgd = gcd(num, den)
        if pgd == 1:
            continue

        redn = (num / pgd, den / pgd)

        nsimp = naivesimplify(num, den)  
        
        if nsimp:
            pgd2 = gcd(nsimp[0], nsimp[1])
            redn2 = (nsimp[0] / pgd2, nsimp[1] / pgd2)

            if redn[0] == redn2[0] and \
                    redn[1] == redn2[1]:
                nnum *= redn[0]
                nden *= redn[1]

pgd3 = gcd(nnum, nden)

print nden / pgd3
