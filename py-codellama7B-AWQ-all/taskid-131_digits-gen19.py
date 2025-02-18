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
        raise ValueError("Negative n")
    product = 1
    while n:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
        n //= 10
    return product
