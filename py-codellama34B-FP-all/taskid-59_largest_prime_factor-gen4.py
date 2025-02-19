def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Note: 1 is not considered a prime, so if 1 is a prime factor, then n is not
    # fully factored.
    for i in range(2, int(n ** 0.5) + 1):  # 2 to sqrt(n), inclusive
        if n % i == 0:
            if is_prime(i):
                return i
            else:
                n = n // i
                return largest_prime_factor(n)
    return n
