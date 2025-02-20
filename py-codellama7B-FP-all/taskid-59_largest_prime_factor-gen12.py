def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n % 2 == 0:
        return 2

    # Make n odd
    n -= 1
    while n % 2 == 0:
        n //= 2

    while True:
        for i in range(int(n ** 0.5) + 1):
            if n % i == 0:
                n //= i
                break
        else:
            return n
