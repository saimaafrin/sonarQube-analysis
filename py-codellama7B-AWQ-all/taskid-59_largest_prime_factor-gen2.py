def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    i = 2
    while True:
        if n % i == 0:
            n = n // i
        else:
            i += 1
        if n <= 1:
            break
    return i
