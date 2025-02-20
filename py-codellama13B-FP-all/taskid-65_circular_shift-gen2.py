def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    # convert integer x to a list of digits
    x_list = list(str(x))

    # reverse the list if shift > number of digits
    if shift > len(x_list):
        x_list = x_list[::-1]

    # shift the digits right by shift
    x_list = x_list[shift:] + x_list[:shift]

    # return the result as a string
    return "".join(x_list)
