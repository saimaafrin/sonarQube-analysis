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

    digits = [i for i in str(n) if i in "13579"]
    if len(digits) == 0:
        return 0
    else:
        return int("".join(digits))
