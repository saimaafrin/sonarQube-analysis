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

    num_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    if base < 2 or base > 10:
        raise ValueError("Wrong base value")
    if x < 0:
        raise ValueError("Negative numbers are not supported")
    num = str(x)
    result = ""
    while len(num) > 0:
        result = num_dict[num[0]] + result
        num = num[1:]
    return result
