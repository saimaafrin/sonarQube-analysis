def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a < 100:
        raise ValueError("a must be larger then 100")
    if a % 3 == 0:
        return is_multiply_prime(a // 3)
    if a % 2 == 0:
        return is_multiply_prime(a // 2)
    if a % 5 == 0:
        return is_multiply_prime(a // 5)
    if a % 7 == 0:
        return is_multiply_prime(a // 7)
    if a % 11 == 0:
        return is_multiply_prime(a // 11)
    if a % 13 == 0:
        return is_multiply_prime(a // 13)
    return False
