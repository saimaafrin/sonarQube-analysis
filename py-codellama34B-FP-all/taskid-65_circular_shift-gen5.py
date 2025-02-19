def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    if shift == 0:
        return str(x)
    if shift >= len(str(x)):
        return str(x)[::-1]
    return str(x)[shift:] + str(x)[:shift]
