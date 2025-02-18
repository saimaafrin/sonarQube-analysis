def is_prime(n: int) -> bool:
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """

    # Corner cases.
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    # Iterate through numbers 3 to sqrt(n) and check if n is divisible by any of them.
    # We don't need to check up to n because, if n is divisible by some number p,
    # then it is also divisible by n/p, which is smaller than sqrt(n).
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
