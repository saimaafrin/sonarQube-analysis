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
        raise ValueError("n should be positive")

    result = 1
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            result *= digit
        n //= 10

    return result
