def choose_num(x: int, y: int) -> int:
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    >>> choose_num(12, 15)
    14
    >>> choose_num(13, 12)
    -1
    """

    if (x % 2 == 0) or (y % 2 == 0):
        if x >= y:
            return x
        else:
            return y
    else:
        if x >= y:
            return -1
        elif x + 1 >= y:
            return x
        else:
            return x + 2
