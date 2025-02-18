def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    n = str(abs(x))
    shift = len(n) - shift - 1 if x < 0 else shift
    return ''.join(n[shift:] + n[:shift])
