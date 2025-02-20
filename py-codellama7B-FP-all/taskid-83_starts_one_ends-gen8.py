def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(1, n):
        for j in range(10):
            if (i * 10 + j) % n == 1 or (j * 10 + i) % n == 1:
                count += 1
    return count
