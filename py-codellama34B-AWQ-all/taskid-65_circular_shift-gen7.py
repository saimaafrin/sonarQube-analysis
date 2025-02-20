def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """


    def num_digits(n: int) -> int:
        return len(str(n))

    digits = str(x)
    digits_len = num_digits(x)
    if digits_len < shift:
        digits = digits[::-1]
    else:
        digits = digits[digits_len - shift:] + digits[:digits_len - shift]
    return digits
