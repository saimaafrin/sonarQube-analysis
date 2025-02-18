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

    # Check if input value is a valid number.
    try:
        value = float(value)
    except ValueError:
        return "Not a valid number."

    # If the given value is equidistant from two integers, return the
    # one that is the farthest away from zero.
    if value % 1 == 0.5:
        if value > 0:
            return int(value + 0.5)
        else:
            return int(value - 0.5)
    else:
        return int(round(value))
