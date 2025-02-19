def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    number_of_digits = len(str(x))
    if number_of_digits <= shift:
        return str(x)[::-1]
    if shift == 0:
        return str(x)
    else:
        return str(x)[shift:] + str(x)[:shift]
