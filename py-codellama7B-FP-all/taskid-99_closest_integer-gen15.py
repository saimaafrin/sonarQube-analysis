def closest_integer(value: str) -> int:
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer('10')
    10
    >>> closest_integer('15.3')
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    """

    # write your code here
    if value == '':
        return 0
    value = float(value)
    # 1. first we find the closest integer to the value, if the integer is equidistant from 2 integers we return the one that is the farthest from zero.
    integer = round(value)
    # 2. if the integer is equidistant from two integers, return the one that is the farthest from zero.
    if abs(integer - value) == 0.5:
        if value < 0:
            return -int(integer)
        return int(integer)
    return int(integer)
