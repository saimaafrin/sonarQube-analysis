def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a <= 0:
        return False
    prime_list = [2, 3, 5]
    for i in prime_list:
        for j in prime_list:
            for k in prime_list:
                if i * j * k == a:
                    return True
    return False
