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

    digits = list(map(int, str(n)))
    if not any(x % 2 == 0 for x in digits):
        return n
    else:
        return sum(x for x in digits if x % 2 != 0)
