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


    # create list for digits
    digits = list()

    # get digits in base 10
    while x > 0:
        digits.append(x % 10)
        x //= 10

    # convert digits to base
    for i in range(len(digits)):
        digits[i] = str(digits[i])

    # return digits in new base
    return "".join(digits)
