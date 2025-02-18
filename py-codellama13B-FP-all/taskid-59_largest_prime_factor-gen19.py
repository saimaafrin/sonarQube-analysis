def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # If n is even, the largest prime factor is 2.
    if n % 2 == 0:
        return 2

    # Iterate over odd numbers between 3 and sqrt(n).
    for i in range(3, int(n ** 0.5) + 1, 2):
        # If the remainder is 0, the number is divisible.
        if n % i == 0:
            return i
    return n
