def special_factorial(n: int) -> int:
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    if n < 0:
        raise ValueError('n must be a positive integer')

    result = n

    for i in range(n - 1, 0, -1):
        result *= i

    return result
