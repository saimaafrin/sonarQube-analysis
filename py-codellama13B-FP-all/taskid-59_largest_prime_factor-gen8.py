def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    assert n > 1 and not is_prime(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    raise ValueError(f"{n} is prime")
