def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Divide n by 2, then 3, then 5, then 7, etc., until we no longer can.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            n //= i
    return n
