def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Divide n by 2 repeatedly. When n is odd, it must be prime.
    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 2
    # From here, we can skip all even numbers.
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
        if n == 1:
            return i
    return n  # n is prime
