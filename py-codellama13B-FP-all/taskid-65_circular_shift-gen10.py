def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    if x < 0:
        x = -x
    digits = len(str(x))
    shift_factor = shift % digits
    if shift_factor == 0:
        return str(x)
    else:
        return str(x)[-shift_factor:] + str(x)[:-shift_factor]
