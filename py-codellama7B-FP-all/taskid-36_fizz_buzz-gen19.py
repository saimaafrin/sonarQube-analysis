def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    # 11: 1, 22, 33, 44, 55, 66, 77, 88, 99
    # 13: 1, 2, 3, 4, 5, 6, 7, 8, 9
    num = 0
    for i in range(n):
        if i % 11 in [7, 11, 22, 33, 44, 55, 66, 77, 88, 99] or i % 13 in [7, 11, 13]:
            num += 1
    return num
