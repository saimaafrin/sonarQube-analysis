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

    digits_list = list(map(int, str(n)))
    list_len = len(digits_list)
    if list_len < 1:
        return 0
    if list_len == 1:
        if digits_list[0] % 2 == 0:
            return 0
        else:
            return digits_list[0]
    else:
        product = 1
        for i in digits_list:
            if i % 2 == 0:
                continue
            else:
                product *= i
        return product
