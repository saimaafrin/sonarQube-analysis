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

    # Convert value to float
    value_float = float(value)

    # Calculate closest integer
    closest_integer = round(value_float)

    # If the number is equidistant from two integers, round it away from zero
    if value_float - closest_integer == 0:
        if closest_integer < 0:
            closest_integer -= 1
        else:
            closest_integer += 1

    return closest_integer
