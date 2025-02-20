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

    digits = []
    for digit in str(n):
        if int(digit) % 2 != 0:
            digits.append(int(digit))
    return int(''.join(map(str, digits)))
