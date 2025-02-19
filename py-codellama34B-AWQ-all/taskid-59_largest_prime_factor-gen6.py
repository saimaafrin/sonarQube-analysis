def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    for factor in range(2, int(n ** 0.5) + 1):
        if n % factor == 0:
            return n // factor if factor == (n // factor) else factor
    return 1  # should never be reached
