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

    if base == 10:
        return str(x)
    quotient = x // base
    remainder = x % base
    if quotient == 0:
        return str(remainder)
    return change_base(quotient, base) + str(remainder)
