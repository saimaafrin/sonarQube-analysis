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


    a, b, c = sorted((x, y, z))

    # if sum of two sides is equal to the third side
    if a + b == c:
        # if all three numbers are integers
        if a % 1 == 0 and b % 1 == 0 and c % 1 == 0:
            # return True
            return True

    # if none of the above conditions are met return False
    return False
