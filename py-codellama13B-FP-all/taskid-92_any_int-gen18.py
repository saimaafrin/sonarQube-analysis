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


    # 1. Check if the numbers are integers.
    x_is_int = x % 1 == 0
    y_is_int = y % 1 == 0
    z_is_int = z % 1 == 0

    # 2. Check if one of the numbers is equal to the sum of the other two.
    sum_of_x_and_y = x + y
    sum_of_x_and_z = x + z
    sum_of_y_and_z = y + z

    x_is_equal_to_sum = x == sum_of_x_and_y or x == sum_of_x_and_z
    y_is_equal_to_sum = y == sum_of_y_and_z or y == sum_of_x_and_y
    z_is_equal_to_sum = z == sum_of_y_and_z or z == sum_of_x_and_z

    # 3. If the numbers are integers and one of the numbers is equal to the sum of the other two, return True.
    if x_is_int and y_is_int and z_is_int:
        if x_is_equal_to_sum or y_is_equal_to_sum or z_is_equal_to_sum:
            return True
        else:
            return False

    # 4. If the numbers are not integers, return False.
    else:
        return False
