def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # 1. Find all prime factors of n using a loop
    # 2. Find the largest prime factor of n using max() and a lambda function
    # 3. Return the largest prime factor

    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n = n // i
    return max(factors, key=lambda x: x ** 0.5)
