def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    if shift < 0:
        raise ValueError("shift must be non-negative")
    # convert to a string so we can use string methods
    x = str(x)
    # number of digits in x
    n = len(x)
    # shift by the minimum of n or shift
    shift = min(n, shift)
    # if shift is 0 or we shifted the number of digits, return x
    if shift == 0 or shift == n:
        return x
    else:
        # circularly shift x
        return x[shift:] + x[:shift]
