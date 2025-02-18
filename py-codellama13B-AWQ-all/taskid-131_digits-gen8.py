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

    res = 1
    for d in str(n):
        if d.isdigit() and int(d) % 2 == 1:
            res *= int(d)
    return res
