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
    while n:
        digit = n % 10
        if digit % 2 != 0:
            result *= digit
        n //= 10
    return result if result != 1 else 0
