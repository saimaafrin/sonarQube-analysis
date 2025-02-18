def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """


    # reverse the digits
    reversed_x = str(x)[::-1]

    # calculate the shift value
    if shift > len(reversed_x):
        shift = len(reversed_x) - shift

    # circular shift the digits
    shifted_x = reversed_x[shift:] + reversed_x[:shift]

    # return the result as a string
    return shifted_x[::-1]
