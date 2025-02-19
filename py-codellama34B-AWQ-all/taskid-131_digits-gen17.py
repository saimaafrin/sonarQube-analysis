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

    prod = 1
    for c in str(n):
        if int(c) % 2 == 1:
            prod *= int(c)
    return prod
