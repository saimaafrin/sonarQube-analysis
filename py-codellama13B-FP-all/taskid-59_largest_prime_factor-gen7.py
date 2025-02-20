def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # factor by 2
    if n % 2 == 0:
        return 2
    # factor by odd numbers
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n
