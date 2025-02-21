def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    factor = 2
    while factor ** 2 <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n
