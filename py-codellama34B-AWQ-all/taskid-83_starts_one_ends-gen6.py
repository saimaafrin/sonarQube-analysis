def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # base case
    if n == 1:
        return 2
    # recursive case
    return n * 2 - 1 + starts_one_ends(n - 1)
