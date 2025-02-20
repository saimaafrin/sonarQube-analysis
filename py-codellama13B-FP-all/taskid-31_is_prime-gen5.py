def is_prime(n: int) -> bool:
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """

    # start at 2, since all primes are odd, and 0 and 1 are not primes.
    # increment by 2, since all primes are odd.
    for i in range(2, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            # if we find a factor, it is not prime
            return False
    # if we reach the end, and haven't found a factor, then it is prime
    return True
