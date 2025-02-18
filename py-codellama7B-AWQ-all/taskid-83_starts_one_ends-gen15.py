def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    assert isinstance(n, int), 'n must be an integer'
    assert n > 0, 'n must be a positive integer'
    return n * 9 + 10
