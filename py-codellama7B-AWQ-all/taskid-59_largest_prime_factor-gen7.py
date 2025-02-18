def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    i = 3
    while i * i <= n:
        if n % i == 0:
            n //= i
            i -= 1
        else:
            i += 1
    return n
