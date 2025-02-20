def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(10):
        if (i == 0) or (i == 9):
            count += 10 * pow(10, n-1)
        else:
            count += pow(10, n-1)
    return count
