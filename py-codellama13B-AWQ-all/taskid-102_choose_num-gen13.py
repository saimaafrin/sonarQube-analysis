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


    if y <= x:
        return -1

    if y % 2 == 0 and y >= x:
        return y

    if y - 1 >= x and (y - 1) % 2 == 0:
        return y - 1

    if y - 2 >= x and (y - 2) % 2 == 0:
        return y - 2

    return -1
