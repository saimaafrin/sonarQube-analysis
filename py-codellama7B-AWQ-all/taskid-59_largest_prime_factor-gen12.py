def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n <= 1:
        raise ValueError(f"n must be > 1, not {n}")
    # if n is a prime, return it
    if n == 2 or n == 3 or n == 5 or n == 7:
        return n
    # if n is composite and is not a prime, find its largest prime factor
    largest = 2
    while n > 1:
        if n % largest == 0:
            n //= largest
        else:
            largest += 2
    return largest
