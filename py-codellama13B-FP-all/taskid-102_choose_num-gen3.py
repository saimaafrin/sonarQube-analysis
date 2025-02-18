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


    # Check if both x and y are positive
    if x < 0 or y < 0:
        return -1

    # Check if x < y
    if x > y:
        return -1

    # Check if x is even
    if x % 2 != 0:
        x += 1

    # Check if y is even
    if y % 2 != 0:
        y -= 1

    # Find the closest even number in the range [x, y]
    result = -1
    while x <= y:
        if x % 2 == 0:
            result = x
            break
        x += 1

    return result
