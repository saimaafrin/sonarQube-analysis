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

    if base >= 10:
        raise ValueError("Invalid base: base >= 10")
    if base <= 0:
        raise ValueError("Invalid base: base <= 0")
    if x < 0:
        raise ValueError("Invalid x: x < 0")

    digits = "0123456789ABCDEF"
    res = ""
    while x > 0:
        res = digits[x % base] + res
        x = x // base
    return res
