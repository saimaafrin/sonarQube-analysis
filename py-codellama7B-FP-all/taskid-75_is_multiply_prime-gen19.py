def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    from math import sqrt
    if a < 3:
        return False
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            n = a // i
            if n == 1:
                return True
            if n < 3:
                return False
            for j in range(2, int(sqrt(n)) + 1):
                if n % j == 0:
                    return False
            return True
    return False
