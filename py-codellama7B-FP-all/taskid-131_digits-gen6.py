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

    digits = [int(x) for x in str(n)]
    if all([x % 2 == 0 for x in digits]):
        return 0
    else:
        return int(''.join([str(x) for x in digits if x % 2 != 0]))
