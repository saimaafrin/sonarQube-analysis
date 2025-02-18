def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # 2, 3, 5, 7, 11, 13, 17, 19, 23
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    # https://en.wikipedia.org/wiki/List_of_prime_numbers
    return a > 1 and a % 2 != 0 and a % 3 != 0 and a % 5 != 0
