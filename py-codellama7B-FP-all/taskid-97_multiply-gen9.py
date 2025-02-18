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

    # Enter your code here.
    # 16 - 16*2 = 0
    # 14 - 14*2 = 0
    # 15 - 15*2 = 0
    # -14 - (-14)*2 = 0
    # -15 - (-15)*2 = 0
    # 14*2 - 14 = 28
    # 15*2 - 15 = 30
    # -14*2 - (-14) = -28
    # -15*2 - (-15) = -30

    if a > 0 and b > 0:
        return (a % 10) * (b % 10)
    elif a < 0 and b < 0:
        return (-a % 10) * (-b % 10)
    elif a < 0 and b > 0:
        return (-a % 10) * (b % 10)
    else:
        return (a % 10) * (-b % 10)
