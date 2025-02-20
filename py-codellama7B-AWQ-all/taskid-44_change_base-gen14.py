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

    if base < 1 or base > 10:
        raise ValueError("Invalid base number")
    if x == 0:
        return "0"
    digs = '0123456789ABCDEF'
    ans = ''
    while x > 0:
        ans = digs[x % base] + ans
        x //= base
    return ans
