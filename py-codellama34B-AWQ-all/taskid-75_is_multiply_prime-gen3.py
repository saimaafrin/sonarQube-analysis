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
    for n1 in range(2, int(a ** 0.5) + 1):
        if a % n1 == 0:
            for n2 in range(2, int(n1 ** 0.5) + 1):
                if n1 % n2 == 0:
                    if a // n1 == n1:
                        return False
                    if a // n1 % n2 == 0:
                        return True
    return False
