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

    # Convert the value to an integer and if there is no decimal, return it
    integer = int(value)
    if "." not in value:
        return integer

    # Get the index of the decimal point
    index = value.index(".")

    # Get the integer portion and the decimal portion
    integer_part = integer
    decimal_part = value[index + 1 :]

    # Round the decimal portion up or down to the nearest integer
    # depending on whether the integer is positive or negative
    if decimal_part[0] == "5":
        if integer > 0:
            integer += 1
        elif integer < 0:
            integer -= 1

    return integer
