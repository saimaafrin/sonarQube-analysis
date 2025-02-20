def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """


    a = str(a)
    for i in a:
        if i in "0123456789":
            return False
        elif int(i) > 3 and int(i) % 2 == 0 and int(i) % 3 == 0 and int(i) % 5 == 0:
            return False
    return True
