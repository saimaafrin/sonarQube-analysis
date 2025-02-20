def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Divide by the smallest prime factor > 1.
    for p in range(2, int(n ** 0.5)):
        if n % p == 0:
            return p
    return n  # n itself is a prime
