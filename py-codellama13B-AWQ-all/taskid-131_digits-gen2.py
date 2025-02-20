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
    while n > 0:
        digits.append(n % 10)
        n //= 10
    result = 1
    for digit in digits:
        if digit % 2 == 1:
            result *= digit
    return result
