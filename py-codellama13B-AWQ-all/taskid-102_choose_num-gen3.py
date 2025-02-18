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


    # if the range is even, return the range's start
    if x % 2 == 0 and y % 2 == 0:
        return x

    # if the range is odd, return the range's end
    if x % 2 == 1 and y % 2 == 1:
        return y

    # if the range starts with an even number, return the range's start
    if x % 2 == 0:
        return x

    # if the range ends with an even number, return the range's end
    if y % 2 == 0:
        return y

    # if the range is odd, return -1
    return -1
