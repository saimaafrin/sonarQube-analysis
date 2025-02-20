def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(1, 10):
        if i == 1 or i == 10:
            count += n
        else:
            count += n - 1
    return count
