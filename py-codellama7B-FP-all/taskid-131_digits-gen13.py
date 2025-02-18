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

    # TODO - you fill in here.
    result = 1
    for i in str(n):
        if int(i) % 2 != 0:
            result *= int(i)
    return result
