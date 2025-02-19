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

    odd_digits = []
    while n > 0:
        r = n % 10
        if r % 2 == 1:
            odd_digits.append(r)
        n = n // 10
    return odd_digits if len(odd_digits) > 0 else 0
