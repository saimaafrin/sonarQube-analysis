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
        raise ValueError("Base must be greater than 1")
    if base > 9:
        raise ValueError("Base must be less than 10")
    if base == 10:
        return str(x)
    if x == 0:
        return "0"
    res = ""
    while x > 0:
        x, r = divmod(x, base)
        res = str(r) + res
    return res
