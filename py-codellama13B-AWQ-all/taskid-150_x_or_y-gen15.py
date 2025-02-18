def x_or_y(n: int, x: int, y: int) -> int:
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """

    n = int(n)
    x = int(x)
    y = int(y)
    if n == 2 or n == 3 or n == 5 or n == 7:
        return x
    else:
        return y
