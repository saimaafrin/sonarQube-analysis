def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    s = str(x)
    if len(s) == 1:
        return s
    else:
        s = list(s)
        shift %= len(s)
        if shift == 0:
            return "".join(s)
        return "".join(s[shift:] + s[:shift])
