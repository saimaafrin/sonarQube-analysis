def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # count = 0
    # for i in range(2, a // 2):
    #     if a % i == 0:
    #         count += 1
    # if count == 2:
    #     return True
    # else:
    #     return False
    # # O(sqrt(n))
    # if a == 1:
    #     return False
    # for i in range(2, int(a ** 0.5) + 1):
    #     if a % i == 0 and is_prime(a // i):
    #         return True
    # return False
    # # O(sqrt(n))
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0 and is_prime(a // i) and is_prime(i):
            return True
    return False
    # # O(n)
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            if is_prime(i) and is_prime(a // i):
                return True
    return False
