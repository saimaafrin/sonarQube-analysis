def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    if a < 10:
        return True
    i = 2
    if a % 2 == 0:
        i = 3
    while i <= a:
        if a % i == 0 and is_prime(i) and is_prime(a // i):
            return True
        i += 1
    return False
