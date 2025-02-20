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

    value = float(value)
    floor = int(value)
    ceil = floor + 1
    abs_floor = abs(value - floor)
    abs_ceil = abs(value - ceil)

    if abs_floor == abs_ceil:
        if value < 0:
            return ceil
        return floor

    if abs_floor < abs_ceil:
        return floor
    return ceil
