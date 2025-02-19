def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Divide out as many 2s as possible
    while n % 2 == 0:
        n //= 2

    # Try all odd numbers up to the square root of n
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i

    return n
