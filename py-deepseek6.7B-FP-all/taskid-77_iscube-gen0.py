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

    x = a ** (1/3)
    return round(x) ** 3 == a or round(x, 10) ** 3 == a
