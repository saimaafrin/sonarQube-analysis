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
        for i in range(int(sqrt(n)), 1, -1):
            if n % i == 0:
                if is_prime(i):
                    return i
                else:
                    return largest_prime_factor(n/i)
