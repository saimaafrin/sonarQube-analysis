def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    number = str(x)
    number_length = len(number)
    if shift == number_length:
        return number[::-1]
    elif shift > number_length:
        raise ValueError("shift is bigger than the number of digits")
    else:
        return number[shift:] + number[:shift]
