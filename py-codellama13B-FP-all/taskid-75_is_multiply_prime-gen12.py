def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a < 1:
        return False
    if a == 1 or a == 2:
        return True
    if a % 2 == 0:
        return False
    if a % 3 == 0:
        return False
    if a % 5 == 0:
        return False
    if a % 7 == 0:
        return False
    if a % 11 == 0:
        return False
    if a % 13 == 0:
        return False
    return True
