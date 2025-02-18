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


    from decimal import Decimal, ROUND_HALF_UP

    if not isinstance(value, str):
        raise TypeError(f"value: expected str, got {type(value).__name__}")

    try:
        value = Decimal(value)
    except (TypeError, ValueError):
        raise ValueError("Invalid number value")

    rounded_value = value.quantize(1, rounding=ROUND_HALF_UP)
    return int(rounded_value)
