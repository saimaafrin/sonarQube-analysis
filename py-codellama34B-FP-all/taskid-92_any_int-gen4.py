def any_int(x: float, y: float, z: float) -> bool:
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    >>> any_int(5, 2, 7)
    True
    
    >>> any_int(3, 2, 2)
    False

    >>> any_int(3, -2, 1)
    True
    
    >>> any_int(3.6, -2.2, 2)
    False
  

    
    """

    a, b, c = x, y, z

    a = int(a)
    b = int(b)
    c = int(c)

    return (a == b + c) or (b == a + c) or (c == a + b)
