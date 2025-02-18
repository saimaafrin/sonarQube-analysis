def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    return sum(starts_ends_at(n, i) for i in range(1, n))
