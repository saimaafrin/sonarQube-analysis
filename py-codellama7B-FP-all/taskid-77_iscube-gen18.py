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

    # 1.0 Solution
    # return a**3 == abs(a)
    # 1.1 Solution
    return a**3 == abs(a)
    # 1.2 Solution
    # return a**3 == abs(a) or a**3 == -abs(a)
    # 2.0 Solution
    # return abs(a) in range(a**2, a**3)
    # 2.1 Solution
    # return (abs(a)**(1/3)) in range(a**2, a**3)
