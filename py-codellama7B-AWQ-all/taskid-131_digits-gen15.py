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

    digits = [int(c) for c in str(n)]
    digits_odd = [d for d in digits if d % 2 != 0]
    if len(digits_odd) == 0:
        return 0
    else:
        return int(''.join(map(str, digits_odd)))
