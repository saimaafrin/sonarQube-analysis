def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    x_str = str(x)
    shift_mod = shift % len(x_str)
    if shift_mod == 0:
        return x_str
    else:
        return x_str[shift_mod:] + x_str[:shift_mod]
