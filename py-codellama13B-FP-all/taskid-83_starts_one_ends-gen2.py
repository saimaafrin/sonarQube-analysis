def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 9
    count = 1
    for i in range(1, n):
        count *= 9
    return 2 * count
