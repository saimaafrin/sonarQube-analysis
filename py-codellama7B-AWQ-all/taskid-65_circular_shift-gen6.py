def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    digits = [int(i) for i in str(x)]
    num_digits = len(digits)
    if shift > num_digits:
        shift = num_digits - 1
    shift = shift % num_digits
    return str(int(''.join([str(i) for i in digits[shift:] + digits[:shift]])))
