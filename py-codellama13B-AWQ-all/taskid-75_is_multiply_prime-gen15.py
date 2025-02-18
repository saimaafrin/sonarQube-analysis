def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a < 3:
        return False
    if a == 3:
        return True
    while a % 3 == 0:
        a = a // 3
    if a == 1:
        return True
    for i in range(5, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    return True
