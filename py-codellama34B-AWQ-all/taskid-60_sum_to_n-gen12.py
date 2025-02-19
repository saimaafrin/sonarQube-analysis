def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """

    assert n > 0, "n must be a positive integer."
    return sum(range(1, n + 1))
