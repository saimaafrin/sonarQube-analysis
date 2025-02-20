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

    assert n >= 0, "n must be greater than or equal to 0"
    odd_digits = []
    while n > 0:
        if n % 2 != 0:
            odd_digits.append(n % 10)
        n = n // 10
    return reduce(lambda x, y: x * y, odd_digits, 1)
