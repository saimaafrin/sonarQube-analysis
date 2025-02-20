def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Start with the largest possible prime factor, which is the square root of n
    factor = int(n ** 0.5)
    while True:
        # If the factor divides n exactly, it is the largest prime factor
        if n % factor == 0:
            return factor
        # Otherwise, increment the factor
        factor -= 1
