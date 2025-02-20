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
        raise ValueError("Invalid base")
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x == 0:
        return "0"
    num = abs(x)
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base
    if x < 0:
        result = "-" + result
    return result
