def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    def count(i, j):
        if j < i:
            return 0
        return (10 ** (j - i + 1) - 1) // 9

    return count(0, n - 1) + count(n - 1, n - 1)
