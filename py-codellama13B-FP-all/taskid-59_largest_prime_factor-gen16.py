def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    prime_factors = []
    for i in range(2, int(n**(1/2) + 1)):
        if n % i == 0:
            prime_factors.append(i)
            n = n // i
        else:
            continue
    prime_factors.append(n)
    return max(prime_factors)
