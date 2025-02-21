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

    if base < 2 or base > 9:
        raise ValueError("base must be between 2 and 9")
    if x < 0:
        raise ValueError("x must be non-negative")
    if x == 0:
        return "0"
    digits = ""
    while x > 0:
        digits = str(x % base) + digits
        x = x // base
    return digits
