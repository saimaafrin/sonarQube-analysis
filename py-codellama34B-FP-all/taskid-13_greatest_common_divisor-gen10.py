def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if a == 0 or b == 0:
        return 0

    # find max and min
    if a < b:
        min_ = a
        max_ = b
    else:
        max_ = a
        min_ = b

    while max_ % min_ != 0:
        remain = max_ % min_
        max_ = min_
        min_ = remain

    return min_
