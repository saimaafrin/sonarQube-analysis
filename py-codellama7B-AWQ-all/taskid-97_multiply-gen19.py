def multiply(a: int, b: int) -> int:
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    >>> multiply(148, 412)
    16
    >>> multiply(19, 28)
    72
    >>> multiply(2020, 1851)
    0
    >>> multiply(14, -15)
    20
    """

    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    if a_unit == 0 or b_unit == 0:
        return 0
    return a_unit * b_unit
