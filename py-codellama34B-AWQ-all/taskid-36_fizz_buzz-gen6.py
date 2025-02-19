def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    return sum(str(i).count("7") for i in range(11, n) if str(i).count("7") and (i % 11 == 0 or i % 13 == 0))
