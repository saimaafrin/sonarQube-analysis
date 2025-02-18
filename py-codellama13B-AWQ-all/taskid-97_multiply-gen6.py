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

    # This function should return the product of the unit digits of a and b
    # where a and b are the given integers
    # a = 148
    # b = 412
    # a.unit_digit = 8
    # b.unit_digit = 2
    # 8*2 = 16
    # return 16

    # print(a.unit_digit)
    # print(b.unit_digit)

    return a % 10 * b % 10
