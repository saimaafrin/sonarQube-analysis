def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize largest prime factor to 1.
    largest_prime_factor = 1

    # Iterate from 2 to the square root of n.
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i, print i and set n to n // i.
        if n % i == 0:
            largest_prime_factor = i
            n = n // i

    # Return the remaining n.
    return largest_prime_factor
