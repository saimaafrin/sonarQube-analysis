def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    i = 2
    max_factor = 1
    while i * i <= n:
        if n % i == 0:
            max_factor = i
            while n % i == 0:
                n = n // i
        i += 1
    if n > max_factor:
        max_factor = n
    return max_factor
