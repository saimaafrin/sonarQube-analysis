def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # 1-digit numbers
    result = 2

    # 2-digit numbers
    result += 2 ** (n - 1)

    # 3-digit numbers and more
    for i in range(2, n):
        result += 2 * (10 ** (i - 1) - 1)

    return result
