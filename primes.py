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
    """Infinite sieve. Like infsieve() but tries to be smarter about creating the
    sieve.
    """
    primes = [1,2]
    prime_len = len(primes)
    cidx = 0
    newmax = None
    while True:
        if cidx < prime_len:
            yield primes[cidx]
            newmax = None
            cidx += 1
        else:
            start = primes[-1]
            offset = start
            newmax = (newmax or start) * 2
            sieve = range(offset, newmax)
            sieve[0] = 0 # we know this is already prime, so make it so it
                         # doesn't get duplicated in the list
            for x in primes[1:]:
                toffset = offset - offset % x + x # figure out the next multiple
                                                  # after the offset
                for j in xrange(toffset, newmax, x):
                    sieve[j - offset] = 0

            for i in xrange(offset, newmax):
                if sieve[i - offset] != 0:
                    for j in xrange(offset + i + i, newmax, i):
                        sieve[offset - j] = 0
            primes.extend([num for num in sieve if num])
            prime_len = len(primes)
