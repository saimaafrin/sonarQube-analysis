def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    # 11, 13, 17, 19
    # 7, 11, 13, 17, 19
    # 11, 7, 13, 17, 19
    # 11, 13, 7, 17, 19
    # 11, 13, 17, 7, 19
    # 11, 13, 17, 19, 7

    # 11 7 13 17 19
    # 11 13 7 17 19
    # 11 13 17 7 19
    # 11 13 17 19 7
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            if '7' in str(i):
                count += 1
    return count
