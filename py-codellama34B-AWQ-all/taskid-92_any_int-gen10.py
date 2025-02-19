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

    if (x+y == z) or (x+z == y) or (y+z == x):
        if int(x) == x and int(y) == y and int(z) == z:
            return True
        else:
            return False
    else:
        return False
