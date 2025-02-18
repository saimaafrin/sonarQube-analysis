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


    while True:
        if x % 2 == 0 and y % 2 == 0:
            if x >= y:
                return -1
            else:
                return x
        elif x % 2 == 0 and y % 2 != 0:
            if y >= x:
                return x
            else:
                return -1
        elif x % 2 != 0 and y % 2 == 0:
            if x >= y:
                return -1
            else:
                return y
        elif x % 2 != 0 and y % 2 != 0:
            if x >= y:
                return -1
            else:
                return x

        x += 2
