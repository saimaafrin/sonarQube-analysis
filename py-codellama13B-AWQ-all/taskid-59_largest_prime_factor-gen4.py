def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Find all the prime factors of n.
    prime_factors = prime_factors(n)

    # Return the largest prime factor.
    return max(prime_factors)
