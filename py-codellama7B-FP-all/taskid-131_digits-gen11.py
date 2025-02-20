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
    ret = 0
    for c in s:
        if c in '13579':
            ret *= 10
            ret += int(c)
    return ret
