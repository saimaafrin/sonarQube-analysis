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

    # convert float to int
    a = int(x)
    b = int(y)
    c = int(z)
    #check if one number is equal to the sum of the other two
    if a + b == c or a + c == b or b + c == a:
        if a == int(a) and b == int(b) and c == int(c):
            return True
        else:
            return False
    else:
        return False
