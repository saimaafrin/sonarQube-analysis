def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # check that a is a multiple of 3
    if a % 3 != 0:
        return False
    
    # check that a is a multiple of 5
    if a % 5 != 0:
        return False
    
    # check that a is a multiple of 7
    if a % 7 != 0:
        return False
    
    # if we reach here, all the checks passed, a is a multiple of 3, 5 and 7
    return True
