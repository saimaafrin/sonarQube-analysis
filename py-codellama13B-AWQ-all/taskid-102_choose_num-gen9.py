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

    result = 0
    if x <= y:
        if x % 2 == 0:
            result = x
        for i in range(x + 2, y + 1, 2):
            if i % 2 == 0:
                result = i
    else:
        result = -1
    return result
