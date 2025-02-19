def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    count = 0
    for i in range(1, n):
        if '7' in str(i) and ('11' in str(i) or '13' in str(i)):
            count += 1
    return count
