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

    # first digit is odd, so multiply by 1.
    result = 1
    while n > 0:
        result *= n % 10
        n //= 10
    return result
