def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        count += n // i
    return count
