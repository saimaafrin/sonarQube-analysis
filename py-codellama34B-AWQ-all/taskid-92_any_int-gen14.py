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

    # Create an empty list
    list_1 = []
    # Check if all parameters are integers
    for i in (x, y, z):
        # If not an integer, then return False
        if type(i) != int:
            return False
        # If an integer, add it to the list
        else:
            list_1.append(i)
    # Check if one number is the sum of the other two numbers
    if (x + y == z) or (x + z == y) or (y + z == x):
        return True
    return False
