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

    assert isinstance(n, int) and n > 0
    product, last = 1, n % 10
    while last % 10 in (1, 3, 5, 7, 9):
        product *= last % 10
        last //= 10
    return product
