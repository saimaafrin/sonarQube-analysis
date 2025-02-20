def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """

    # Your code here
    digits = [int(i) for i in str(x)]
    print(digits)

    if shift >= len(digits):
        digits.reverse()
        return ''.join(str(i) for i in digits)
    else:
        digits = digits[shift:] + digits[:shift]
        return ''.join(str(i) for i in digits)
