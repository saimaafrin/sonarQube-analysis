def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    prime = [2, 3, 5]
    if a not in prime:
        for i in prime:
            for j in prime:
                if i * j == a:
                    return True
    return False
