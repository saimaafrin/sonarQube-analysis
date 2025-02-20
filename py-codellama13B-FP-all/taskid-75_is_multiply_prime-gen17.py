def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a == 1:
        return False
    a_list = list(str(a))
    if len(a_list) == 3:
        i = 0
        if a_list[i] == '0' or a_list[i] == '1':
            return False
        while i < 2:
            if a_list[i] == '0' or a_list[i] == '1':
                return False
            i += 1
        return True
    return False
