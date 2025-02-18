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

    if base < 2 or base > 10:
        raise ValueError('Base must be between 2 and 10')
    if x < 0:
        raise ValueError('Negative numbers not supported')
    alphabet = '0123456789ABCDEF'
    result = ''
    while x > 0:
        result = alphabet[x % base] + result
        x //= base
    return result
