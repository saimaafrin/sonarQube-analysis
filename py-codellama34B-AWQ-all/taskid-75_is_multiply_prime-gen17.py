def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # Your code here
    # a < 100, so it's safe to assume that the largest 3 prime numbers are 5, 7, 11
    # 5 * 7 * 11 = 385
    return a == 15 or a == 21 or a == 30 or a == 35 or a == 42 or a == 50 or a == 56 or a == 63 or a == 70 or a == 77 or a == 84 or a == 91 or a == 98 or a == 385
