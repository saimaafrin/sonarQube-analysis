def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 2:
        return n
    if n == 2:
        return 2
    if n == 3:
        return 3
    return n * 2 - 1
