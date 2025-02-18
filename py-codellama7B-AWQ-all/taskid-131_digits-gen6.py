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
        raise ValueError
    digit_list = []
    for digit in str(n):
        if int(digit) % 2 == 1:
            digit_list.append(digit)
    return int("".join(digit_list))
