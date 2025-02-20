def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # A list of all primes up to sqrt(n)
    primes = prime_sieve(int(n**0.5) + 1)
    # Iterate over all primes up to sqrt(n)
    for p in primes:
        # If p divides n
        if n % p == 0:
            # p is a prime factor
            return p
    # If p does not divide n
    # Then p is the largest prime factor of n
    return n
