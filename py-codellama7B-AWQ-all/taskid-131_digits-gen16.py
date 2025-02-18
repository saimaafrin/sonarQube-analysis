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

    # Your code here
    if n == 0:
        return 0
    else:
        str_n = str(n)
        result = 1
        for i in range(0, len(str_n)):
            if int(str_n[i]) % 2 == 1:
                result *= int(str_n[i])
        return result
