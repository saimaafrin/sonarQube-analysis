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

    # If number is less than 2, it's not prime
    if n < 2:
        return False
    # If number is 2 or 3, it's prime
    if n == 2 or n == 3:
        return True
    # If number is divisible by 2 or 3, it's not prime
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Try to find divisor from 5 to sqrt(n)
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    # Otherwise, it's prime
    return True
