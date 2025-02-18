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

    s = str(n)
    p = 0
    for d in s:
        if int(d) % 2 == 1:
            p *= 10
            p += int(d)
    return p
