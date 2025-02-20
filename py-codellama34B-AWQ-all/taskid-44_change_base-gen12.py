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

    if base > 10:
        raise ValueError("base numbers must be less than 10")
    if x == 0:
        return "0"
    if x < 0:
        raise ValueError("cannot handle negative numbers")
    result = ""
    while x > 0:
        result = str(x % base) + result
        x = x // base
    return result
