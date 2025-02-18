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

    # your code here
    if x % 2 == 0:
        x = x + 1
    if y % 2 == 0:
        y = y - 1
    if y < x:
        return -1
    if y == x:
        return x
    else:
        while x <= y:
            if x % 2 == 0:
                return x
            else:
                x = x + 1
    return -1
