def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # 30 = 2 * 3 * 5
    # 30 = 3 * 5 * 2
    # 30 = 5 * 2 * 3
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j * a % i == 0 and j * a % j == 0 and a % i == 0 and a % j == 0:
                return True
    return False
