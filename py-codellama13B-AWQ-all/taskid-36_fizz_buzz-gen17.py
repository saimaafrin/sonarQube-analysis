def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """


    # Solution 1
    # count_7 = 0
    # for i in range(1, n):
    #     if i % 11 == 0 or i % 13 == 0:
    #         count_7 += str(i).count('7')
    # return count_7

    # Solution 2
    count_7 = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            while '7' in str(i):
                count_7 += 1
                i //= 10
    return count_7
