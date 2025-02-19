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

    #check if all numbers are integers
    if x.is_integer() and y.is_integer() and z.is_integer():
        x = int(x)
        y = int(y)
        z = int(z)
        
        if x == y + z:
            return True
        elif y == z + x:
            return True
        elif z == x + y:
            return True
        else:
            return False
    else:
        return False
