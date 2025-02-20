def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    # Your code here
    str_x = str(x)
    digits = len(str_x)
    if shift >= digits:
        return str_x[::-1]
    else:
        return str_x[-shift:] + str_x[:-shift]
