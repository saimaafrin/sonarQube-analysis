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

    # all prime numbers are greater than 1
    if n <= 1:
        return False
    # check if n is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
