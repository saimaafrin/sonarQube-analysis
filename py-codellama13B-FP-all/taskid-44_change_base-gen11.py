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

    # calculate the digit count of x
    count = 0
    while x > 0:
        x //= base
        count += 1
    # convert each digit to base-digit representation
    result = ''
    while x > 0:
        result = str(x % base) + result
        x //= base
    # add 0 if result length is smaller than digit count
    if len(result) < count:
        result = '0' * (count - len(result)) + result
    return result
