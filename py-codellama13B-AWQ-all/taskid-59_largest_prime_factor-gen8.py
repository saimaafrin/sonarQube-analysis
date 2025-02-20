def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # find the largest factor of n
    largest_factor = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            largest_factor = i

    # if the largest factor is a prime, return it
    if is_prime(largest_factor):
        return largest_factor

    # if the largest factor is not a prime, divide it by its largest prime factor
    else:
        return largest_prime_factor(largest_factor)
