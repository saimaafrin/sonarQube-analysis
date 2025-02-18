def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # your code here
    if n == 2:
        return 2
    while n % 2 == 0:
        n = n // 2
    for i in range(int(n ** 0.5), 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    raise Exception("No prime factors")
