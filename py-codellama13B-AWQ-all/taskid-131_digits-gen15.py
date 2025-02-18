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

    result = 1
    while n > 0:
        remainder = n % 10
        if remainder % 2 != 0:
            result *= remainder
        n = n // 10
    return result
