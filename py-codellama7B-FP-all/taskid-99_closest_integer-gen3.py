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


    # Use float to cast the string to a number
    number = float(value)
    # Use round to get the closest integer
    result = round(number)
    # If the value was equidistant, round it away from zero
    if abs(number - result) == 0.5:
        if number > 0:
            result += 1
        else:
            result -= 1

    # Use int to cast the result to an integer
    return int(result)
