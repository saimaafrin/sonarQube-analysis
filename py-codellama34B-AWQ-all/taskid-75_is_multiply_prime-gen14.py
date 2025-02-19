def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a < 3 or a > 100:
        return False

    result = True
    i = 2
    while result and i < a ** 0.5:
        if a % i == 0:
            if is_prime(i) and is_prime(a // i):
                return True
            else:
                result = False
        i += 1
    return result
