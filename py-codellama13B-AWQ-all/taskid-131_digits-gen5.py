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

    digits_product = 1
    while n > 0:
        if n % 2 != 0:
            digits_product *= n % 10
        n = n // 10
    return digits_product
