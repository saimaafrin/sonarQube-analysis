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

    a_last_digit = abs(a) % 10
    b_last_digit = abs(b) % 10
    return (a_last_digit * b_last_digit) % 10
