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

    if base > 10:
        raise ValueError("Base numbers are less than 10")
    if base == 10:
        return str(x)

    nums = "0123456789"
    rem = []
    while x > 0:
        rem.append(x % base)
        x = x // base
    return "".join(nums[n] for n in rem[::-1])
