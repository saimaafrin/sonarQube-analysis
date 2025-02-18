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

    assert 0 <= x < base ** 3, "x is out of range"
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        digits.append(x % base)
        x = x // base
    return "".join(map(str, reversed(digits)))
