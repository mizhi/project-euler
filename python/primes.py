from math import sqrt

def isprime(n):
    if n == 2: return True
    for x in xrange(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

def sieve(n):
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    print "Sifting."
    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)
            yield i

def getprimes(n):
    return [x for x in sieve(n)]

def infsieve():
    primes = [2]
    prime_len = len(primes)

    next_prime_index = 0
    while True:
        if next_prime_index < prime_len:
            yield primes[next_prime_index]
            next_prime_index += 1
        else:
            start = primes[-1] + 1 # start the partial seive at one past the max prime already found
            newmax = start * 2     # bump the capacity of the partial sieve to be 2x
            partial_sieve = [x for x in range(start, newmax)] # a partial sieve of integers.

            # the existing primes already eliminated a bunch of numbers
            # in previous partial sieves. This iterates through those
            # primes and bumps multiples in the partial_sieve.
            for x in primes[0:]:
                # this is probably the trickiest part in the code. We have a prime,
                # and we need to bump its multiple in partial_sieve. The partial_sieve
                # can be viewed as a window onto the integers that has been shifted by
                # start places.
                #
                # So the way this works is, we figure out the remainder of x going into
                # the last prime found. If we subtract this off of the start, then we
                # know the last integer at which x divided evenly into the numerator.
                # Therefore, the next multiple of x is derived from the addition of x.
                next_multiple = primes[-1] - primes[-1] % x + x

                # Now that we have the next multiple, we can start there and count up by x,
                # taking care to compute the offset index in the partial_sieve.
                for j in range(next_multiple, newmax, x):
                    partial_sieve[j - start] = 0

            # Now that we've knocked out everything from the previous n primes, we start searching
            # in the new partial sieve
            for i in range(start, newmax):
                if partial_sieve[i - start] != 0:
                    for j in range(start + i + i, newmax, i):
                        partial_sieve[start - j] = 0
            primes.extend([num for num in partial_sieve if num])
            prime_len = len(primes)

import itertools
print(sum(itertools.takewhile(lambda x: x <= 2000000, infsieve2())))
