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

    # Convert the numbers to ints and sum them.
    x_int, y_int, z_int = int(x), int(y), int(z)
    sum_int = x_int + y_int + z_int

    # Check if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    if (x_int + y_int == z_int or x_int + z_int == y_int or y_int + z_int == x_int) and all([isinstance(i, int) for i in (x, y, z)]):
        return True
    else:
        return False
