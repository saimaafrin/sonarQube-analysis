def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if is_prime(n):
        return n
    else:
        i = 2
        while n % i != 0:
            i += 1
        return largest_prime_factor(i)
