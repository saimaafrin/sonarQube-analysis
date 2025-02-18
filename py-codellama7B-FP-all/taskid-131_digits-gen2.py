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
        raise ValueError("Negative number")
    if n < 10:
        return 0
    d = n % 10
    if d % 2 != 0:
        return d
    return digits(n // 10)
