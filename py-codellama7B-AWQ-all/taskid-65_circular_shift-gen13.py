def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    num_digits = len(str(x))
    shift = shift % num_digits
    if shift == 0:
        return str(x)

    result = str(x)[shift:] + str(x)[:shift]
    return result
