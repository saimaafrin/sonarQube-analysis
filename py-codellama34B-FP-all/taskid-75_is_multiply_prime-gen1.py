def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # if (a<3 or a%2==0 or a%3==0 or a%5==0):
    #     return False
    # return True
    if a<3 or a%2==0 or a%3==0 or a%5==0:
        return False
    return True
