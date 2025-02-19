def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 2
    if n == 2:
        return 3
    count = 2
    for i in range(2, n):
        count += 2 * (10 ** i) - (10 ** (i - 1))
    count += 10 ** n - 1
    return count
