def x_or_y(n: int, x: int, y: int) -> int:
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """


    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return y
    return x
