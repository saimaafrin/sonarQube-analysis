def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # We know that n is not prime, so n > 1. If n is odd, then its largest
    # prime factor is n // 2, which is also an integer. If n is even, then
    # its largest prime factor is n // 2 + 1, which is also an integer.
    if n & 1 == 0:
        return largest_prime_factor(n // 2 + 1)
    else:
        return n // 2
