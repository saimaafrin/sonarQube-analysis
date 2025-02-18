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

    assert base < 10, "base number cannot be bigger than 10"
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        result += str(x % base)
        x = x // base
    return result[::-1]
