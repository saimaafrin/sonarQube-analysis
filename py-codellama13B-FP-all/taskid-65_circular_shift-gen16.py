def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    # Convert x to a list
    x_list = list(str(x))

    # Calculate the shift
    if shift > len(x_list):
        shift = shift % len(x_list)

    # Calculate the length of the shift
    shift_len = len(x_list) - shift

    # Reverse the shift length
    shift_len = len(x_list) - shift

    # Shift the list
    x_list = x_list[shift_len:] + x_list[:shift_len]

    # Return the list as a string
    return "".join(x_list)
