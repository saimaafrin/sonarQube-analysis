def iscube(a: int) -> bool:
    """
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    >>> iscube(1)
    True
    >>> iscube(2)
    False
    >>> iscube(-1)
    True
    >>> iscube(64)
    True
    >>> iscube(0)
    True
    >>> iscube(180)
    False
    """


    """ALGORITHM"""
    ###########################
    # 1. Check if a == 0
    # 2. Check if a == 1
    # 3. Check if a is a perfect cube
    # 4. If a is a perfect cube, return True
    # 5. If a is not a perfect cube, return False
    ###########################

    """
    PSEUDOCODE

    Input: a (integer)
    Output: (boolean)
    --------------------
    if a == 0:
        return True
    elif a == 1:
        return True
    else:
        for i in range(1, a):
            if (i**3) == a:
                return True
            else:
                return False
    """

    if a == 0:
        return True
    elif a == 1:
        return True
    else:
        for i in range(1, a):
            if (i**3) == a:
                return True
            else:
                return False
