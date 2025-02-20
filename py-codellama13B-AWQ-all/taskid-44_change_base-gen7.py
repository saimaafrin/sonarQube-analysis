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


    if not 0 <= base < 10:
        raise ValueError("base must be between 0 and 9.")
    if not 0 <= x < base ** 2:
        raise ValueError("x must be between 0 and base^2.")

    base = int(base)
    x = int(x)

    if x == 0:
        return "0"
    if base == 1:
        return "1" * x

    return "".join([str(x % base) for x in reversed(range(1, x + 1))])
