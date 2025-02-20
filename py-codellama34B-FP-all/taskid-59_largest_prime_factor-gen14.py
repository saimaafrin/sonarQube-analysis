def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n < 2:
        raise ValueError("n must be greater than 1")
    for p in range(2, int(n**0.5) + 1):
        while n % p == 0:
            n //= p
        if n == 1:
            return p
    return n
