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
        raise ValueError("base must be >= 2")

    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1

    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base

    digits.reverse()
    return sign * "".join(str(d) for d in digits)
