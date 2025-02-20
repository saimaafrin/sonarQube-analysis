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

    result = -1
    if x % 2 == 0:
        result = x
    else:
        result = x + 1
    for i in range(result + 1, y + 1):
        if i % 2 == 0:
            result = i
            break
    return result
