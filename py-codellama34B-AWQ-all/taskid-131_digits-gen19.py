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

    # Base case
    if n == 0:
        return 0
    # Recursive case
    if n % 2 == 1:
        return n * digits(n // 10)
    # n % 2 == 0
    return digits(n // 10)
