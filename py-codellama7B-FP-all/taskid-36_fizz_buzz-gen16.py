def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    import itertools
    # We could just use filter(lambda x: x % 11 == 0 or x % 13 == 0, range(n))
    return sum(1 for x in itertools.count(1) if x % 11 == 0 or x % 13 == 0)
