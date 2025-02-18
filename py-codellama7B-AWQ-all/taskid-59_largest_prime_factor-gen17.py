def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    i = 3
    while i <= int(sqrt(n)) + 1:
        if n % i == 0:
            n //= i
            i = 2
        else:
            i += 2
    return n
