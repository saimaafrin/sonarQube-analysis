def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n % 2 == 0:
        return largest_prime_factor(n // 2)
    for p in range(int(n ** 0.5), 1, -1):
        if n % p == 0:
            return p
    return 1  # n is prime
