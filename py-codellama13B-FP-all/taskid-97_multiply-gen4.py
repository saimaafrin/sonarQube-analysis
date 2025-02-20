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

    # This function should take two integers and return the product of their unit digits
    # For example:
    # multiply(148, 412) => 16
    # multiply(19, 28) => 72
    # multiply(2020, 1851) => 0

    return (a % 10) * (b % 10)
