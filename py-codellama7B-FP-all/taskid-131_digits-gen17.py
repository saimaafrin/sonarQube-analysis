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
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] % 2 != 0:
            odd_digits.append(int(n_str[i]))
    product = 1
    for i in range(len(odd_digits)):
        product *= odd_digits[i]
    return product
