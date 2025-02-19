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


    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # if n > 3:
    #     if n % 3 == 0:
    #         return False

    return True
