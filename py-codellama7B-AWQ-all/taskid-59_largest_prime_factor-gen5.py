def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Find the largest prime factor of n using trial division,
    # starting with 2 and trying all odd numbers up to the square root of n.
    # If you get to the square root of n, you are done.
    # If you find a factor, divide n by it and start again.
    max_factor = 0
    factor = 2
    while factor <= n ** 0.5:
        if n % factor == 0:
            max_factor = factor
            n //= factor
        factor += 2
    return max_factor
