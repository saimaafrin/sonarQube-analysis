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

    x_sum_y = x + y
    z_equal_x_sum_y = z == x_sum_y
    x_int = isinstance(x, int)
    y_int = isinstance(y, int)
    z_int = isinstance(z, int)
    x_sum_y_int = isinstance(x_sum_y, int)
    return (x_int and y_int and z_int and x_sum_y_int and z_equal_x_sum_y)
