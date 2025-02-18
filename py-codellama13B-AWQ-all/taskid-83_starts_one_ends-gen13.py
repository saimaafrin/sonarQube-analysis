def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # 10 ** (n - 1) gives us the number of possible digits, but we need to
    # remove the count for digits that start with 0.
    return 10 ** (n - 1) - 9 * 10 ** (n - 2)
