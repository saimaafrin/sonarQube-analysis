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

    if base < 1 or base > 9:
        raise ValueError("Base should be between 1 and 9")

    if x < 0:
        raise ValueError("x should be non-negative")

    if x == 0:
        return "0"

    if x == 1:
        return "1"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while x > 0:
        result.append(digits[x % base])
        x //= base

    return "".join(result)
