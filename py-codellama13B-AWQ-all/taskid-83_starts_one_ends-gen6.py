def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(1, 10):
        for j in range(10 ** (n - 1)):
            count += int(str(i) + str(j) + str(i))
    return count
