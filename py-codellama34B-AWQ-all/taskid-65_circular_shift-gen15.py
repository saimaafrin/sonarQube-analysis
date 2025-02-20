def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    if x < 0:
        raise ValueError

    digits = [int(digit) for digit in str(x)]
    shift %= len(digits)
    if shift == 0:
        return "".join(str(digit) for digit in digits)
    else:
        return "".join(str(digit) for digit in digits[-shift:] + digits[:-shift])
