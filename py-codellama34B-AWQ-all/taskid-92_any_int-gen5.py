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

    if type(x) is not int or type(y) is not int or type(z) is not int:
        return False
    else:
        a = [x, y, z]
        for i in range(0, len(a)):
            for j in range(i + 1, len(a)):
                if (a[i] + a[j]) == a[j - i - 1] or (a[j - i - 1] + a[j]) == a[i]:
                    return True
