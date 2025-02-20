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

    min_ = min(x, y)
    max_ = max(x, y)

    for i in range(min_, max_+1):
        if i % 2 == 0:
            return i

    return -1
