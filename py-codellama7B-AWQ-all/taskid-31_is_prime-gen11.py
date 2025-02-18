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


    # check if the number is less than 2
    if n < 2:
        return False

    # check if the number is divisible by 2
    if n % 2 == 0 and n != 2:
        return False

    # check if the number is divisible by 3
    if n % 3 == 0 and n != 3:
        return False

    # check if the number is divisible by 5
    if n % 5 == 0 and n != 5:
        return False

    # check if the number is divisible by 7
    if n % 7 == 0 and n != 7:
        return False

    # check if the number is divisible by 11
    if n % 11 == 0 and n != 11:
        return False

    # check if the number is divisible by 13
    if n % 13 == 0 and n != 13:
        return False

    # check if the number is divisible by 17
    if n % 17 == 0 and n != 17:
        return False

    # check if the number is divisible by 19
    if n % 19 == 0 and n != 19:
        return False

    # check if the number is divisible by 23
    if n % 23 == 0 and n != 23:
        return False

    # check if the number is divisible by 29
    if n % 29 == 0 and n != 29:
        return False

    # check if the number is divisible by 31
    if n % 31 == 0 and n != 31:
        return False

    # check if the number is divisible by 37
    if n % 37 == 0 and n != 37:
        return False

    # check if the number is divisible by 41
    if n % 41 == 0 and n != 41:
        return False

    # check if the number is divisible by 43
    if n % 43 == 0 and n != 43:
        return False

    # check if the number is divisible by 47
    if n % 47 == 0 and n != 47:
        return False

    # check if the number is divisible by 53
    if n % 53 == 0 and n != 53:
        return False

    # check if the number is divisible by 59
    if n % 59 == 0 and n != 59:
        return False

    # check if the number is divisible by 61
    if n % 61 == 0 and n != 61:
        return False

    # check if the number is divisible by 67
    if n % 67 == 0 and n != 67:
        return False

    # check if the number is divisible by 71
    if n % 71 == 0 and n != 71:
        return False

    # check if the number is divisible by 73
    if n % 73 == 0 and n != 73:
        return False

    # check if the number is divisible by 79
    if n % 79 == 0 and n != 79:
        return False

    # check if the number is divisible by 83
    if n % 83 == 0 and n != 83:
        return False

    # check if the number is divisible by 89
    if n % 89 == 0 and n != 89:
        return
