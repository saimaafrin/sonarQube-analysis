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

    # TODO: rewrite this to divide x by base repeatedly to find its representation
    #       and use recursion to get the base-10 representation of x, then convert
    #       to base
    if x == 0:
        return "0"
    if x < 0:
        raise ValueError("x should be positive")
    if base == 10:
        return str(x)
    if base < 0 or base > 10:
        raise ValueError("base should be between 1 and 10")

    base_str = "0123456789ABCDEF"
    result = ""
    while x > 0:
        remainder = x % base
        result = base_str[remainder] + result
        x //= base

    return result
