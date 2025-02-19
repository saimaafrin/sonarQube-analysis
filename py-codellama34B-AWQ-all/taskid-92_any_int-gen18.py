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

    # Your code here
    # Check if the numbers are integers
    if x % 1 == 0 and y % 1 == 0 and z % 1 == 0:
        # Check if one number is equal to the sum of the other two
        if x == y + z or y == x + z or z == x + y:
            return True
        else:
            return False
    else:
        return False
