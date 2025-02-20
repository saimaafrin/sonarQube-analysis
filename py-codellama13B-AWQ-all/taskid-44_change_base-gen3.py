def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    if base < 2:
        raise ValueError(f"base must be >= 2, not {base}")
    digits = "0123456789ABCDEF"
    if x < 0:
        sign = -1
    else:
        sign = 1
    x *= sign
    if x == 0:
        return "0"
    digits_array = []
    while x > 0:
        digits_array.append(x % base)
        x //= base
    digits_array.reverse()
    result = ""
    for d in digits_array:
        result += digits[d]
    if sign < 0:
        result = "-" + result
    return result
