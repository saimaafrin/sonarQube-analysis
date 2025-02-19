def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    assert n > 1 and not is_prime(n)

    # loop through odd numbers from n // 2 down to 3
    for i in range(n // 2, 2, -2):
        if n % i == 0 and is_prime(i):
            return i
