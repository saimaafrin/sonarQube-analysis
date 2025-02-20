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

    odd = 1
    even = 0
    while n > 0:
        remainder = n % 10
        if remainder % 2 == 1:
            odd *= remainder
        else:
            even *= remainder
        n //= 10
    return odd if odd > 1 else even
