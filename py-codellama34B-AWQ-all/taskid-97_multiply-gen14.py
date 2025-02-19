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


    def unit_digit(x: int) -> int:
        """
        >>> unit_digit(1234)
        4
        """
        return x % 10

    return unit_digit(a) * unit_digit(b)
