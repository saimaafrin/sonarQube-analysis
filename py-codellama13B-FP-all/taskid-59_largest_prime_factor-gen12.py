def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # for i in range(2, n):
    #     if n % i == 0:
    #         return i

    # This is a more concise implementation, but is less efficient than the
    # one above.
    return [i for i in range(2, n) if n % i == 0][-1]
