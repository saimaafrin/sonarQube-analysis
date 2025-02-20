def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    # 0123456789
    # 1234567890
    # 1011121314
    # 1011121314
    # 0123456789

    # n = number of digits
    # if shift >= n
    # return digits reversed
    # else
    # digits = digits[shift:n] + digits[:shift]

    x_str = str(x)
    n = len(x_str)
    if shift >= n:
        return x_str[::-1]

    return x_str[shift:] + x_str[:shift]
