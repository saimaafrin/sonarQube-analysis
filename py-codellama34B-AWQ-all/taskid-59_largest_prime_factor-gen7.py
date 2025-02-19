def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    assert n > 1
    assert n % 2 != 0  # n is not a prime number

    # Since n is not a prime, it must have a prime factor that is <= sqrt(n)
    for prime in range(3, int(n ** 0.5) + 1, 2):
        if n % prime == 0:
            return prime
