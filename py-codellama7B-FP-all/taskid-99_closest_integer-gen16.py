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

    # Step 1: convert the string to a float
    float_value = float(value)

    # Step 2: round the float to the nearest integer
    integer = round(float_value)

    # Step 3: if the rounded float is equidistant from two integers,
    # return the one that is the farthest from zero.
    if abs(integer - float_value) == 0.5:
        if integer > 0:
            return integer
        else:
            return integer - 1

    return integer
