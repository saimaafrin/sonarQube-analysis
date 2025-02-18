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

    #Checks that all numbers are ints
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False

    #Checks if one of the numbers is equal to the sum of the other two numbers
    if x == y + z or x == y - z or x == z - y or y == x + z or y == x - z or y == z - x or z == x + y or z == x - y or z == y - x:
        return True
    else:
        return False
