def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """


    def circular_shift_helper(x: int, shift: int, num_digits: int) -> str:
        if num_digits == 0:
            return ""
        return str(x % 10) + circular_shift_helper(x // 10, shift, num_digits - 1)

    num_digits = len(str(x))
    if shift > num_digits:
        return circular_shift_helper(x, num_digits, num_digits)[::-1]
    return circular_shift_helper(x, shift, num_digits)
