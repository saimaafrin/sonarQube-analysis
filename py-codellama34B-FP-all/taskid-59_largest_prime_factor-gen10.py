def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Divide n by 2 once, since half of all numbers are even.
    n = n // 2
    while n % 2 == 0:
        n = n // 2
    # Now, n is odd, so start at 3 and increase by 2, skipping all even numbers.
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n = n // i
    return n
