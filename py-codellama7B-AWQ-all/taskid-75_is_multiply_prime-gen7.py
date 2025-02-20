def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """


    # We know that if (a) is the multiplication of 3 prime numbers it must be less then 100
    # So we can't find such (a) number
    if a > 99:
        return False

    for i in range(1, a + 1):
        for j in range(1, a + 1):
            for k in range(1, a + 1):
                if i * j * k == a:
                    return True
    return False
