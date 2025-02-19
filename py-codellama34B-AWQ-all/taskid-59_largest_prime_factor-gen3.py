def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # find the largest prime factor
    largest_prime = 2
    while True:
        largest_prime += 1
        if n % largest_prime == 0:
            if n == largest_prime:
                return n
            else:
                n = n // largest_prime
                if n == 1:
                    return largest_prime
        else:
            if n == largest_prime:
                return n
