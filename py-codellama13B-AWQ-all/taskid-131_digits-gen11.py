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

    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, map(lambda x: int(x), str(n))))
