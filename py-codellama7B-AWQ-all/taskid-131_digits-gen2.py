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

    odd_digits_product = 0
    for digit in str(n):
        if int(digit) % 2 == 1:
            odd_digits_product *= int(digit)
    return odd_digits_product
