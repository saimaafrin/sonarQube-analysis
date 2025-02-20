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
        raise ValueError("base must be greater than 1")
    base_digits = "0123456789ABCDEF"
    if x < base:
        return base_digits[x]
    result = []
    while x > 0:
        result.append(base_digits[x % base])
        x //= base
    result.reverse()
    return "".join(result)
