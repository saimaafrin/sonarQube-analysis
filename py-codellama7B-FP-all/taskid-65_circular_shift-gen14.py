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
    x_list = list(x_str)
    if len(x_list) < shift:
        return ''.join(reversed(x_list))
    else:
        shift_index = (len(x_list) - shift) % len(x_list)
        shifted = x_list[shift_index:] + x_list[:shift_index]
        return ''.join(shifted)
