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

    n = str(n)
    s = 1
    for i in n:
        if int(i) % 2 != 0:
            s *= int(i)
    return s
