def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    max_div = 0
    i = 1
    while i * i <= n:
        if n % i:
            i += 1
        else:
            max_div = i
            n //= i
    return max_div
