def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    # Reverse
    rev = str(x)[::-1]
    # Circular shift
    if len(rev) <= abs(shift):
        return rev
    elif shift >= 0:
        return rev[abs(shift):] + rev[:abs(shift)]
    else:
        return rev[shift:] + rev[:shift]
