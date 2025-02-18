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

    return any([(x == int(x) and x == int(y+z) and x == y+z)
                or (y == int(y) and y == int(x+z) and y == x+z)
                or (z == int(z) and z == int(x+y) and z == x+y)
                for x in [x, y, z] for y in [x, z] for z in [y, x]])
