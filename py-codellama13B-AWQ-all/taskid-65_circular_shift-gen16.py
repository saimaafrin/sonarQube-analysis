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
    x_digits = [d for d in x_str]

    if shift > len(x_digits):
        return x_str[::-1]
    else:
        return ''.join(x_digits[shift:] + x_digits[:shift])
