def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    >>> digits(1)
    1
    >>> digits(4)
    0
    >>> digits(235)
    15
    """

    if n < 0:
        raise ValueError("n must be a positive integer")
    str_n = str(n)
    result = 0
    for i in str_n:
        if i.isdigit() and int(i) % 2 != 0:
            result *= int(i)
    return result
