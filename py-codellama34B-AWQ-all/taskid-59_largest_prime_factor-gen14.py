def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # This is guaranteed to return at least a factor of 2
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 1
    # If we got here, then n must be prime
    return n if n > 1 else i - 1
