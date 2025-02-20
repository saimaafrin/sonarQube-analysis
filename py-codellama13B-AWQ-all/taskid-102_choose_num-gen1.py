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


    if x < 1 or y < 1:
        raise ValueError
    elif x > y:
        return -1
    else:
        for n in range(x, y + 1):
            if n % 2 == 0:
                return n
        return -1
